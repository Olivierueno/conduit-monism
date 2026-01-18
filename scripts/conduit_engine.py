#!/usr/bin/env python3
"""
Conduit Engine v0.2
===================

The executable implementation of Conduit Monism v9.2.

This system:
- Encodes mental states as structural topology (not semantics)
- Uses empirically grounded calibration values (PCI, LZc, MSE)
- Stores states in a persistent vector database
- Uses operators to simulate state transitions
- Discovers patterns through geometric proximity

Formula: D = φ × τ × ρ × [(1 - √H) + (H × κ)]

Per the AI deliberation consensus:
- Gemini: Provided the substrate (database structure)
- ChatGPT: Enforced constraints (no premature semantic commitment)
- Claude: Provided the mechanics (operators)

The system is an INSTRUMENT, not a mind.
It discovers structure. Humans interpret meaning.

Updated: 2026-01-17
- Integrated calibration library v1.1
- Updated to v9.2 formula with coherence gate
- Added empirically grounded seeding
"""

import sys
from pathlib import Path

# Add project paths
PROJECT_ROOT = Path(__file__).parent.parent
CALIBRATION_PATH = PROJECT_ROOT / "calibration"
SRC_PATH = PROJECT_ROOT / "src"

for path in [str(CALIBRATION_PATH), str(SRC_PATH)]:
    if path not in sys.path:
        sys.path.insert(0, path)

from src.database import ConduitDB
from src.encoder import (
    encode,
    encode_from_calibration,
    get_all_calibrated_states,
    StateVector,
    create_trajectory,
)
from src.operators import (
    op_perturb_binding,
    op_fracture_integration,
    op_stretch_temporal_depth,
    op_inject_entropy
)
from src.density_models import density_v92, decompose_density

# Check calibration availability
try:
    from mapping_functions import get_calibrated_states, Confidence
    CALIBRATION_AVAILABLE = True
except ImportError:
    CALIBRATION_AVAILABLE = False
    print("Warning: Calibration library not available. Using fallback values.")


def print_banner():
    """Display startup banner."""
    print("=" * 60)
    print("CONDUIT ENGINE v0.2")
    print("Conduit Monism v9.2 - Structural Topology System")
    print("Formula: D = φ × τ × ρ × [(1 - √H) + (H × κ)]")
    print("=" * 60)
    if CALIBRATION_AVAILABLE:
        print("Calibration: v1.1 (Empirically Grounded)")
    else:
        print("Calibration: FALLBACK MODE")
    print()


def seed_calibrated_states(db: ConduitDB):
    """
    Seed the database with empirically grounded states from calibration library.

    These provide anchor points in the state space with known properties.
    """
    print("Seeding empirically grounded states...")
    print()

    if not CALIBRATION_AVAILABLE:
        print("Warning: Calibration not available. Using legacy seeding.")
        seed_liminal_cases_legacy(db)
        return

    states = get_calibrated_states()

    # Seed key anchor states
    key_states = [
        "wakefulness",
        "propofol_anesthesia",
        "ketamine_anesthesia",
        "xenon_anesthesia",
        "REM_sleep",
        "NREM_sleep_N3",
        "flow_state",
        "deep_meditation",
        "panic_attack",
        "psilocybin",
        "DMT_breakthrough",
        "vegetative_state",
        "locked_in_syndrome",
    ]

    for state_name in key_states:
        if state_name in states:
            state = states[state_name]
            # Convert to 6D vector for database (legacy compatibility)
            vec = [
                state.phi.value,
                state.tau.value,
                state.rho.value,
                state.H.value,
                state.kappa.value,
                0.0  # Latent dimension
            ]
            db.seed_state_vector(
                name=state.name,
                vector=vec,
                description=f"D={state.density():.4f}, Conf={state.overall_confidence().value}",
                metadata={
                    "density": state.density(),
                    "confidence": state.overall_confidence().value,
                    "calibration_version": "1.1"
                }
            )
            print(f"  Seeded: {state.name} (D={state.density():.4f})")

    print()


