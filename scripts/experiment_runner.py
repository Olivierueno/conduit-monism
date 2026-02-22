#!/usr/bin/env python3
"""
Experiment Runner - Conduit Monism v9.2

Professional framework for running adversarial tests and experiments.
All experiments use the calibration library for empirically grounded values.

Usage:
    python experiment_runner.py                    # Run all validation tests
    python experiment_runner.py --test AT06        # Run specific test
    python experiment_runner.py --compare state1 state2
    python experiment_runner.py --trajectory baseline peak
    python experiment_runner.py --list             # List available states

Updated: 2026-01-17
"""

import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add project paths
PROJECT_ROOT = Path(__file__).parent.parent
CALIBRATION_PATH = PROJECT_ROOT / "calibration"
SRC_PATH = PROJECT_ROOT / "src"

for path in [str(CALIBRATION_PATH), str(SRC_PATH)]:
    if path not in sys.path:
        sys.path.insert(0, path)

from mapping_functions import (
    get_calibrated_states,
    create_grounded_state,
    GroundedState,
    Confidence,
)
from encoder import StateVector, encode, encode_from_calibration, create_trajectory
from density_models import density_v92, decompose_density, density_ratio


# =============================================================================
# Experiment Framework
# =============================================================================

@dataclass
class ExperimentResult:
    """Result of a single experiment or test."""
    name: str
    status: str  # PASS, FAIL, WARNING
    description: str
    values: Dict
    criterion: str
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ExperimentSuite:
    """A collection of experiment results."""
    name: str
    date: str
    framework_version: str = "v9.2"
    calibration_version: str = "v1.1"
    results: List[ExperimentResult] = None

    def __post_init__(self):
        if self.results is None:
            self.results = []

    def add_result(self, result: ExperimentResult):
        self.results.append(result)

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.status == "PASS")

    @property
    def failed(self) -> int:
        return sum(1 for r in self.results if r.status == "FAIL")

    @property
    def total(self) -> int:
        return len(self.results)

    def summary(self) -> str:
        lines = [
            "=" * 60,
            f"EXPERIMENT SUITE: {self.name}",
            f"Date: {self.date}",
            f"Framework: {self.framework_version} | Calibration: {self.calibration_version}",
            "=" * 60,
            ""
        ]

        for result in self.results:
            status_icon = "✓" if result.status == "PASS" else "✗" if result.status == "FAIL" else "⚠"
            lines.append(f"{status_icon} {result.name}: {result.status}")
            lines.append(f"   {result.description}")
            lines.append(f"   Criterion: {result.criterion}")
            for k, v in result.values.items():
                if isinstance(v, float):
                    lines.append(f"   {k}: {v:.4f}")
                else:
                    lines.append(f"   {k}: {v}")
            if result.notes:
                lines.append(f"   Note: {result.notes}")
            lines.append("")

        lines.append("-" * 60)
        lines.append(f"SUMMARY: {self.passed}/{self.total} tests passed")
        if self.failed > 0:
            lines.append(f"         {self.failed} tests FAILED")
        lines.append("=" * 60)

        return "\n".join(lines)

    def to_json(self) -> str:
        data = {
            "name": self.name,
            "date": self.date,
            "framework_version": self.framework_version,
            "calibration_version": self.calibration_version,
            "summary": {
                "passed": self.passed,
                "failed": self.failed,
                "total": self.total
            },
            "results": [r.to_dict() for r in self.results]
        }
        return json.dumps(data, indent=2)


# =============================================================================
# Core Validation Tests
# =============================================================================

def test_ketamine_propofol_split() -> ExperimentResult:
    """
    AT06 Core Test: Ketamine vs Propofol at equivalent behavioral unresponsiveness.

    Criterion: D(ketamine) / D(propofol) > 10×
    Expected: ~13-16×
    """
    states = get_calibrated_states()

    ket = states["ketamine_anesthesia"]
    prop = states["propofol_anesthesia"]

    ket_D = ket.density()
    prop_D = prop.density()
    ratio = ket_D / prop_D if prop_D > 0 else float('inf')

    passed = ratio > 10.0

    return ExperimentResult(
        name="Ketamine/Propofol Split (AT06)",
        status="PASS" if passed else "FAIL",
        description="Dissociative vs sedative anesthesia at equivalent unresponsiveness",
        values={
            "ketamine_D": ket_D,
            "propofol_D": prop_D,
            "ratio": ratio,
            "ketamine_rho": ket.rho.value,
            "propofol_rho": prop.rho.value,
        },
        criterion="D(ketamine) / D(propofol) > 10×",
        notes=f"Ketamine ρ={ket.rho.value:.2f} (PCI=0.44), Propofol ρ={prop.rho.value:.2f} (PCI=0.24)"
    )


