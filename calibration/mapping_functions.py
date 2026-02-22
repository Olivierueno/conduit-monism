"""
Mapping Functions for Conduit Monism Empirical Calibration

This module provides explicit transformation functions from empirical
measurements to framework variables (φ, τ, ρ, H, κ).

Version: 1.1
Date: 2026-01-17
Framework: Conduit Monism v9.2
Updated: Integrated Compass research data (Ketamine PCI = 0.44 mean)
"""

import json
import math
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


class Confidence(Enum):
    HIGH = "HIGH"
    MODERATE = "MODERATE"
    LOW = "LOW"
    THEORETICAL = "THEORETICAL"


@dataclass
class CalibratedValue:
    """A framework variable value with empirical grounding."""
    value: float
    confidence: Confidence
    source: str
    empirical_measure: Optional[float] = None
    empirical_range: Optional[tuple] = None
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "confidence": self.confidence.value,
            "source": self.source,
            "empirical_measure": self.empirical_measure,
            "empirical_range": self.empirical_range,
            "notes": self.notes
        }


# =============================================================================
# ρ (Rho): Re-entrant Binding ← PCI
# =============================================================================

def pci_to_rho(pci: float) -> CalibratedValue:
    """
    Map Perturbational Complexity Index to ρ (binding).

    Direct mapping: ρ = PCI

    PCI is already normalized to approximately 0-1 range.
    Values from Casali et al. (2013):
        - Wakefulness: 0.44-0.67
        - REM: 0.41-0.48
        - NREM: 0.18-0.28
        - Anesthesia: 0.12-0.31

    Args:
        pci: Perturbational Complexity Index value (0-1)

    Returns:
        CalibratedValue with ρ and metadata
    """
    if not 0 <= pci <= 1:
        raise ValueError(f"PCI must be between 0 and 1, got {pci}")

    return CalibratedValue(
        value=pci,
        confidence=Confidence.HIGH,
        source="PCI direct mapping",
        empirical_measure=pci,
        notes="Direct mapping: ρ = PCI (Casali et al., 2013)"
    )


