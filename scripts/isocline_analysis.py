"""
Isocline Degeneracy Analysis for Conduit Monism v9.2

This experiment systematically identifies "isocline degeneracies" -- pairs of
phenomenologically distinct consciousness states that produce identical or
near-identical D values under the formula:

    D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]

Because 5 inputs collapse to 1 scalar output, the formula necessarily loses
4 dimensions of variation. This script maps the full geometry of that loss.

Experiment ID: 260222_IDA
Date: 2026-02-22
Framework: Conduit Monism v9.2
"""

import math
import json
import itertools
import os
import sys
from datetime import datetime
from collections import defaultdict

import numpy as np

# ---------------------------------------------------------------------------
# Core formula
# ---------------------------------------------------------------------------

def density(phi, tau, rho, H, kappa):
    """Compute v9.2 perspectival density (vectorized-safe)."""
    structure = phi * tau * rho
    entropy_gate = (1.0 - np.sqrt(H)) + (H * kappa)
    return structure * entropy_gate


# ---------------------------------------------------------------------------
# Calibrated canonical states from CANON.md (lines 338-348)
# ---------------------------------------------------------------------------

CANONICAL_STATES = {
    "Wakefulness":  {"phi": 0.80, "tau": 0.75, "rho": 0.65, "H": 0.50, "kappa": 0.65},
    "REM Sleep":    {"phi": 0.60, "tau": 0.50, "rho": 0.45, "H": 0.55, "kappa": 0.55},
    "NREM N3":      {"phi": 0.40, "tau": 0.15, "rho": 0.23, "H": 0.40, "kappa": 0.30},
    "Propofol":     {"phi": 0.25, "tau": 0.10, "rho": 0.24, "H": 0.35, "kappa": 0.20},
    "Ketamine":     {"phi": 0.50, "tau": 0.50, "rho": 0.44, "H": 0.55, "kappa": 0.80},
    "Psilocybin":   {"phi": 0.70, "tau": 0.65, "rho": 0.55, "H": 0.60, "kappa": 0.85},
    "DMT":          {"phi": 0.85, "tau": 0.90, "rho": 0.70, "H": 0.70, "kappa": 0.90},
    "Flow":         {"phi": 0.90, "tau": 0.70, "rho": 0.65, "H": 0.55, "kappa": 0.75},
    "Meditation":   {"phi": 0.85, "tau": 0.80, "rho": 0.70, "H": 0.40, "kappa": 0.80},
}

# Additional states from calibration library for degeneracy tests
EXTENDED_STATES = {
    "Panic Attack":     {"phi": 0.88, "tau": 0.50, "rho": 0.70, "H": 0.675, "kappa": 0.20},
    "Light Anesthesia": {"phi": 0.40, "tau": 0.25, "rho": 0.35, "H": 0.40, "kappa": 0.30},
    "Drowsiness":       {"phi": 0.65, "tau": 0.40, "rho": 0.50, "H": 0.45, "kappa": 0.45},
    "Epileptic Seizure":{"phi": 0.80, "tau": 0.10, "rho": 0.15, "H": 0.70, "kappa": 0.10},
    "Locked-in":        {"phi": 0.80, "tau": 0.75, "rho": 0.57, "H": 0.50, "kappa": 0.50},
    "Vegetative (UWS)": {"phi": 0.20, "tau": 0.25, "rho": 0.29, "H": 0.375, "kappa": 0.30},
    "MCS":              {"phi": 0.40, "tau": 0.25, "rho": 0.41, "H": 0.425, "kappa": 0.50},
}

ALL_STATES = {**CANONICAL_STATES, **EXTENDED_STATES}


def compute_state_D(state_dict):
    """Compute D for a state dictionary."""
    return density(
        state_dict["phi"], state_dict["tau"], state_dict["rho"],
        state_dict["H"], state_dict["kappa"]
    )


# ---------------------------------------------------------------------------
# 1. Dense grid sampling
# ---------------------------------------------------------------------------