def seed_liminal_cases_legacy(db: ConduitDB):
    """
    LEGACY: Seed with hardcoded values when calibration unavailable.
    """
    print("Seeding liminal cases (legacy mode)...")
    print()

    # Baseline: Healthy, awake, integrated consciousness
    db.seed_state(
        name="Healthy Awake",
        phi=0.8, tau=0.5, rho=0.55, entropy=0.5,
        description="Baseline integrated consciousness"
    )

    # Deep Anesthesia
    db.seed_state(
        name="Deep Anesthesia",
        phi=0.2, tau=0.1, rho=0.24, entropy=0.35,
        description="Near-zero consciousness (propofol-like)"
    )

    # Ketamine
    db.seed_state(
        name="Ketamine Anesthesia",
        phi=0.48, tau=0.25, rho=0.45, entropy=0.55,
        description="Dissociative anesthesia, preserved binding"
    )

    # Panic Attack (fixed)
    db.seed_state(
        name="Panic Attack",
        phi=0.88, tau=0.5, rho=0.7, entropy=0.68,
        description="Hyper-conscious terror, high binding, unstructured"
    )

    # Flow State
    db.seed_state(
        name="Flow State",
        phi=0.92, tau=0.7, rho=0.7, entropy=0.45,
        description="Maximum integration and binding, high coherence"
    )

    # Deep Meditation
    db.seed_state(
        name="Deep Meditation",
        phi=0.85, tau=0.8, rho=0.65, entropy=0.43,
        description="High temporal depth, high coherence"
    )

    print()


def run_simulation_1(db: ConduitDB):
    """
    Simulation 1: Fracturing Integration

    Question: If we take a healthy state and fracture its integration (φ),
    what does it become geometrically?
    """
    print("=" * 60)
    print("SIMULATION 1: Fracturing Integration")
    print("=" * 60)
    print()

    if CALIBRATION_AVAILABLE:
        wake = encode_from_calibration("wakefulness")
        print(f"Starting with: {wake}")
    else:
        wake = encode(phi=0.8, tau=0.5, rho=0.55, entropy=0.5, kappa=0.5, name="Wakefulness")
        print(f"Starting with: {wake} (legacy values)")

    print("Applying operator: Fracture φ by -0.4 (simulating trauma/dissociation)")
    print()

    # Apply operator
    fractured_vec = op_fracture_integration(wake.to_vector_6d(), 0.4)

    # Query database
    neighbors = db.query_vector(fractured_vec, n_results=3)

    print("Resulting state is geometrically closest to:")
    for i, neighbor in enumerate(neighbors, 1):
        print(f"  {i}. {neighbor['name']} (distance: {neighbor['distance']:.4f})")

    print()
    print("The system discovered this relationship structurally,")
    print("not because we labeled it, but because the geometry maps this way.")
    print()


def run_simulation_2(db: ConduitDB):
    """
    Simulation 2: Ketamine vs Propofol

    Question: Does the geometry correctly separate dissociative from sedative?
    """
    print("=" * 60)
    print("SIMULATION 2: Dissociative vs Sedative Split")
    print("=" * 60)
    print()

    if CALIBRATION_AVAILABLE:
        ket = encode_from_calibration("ketamine_anesthesia")
        prop = encode_from_calibration("propofol_anesthesia")

        print(f"Ketamine: {ket}")
        print(f"Propofol: {prop}")
        print()

        ratio = ket.density() / prop.density() if prop.density() > 0 else float('inf')
        print(f"Density ratio: {ratio:.1f}× (Ketamine / Propofol)")
        print()

        if ratio > 10:
            print("✓ Framework correctly separates dissociative from sedative anesthesia")
        else:
            print("✗ WARNING: Ratio below expected threshold")
    else:
        print("Calibration not available. Cannot run comparison.")

    print()