def test_wakefulness_baseline() -> ExperimentResult:
    """
    Wakefulness should have D in range 0.10-0.15.
    """
    states = get_calibrated_states()
    wake = states["wakefulness"]
    D = wake.density()

    passed = 0.10 <= D <= 0.15

    return ExperimentResult(
        name="Wakefulness Baseline",
        status="PASS" if passed else "FAIL",
        description="Baseline wakefulness density should be moderate",
        values={"D": D},
        criterion="0.10 ≤ D ≤ 0.15"
    )


def test_panic_vs_khole() -> ExperimentResult:
    """
    Panic Attack should have higher D than K-hole (hyper-conscious vs dissociated).

    The fix from earlier: Panic ρ=0.70 (acute self-awareness), not low.
    """
    states = get_calibrated_states()

    panic = states["panic_attack"]
    khole = states["ketamine_anesthesia"]

    panic_D = panic.density()
    khole_D = khole.density()

    passed = panic_D > khole_D

    return ExperimentResult(
        name="Panic vs K-hole Ordering",
        status="PASS" if passed else "FAIL",
        description="Panic (hyper-conscious) should have higher D than K-hole (dissociated)",
        values={
            "panic_D": panic_D,
            "khole_D": khole_D,
            "panic_rho": panic.rho.value,
            "panic_kappa": panic.kappa.value,
        },
        criterion="D(panic) > D(ketamine)",
        notes="Panic is 'loud but brittle' - high binding but unstructured entropy"
    )


def test_flow_state() -> ExperimentResult:
    """
    Flow state should have higher D than wakefulness.
    """
    states = get_calibrated_states()

    flow = states["flow_state"]
    wake = states["wakefulness"]

    flow_D = flow.density()
    wake_D = wake.density()

    passed = flow_D > wake_D

    return ExperimentResult(
        name="Flow State Elevation",
        status="PASS" if passed else "FAIL",
        description="Flow state should exceed baseline wakefulness",
        values={
            "flow_D": flow_D,
            "wakefulness_D": wake_D,
        },
        criterion="D(flow) > D(wakefulness)"
    )


def test_pci_threshold() -> ExperimentResult:
    """
    Test that states above/below PCI* = 0.31 threshold are correctly classified.

    - Ketamine (ρ=0.45, PCI~0.44) → above threshold → conscious
    - Propofol (ρ=0.21, PCI~0.24) → below threshold → unconscious
    """
    states = get_calibrated_states()

    PCI_THRESHOLD = 0.31

    above = ["wakefulness", "ketamine_anesthesia", "REM_sleep", "locked_in_syndrome", "flow_state"]
    below = ["propofol_anesthesia", "xenon_anesthesia", "NREM_sleep_N3"]

    above_correct = 0
    below_correct = 0

    for name in above:
        if name in states:
            if states[name].rho.value >= PCI_THRESHOLD:
                above_correct += 1

    for name in below:
        if name in states:
            if states[name].rho.value < PCI_THRESHOLD:
                below_correct += 1

    total_above = len([n for n in above if n in states])
    total_below = len([n for n in below if n in states])

    passed = (above_correct == total_above) and (below_correct == total_below)

    return ExperimentResult(
        name="PCI* Threshold Classification",
        status="PASS" if passed else "FAIL",
        description="States should be correctly classified by PCI* = 0.31 threshold",
        values={
            "above_threshold_correct": f"{above_correct}/{total_above}",
            "below_threshold_correct": f"{below_correct}/{total_below}",
            "PCI_threshold": PCI_THRESHOLD,
        },
        criterion="All conscious states ρ ≥ 0.31, all unconscious states ρ < 0.31",
        notes="Based on Casarotto 2016 validation (100% accuracy)"
    )


