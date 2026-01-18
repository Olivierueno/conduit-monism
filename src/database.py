"""
Database Module - Conduit Engine v0.2

Interface to the persistent vector store (ChromaDB).
The database is the "Conduit" - it holds the structure when neither human nor AI is looking.

Updated: 2026-01-17
- Added seed_state_vector for v9.2 5D/6D vectors
- Updated to v9.2 description
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional, Any
import chromadb
from chromadb.config import Settings

from .encoder import encode_legacy as encode, compute_density


class ConduitDB:
    """
    Persistent vector database for topological states.

    This is the substrate - the memory that persists across sessions.
    """

    def __init__(self, persist_directory: str = "./data/conduit_memory"):
        """
        Initialize the Conduit database.

        Parameters:
        -----------
        persist_directory : str
            Path where the database will be persisted
        """
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="topology_space",
            metadata={"description": "Conduit Monism v7.0 - Structural Only"}
        )

    def seed_state(
        self,
        name: str,
        phi: float,
        tau: float,
        rho: float,
        entropy: float,
        description: str = ""
    ) -> str:
        """
        Add a named state to the database.

        Parameters:
        -----------
        name : str
            Human-readable label for this state (metadata only, not structure)
        phi, tau, rho, entropy : float
            The four structural invariants
        description : str
            Optional description (metadata only)

        Returns:
        --------
        str
            UUID of the created state
        """
        vec = encode(phi, tau, rho, entropy)
        density = compute_density(phi, tau, rho)
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
                "entropy": entropy,
                "density": round(density, 4),
                "timestamp": datetime.now().isoformat()
            }]
        )

        print(f"Seeded: [{name}] (φ={phi:.2f}, τ={tau:.2f}, ρ={rho:.2f}, H={entropy:.2f}, Density={density:.3f})")
        return state_id

    def seed_state_vector(
        self,
        name: str,
        vector: List[float],
        description: str = "",
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Add a named state using a pre-computed vector.

        For v9.2 states with 5 or 6 dimensions [φ, τ, ρ, H, κ, (latent)].

        Parameters:
        -----------
        name : str
            Human-readable label for this state
        vector : List[float]
            The state vector (5D or 6D)
        description : str
            Optional description
        metadata : Dict
            Additional metadata to store

        Returns:
        --------
        str
            UUID of the created state
        """
        state_id = str(uuid.uuid4())

        # Build metadata
        meta = {
            "name": name,
            "description": description,
            "timestamp": datetime.now().isoformat(),
            "vector_dim": len(vector),
        }

        # Add vector components if available
        if len(vector) >= 4:
            meta["phi"] = vector[0]
            meta["tau"] = vector[1]
            meta["rho"] = vector[2]
            meta["entropy"] = vector[3]
        if len(vector) >= 5:
            meta["kappa"] = vector[4]

        # Merge additional metadata
        if metadata:
            meta.update(metadata)

        self.collection.add(
            ids=[state_id],
            embeddings=[vector],
            metadatas=[meta]
        )

        return state_id

    def find_neighbors(
        self,
        phi: float,
        tau: float,
        rho: float,
        entropy: float,
        n_results: int = 3
    ) -> List[Dict]:
        """
        Find the nearest neighbors to a given state in topological space.

        This is "geometric thought" - finding what a state is structurally similar to.

        Parameters:
        -----------
        phi, tau, rho, entropy : float
            The query state
        n_results : int
            Number of neighbors to return

        Returns:
        --------
        List[Dict]
            List of neighbor states with their metadata and distances
        """
        query_vec = encode(phi, tau, rho, entropy)
        results = self.collection.query(
            query_embeddings=[query_vec],
            n_results=min(n_results, self.collection.count())
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

    def query_vector(self, vector: List[float], n_results: int = 3) -> List[Dict]:
        """
        Query the database with a raw vector (e.g., after applying operators).

        Parameters:
        -----------
        vector : List[float]
            The state vector to query with
        n_results : int
            Number of neighbors to return

        Returns:
        --------
        List[Dict]
            List of neighbor states with their metadata and distances
        """
        results = self.collection.query(
            query_embeddings=[vector],
            n_results=min(n_results, self.collection.count())
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

    def count(self) -> int:
        """Return the number of states in the database."""
        return self.collection.count()

    def reset(self):
        """Delete all states from the database (use with caution)."""
        self.client.delete_collection("topology_space")
        self.collection = self.client.get_or_create_collection(
            name="topology_space",
            metadata={"description": "Conduit Monism v7.0 - Structural Only"}
        )
        print("Database reset.")