def run_simulation_3(db: ConduitDB):
    """
    Simulation 3: Entropy Injection

    Question: What happens when we inject high entropy into a flow state?
    """
    print("=" * 60)
    print("SIMULATION 3: Injecting Entropy into Flow")
    print("=" * 60)
    print()

    if CALIBRATION_AVAILABLE:
        flow = encode_from_calibration("flow_state")
        print(f"Starting with: {flow}")
    else:
        flow = encode(phi=0.92, tau=0.7, rho=0.7, entropy=0.45, kappa=0.75, name="Flow State")
        print(f"Starting with: {flow} (legacy values)")

    print("Applying operator: Inject entropy +0.4")
    print()

    perturbed_vec = op_inject_entropy(flow.to_vector_6d(), 0.4)

    neighbors = db.query_vector(perturbed_vec, n_results=3)

    print("Resulting state is geometrically closest to:")
    for i, neighbor in enumerate(neighbors, 1):
        print(f"  {i}. {neighbor['name']} (distance: {neighbor['distance']:.4f})")

    print()


def run_exploration_mode(db: ConduitDB):
    """
    Interactive exploration mode.

    Allows manual queries of the topological space.
    """
    print("=" * 60)
    print("EXPLORATION MODE")
    print("=" * 60)
    print()
    print("Query the topological space by providing φ, τ, ρ, H, κ values.")
    print("Format: φ τ ρ H κ (5 numbers between 0 and 1)")
    print("Or type a state name (e.g., 'wakefulness', 'ketamine_anesthesia')")
    print("Type 'quit' to exit, 'list' to see available states.")
    print()

    available_states = {}
    if CALIBRATION_AVAILABLE:
        available_states = get_all_calibrated_states()

    while True:
        try:
            cmd = input("Query> ").strip()
            if cmd.lower() in ['quit', 'exit', 'q']:
                break

            if cmd.lower() == 'list':
                if available_states:
                    print("\nAvailable calibrated states:")
                    for name, state in sorted(available_states.items(), key=lambda x: x[1].density(), reverse=True):
                        print(f"  {name}: D={state.density():.4f}")
                    print()
                else:
                    print("No calibrated states available.")
                continue

            # Try as state name first
            if cmd.lower().replace(" ", "_") in available_states:
                state = available_states[cmd.lower().replace(" ", "_")]
                print(f"\n{state}")
                decomp = state.decompose()
                print(f"  Structure: {decomp['structure']:.4f}")
                print(f"  Entropy gate: {decomp['entropy_gate']:.4f}")
                print(f"  Confidence: {state.confidence}")
                print()
                continue

            # Try as numeric values
            values = [float(x) for x in cmd.split()]
            if len(values) == 5:
                phi, tau, rho, H, kappa = values
                state = encode(phi=phi, tau=tau, rho=rho, entropy=H, kappa=kappa)
                print(f"\nState: {state}")

                # Query neighbors
                neighbors = db.query_vector(state.to_vector_6d(), n_results=3)
                print("\nNearest calibrated neighbors:")
                for i, neighbor in enumerate(neighbors, 1):
                    print(f"  {i}. {neighbor['name']} (distance: {neighbor['distance']:.4f})")
                print()
            elif len(values) == 4:
                # Legacy 4-value format (assume kappa=0.5)
                phi, tau, rho, H = values
                print("Note: Using default κ=0.50. Use 5 values for full v9.2 encoding.")
                state = encode(phi=phi, tau=tau, rho=rho, entropy=H, kappa=0.5)
                print(f"\nState: {state}")
                print()
            else:
                print("Error: Please provide 5 values (φ τ ρ H κ) or a state name")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n")
            break


def main():
    """Main execution function."""
    print_banner()

    # Initialize database
    db = ConduitDB()
    print(f"Database initialized. Current state count: {db.count()}")
    print()

    # Seed if empty
    if db.count() == 0:
        seed_calibrated_states(db)
    else:
        print(f"Database already contains {db.count()} states. Skipping seeding.")
        print("(Delete data/conduit_memory to reset)")
        print()

    # Run simulations
    run_simulation_1(db)
    run_simulation_2(db)
    run_simulation_3(db)

    # Interactive mode
    print("Starting interactive exploration mode...")
    print()
    run_exploration_mode(db)

    print()
    print("=" * 60)
    print("SESSION ENDED")
    print("The Conduit persists. The structure remains.")
    print("=" * 60)


if __name__ == "__main__":
    main()
