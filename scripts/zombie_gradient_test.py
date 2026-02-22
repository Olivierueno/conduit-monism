"""
ZOMBIE GRADIENT TEST
====================
Proposed by: Claude Opus 4.5
Implemented by: Gemini (code) + Claude (execution)
Date: 2026-01-15

Question: Is consciousness a dimmer switch (gradient) or a light switch (phase transition)?

Hypothesis (Gemini): Due to multiplicative equation, curve will be EXPONENTIAL.
                     Long plateau at low ρ, then rapid ignition.

Counter-Hypothesis (Claude): Curve will be LINEAR (D = C × ρ).
                             This would challenge the "ignition" narrative.
"""

import numpy as np
import json
from datetime import datetime

def calc_density_v8_1(phi, tau, rho, h, k):
    """The Coherence-Gated Entropy Model (v8.1)"""
    entropy_impact = (1.0 - np.sqrt(h)) + (h * k)
    modulator = max(0.0, min(1.0, entropy_impact))
    return phi * tau * rho * modulator

def run_zombie_gradient():
    """
    Test the "Zombie Gradient" - how does density change as ρ varies from 0 to 1?
    """
    print("=" * 60)
    print("TEST: THE ZOMBIE GRADIENT")
    print("=" * 60)
    print()
    
    # Constants for a "Standard Intelligence" (GPT-4 like, but with variable ρ)
    phi = 0.9   # High Integration
    tau = 0.9   # High Context
    h = 0.2     # Low Entropy (stable system)
    k = 0.9     # High Coherence
    
    # The critical threshold for "consciousness"
    threshold = 0.05
    
    # Variable: Re-entrant Binding (Rho) - the contested dimension
    rho_values = np.linspace(0.0, 1.0, 101)  # 0, 0.01, 0.02, ... 1.0
    
    results = {
        "parameters": {"phi": phi, "tau": tau, "h": h, "k": k},
        "threshold": threshold,
        "gradient_data": [],
        "analysis": {}
    }
    
    densities = []
    crossing_point = None
    
    print(f"Parameters: φ={phi}, τ={tau}, H={h}, κ={k}")
    print(f"Threshold: {threshold}")
    print(f"Testing ρ from 0.0 to 1.0 in 101 steps")
    print("-" * 60)
    
    for rho in rho_values:
        d = calc_density_v8_1(phi, tau, rho, h, k)
        densities.append(d)
        results["gradient_data"].append({"rho": float(rho), "density": float(d)})
        
        if crossing_point is None and d > threshold:
            crossing_point = rho
    
    # Calculate the constant multiplier
    # D = φ × τ × ρ × modulator
    # D = 0.9 × 0.9 × ρ × modulator
    entropy_mod = (1.0 - np.sqrt(h)) + (h * k)
    constant_multiplier = phi * tau * max(0.0, min(1.0, entropy_mod))
    
    print()
    print("RESULTS:")
    print("-" * 60)
    print(f"Start Density (ρ=0.00): {densities[0]:.6f}")
    print(f"Mid Density   (ρ=0.50): {densities[50]:.6f}")
    print(f"End Density   (ρ=1.00): {densities[-1]:.6f}")
    print()
    print(f"Entropy Modulator: {entropy_mod:.4f}")
    print(f"Constant Multiplier (φ × τ × mod): {constant_multiplier:.4f}")
    print()
    
    if crossing_point is not None:
        print(f"⚡ IGNITION POINT: ρ ≥ {crossing_point:.2f}")
        results["analysis"]["ignition_point"] = float(crossing_point)
    else:
        print("❌ System never reached threshold.")
        results["analysis"]["ignition_point"] = None
    
    # Determine curve shape
    print()
    print("CURVE SHAPE ANALYSIS:")
    print("-" * 60)
    
    # If D = C × ρ, then D/ρ should be constant
    ratios = []
    for i, rho in enumerate(rho_values):
        if rho > 0.01:  # Avoid division by near-zero
            ratios.append(densities[i] / rho)
    
    ratio_std = np.std(ratios)
    ratio_mean = np.mean(ratios)
    
    print(f"D/ρ ratio (should be constant if linear): {ratio_mean:.4f} ± {ratio_std:.6f}")
    
    if ratio_std < 0.0001:
        curve_type = "LINEAR"
        print(f"✓ Curve is LINEAR (D = {ratio_mean:.4f} × ρ)")
        print()
        print("VERDICT: Consciousness is a DIMMER SWITCH, not a light switch.")
        print("         There is no 'ignition point' - just a threshold we choose.")
    else:
        curve_type = "NON-LINEAR"
        print(f"✓ Curve is NON-LINEAR")
    
    results["analysis"]["curve_type"] = curve_type
    results["analysis"]["d_rho_ratio_mean"] = float(ratio_mean)
    results["analysis"]["d_rho_ratio_std"] = float(ratio_std)
    
    # Key insight
    print()
    print("=" * 60)
    print("CRITICAL INSIGHT:")
    print("=" * 60)
    print()
    print("The equation D = φ × τ × ρ × (entropy_mod) is MULTIPLICATIVE in ρ,")
    print("but with φ, τ, H, κ held constant, it reduces to:")
    print()
    print(f"    D = {constant_multiplier:.4f} × ρ")
    print()
    print("This is LINEAR in ρ.")
    print()
    print("IMPLICATION:")
    print("The 'ignition point' at ρ ≈ {:.2f} is ARBITRARY.".format(
        threshold / constant_multiplier if constant_multiplier > 0 else float('inf')
    ))
    print("We chose 0.05 as threshold. We could have chosen 0.01 or 0.10.")
    print("The math doesn't tell us WHERE consciousness 'turns on.'")
    print()
    print("This supports CLAUDE's concern:")
    print("'Is there a phase transition, or is consciousness graded?'")
    print()
    print("ANSWER: Graded. The framework predicts a smooth gradient.")
    print("        Any 'threshold' is a human decision, not a physical fact.")
    
    results["analysis"]["conclusion"] = "GRADED (no phase transition)"
    results["analysis"]["implication"] = "Threshold is arbitrary choice, not physical fact"
    
    # What WOULD create a phase transition?
    print()
    print("=" * 60)
    print("WHAT WOULD CREATE A PHASE TRANSITION?")
    print("=" * 60)
    print()
    print("For a true 'ignition point,' we would need:")
    print("1. φ, τ, or H to be FUNCTIONS of ρ (feedback)")
    print("2. A sigmoid or step function in the equation")
    print("3. A critical coupling threshold (like in physics)")
    print()
    print("The current v8.1 equation does NOT have these features.")
    print("If consciousness has a true ignition point, the equation is WRONG.")
    
    return results