def generate_grid(resolution=21):
    """
    Generate a dense grid of states in [0,1]^5.
    resolution=21 gives 0.00, 0.05, 0.10, ..., 1.00 per axis.
    Total points: 21^5 = 4,084,101
    """
    axis = np.linspace(0.0, 1.0, resolution)
    print(f"  Grid resolution: {resolution} points per axis")
    print(f"  Total grid points: {resolution**5:,}")

    # Use meshgrid for vectorized computation
    phi, tau, rho, H, kappa = np.meshgrid(axis, axis, axis, axis, axis, indexing='ij')
    phi_flat = phi.ravel()
    tau_flat = tau.ravel()
    rho_flat = rho.ravel()
    H_flat = H.ravel()
    kappa_flat = kappa.ravel()

    D_flat = density(phi_flat, tau_flat, rho_flat, H_flat, kappa_flat)

    return phi_flat, tau_flat, rho_flat, H_flat, kappa_flat, D_flat


# ---------------------------------------------------------------------------
# 2. Isocline extraction at specific D levels
# ---------------------------------------------------------------------------

def extract_isocline(phi, tau, rho, H, kappa, D_all, target_D, tolerance=0.005):
    """Find all grid points within tolerance of target D."""
    mask = np.abs(D_all - target_D) <= tolerance
    n_hits = np.sum(mask)
    return {
        "phi": phi[mask],
        "tau": tau[mask],
        "rho": rho[mask],
        "H": H[mask],
        "kappa": kappa[mask],
        "D": D_all[mask],
        "count": int(n_hits),
        "fraction": float(n_hits) / len(D_all),
    }


# ---------------------------------------------------------------------------
# 3. Phenomenological classification
# ---------------------------------------------------------------------------

def classify_profile(phi, tau, rho, H, kappa):
    """
    Classify a parameter vector into a phenomenological profile string.
    Uses threshold of 0.5 as boundary between 'low' and 'high'.
    """
    labels = []
    if H < 0.35:
        labels.append("low-entropy")
    elif H > 0.65:
        labels.append("high-entropy")
    else:
        labels.append("mid-entropy")

    if kappa < 0.35:
        labels.append("incoherent")
    elif kappa > 0.65:
        labels.append("coherent")
    else:
        labels.append("mid-coherence")

    if phi > 0.65:
        labels.append("integrated")
    elif phi < 0.35:
        labels.append("fragmented")
    else:
        labels.append("mid-integration")

    if tau > 0.65:
        labels.append("deep-temporal")
    elif tau < 0.35:
        labels.append("shallow-temporal")
    else:
        labels.append("mid-temporal")

    if rho > 0.65:
        labels.append("bound")
    elif rho < 0.35:
        labels.append("unbound")
    else:
        labels.append("mid-binding")

    return "|".join(labels)


def profile_distribution(isocline):
    """Classify all points on an isocline by phenomenological profile."""
    profiles = defaultdict(int)
    n = isocline["count"]
    if n == 0:
        return profiles

    for i in range(n):
        p = classify_profile(
            isocline["phi"][i], isocline["tau"][i], isocline["rho"][i],
            isocline["H"][i], isocline["kappa"][i]
        )
        profiles[p] += 1

    return dict(profiles)


# ---------------------------------------------------------------------------
# 4. Degeneracy pair detection
# ---------------------------------------------------------------------------

def euclidean_distance_5d(s1, s2):
    """Euclidean distance in 5D parameter space."""
    return math.sqrt(
        (s1["phi"] - s2["phi"])**2 +
        (s1["tau"] - s2["tau"])**2 +
        (s1["rho"] - s2["rho"])**2 +
        (s1["H"] - s2["H"])**2 +
        (s1["kappa"] - s2["kappa"])**2
    )


