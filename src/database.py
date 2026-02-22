"""
Database Module - Conduit Engine v0.3

Interface to the persistent vector store (ChromaDB).
Updated to v9.2: stores 5D StateVectors [φ, τ, ρ, H, κ].
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional, Any
import chromadb

from .encoder import StateVector, compute_density_v92


class ConduitDB:
    """
    Persistent vector database for topological states.
    """

    def __init__(self, persist_directory: str = "./data/conduit_memory"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="topology_space",
            metadata={"description": "Conduit Monism v9.2 - Five Invariant Space"}
        )

    def seed_state(
        self,
        name: str,
        phi: float,
        tau: float,
        rho: float,
        H: float,
        kappa: float = 0.50,
        description: str = ""
    ) -> str:
        """
        Add a named state to the database using all five invariants.

        Returns:
            UUID of the created state
        """
        state = StateVector(phi=phi, tau=tau, rho=rho, H=H, kappa=kappa, name=name)
        vec = state.to_vector()
        density = state.density()
        state_id = str(uuid.uuid4())

        self.collection.add(
            ids=[state_id],
            embeddings=[vec],
            metadatas=[{
                "name": name,
                "description": description,
                "phi": phi,
                "tau": tau,
                "rho": rho,
                "H": H,
                "kappa": kappa,
                "density": round(density, 6),
                "timestamp": datetime.now().isoformat()
            }]
        )

        return state_id

    def seed_state_vector(
        self,
        name: str,
        state: StateVector,
        description: str = "",
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Add a StateVector directly to the database.
        """
        state_id = str(uuid.uuid4())
        vec = state.to_vector()

        meta = {
            "name": name,
            "description": description,
            "phi": state.phi,
            "tau": state.tau,
            "rho": state.rho,
            "H": state.H,
            "kappa": state.kappa,
            "density": round(state.density(), 6),
            "timestamp": datetime.now().isoformat(),
        }

        if metadata:
            meta.update(metadata)

        self.collection.add(
            ids=[state_id],
            embeddings=[vec],
            metadatas=[meta]
        )

        return state_id

    def find_neighbors(
        self,
        phi: float,
        tau: float,
        rho: float,
        H: float,
        kappa: float = 0.50,
        n_results: int = 3
    ) -> List[Dict]:
        """
        Find nearest neighbors to a given state in 5D topological space.
        """
        query_vec = [phi, tau, rho, H, kappa]
        count = self.collection.count()
        if count == 0:
            return []

        results = self.collection.query(
            query_embeddings=[query_vec],
            n_results=min(n_results, count)
        )

        neighbors = []
        for i in range(len(results['ids'][0])):
            neighbors.append({
                'id': results['ids'][0][i],
                'name': results['metadatas'][0][i]['name'],
                'distance': results['distances'][0][i],
                'metadata': results['metadatas'][0][i]
            })

        return neighbors

    def query_state(self, state: StateVector, n_results: int = 3) -> List[Dict]:
        """
        Query using a StateVector directly.
        """
        return self.find_neighbors(
            state.phi, state.tau, state.rho, state.H, state.kappa,
            n_results=n_results
        )

    def count(self) -> int:
        return self.collection.count()

    def reset(self):
        self.client.delete_collection("topology_space")
        self.collection = self.client.get_or_create_collection(
            name="topology_space",
            metadata={"description": "Conduit Monism v9.2 - Five Invariant Space"}
        )