def test_coherence_gate() -> ExperimentResult:
    """
    Test the coherence gate: high entropy + high coherence should preserve density.

    Compare:
    - High H, Low κ (panic-like): Should be penalized
    - High H, High κ (psychedelic-like): Should be partially rescued
    """
    # Fixed structure
    phi, tau, rho = 0.60, 0.50, 0.50
    H = 0.75  # High entropy

    low_kappa = 0.20
    high_kappa = 0.85

    D_low_kappa = density_v92(phi, tau, rho, H, low_kappa)
    D_high_kappa = density_v92(phi, tau, rho, H, high_kappa)

    # High kappa should rescue
    rescue_factor = D_high_kappa / D_low_kappa if D_low_kappa > 0 else float('inf')

    passed = rescue_factor > 1.5  # Significant rescue

    return ExperimentResult(
        name="Coherence Gate Rescue",
        status="PASS" if passed else "FAIL",
        description="High coherence should rescue high-entropy states",
        values={
            "D_low_kappa": D_low_kappa,
            "D_high_kappa": D_high_kappa,
            "rescue_factor": rescue_factor,
            "H": H,
            "low_kappa": low_kappa,
            "high_kappa": high_kappa,
        },
        criterion="D(high κ) / D(low κ) > 1.5 at fixed high H",
        notes="This is the DMT resolution: structured chaos maintains density"
    )


def test_zero_floor() -> ExperimentResult:
    """
    Test that zero in any structural dimension means zero D.
    """
    test_cases = [
        (0.0, 0.5, 0.5, 0.5, 0.5, "phi=0"),
        (0.5, 0.0, 0.5, 0.5, 0.5, "tau=0"),
        (0.5, 0.5, 0.0, 0.5, 0.5, "rho=0"),
    ]

    all_zero = True
    for phi, tau, rho, H, kappa, case in test_cases:
        D = density_v92(phi, tau, rho, H, kappa)
        if D != 0.0:
            all_zero = False
            break

    return ExperimentResult(
        name="Zero Floor Constraint",
        status="PASS" if all_zero else "FAIL",
        description="Zero in any structural dimension (φ, τ, ρ) should give D=0",
        values={"all_zero": all_zero},
        criterion="D=0 when any of φ, τ, ρ = 0",
        notes="This is the 'no free lunch' principle - structure is required"
    )


def test_anesthetic_hierarchy() -> ExperimentResult:
    """
    Test the anesthetic hierarchy matches empirical PCI ordering.

    Expected: Xenon < Propofol < Midazolam < Ketamine
    """
    states = get_calibrated_states()

    order = ["xenon_anesthesia", "propofol_anesthesia", "midazolam_anesthesia", "ketamine_anesthesia"]
    densities = []

    for name in order:
        if name in states:
            densities.append((name, states[name].density()))

    # Check ordering
    correct_order = all(
        densities[i][1] < densities[i+1][1]
        for i in range(len(densities) - 1)
    )

    return ExperimentResult(
        name="Anesthetic Hierarchy",
        status="PASS" if correct_order else "FAIL",
        description="Anesthetic D should follow PCI ordering",
        values={name: D for name, D in densities},
        criterion="D(xenon) < D(propofol) < D(midazolam) < D(ketamine)",
        notes="Based on Sarasso 2015 PCI measurements"
    )


# =============================================================================
# Experiment Suite Runners
# =============================================================================