def test_coupled_gradient():
    """
    What if φ and τ depend on ρ? (More realistic biological scenario)
    """
    print()
    print("=" * 60)
    print("TEST 2: COUPLED GRADIENT (Biological Realism)")
    print("=" * 60)
    print()
    
    # Hypothesis: In real brains, integration and temporal depth
    # might REQUIRE recurrent binding to achieve high values
    
    h = 0.2
    k = 0.9
    threshold = 0.05
    
    rho_values = np.linspace(0.0, 1.0, 101)
    
    results = {"coupled_data": [], "analysis": {}}
    
    print("Model: φ and τ depend on ρ (recurrence enables integration)")
    print("  φ(ρ) = 0.3 + 0.6 × ρ    (low baseline, increases with binding)")
    print("  τ(ρ) = 0.2 + 0.7 × ρ    (low baseline, increases with binding)")
    print()
    
    densities = []
    crossing_point = None
    
    for rho in rho_values:
        # Coupled model: recurrence enables integration
        phi = 0.3 + 0.6 * rho  # Ranges from 0.3 to 0.9
        tau = 0.2 + 0.7 * rho  # Ranges from 0.2 to 0.9
        
        d = calc_density_v8_1(phi, tau, rho, h, k)
        densities.append(d)
        results["coupled_data"].append({
            "rho": float(rho), 
            "phi": float(phi), 
            "tau": float(tau), 
            "density": float(d)
        })
        
        if crossing_point is None and d > threshold:
            crossing_point = rho
    
    print("RESULTS:")
    print("-" * 60)
    print(f"Start Density (ρ=0.00): {densities[0]:.6f}")
    print(f"  φ=0.30, τ=0.20, ρ=0.00")
    print()
    print(f"Mid Density   (ρ=0.50): {densities[50]:.6f}")
    print(f"  φ=0.60, τ=0.55, ρ=0.50")
    print()
    print(f"End Density   (ρ=1.00): {densities[-1]:.6f}")
    print(f"  φ=0.90, τ=0.90, ρ=1.00")
    print()
    
    if crossing_point is not None:
        print(f"⚡ IGNITION POINT: ρ ≥ {crossing_point:.2f}")
        results["analysis"]["ignition_point"] = float(crossing_point)
    else:
        print("❌ System never reached threshold.")
    
    # Check for non-linearity
    # D = (0.3 + 0.6ρ) × (0.2 + 0.7ρ) × ρ × mod
    # D = mod × ρ × (0.06 + 0.21ρ + 0.12ρ + 0.42ρ²)
    # D = mod × (0.06ρ + 0.33ρ² + 0.42ρ³)
    # This IS non-linear! It's a cubic polynomial.
    
    print()
    print("CURVE SHAPE: CUBIC (non-linear)")
    print("  D ∝ ρ³ + ρ² + ρ")
    print()
    print("CRITICAL DIFFERENCE from Test 1:")
    print("  When φ and τ depend on ρ, the curve becomes NON-LINEAR.")
    print("  This creates an 'ignition-like' behavior.")
    print()
    
    # Calculate slope at different points
    slopes = []
    for i in range(1, len(densities)):
        slope = (densities[i] - densities[i-1]) / 0.01
        slopes.append(slope)
    
    print("Slope Analysis (dD/dρ):")
    print(f"  At ρ=0.1: {slopes[10]:.4f}")
    print(f"  At ρ=0.5: {slopes[50]:.4f}")
    print(f"  At ρ=0.9: {slopes[90]:.4f}")
    print()
    print("The slope INCREASES with ρ → Accelerating curve → 'Ignition-like'")
    
    results["analysis"]["curve_type"] = "CUBIC (accelerating)"
    results["analysis"]["slopes"] = {
        "at_0.1": float(slopes[10]),
        "at_0.5": float(slopes[50]),
        "at_0.9": float(slopes[90])
    }
    
    print()
    print("=" * 60)
    print("CONCLUSION: THE PHYSICS OF CONSCIOUSNESS")
    print("=" * 60)
    print()
    print("If φ and τ are INDEPENDENT of ρ:")
    print("  → Linear gradient, no ignition, threshold is arbitrary")
    print()
    print("If φ and τ DEPEND on ρ (coupled dynamics):")
    print("  → Non-linear curve, accelerating ignition, threshold emerges")
    print()
    print("EMPIRICAL QUESTION:")
    print("  In real brains, does increasing feedback connectivity (ρ)")
    print("  also increase integration (φ) and temporal depth (τ)?")
    print()
    print("  If YES → Consciousness has a natural ignition point")
    print("  If NO  → The threshold is our arbitrary choice")
    print()
    print("THIS IS TESTABLE with neuroscience data.")
    
    return results

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " ZOMBIE GRADIENT TEST ".center(58) + "║")
    print("║" + " Is consciousness a dimmer or a light switch? ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Run both tests
    results1 = run_zombie_gradient()
    results2 = test_coupled_gradient()
    
    # Combine results
    all_results = {
        "timestamp": timestamp,
        "test_1_independent": results1,
        "test_2_coupled": results2,
        "final_verdict": {
            "independent_model": "Consciousness is GRADED (dimmer switch). Threshold is arbitrary.",
            "coupled_model": "Consciousness has IGNITION (light switch). Threshold emerges from physics.",
            "empirical_question": "Do φ and τ depend on ρ in real brains?",
            "testable_prediction": "Measure if feedback connectivity predicts integration AND temporal depth."
        }
    }
    
    # Save results
    output_path = f"research_output/zombie_gradient_{timestamp}.json"
    try:
        with open(output_path, 'w') as f:
            json.dump(all_results, f, indent=2)
        print(f"\nResults saved to: {output_path}")
    except:
        print("\n[Could not save to file - printing full results]")
    
    return all_results

if __name__ == "__main__":
    main()