def _clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Clamp value to [min_val, max_val] range."""
    return max(min_val, min(max_val, value))


def pci_range_to_rho(pci_min: float, pci_max: float) -> CalibratedValue:
    """
    Map PCI range to ρ using midpoint.

    Args:
        pci_min: Lower bound of PCI range
        pci_max: Upper bound of PCI range

    Returns:
        CalibratedValue with ρ at midpoint and range metadata
    """
    midpoint = _clamp((pci_min + pci_max) / 2)

    return CalibratedValue(
        value=midpoint,
        confidence=Confidence.HIGH,
        source="PCI range midpoint",
        empirical_measure=midpoint,
        empirical_range=(pci_min, pci_max),
        notes=f"Midpoint of PCI range [{pci_min:.2f}, {pci_max:.2f}]"
    )


# =============================================================================
# H: Entropy ← Lempel-Ziv Complexity
# =============================================================================

# Baseline LZc for normalization (waking state)
LZC_BASELINE = 0.50  # Normalized baseline

def lzc_to_H(lzc_normalized: float) -> CalibratedValue:
    """
    Map Lempel-Ziv Complexity to H (entropy).

    Direct mapping after normalization: H = LZc_normalized

    Normalization treats waking baseline as 0.50.
    Schartner et al. (2017) values:
        - Baseline: ~0.45-0.50 (reference)
        - Propofol: ~0.35 (-30%)
        - Psilocybin: ~0.60 (+15-20%)

    Args:
        lzc_normalized: Normalized Lempel-Ziv complexity (0-1)

    Returns:
        CalibratedValue with H and metadata
    """
    if not 0 <= lzc_normalized <= 1:
        raise ValueError(f"Normalized LZc must be between 0 and 1, got {lzc_normalized}")

    return CalibratedValue(
        value=lzc_normalized,
        confidence=Confidence.HIGH,
        source="LZc normalized",
        empirical_measure=lzc_normalized,
        notes="H = LZc_normalized (Schartner et al., 2015, 2017)"
    )


def lzc_percent_change_to_H(percent_change: float, baseline: float = LZC_BASELINE) -> CalibratedValue:
    """
    Map LZc percent change from baseline to H.

    Args:
        percent_change: Percent change from baseline (-100 to +100)
        baseline: Baseline H value (default 0.50)

    Returns:
        CalibratedValue with H
    """
    h_value = _clamp(baseline * (1 + percent_change / 100))  # Clamp to [0, 1]

    confidence = Confidence.HIGH if abs(percent_change) <= 30 else Confidence.MODERATE

    return CalibratedValue(
        value=h_value,
        confidence=confidence,
        source="LZc percent change",
        empirical_measure=percent_change,
        notes=f"H = {baseline} × (1 + {percent_change}%)"
    )


# =============================================================================
# τ (Tau): Temporal Depth ← Temporal Integration Window
# =============================================================================

# Baseline temporal integration window in milliseconds (Pöppel 1997)
TAU_BASELINE_MS = 3000  # 3 seconds

def temporal_window_to_tau(window_ms: float) -> CalibratedValue:
    """
    Map temporal integration window to τ (temporal depth).

    Mapping: τ = window_ms / 3000

    Baseline: ~3 seconds for waking adults (Pöppel 1997)

    Args:
        window_ms: Temporal integration window in milliseconds

    Returns:
        CalibratedValue with τ and metadata
    """
    tau_value = _clamp(window_ms / TAU_BASELINE_MS)  # Clamp to [0, 1]

    # Confidence based on distance from baseline
    if 2000 <= window_ms <= 4000:
        confidence = Confidence.HIGH
    elif 1000 <= window_ms <= 6000:
        confidence = Confidence.MODERATE
    else:
        confidence = Confidence.LOW

    return CalibratedValue(
        value=tau_value,
        confidence=confidence,
        source="Temporal window normalization",
        empirical_measure=window_ms,
        notes=f"τ = {window_ms}ms / {TAU_BASELINE_MS}ms (Pöppel 1997 baseline)"
    )


def subjective_time_to_tau(description: str) -> CalibratedValue:
    """
    Map subjective time descriptions to τ.

    Used when precise measurements unavailable.

    Args:
        description: One of 'collapsed', 'fragmented', 'reduced',
                     'normal', 'extended', 'expanded', 'transcendent'

    Returns:
        CalibratedValue with τ
    """
    mappings = {
        "collapsed": (0.10, "No temporal continuity"),
        "fragmented": (0.25, "Broken temporal integration"),
        "reduced": (0.35, "Shortened temporal window"),
        "normal": (0.50, "Baseline 2-3 second window"),
        "moderate": (0.50, "Baseline temporal depth"),
        "extended": (0.70, "Subjectively expanded time"),
        "expanded": (0.80, "Significantly expanded temporal depth"),
        "transcendent": (0.90, "Reports of eternity/infinite time")
    }

    if description.lower() not in mappings:
        raise ValueError(f"Unknown description: {description}. "
                        f"Valid: {list(mappings.keys())}")

    value, notes = mappings[description.lower()]

    return CalibratedValue(
        value=value,
        confidence=Confidence.MODERATE,
        source="Subjective time mapping",
        notes=notes
    )


# =============================================================================
# φ (Phi): Structural Integration ← Effective Connectivity
# =============================================================================

# Baseline effective connectivity (waking state = 1.0 for relative measures)
PHI_BASELINE = 0.80  # Waking baseline in framework units

def effective_connectivity_to_phi(
    connectivity_ratio: float,
    baseline: float = PHI_BASELINE
) -> CalibratedValue:
    """
    Map effective connectivity ratio to φ (integration).

    Connectivity is measured relative to waking baseline.
    E.g., Ferrarelli (2010): propofol → 75% reduction → ratio = 0.25

    Args:
        connectivity_ratio: Ratio of connectivity to baseline (0-1+)
        baseline: Framework baseline for waking (default 0.80)

    Returns:
        CalibratedValue with φ
    """
    phi_value = _clamp(baseline * connectivity_ratio)

    return CalibratedValue(
        value=phi_value,
        confidence=Confidence.MODERATE,
        source="Effective connectivity ratio",
        empirical_measure=connectivity_ratio,
        notes=f"φ = {baseline} × {connectivity_ratio:.2f} (relative to waking)"
    )


def connectivity_reduction_to_phi(
    percent_reduction: float,
    baseline: float = PHI_BASELINE
) -> CalibratedValue:
    """
    Map connectivity reduction percentage to φ.

    E.g., 75% reduction under propofol (Ferrarelli 2010)

    Args:
        percent_reduction: Percent reduction from baseline (0-100)
        baseline: Framework baseline for waking

    Returns:
        CalibratedValue with φ
    """
    ratio = 1 - (percent_reduction / 100)
    phi_value = _clamp(baseline * ratio)

    return CalibratedValue(
        value=phi_value,
        confidence=Confidence.MODERATE,
        source="Connectivity reduction",
        empirical_measure=percent_reduction,
        notes=f"φ = {baseline} × (1 - {percent_reduction}%) (Ferrarelli 2010 method)"
    )


# =============================================================================
# κ (Kappa): Coherence ← Phase-Locking / Fractal Dimension
# =============================================================================

def coherence_descriptive_to_kappa(description: str) -> CalibratedValue:
    """
    Map coherence descriptions to κ.

    Used for phenomenologically-derived coherence estimates.

    Args:
        description: One of 'stereotyped', 'random', 'minimal', 'low',
                     'moderate', 'baseline', 'high', 'structured', 'hyperdimensional'

    Returns:
        CalibratedValue with κ
    """
    mappings = {
        "stereotyped": (0.10, "No structure in high entropy (seizure)"),
        "random": (0.20, "Meaning-destroying chaos (panic)"),
        "minimal": (0.20, "Very little structure"),
        "low": (0.30, "Limited patterning"),
        "moderate": (0.50, "Normal structured cognition"),
        "baseline": (0.50, "Waking baseline"),
        "high": (0.75, "Effortless order (flow)"),
        "structured": (0.80, "Meaningful novel combinations"),
        "fractal": (0.85, "Structured chaos (psychedelics)"),
        "hyperdimensional": (0.90, "Geometric meaningful visions (DMT)")
    }

    if description.lower() not in mappings:
        raise ValueError(f"Unknown description: {description}. "
                        f"Valid: {list(mappings.keys())}")

    value, notes = mappings[description.lower()]

    return CalibratedValue(
        value=value,
        confidence=Confidence.LOW,
        source="Phenomenological coherence mapping",
        notes=notes
    )


# =============================================================================
# Composite Functions
# =============================================================================

@dataclass
class GroundedState:
    """A consciousness state with empirically grounded variable values."""
    name: str
    phi: CalibratedValue
    tau: CalibratedValue
    rho: CalibratedValue
    H: CalibratedValue
    kappa: CalibratedValue
    citations: list
    notes: str = ""

    def density(self) -> float:
        """Calculate perspectival density using v9.2 formula."""
        phi = self.phi.value
        tau = self.tau.value
        rho = self.rho.value
        h = self.H.value
        kappa = self.kappa.value

        # D = φ × τ × ρ × [(1 - √H) + (H × κ)]
        structure = phi * tau * rho
        entropy_gate = (1 - math.sqrt(h)) + (h * kappa)
        return structure * entropy_gate

    def overall_confidence(self) -> Confidence:
        """Return lowest confidence among all variables."""
        confidences = [
            self.phi.confidence,
            self.tau.confidence,
            self.rho.confidence,
            self.H.confidence,
            self.kappa.confidence
        ]
        order = [Confidence.THEORETICAL, Confidence.LOW,
                 Confidence.MODERATE, Confidence.HIGH]
        return min(confidences, key=lambda c: order.index(c))

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "phi": self.phi.to_dict(),
            "tau": self.tau.to_dict(),
            "rho": self.rho.to_dict(),
            "H": self.H.to_dict(),
            "kappa": self.kappa.to_dict(),
            "density": self.density(),
            "overall_confidence": self.overall_confidence().value,
            "citations": self.citations,
            "notes": self.notes
        }


def create_grounded_state(
    name: str,
    pci: Optional[tuple] = None,
    lzc_change: Optional[float] = None,
    temporal_desc: Optional[str] = None,
    connectivity_reduction: Optional[float] = None,
    coherence_desc: Optional[str] = None,
    citations: Optional[list] = None,
    notes: str = "",
    # Manual overrides when empirical data unavailable
    phi_override: Optional[float] = None,
    tau_override: Optional[float] = None,
    rho_override: Optional[float] = None,
    H_override: Optional[float] = None,
    kappa_override: Optional[float] = None
) -> GroundedState:
    """
    Create a grounded consciousness state from empirical measurements.

    Args:
        name: State name
        pci: Tuple of (pci_min, pci_max) or single value
        lzc_change: Percent change from LZc baseline
        temporal_desc: Temporal depth description
        connectivity_reduction: Percent reduction in connectivity
        coherence_desc: Coherence description
        citations: List of citation keys
        notes: Additional notes
        *_override: Manual values when empirical data unavailable

    Returns:
        GroundedState with all calibrated values
    """
    # ρ from PCI
    if pci is not None:
        if isinstance(pci, tuple):
            rho = pci_range_to_rho(pci[0], pci[1])
        else:
            rho = pci_to_rho(pci)
    elif rho_override is not None:
        rho = CalibratedValue(rho_override, Confidence.LOW, "manual override")
    else:
        rho = CalibratedValue(0.50, Confidence.THEORETICAL, "no data")

    # H from LZc
    if lzc_change is not None:
        H = lzc_percent_change_to_H(lzc_change)
    elif H_override is not None:
        H = CalibratedValue(H_override, Confidence.LOW, "manual override")
    else:
        H = CalibratedValue(0.50, Confidence.THEORETICAL, "no data")

    # τ from temporal description
    if temporal_desc is not None:
        tau = subjective_time_to_tau(temporal_desc)
    elif tau_override is not None:
        tau = CalibratedValue(tau_override, Confidence.LOW, "manual override")
    else:
        tau = CalibratedValue(0.50, Confidence.THEORETICAL, "no data")

    # φ from connectivity
    if connectivity_reduction is not None:
        phi = connectivity_reduction_to_phi(connectivity_reduction)
    elif phi_override is not None:
        phi = CalibratedValue(phi_override, Confidence.LOW, "manual override")
    else:
        phi = CalibratedValue(0.80, Confidence.THEORETICAL, "no data")

    # κ from coherence description
    if coherence_desc is not None:
        kappa = coherence_descriptive_to_kappa(coherence_desc)
    elif kappa_override is not None:
        kappa = CalibratedValue(kappa_override, Confidence.LOW, "manual override")
    else:
        kappa = CalibratedValue(0.50, Confidence.THEORETICAL, "no data")

    return GroundedState(
        name=name,
        phi=phi,
        tau=tau,
        rho=rho,
        H=H,
        kappa=kappa,
        citations=citations or [],
        notes=notes
    )


# =============================================================================
# Pre-defined Grounded States
# =============================================================================

def get_calibrated_states() -> dict:
    """Return dictionary of pre-calibrated consciousness states."""

    states = {}

    # Wakefulness (Baseline)
    # UPDATED: PCI mean = 0.50 ± 0.05 (Casarotto 2016)
    states["wakefulness"] = create_grounded_state(
        name="Wakefulness (Baseline)",
        pci=(0.44, 0.67),  # Range from Casali 2013
        lzc_change=0,
        temporal_desc="normal",
        connectivity_reduction=0,
        coherence_desc="baseline",
        citations=["Casali2013", "Casarotto2016", "Schartner2017", "Poppel1997"],
        notes="Healthy adult, eyes open, resting state. PCI mean 0.50 ± 0.05"
    )

    # Propofol Anesthesia
    # UPDATED: PCI mean = 0.24 ± 0.07 (Sarasso 2015, Kim 2018)
    states["propofol_anesthesia"] = create_grounded_state(
        name="Propofol Anesthesia",
        pci=(0.12, 0.31),  # Range per Casali 2013, mean 0.24
        lzc_change=-30,
        temporal_desc="collapsed",
        connectivity_reduction=75,
        coherence_desc="minimal",
        citations=["Casali2013", "Sarasso2015", "Kim2018", "Ferrarelli2010", "Schartner2015"],
        notes="Surgical anesthesia level. PCI mean 0.24 ± 0.07"
    )

    # Xenon Anesthesia
    # NEW: Added from Compass research
    states["xenon_anesthesia"] = create_grounded_state(
        name="Xenon Anesthesia",
        pci=0.17,  # PCI mean = 0.17 ± 0.05 (Sarasso 2015)
        lzc_change=-35,
        temporal_desc="collapsed",
        connectivity_reduction=80,
        coherence_desc="minimal",
        citations=["Sarasso2015"],
        notes="Xenon anesthesia, lowest PCI among tested anesthetics. PCI mean 0.17 ± 0.05"
    )

    # Midazolam Anesthesia
    # NEW: Added from Compass research
    states["midazolam_anesthesia"] = create_grounded_state(
        name="Midazolam Anesthesia",
        pci=0.27,  # PCI mean = 0.27 ± 0.06 (Ferrarelli 2010)
        lzc_change=-25,
        temporal_desc="collapsed",
        connectivity_reduction=70,
        coherence_desc="minimal",
        citations=["Ferrarelli2010"],
        notes="Benzodiazepine anesthesia. PCI mean 0.27 ± 0.06"
    )

    # Ketamine Anesthesia
    # UPDATED: Compass research shows PCI mean = 0.44 ± 0.10 (Sarasso 2015)
    # Range 0.35-0.55 (higher than previously estimated 0.28-0.43)
    states["ketamine_anesthesia"] = create_grounded_state(
        name="Ketamine Anesthesia",
        pci=(0.35, 0.55),  # Updated from (0.28, 0.43) per Sarasso 2015 reanalysis
        lzc_change=10,  # Psychoactive effect increases entropy
        temporal_desc="fragmented",
        connectivity_reduction=40,
        coherence_desc="moderate",
        citations=["Sarasso2015", "Schartner2017", "Kim2018"],
        notes="Dissociative anesthesia, PCI mean 0.44 ± 0.10, maintains near-waking complexity"
    )

    # REM Sleep
    states["REM_sleep"] = create_grounded_state(
        name="REM Sleep",
        pci=(0.41, 0.48),
        lzc_change=-5,
        temporal_desc="moderate",
        connectivity_reduction=25,
        coherence_desc="moderate",
        citations=["Casali2013"],
        notes="Active dreaming state"
    )

    # NREM Sleep (N3)
    states["NREM_sleep_N3"] = create_grounded_state(
        name="NREM Sleep (N3)",
        pci=(0.18, 0.28),
        lzc_change=-20,
        temporal_desc="reduced",
        connectivity_reduction=50,
        coherence_desc="low",
        citations=["Casali2013", "Massimini2005", "Schartner2015"],
        notes="Deep slow-wave sleep"
    )

    # Vegetative State (UWS)
    states["vegetative_state"] = create_grounded_state(
        name="Vegetative State (UWS)",
        pci=(0.19, 0.38),
        lzc_change=-25,
        temporal_desc="fragmented",
        connectivity_reduction=75,
        coherence_desc="low",
        citations=["Casali2013"],
        notes="Unresponsive wakefulness syndrome"
    )

    # Minimally Conscious State
    states["minimally_conscious"] = create_grounded_state(
        name="Minimally Conscious State (MCS)",
        pci=(0.32, 0.49),
        lzc_change=-15,
        temporal_desc="fragmented",
        connectivity_reduction=50,
        coherence_desc="moderate",
        citations=["Casali2013"],
        notes="Preserved but inconsistent awareness"
    )

    # Locked-in Syndrome
    states["locked_in_syndrome"] = create_grounded_state(
        name="Locked-in Syndrome",
        pci=(0.51, 0.62),
        lzc_change=0,
        temporal_desc="normal",
        connectivity_reduction=0,
        coherence_desc="baseline",
        citations=["Casali2013"],
        notes="Full consciousness, motor disconnection only"
    )

    # Psilocybin Peak
    states["psilocybin"] = create_grounded_state(
        name="Psilocybin (Peak)",
        pci=None,  # No PCI data for psychedelics
        lzc_change=18,
        temporal_desc="extended",
        connectivity_reduction=-10,  # Negative = increased cross-network
        coherence_desc="fractal",
        citations=["Schartner2017", "CarhartHarris2014", "Tagliazucchi2014"],
        notes="Peak psychedelic experience, high entropy but structured",
        rho_override=0.60  # Estimated: binding maintained
    )

    # LSD Peak
    states["LSD"] = create_grounded_state(
        name="LSD (Peak)",
        pci=None,
        lzc_change=15,
        temporal_desc="extended",
        connectivity_reduction=-10,
        coherence_desc="fractal",
        citations=["Schartner2017", "CarhartHarris2014"],
        notes="Peak psychedelic experience",
        rho_override=0.60
    )

    # DMT Breakthrough
    states["DMT_breakthrough"] = create_grounded_state(
        name="DMT Breakthrough",
        pci=None,
        lzc_change=40,  # Extrapolated
        temporal_desc="transcendent",
        connectivity_reduction=-20,
        coherence_desc="hyperdimensional",
        citations=["CarhartHarris2014"],
        notes="Extreme state, extrapolated from psilocybin data",
        rho_override=0.70
    )

    # Flow State
    states["flow_state"] = create_grounded_state(
        name="Flow State",
        pci=None,
        lzc_change=-10,  # Reduced entropy, high focus
        temporal_desc="extended",
        connectivity_reduction=-15,  # Enhanced integration
        coherence_desc="high",
        citations=["Csikszentmihalyi1990"],
        notes="Optimal performance state, phenomenologically derived",
        rho_override=0.70
    )

    # Deep Meditation
    states["deep_meditation"] = create_grounded_state(
        name="Deep Meditation",
        pci=None,
        lzc_change=-15,
        temporal_desc="expanded",
        connectivity_reduction=-10,
        coherence_desc="high",
        citations=["Wittmann2015"],
        notes="Experienced meditators, long-term practice",
        rho_override=0.65
    )

    # Panic Attack
    # REVISED: Panic is hyper-conscious, not barely conscious
    # High ρ: acute self-awareness, hyper-vigilant recursive monitoring
    # High φ: everything feels connected to threat, global alarm state
    # Moderate τ: time distorted but continuity maintained
    # High H: racing thoughts, unpredictable state trajectory
    # Low κ: chaos is random, meaning-destroying (not structured like DMT)
    states["panic_attack"] = create_grounded_state(
        name="Panic Attack",
        pci=None,
        lzc_change=35,  # High entropy - racing thoughts
        temporal_desc="moderate",  # Time distorted but continuous
        connectivity_reduction=-10,  # INCREASED connectivity - global alarm
        coherence_desc="random",  # Unstructured chaos
        citations=[],
        notes="Hyper-conscious terror: high binding, high integration, unstructured entropy",
        rho_override=0.70  # HIGH - acute self-awareness
    )

    # Epileptic Seizure
    states["epileptic_seizure"] = create_grounded_state(
        name="Epileptic Seizure (Generalized)",
        pci=None,
        lzc_change=-50,  # Hypersynchronous = low complexity
        temporal_desc="collapsed",
        connectivity_reduction=0,  # Hypersynchronous connectivity
        coherence_desc="stereotyped",
        citations=[],
        notes="Hypersynchronous activity, high entropy spread but no structure",
        rho_override=0.15,
        H_override=0.70  # High entropy despite low LZc (stereotyped but unpredictable spread)
    )

    return states


# =============================================================================
# Utility Functions
# =============================================================================

def export_grounded_states_json(output_path: str = None) -> str:
    """Export all grounded states to JSON."""
    states = get_calibrated_states()

    output = {
        "metadata": {
            "version": "1.1",
            "date": "2026-01-17",
            "framework": "Conduit Monism v9.2",
            "description": "Empirically grounded consciousness states",
            "changes": "Integrated Compass research: Ketamine PCI=0.44, added xenon/midazolam, PCI* threshold 0.31"
        },
        "states": {name: state.to_dict() for name, state in states.items()}
    }

    json_str = json.dumps(output, indent=2)

    if output_path:
        with open(output_path, 'w') as f:
            f.write(json_str)

    return json_str


def compare_grounded_vs_estimated(name: str, estimated_values: dict) -> dict:
    """
    Compare grounded values with original estimates.

    Args:
        name: State name
        estimated_values: Dict with phi, tau, rho, H, kappa estimates

    Returns:
        Comparison dict with deltas and density difference
    """
    states = get_calibrated_states()

    if name not in states:
        raise ValueError(f"State '{name}' not found in calibrated states")

    grounded = states[name]

    # Calculate estimated density
    e = estimated_values
    est_structure = e['phi'] * e['tau'] * e['rho']
    est_entropy_gate = (1 - math.sqrt(e['H'])) + (e['H'] * e['kappa'])
    est_density = est_structure * est_entropy_gate

    return {
        "state": name,
        "estimated": {
            "phi": e['phi'],
            "tau": e['tau'],
            "rho": e['rho'],
            "H": e['H'],
            "kappa": e['kappa'],
            "density": est_density
        },
        "grounded": {
            "phi": grounded.phi.value,
            "tau": grounded.tau.value,
            "rho": grounded.rho.value,
            "H": grounded.H.value,
            "kappa": grounded.kappa.value,
            "density": grounded.density()
        },
        "delta": {
            "phi": grounded.phi.value - e['phi'],
            "tau": grounded.tau.value - e['tau'],
            "rho": grounded.rho.value - e['rho'],
            "H": grounded.H.value - e['H'],
            "kappa": grounded.kappa.value - e['kappa'],
            "density": grounded.density() - est_density
        },
        "confidence": grounded.overall_confidence().value
    }


if __name__ == "__main__":
    # Demo: Print all grounded states
    print("=" * 60)
    print("CONDUIT MONISM: Empirically Grounded States")
    print("=" * 60)

    states = get_calibrated_states()

    for name, state in states.items():
        print(f"\n{state.name}")
        print("-" * 40)
        print(f"  φ (Integration):    {state.phi.value:.2f} [{state.phi.confidence.value}]")
        print(f"  τ (Temporal):       {state.tau.value:.2f} [{state.tau.confidence.value}]")
        print(f"  ρ (Binding):        {state.rho.value:.2f} [{state.rho.confidence.value}]")
        print(f"  H (Entropy):        {state.H.value:.2f} [{state.H.confidence.value}]")
        print(f"  κ (Coherence):      {state.kappa.value:.2f} [{state.kappa.confidence.value}]")
        print(f"  D (Density):        {state.density():.4f}")
        print(f"  Overall Confidence: {state.overall_confidence().value}")
        print(f"  Citations:          {', '.join(state.citations) or 'None'}")