def find_maximum_degeneracy(isocline, n_samples=5000):
    """
    Find the pair of points on the isocline with maximum 5D distance.
    This represents the most phenomenologically distant pair sharing the same D.
    """
    n = isocline["count"]
    if n < 2:
        return None

    # Sample if too many points
    if n > n_samples:
        idx = np.random.choice(n, n_samples, replace=False)
    else:
        idx = np.arange(n)

    points = np.column_stack([
        isocline["phi"][idx],
        isocline["tau"][idx],
        isocline["rho"][idx],
        isocline["H"][idx],
        isocline["kappa"][idx],
    ])

    # Find maximum pairwise distance efficiently
    max_dist = 0.0
    best_pair = (None, None)

    # Use random sampling of pairs for large sets
    n_pts = len(points)
    if n_pts > 500:
        # Sample 50000 random pairs
        n_pairs = min(50000, n_pts * (n_pts - 1) // 2)
        for _ in range(n_pairs):
            i, j = np.random.choice(n_pts, 2, replace=False)
            d = np.linalg.norm(points[i] - points[j])
            if d > max_dist:
                max_dist = d
                best_pair = (
                    {k: float(v) for k, v in zip(
                        ["phi", "tau", "rho", "H", "kappa"], points[i])},
                    {k: float(v) for k, v in zip(
                        ["phi", "tau", "rho", "H", "kappa"], points[j])}
                )
    else:
        for i in range(n_pts):
            for j in range(i + 1, n_pts):
                d = np.linalg.norm(points[i] - points[j])
                if d > max_dist:
                    max_dist = d
                    best_pair = (
                        {k: float(v) for k, v in zip(
                            ["phi", "tau", "rho", "H", "kappa"], points[i])},
                        {k: float(v) for k, v in zip(
                            ["phi", "tau", "rho", "H", "kappa"], points[j])}
                    )

    return {
        "distance_5d": float(max_dist),
        "max_possible": math.sqrt(5),  # diagonal of unit 5-cube
        "degeneracy_ratio": float(max_dist) / math.sqrt(5),
        "point_a": best_pair[0],
        "point_b": best_pair[1],
        "profile_a": classify_profile(**best_pair[0]) if best_pair[0] else None,
        "profile_b": classify_profile(**best_pair[1]) if best_pair[1] else None,
    }


# ---------------------------------------------------------------------------
# 5. Specific pair tests
# ---------------------------------------------------------------------------

SPECIFIC_PAIRS = [
    ("Meditation", "Light Anesthesia"),
    ("REM Sleep", "Ketamine"),
    ("Panic Attack", "Drowsiness"),
    ("Flow", "Psilocybin"),
    ("Wakefulness", "Locked-in"),
    ("NREM N3", "Vegetative (UWS)"),
    ("DMT", "Meditation"),
    ("Epileptic Seizure", "Propofol"),
]


def test_specific_pairs():
    """Test D-distance between phenomenologically distinct state pairs."""
    results = []
    for name_a, name_b in SPECIFIC_PAIRS:
        if name_a not in ALL_STATES or name_b not in ALL_STATES:
            continue
        sa, sb = ALL_STATES[name_a], ALL_STATES[name_b]
        Da = compute_state_D(sa)
        Db = compute_state_D(sb)
        dist_5d = euclidean_distance_5d(sa, sb)
        results.append({
            "state_a": name_a,
            "state_b": name_b,
            "D_a": float(Da),
            "D_b": float(Db),
            "D_difference": float(abs(Da - Db)),
            "distance_5d": float(dist_5d),
            "params_a": sa,
            "params_b": sb,
            "profile_a": classify_profile(**sa),
            "profile_b": classify_profile(**sb),
            "degeneracy_severity": "CRITICAL" if abs(Da - Db) < 0.01 else
                                   "HIGH" if abs(Da - Db) < 0.03 else
                                   "MODERATE" if abs(Da - Db) < 0.05 else "LOW",
        })

    results.sort(key=lambda x: x["D_difference"])
    return results


# ---------------------------------------------------------------------------
# 6. Isocline volume and dimensionality analysis
# ---------------------------------------------------------------------------

def compute_isocline_volumes(D_all, n_bins=100):
    """
    Compute the fraction of parameter space mapping to each D level.
    This gives the 'isocline volume' -- how degenerate each D level is.
    """
    # Filter out D=0 (trivial degeneracy when any multiplicative term is 0)
    D_nonzero = D_all[D_all > 0.001]
    D_max = np.max(D_all)

    bins = np.linspace(0.0, D_max, n_bins + 1)
    counts, edges = np.histogram(D_all, bins=bins)
    total = len(D_all)

    volumes = []
    for i in range(len(counts)):
        d_center = (edges[i] + edges[i + 1]) / 2.0
        volumes.append({
            "D_center": float(d_center),
            "D_range": (float(edges[i]), float(edges[i + 1])),
            "count": int(counts[i]),
            "fraction": float(counts[i]) / total,
        })

    return volumes


def compute_sensitivity_analysis():
    """
    For each canonical state, compute partial derivatives of D with respect
    to each parameter. This reveals which dimensions are most/least
    informative at each state.
    """
    delta = 0.001
    results = {}

    for name, s in ALL_STATES.items():
        D0 = compute_state_D(s)
        partials = {}

        for param in ["phi", "tau", "rho", "H", "kappa"]:
            s_plus = dict(s)
            s_minus = dict(s)
            val = s[param]

            # Central difference when possible
            if val + delta <= 1.0 and val - delta >= 0.0:
                s_plus[param] = val + delta
                s_minus[param] = val - delta
                dD = (compute_state_D(s_plus) - compute_state_D(s_minus)) / (2 * delta)
            elif val + delta <= 1.0:
                s_plus[param] = val + delta
                dD = (compute_state_D(s_plus) - D0) / delta
            else:
                s_minus[param] = val - delta
                dD = (D0 - compute_state_D(s_minus)) / delta

            partials[param] = float(dD)

        # Normalized sensitivities (fraction of total gradient magnitude)
        grad_mag = math.sqrt(sum(v**2 for v in partials.values()))
        normalized = {}
        if grad_mag > 0:
            for k, v in partials.items():
                normalized[k] = abs(v) / grad_mag
        else:
            normalized = {k: 0.0 for k in partials}

        results[name] = {
            "D": float(D0),
            "partials": partials,
            "gradient_magnitude": float(grad_mag),
            "normalized_sensitivity": normalized,
            "least_sensitive": min(normalized, key=normalized.get),
            "most_sensitive": max(normalized, key=normalized.get),
        }

    return results


# ---------------------------------------------------------------------------
# 7. Information loss quantification
# ---------------------------------------------------------------------------

def compute_information_loss():
    """
    Quantify information loss by measuring how much of the 5D variance
    is captured by D alone.

    Method: sample random states, compute D, then measure the variance
    in each parameter conditional on D being in a narrow band.
    """
    np.random.seed(42)
    n_samples = 500000
    phi = np.random.uniform(0, 1, n_samples)
    tau = np.random.uniform(0, 1, n_samples)
    rho = np.random.uniform(0, 1, n_samples)
    H = np.random.uniform(0, 1, n_samples)
    kappa = np.random.uniform(0, 1, n_samples)
    D = density(phi, tau, rho, H, kappa)

    # Overall variance of each parameter
    overall_var = {
        "phi": float(np.var(phi)),
        "tau": float(np.var(tau)),
        "rho": float(np.var(rho)),
        "H": float(np.var(H)),
        "kappa": float(np.var(kappa)),
    }

    # Conditional variance: for points with D in a narrow band,
    # how much variance remains in each parameter?
    target_bands = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
    band_width = 0.005

    conditional_results = {}
    for target in target_bands:
        mask = np.abs(D - target) <= band_width
        n_in_band = np.sum(mask)
        if n_in_band < 10:
            continue

        cond_var = {
            "phi": float(np.var(phi[mask])),
            "tau": float(np.var(tau[mask])),
            "rho": float(np.var(rho[mask])),
            "H": float(np.var(H[mask])),
            "kappa": float(np.var(kappa[mask])),
        }

        # Variance retained = conditional / overall
        retained = {k: cond_var[k] / overall_var[k] if overall_var[k] > 0 else 0
                    for k in cond_var}

        conditional_results[f"D={target:.2f}"] = {
            "n_points": int(n_in_band),
            "conditional_variance": cond_var,
            "variance_retained_fraction": retained,
            "mean_retention": float(np.mean(list(retained.values()))),
            "interpretation": (
                "Knowing D barely constrains parameters"
                if np.mean(list(retained.values())) > 0.7
                else "D provides moderate constraint"
                if np.mean(list(retained.values())) > 0.4
                else "D significantly constrains parameters"
            ),
        }

    return {
        "overall_variance": overall_var,
        "conditional_analysis": conditional_results,
    }


# ---------------------------------------------------------------------------
# 8. Trade-off surface analysis: H-kappa exchange
# ---------------------------------------------------------------------------

def analyze_H_kappa_tradeoff():
    """
    The entropy gate g(H, kappa) = (1 - sqrt(H)) + H*kappa allows H and kappa
    to trade off against each other. This function maps the full trade-off
    surface to show when low-H/low-kappa states are indistinguishable from
    high-H/high-kappa states.
    """
    H_vals = np.linspace(0.0, 1.0, 201)
    kappa_vals = np.linspace(0.0, 1.0, 201)
    H_grid, K_grid = np.meshgrid(H_vals, kappa_vals, indexing='ij')

    gate_grid = (1.0 - np.sqrt(H_grid)) + (H_grid * K_grid)

    # Find iso-gate curves: for each gate value, find all (H, kappa) pairs
    target_gates = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    iso_gate_curves = {}
    for g_target in target_gates:
        mask = np.abs(gate_grid - g_target) < 0.005
        if np.sum(mask) > 0:
            h_on_curve = H_grid[mask]
            k_on_curve = K_grid[mask]
            iso_gate_curves[f"g={g_target:.1f}"] = {
                "n_points": int(np.sum(mask)),
                "H_range": (float(np.min(h_on_curve)), float(np.max(h_on_curve))),
                "kappa_range": (float(np.min(k_on_curve)), float(np.max(k_on_curve))),
                "H_spread": float(np.max(h_on_curve) - np.min(h_on_curve)),
                "kappa_spread": float(np.max(k_on_curve) - np.min(k_on_curve)),
            }

    # Gate value at canonical states
    canonical_gates = {}
    for name, s in CANONICAL_STATES.items():
        g = (1.0 - math.sqrt(s["H"])) + (s["H"] * s["kappa"])
        canonical_gates[name] = {
            "H": s["H"],
            "kappa": s["kappa"],
            "gate_value": float(g),
        }

    return {
        "gate_range": (float(np.min(gate_grid)), float(np.max(gate_grid))),
        "iso_gate_curves": iso_gate_curves,
        "canonical_gates": canonical_gates,
    }


# ---------------------------------------------------------------------------
# 9. Construct maximally absurd degeneracies
# ---------------------------------------------------------------------------

def find_absurd_degeneracies():
    """
    For each canonical state, find the most phenomenologically OPPOSITE state
    that shares the same D value (within tolerance).

    Strategy: fix D, then search for parameter vectors that maximize some
    measure of phenomenological dissimilarity.
    """
    np.random.seed(123)
    n_search = 2000000
    phi_r = np.random.uniform(0, 1, n_search)
    tau_r = np.random.uniform(0, 1, n_search)
    rho_r = np.random.uniform(0, 1, n_search)
    H_r = np.random.uniform(0, 1, n_search)
    kappa_r = np.random.uniform(0, 1, n_search)
    D_r = density(phi_r, tau_r, rho_r, H_r, kappa_r)

    absurd_pairs = []

    for name, s in CANONICAL_STATES.items():
        D_target = compute_state_D(s)
        tolerance = 0.005

        mask = np.abs(D_r - D_target) <= tolerance
        if np.sum(mask) < 5:
            continue

        s_vec = np.array([s["phi"], s["tau"], s["rho"], s["H"], s["kappa"]])
        candidates = np.column_stack([
            phi_r[mask], tau_r[mask], rho_r[mask], H_r[mask], kappa_r[mask]
        ])

        # Find the candidate most distant from the canonical state
        dists = np.linalg.norm(candidates - s_vec, axis=1)
        best_idx = np.argmax(dists)
        best = candidates[best_idx]

        match_dict = {k: float(v) for k, v in zip(
            ["phi", "tau", "rho", "H", "kappa"], best)}
        match_D = float(density(best[0], best[1], best[2], best[3], best[4]))

        absurd_pairs.append({
            "canonical_state": name,
            "canonical_params": s,
            "canonical_D": float(D_target),
            "degenerate_params": match_dict,
            "degenerate_D": match_D,
            "distance_5d": float(dists[best_idx]),
            "degeneracy_ratio": float(dists[best_idx]) / math.sqrt(5),
            "canonical_profile": classify_profile(**s),
            "degenerate_profile": classify_profile(**match_dict),
            "phenomenological_description": describe_degeneracy(s, match_dict, name),
        })

    absurd_pairs.sort(key=lambda x: x["distance_5d"], reverse=True)
    return absurd_pairs


def describe_degeneracy(canon, degen, name):
    """Generate a human-readable description of why a degeneracy is absurd."""
    diffs = []
    if abs(canon["H"] - degen["H"]) > 0.3:
        if canon["H"] < degen["H"]:
            diffs.append(f"orderly ({name}) vs chaotic (degenerate)")
        else:
            diffs.append(f"chaotic ({name}) vs orderly (degenerate)")

    if abs(canon["kappa"] - degen["kappa"]) > 0.3:
        if canon["kappa"] > degen["kappa"]:
            diffs.append(f"meaningful structure ({name}) vs random noise (degenerate)")
        else:
            diffs.append(f"random noise ({name}) vs meaningful structure (degenerate)")

    if abs(canon["phi"] - degen["phi"]) > 0.3:
        if canon["phi"] > degen["phi"]:
            diffs.append(f"unified ({name}) vs fragmented (degenerate)")
        else:
            diffs.append(f"fragmented ({name}) vs unified (degenerate)")

    if abs(canon["tau"] - degen["tau"]) > 0.3:
        if canon["tau"] > degen["tau"]:
            diffs.append(f"temporally deep ({name}) vs momentary (degenerate)")
        else:
            diffs.append(f"momentary ({name}) vs temporally deep (degenerate)")

    if abs(canon["rho"] - degen["rho"]) > 0.3:
        if canon["rho"] > degen["rho"]:
            diffs.append(f"tightly bound ({name}) vs loosely bound (degenerate)")
        else:
            diffs.append(f"loosely bound ({name}) vs tightly bound (degenerate)")

    if not diffs:
        return "Parameters differ but not dramatically."
    return "; ".join(diffs)


# ---------------------------------------------------------------------------
# 10. D=0 analysis (trivial degeneracy)
# ---------------------------------------------------------------------------

def analyze_D_zero():
    """
    D = 0 whenever phi=0 OR tau=0 OR rho=0. This is the largest degeneracy
    in the formula. Quantify exactly what fraction of parameter space maps to D=0.
    """
    # Analytical: P(D=0) = P(phi=0 OR tau=0 OR rho=0)
    # On a continuous grid with resolution n, the fraction is:
    # 1 - ((n-1)/n)^3 for the multiplicative terms (if any is 0)
    # But on the continuous [0,1] interval, the probability is exactly 0
    # (measure-zero set). On a discrete grid, it depends on whether 0 is included.

    # More interesting: what fraction has D < epsilon for small epsilon?
    np.random.seed(99)
    n = 1000000
    phi = np.random.uniform(0, 1, n)
    tau = np.random.uniform(0, 1, n)
    rho = np.random.uniform(0, 1, n)
    H = np.random.uniform(0, 1, n)
    kappa = np.random.uniform(0, 1, n)
    D = density(phi, tau, rho, H, kappa)

    thresholds = [0.001, 0.005, 0.01, 0.02, 0.05, 0.10]
    near_zero = {}
    for t in thresholds:
        frac = float(np.mean(D < t))
        near_zero[f"D<{t}"] = {
            "fraction": frac,
            "percentage": f"{frac*100:.2f}%",
        }

    # Median and percentiles
    return {
        "D_median": float(np.median(D)),
        "D_mean": float(np.mean(D)),
        "D_std": float(np.std(D)),
        "D_percentiles": {
            "5th": float(np.percentile(D, 5)),
            "25th": float(np.percentile(D, 25)),
            "50th": float(np.percentile(D, 50)),
            "75th": float(np.percentile(D, 75)),
            "95th": float(np.percentile(D, 95)),
        },
        "near_zero_fractions": near_zero,
    }


# ===========================================================================
# MAIN EXECUTION
# ===========================================================================

def main():
    print("=" * 70)
    print("ISOCLINE DEGENERACY ANALYSIS")
    print("Conduit Monism v9.2 -- Experiment 260222_IDA")
    print("=" * 70)
    print()

    results = {
        "metadata": {
            "experiment_id": "260222_IDA",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "framework": "Conduit Monism v9.2",
            "formula": "D = phi * tau * rho * [(1 - sqrt(H)) + (H * kappa)]",
            "purpose": "Identify and analyze isocline degeneracies where phenomenologically distinct states share identical D values",
        }
    }

    # --- Step 0: Compute D for all canonical states ---
    print("[0] Computing D for canonical states...")
    canonical_D = {}
    for name, s in ALL_STATES.items():
        d = compute_state_D(s)
        canonical_D[name] = {"params": s, "D": float(d)}
        print(f"    {name:25s}  D = {d:.6f}")
    results["canonical_states"] = canonical_D
    print()

    # --- Step 1: Dense grid ---
    print("[1] Generating dense grid (resolution=21 per axis)...")
    phi, tau, rho, H, kappa, D_all = generate_grid(resolution=21)
    print(f"    D range: [{np.min(D_all):.6f}, {np.max(D_all):.6f}]")
    print(f"    D mean: {np.mean(D_all):.6f}")
    print(f"    D median: {np.median(D_all):.6f}")
    print()

    # --- Step 2: Isocline extraction at canonical D levels ---
    target_D_values = [
        ("REM/Ketamine", 0.077),
        ("Wakefulness", 0.241),
        ("Meditation", 0.327),
        ("Psilocybin", 0.184),
        ("DMT", 0.425),
        ("Flow", 0.275),
        ("Low (NREM)", 0.007),
    ]
    print("[2] Extracting isoclines at canonical D levels (tolerance=0.005)...")
    isocline_results = {}
    for label, d_target in target_D_values:
        iso = extract_isocline(phi, tau, rho, H, kappa, D_all, d_target, tolerance=0.005)
        profiles = profile_distribution(iso)
        n_profiles = len(profiles)

        print(f"    D={d_target:.3f} ({label}): {iso['count']:,} states, "
              f"{n_profiles} distinct profiles, "
              f"volume fraction = {iso['fraction']:.6f}")

        # Find max degeneracy on this isocline
        max_degen = None
        if iso["count"] > 1:
            max_degen = find_maximum_degeneracy(iso)
            if max_degen:
                print(f"      Max 5D distance on isocline: {max_degen['distance_5d']:.4f} "
                      f"({max_degen['degeneracy_ratio']*100:.1f}% of max)")
                print(f"      Profile A: {max_degen['profile_a']}")
                print(f"      Profile B: {max_degen['profile_b']}")

        isocline_results[f"D={d_target:.3f} ({label})"] = {
            "target_D": d_target,
            "count": iso["count"],
            "volume_fraction": iso["fraction"],
            "n_distinct_profiles": n_profiles,
            "top_profiles": dict(sorted(profiles.items(), key=lambda x: -x[1])[:10]),
            "max_degeneracy": max_degen,
        }
    results["isocline_analysis"] = isocline_results
    print()

    # --- Step 3: Specific pair tests ---
    print("[3] Testing specific phenomenological pairs...")
    pair_results = test_specific_pairs()
    for p in pair_results:
        severity = p["degeneracy_severity"]
        marker = "***" if severity in ("CRITICAL", "HIGH") else "   "
        print(f"  {marker} {p['state_a']:20s} vs {p['state_b']:20s}  "
              f"|dD| = {p['D_difference']:.6f}  "
              f"dist_5D = {p['distance_5d']:.4f}  [{severity}]")
    results["specific_pairs"] = pair_results
    print()

    # --- Step 4: Isocline volumes ---
    print("[4] Computing isocline volume distribution...")
    volumes = compute_isocline_volumes(D_all, n_bins=50)
    peak_vol = max(volumes, key=lambda x: x["fraction"])
    print(f"    Peak volume at D ~ {peak_vol['D_center']:.3f}: "
          f"{peak_vol['fraction']*100:.2f}% of space")
    results["isocline_volumes"] = volumes
    print()

    # --- Step 5: Sensitivity analysis ---
    print("[5] Computing parameter sensitivity at each state...")
    sensitivity = compute_sensitivity_analysis()
    for name, s in sensitivity.items():
        print(f"    {name:25s}  most={s['most_sensitive']}, "
              f"least={s['least_sensitive']}, |grad|={s['gradient_magnitude']:.4f}")
    results["sensitivity_analysis"] = sensitivity
    print()

    # --- Step 6: Information loss ---
    print("[6] Quantifying information loss (500k Monte Carlo samples)...")
    info_loss = compute_information_loss()
    for band, data in info_loss["conditional_analysis"].items():
        print(f"    {band}: mean retention = {data['mean_retention']:.3f} "
              f"-- {data['interpretation']}")
    results["information_loss"] = info_loss
    print()

    # --- Step 7: H-kappa trade-off ---
    print("[7] Analyzing H-kappa trade-off surface...")
    hk_tradeoff = analyze_H_kappa_tradeoff()
    for gate_label, curve in hk_tradeoff["iso_gate_curves"].items():
        print(f"    {gate_label}: H in [{curve['H_range'][0]:.2f}, {curve['H_range'][1]:.2f}], "
              f"kappa in [{curve['kappa_range'][0]:.2f}, {curve['kappa_range'][1]:.2f}]")
    results["H_kappa_tradeoff"] = hk_tradeoff
    print()

    # --- Step 8: Absurd degeneracies ---
    print("[8] Searching for maximally absurd degeneracies (2M samples)...")
    absurd = find_absurd_degeneracies()
    for a in absurd[:5]:
        print(f"    {a['canonical_state']:15s} (D={a['canonical_D']:.4f}): "
              f"dist={a['distance_5d']:.4f} ({a['degeneracy_ratio']*100:.1f}%)")
        print(f"      Canon:  {a['canonical_profile']}")
        print(f"      Degen:  {a['degenerate_profile']}")
        print(f"      Why absurd: {a['phenomenological_description']}")
    results["absurd_degeneracies"] = absurd
    print()

    # --- Step 9: D=0 analysis ---
    print("[9] Analyzing D ~ 0 concentration...")
    d_zero = analyze_D_zero()
    print(f"    D median: {d_zero['D_median']:.4f}")
    print(f"    D mean: {d_zero['D_mean']:.4f}")
    for threshold, data in d_zero["near_zero_fractions"].items():
        print(f"    {threshold}: {data['percentage']} of parameter space")
    results["D_zero_analysis"] = d_zero
    print()

    # --- Save results ---
    output_dir = os.path.join(os.path.dirname(__file__), "..", "research_output")
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"260222_isocline_degeneracy_{timestamp}.json")

    # Convert numpy types for JSON serialization
    def convert_numpy(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return obj

    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            result = convert_numpy(obj)
            if result is not obj:
                return result
            return super().default(obj)

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"Results saved to: {output_path}")

    print()
    print("=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

    return results


if __name__ == "__main__":
    results = main()