def run_core_validation() -> ExperimentSuite:
    """Run all core validation tests."""
    suite = ExperimentSuite(
        name="Core Validation Suite",
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    tests = [
        test_ketamine_propofol_split,
        test_wakefulness_baseline,
        test_panic_vs_khole,
        test_flow_state,
        test_pci_threshold,
        test_coherence_gate,
        test_zero_floor,
        test_anesthetic_hierarchy,
    ]

    for test in tests:
        result = test()
        suite.add_result(result)

    return suite


def run_gradient_analysis(start_state: str, end_state: str, steps: int = 10) -> Dict:
    """
    Run gradient analysis between two states.

    Useful for testing trajectories like:
    - Wakefulness → Propofol (anesthesia onset)
    - Baseline → Psychedelic Peak
    - Wake → K-hole
    """
    states = get_calibrated_states()

    if start_state not in states or end_state not in states:
        available = list(states.keys())
        raise ValueError(f"States not found. Available: {available}")

    start = encode_from_calibration(start_state)
    end = encode_from_calibration(end_state)

    trajectory = create_trajectory(start, end, steps=steps)

    results = []
    for i, state in enumerate(trajectory):
        t = i / steps
        results.append({
            "step": i,
            "t": t,
            "phi": state.phi,
            "tau": state.tau,
            "rho": state.rho,
            "H": state.H,
            "kappa": state.kappa,
            "D": state.density(),
        })

    return {
        "start": start_state,
        "end": end_state,
        "steps": steps,
        "trajectory": results,
        "D_start": trajectory[0].density(),
        "D_end": trajectory[-1].density(),
        "D_ratio": trajectory[0].density() / trajectory[-1].density() if trajectory[-1].density() > 0 else float('inf')
    }


def compare_states_detailed(*state_names: str) -> Dict:
    """
    Detailed comparison of multiple states.
    """
    states = get_calibrated_states()

    results = {}
    for name in state_names:
        if name in states:
            state = states[name]
            results[name] = {
                "phi": state.phi.value,
                "tau": state.tau.value,
                "rho": state.rho.value,
                "H": state.H.value,
                "kappa": state.kappa.value,
                "D": state.density(),
                "confidence": state.overall_confidence().value,
            }

    return results


def list_all_states() -> Dict:
    """List all available calibrated states with their densities."""
    states = get_calibrated_states()

    results = {}
    for name, state in states.items():
        results[name] = {
            "D": state.density(),
            "rho": state.rho.value,
            "confidence": state.overall_confidence().value,
        }

    # Sort by density
    sorted_results = dict(sorted(results.items(), key=lambda x: x[1]["D"], reverse=True))
    return sorted_results


# =============================================================================
# CLI Interface
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Conduit Monism v9.2 Experiment Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python experiment_runner.py                    # Run all validation tests
    python experiment_runner.py --test AT06        # Run specific test
    python experiment_runner.py --compare wakefulness ketamine_anesthesia propofol_anesthesia
    python experiment_runner.py --trajectory wakefulness propofol_anesthesia
    python experiment_runner.py --list             # List all calibrated states
        """
    )

    parser.add_argument("--test", type=str, help="Run specific test (e.g., AT06)")
    parser.add_argument("--compare", nargs="+", help="Compare multiple states")
    parser.add_argument("--trajectory", nargs=2, help="Generate trajectory between two states")
    parser.add_argument("--list", action="store_true", help="List all calibrated states")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--output", type=str, help="Save results to file")

    args = parser.parse_args()

    if args.list:
        states = list_all_states()
        if args.json:
            print(json.dumps(states, indent=2))
        else:
            print("=" * 60)
            print("CALIBRATED STATES (sorted by density)")
            print("=" * 60)
            for name, info in states.items():
                print(f"{name:30} D={info['D']:.4f}  ρ={info['rho']:.2f}  [{info['confidence']}]")

    elif args.compare:
        results = compare_states_detailed(*args.compare)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("=" * 60)
            print("STATE COMPARISON")
            print("=" * 60)
            for name, info in results.items():
                print(f"\n{name}:")
                for k, v in info.items():
                    if isinstance(v, float):
                        print(f"  {k}: {v:.4f}")
                    else:
                        print(f"  {k}: {v}")

    elif args.trajectory:
        results = run_gradient_analysis(args.trajectory[0], args.trajectory[1])
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("=" * 60)
            print(f"TRAJECTORY: {results['start']} → {results['end']}")
            print("=" * 60)
            print(f"D ratio: {results['D_ratio']:.1f}×")
            print()
            for step in results['trajectory']:
                print(f"  t={step['t']:.1f}: D={step['D']:.4f}")

    else:
        # Default: run core validation
        suite = run_core_validation()

        if args.json:
            output = suite.to_json()
        else:
            output = suite.summary()

        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Results saved to {args.output}")
        else:
            print(output)


if __name__ == "__main__":
    main()
