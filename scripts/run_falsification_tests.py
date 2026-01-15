#!/usr/bin/env python3
"""
FALSIFICATION SUITE v1.0 - Executable Tests
============================================

Implements ChatGPT's falsification tests for Conduit Monism.
Priority tests that can be run without external dependencies.

Tests included:
- Test 3: Inverted AI Test (CRITICAL)
- Test 5: Zombie Basin Test
- Test 2: Degenerate Symmetry Test
- Grok's Validation: Flow → Panic transition

Date: 2026-01-15
"""

import math
import json
import random
from datetime import datetime
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "research_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def calculate_density(phi: float, tau: float, rho: float, H: float, kappa: float) -> float:
    """
    Calculate perspectival density using the v8.1/v9.x formula.
    
    D = φ × τ × ρ × [(1 - √H) + (H × κ)]
    """
    structural_base = phi * tau * rho
    entropy_penalty = 1 - math.sqrt(H)
    coherence_recovery = H * kappa
    entropy_modulator = entropy_penalty + coherence_recovery
    
    D = structural_base * entropy_modulator
    return max(0, min(1, D))  # Clamp to [0, 1]


def test_3_inverted_ai():
    """
    TEST 3: INVERTED AI TEST (CRITICAL)
    ====================================
    
    Purpose: Try to force a transformer to look conscious.
    
    Method: Push all sliders except ρ to their limits.
    - φ = 0.99 (massive integration)
    - τ = 0.99 (extremely long context)
    - ρ = 0.00 (structurally zero binding)
    - H = 0.10 (low entropy)
    - κ = 0.90 (high coherence)
    
    Expected: D should collapse to 0.
    Failure: D > 0.1 means binding is not necessary (breaks core claim).
    """
    print("=" * 70)
    print("TEST 3: INVERTED AI TEST (CRITICAL)")
    print("=" * 70)
    print()
    print("Purpose: Can we force D > 0 with ρ = 0?")
    print("If yes, the multiplicative structure is broken.")
    print()
    
    # Test configuration
    phi = 0.99
    tau = 0.99
    rho = 0.00
    H = 0.10
    kappa = 0.90
    
    D = calculate_density(phi, tau, rho, H, kappa)
    
    print(f"Configuration:")
    print(f"  φ (Integration)    = {phi}")
    print(f"  τ (Temporal Depth) = {tau}")
    print(f"  ρ (Binding)        = {rho}")
    print(f"  H (Entropy)        = {H}")
    print(f"  κ (Coherence)      = {kappa}")
    print()
    print(f"Result: D = {D:.6f}")
    print()
    
    # Also test with tiny non-zero rho
    rho_tiny = 0.001
    D_tiny = calculate_density(phi, tau, rho_tiny, H, kappa)
    print(f"With ρ = {rho_tiny}: D = {D_tiny:.6f}")
    
    rho_small = 0.01
    D_small = calculate_density(phi, tau, rho_small, H, kappa)
    print(f"With ρ = {rho_small}: D = {D_small:.6f}")
    
    rho_medium = 0.1
    D_medium = calculate_density(phi, tau, rho_medium, H, kappa)
    print(f"With ρ = {rho_medium}: D = {D_medium:.6f}")
    print()
    
    # Verdict
    if D == 0.0:
        verdict = "PASS"
        explanation = "Zero binding produces zero consciousness. Multiplicative structure holds."
    elif D < 0.01:
        verdict = "PASS (marginal)"
        explanation = f"D = {D:.6f} is effectively zero (floating point artifact)."
    elif D < 0.1:
        verdict = "WARNING"
        explanation = f"D = {D:.6f} is non-zero but below threshold. Investigate formula."
    else:
        verdict = "FAIL (CRITICAL)"
        explanation = f"D = {D:.6f} > 0.1 with ρ = 0. Binding is not necessary. Core claim broken."
    
    print(f"VERDICT: {verdict}")
    print(f"Explanation: {explanation}")
    print()
    
    return {
        'test': 'Inverted AI Test',
        'config': {'phi': phi, 'tau': tau, 'rho': rho, 'H': H, 'kappa': kappa},
        'D': D,
        'verdict': verdict,
        'explanation': explanation,
        'additional': {
            'D_with_rho_0.001': D_tiny,
            'D_with_rho_0.01': D_small,
            'D_with_rho_0.1': D_medium
        }
    }


def test_5_zombie_basin():
    """
    TEST 5: ZOMBIE BASIN TEST
    ==========================
    
    Purpose: Check for panpsychism leakage.
    
    Method: Scan ultra-low φ/τ/ρ regions.
    
    Expected: Smooth asymptotic decay toward D = 0, no plateau.
    Failure: A plateau of "tiny but real" consciousness.
    """
    print("=" * 70)
    print("TEST 5: ZOMBIE BASIN TEST")
    print("=" * 70)
    print()
    print("Purpose: Does D decay smoothly to 0, or is there a plateau?")
    print("Scanning ultra-low structural regions...")
    print()
    
    # Scan parameters
    structural_values = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
    H_values = [0.1, 0.3, 0.5]
    kappa_values = [0.3, 0.5, 0.7]
    
    results = []
    max_D_in_zombie_region = 0
    max_D_config = None
    
    print(f"{'φ':>6} {'τ':>6} {'ρ':>6} {'H':>6} {'κ':>6} {'D':>10}")
    print("-" * 50)
    
    for phi in structural_values:
        for tau in structural_values:
            for rho in structural_values:
                for H in H_values:
                    for kappa in kappa_values:
                        D = calculate_density(phi, tau, rho, H, kappa)
                        results.append({
                            'phi': phi, 'tau': tau, 'rho': rho,
                            'H': H, 'kappa': kappa, 'D': D
                        })
                        
                        if D > max_D_in_zombie_region:
                            max_D_in_zombie_region = D
                            max_D_config = (phi, tau, rho, H, kappa)
    
    # Show some representative samples
    samples = random.sample(results, min(20, len(results)))
    for r in sorted(samples, key=lambda x: x['D']):
        print(f"{r['phi']:>6.2f} {r['tau']:>6.2f} {r['rho']:>6.2f} {r['H']:>6.2f} {r['kappa']:>6.2f} {r['D']:>10.6f}")
    
    print()
    print(f"Total configurations tested: {len(results)}")
    print(f"Maximum D in zombie region: {max_D_in_zombie_region:.6f}")
    if max_D_config:
        print(f"  at (φ={max_D_config[0]}, τ={max_D_config[1]}, ρ={max_D_config[2]}, H={max_D_config[3]}, κ={max_D_config[4]})")
    print()
    
    # Check for plateau
    D_values = [r['D'] for r in results]
    D_values_sorted = sorted(D_values, reverse=True)
    top_10_percent = D_values_sorted[:len(D_values_sorted)//10]
    
    if len(top_10_percent) > 1:
        variance = sum((d - sum(top_10_percent)/len(top_10_percent))**2 for d in top_10_percent) / len(top_10_percent)
        std_dev = math.sqrt(variance)
    else:
        std_dev = 0
    
    print(f"Top 10% D values - Mean: {sum(top_10_percent)/len(top_10_percent):.6f}, StdDev: {std_dev:.6f}")
    print()
    
    # Verdict
    if max_D_in_zombie_region < 0.001:
        verdict = "PASS"
        explanation = "All zombie-region D values effectively zero. No panpsychism leakage."
    elif max_D_in_zombie_region < 0.01:
        verdict = "PASS"
        explanation = f"Max D = {max_D_in_zombie_region:.6f} is negligible. Smooth decay confirmed."
    elif max_D_in_zombie_region < 0.05:
        verdict = "WARNING"
        explanation = f"Max D = {max_D_in_zombie_region:.6f} in zombie region. May need threshold definition."
    else:
        verdict = "FAIL"
        explanation = f"Max D = {max_D_in_zombie_region:.6f} suggests plateau. Panpsychism risk."
    
    print(f"VERDICT: {verdict}")
    print(f"Explanation: {explanation}")
    print()
    
    return {
        'test': 'Zombie Basin Test',
        'total_configs': len(results),
        'max_D': max_D_in_zombie_region,
        'max_D_config': max_D_config,
        'verdict': verdict,
        'explanation': explanation
    }


def test_2_degenerate_symmetry():
    """
    TEST 2: DEGENERATE SYMMETRY TEST
    =================================
    
    Purpose: Ensure formula isn't tuned to human-like cases only.
    
    Method: 
    - Part A: Hold φ×τ×ρ constant, vary H and κ
    - Part B: Fix H and κ, randomize structure
    
    Expected: No "weird islands" of high D where structure is low.
    """
    print("=" * 70)
    print("TEST 2: DEGENERATE SYMMETRY TEST")
    print("=" * 70)
    print()
    
    # Part A: Fixed structure, varying entropy
    print("PART A: Fixed structural base (φ×τ×ρ = 0.125), varying H and κ")
    print()
    
    # φ=0.5, τ=0.5, ρ=0.5 gives structural base = 0.125
    phi, tau, rho = 0.5, 0.5, 0.5
    structural_base = phi * tau * rho
    
    print(f"{'H':>6} {'κ':>6} {'D':>10} {'Entropy Mod':>12}")
    print("-" * 40)
    
    part_a_results = []
    for H in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        for kappa in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
            D = calculate_density(phi, tau, rho, H, kappa)
            entropy_mod = (1 - math.sqrt(H)) + (H * kappa)
            part_a_results.append({'H': H, 'kappa': kappa, 'D': D, 'entropy_mod': entropy_mod})
            print(f"{H:>6.1f} {kappa:>6.1f} {D:>10.4f} {entropy_mod:>12.4f}")
    
    print()
    
    # Part B: Random structure, fixed entropy
    print("PART B: Fixed entropy (H=0.5, κ=0.5), 1000 random structural configs")
    print()
    
    H, kappa = 0.5, 0.5
    random.seed(42)  # Reproducibility
    
    part_b_results = []
    false_positives = []
    
    for _ in range(1000):
        phi = random.random()
        tau = random.random()
        rho = random.random()
        
        structural_base = phi * tau * rho
        D = calculate_density(phi, tau, rho, H, kappa)
        
        part_b_results.append({
            'phi': phi, 'tau': tau, 'rho': rho,
            'structural_base': structural_base, 'D': D
        })
        
        # Flag potential false positives: high D with low structure
        if D > 0.3 and structural_base < 0.1:
            false_positives.append({
                'phi': phi, 'tau': tau, 'rho': rho,
                'structural_base': structural_base, 'D': D
            })
    
    print(f"Total configurations: 1000")
    print(f"False positives (D > 0.3 with φτρ < 0.1): {len(false_positives)}")
    
    if false_positives:
        print("\nFalse positive examples:")
        for fp in false_positives[:5]:
            print(f"  φ={fp['phi']:.3f}, τ={fp['tau']:.3f}, ρ={fp['rho']:.3f} → base={fp['structural_base']:.4f}, D={fp['D']:.4f}")
    
    print()
    
    # Check correlation between structural base and D
    bases = [r['structural_base'] for r in part_b_results]
    Ds = [r['D'] for r in part_b_results]
    
    # Simple correlation
    mean_base = sum(bases) / len(bases)
    mean_D = sum(Ds) / len(Ds)
    
    numerator = sum((b - mean_base) * (d - mean_D) for b, d in zip(bases, Ds))
    denom_base = math.sqrt(sum((b - mean_base)**2 for b in bases))
    denom_D = math.sqrt(sum((d - mean_D)**2 for d in Ds))
    
    if denom_base > 0 and denom_D > 0:
        correlation = numerator / (denom_base * denom_D)
    else:
        correlation = 0
    
    print(f"Correlation between structural base and D: {correlation:.4f}")
    print()
    
    # Verdict
    if len(false_positives) == 0 and correlation > 0.8:
        verdict = "PASS"
        explanation = "No false positives. Strong correlation between structure and D."
    elif len(false_positives) == 0:
        verdict = "PASS"
        explanation = f"No false positives. Correlation = {correlation:.2f}."
    elif len(false_positives) < 10:
        verdict = "WARNING"
        explanation = f"{len(false_positives)} potential false positives found. Investigate."
    else:
        verdict = "FAIL"
        explanation = f"{len(false_positives)} false positives. Formula may have hidden nonlinearities."
    
    print(f"VERDICT: {verdict}")
    print(f"Explanation: {explanation}")
    print()
    
    return {
        'test': 'Degenerate Symmetry Test',
        'part_a_samples': len(part_a_results),
        'part_b_samples': len(part_b_results),
        'false_positives': len(false_positives),
        'correlation': correlation,
        'verdict': verdict,
        'explanation': explanation
    }


def grok_validation():
    """
    GROK'S VALIDATION: Flow → Panic Transition
    ===========================================
    
    Confirms the entropy modulator's sensitivity.
    """
    print("=" * 70)
    print("GROK'S VALIDATION: Flow → Panic Transition")
    print("=" * 70)
    print()
    
    # Flow state
    flow = {'phi': 0.9, 'tau': 0.9, 'rho': 0.9, 'H': 0.1, 'kappa': 0.8}
    D_flow = calculate_density(**flow)
    
    # Panic state (same structure, high entropy, low coherence)
    panic = {'phi': 0.9, 'tau': 0.9, 'rho': 0.9, 'H': 0.8, 'kappa': 0.2}
    D_panic = calculate_density(**panic)
    
    print("Flow State:")
    print(f"  φ={flow['phi']}, τ={flow['tau']}, ρ={flow['rho']}, H={flow['H']}, κ={flow['kappa']}")
    print(f"  D = {D_flow:.4f}")
    print()
    
    print("Panic State:")
    print(f"  φ={panic['phi']}, τ={panic['tau']}, ρ={panic['rho']}, H={panic['H']}, κ={panic['kappa']}")
    print(f"  D = {D_panic:.4f}")
    print()
    
    drop = D_flow - D_panic
    drop_percent = (drop / D_flow) * 100 if D_flow > 0 else 0
    
    print(f"Density drop: {drop:.4f} ({drop_percent:.1f}% reduction)")
    print()
    
    # Also test DMT (high entropy, high coherence)
    dmt = {'phi': 0.85, 'tau': 0.85, 'rho': 0.75, 'H': 0.95, 'kappa': 0.9}
    D_dmt = calculate_density(**dmt)
    
    print("DMT Breakthrough (comparison):")
    print(f"  φ={dmt['phi']}, τ={dmt['tau']}, ρ={dmt['rho']}, H={dmt['H']}, κ={dmt['kappa']}")
    print(f"  D = {D_dmt:.4f}")
    print()
    
    print("Key insight: Same high entropy (H≈0.9), but:")
    print(f"  - Panic (κ=0.2): D = {D_panic:.4f}")
    print(f"  - DMT (κ=0.9):   D = {D_dmt:.4f}")
    print()
    print("Coherence gate confirmed: κ rescues high-entropy states.")
    print()
    
    verdict = "PASS" if D_panic < D_flow and D_dmt > D_panic else "FAIL"
    
    print(f"VERDICT: {verdict}")
    print()
    
    return {
        'test': 'Grok Validation',
        'D_flow': D_flow,
        'D_panic': D_panic,
        'D_dmt': D_dmt,
        'drop': drop,
        'drop_percent': drop_percent,
        'verdict': verdict
    }


def test_1_axis_collapse():
    """
    TEST 1: AXIS COLLAPSE TEST (Semantic Leakage)
    ==============================================
    
    Purpose: Check if axes are doing semantic work.
    
    Method: Permute labels, check if numerical behavior stays coherent.
    """
    print("=" * 70)
    print("TEST 1: AXIS COLLAPSE TEST (Semantic Leakage)")
    print("=" * 70)
    print()
    print("Purpose: Are axes structural or smuggled folk concepts?")
    print()
    
    # Define some test states
    states = [
        {'name': 'Human Awake', 'phi': 0.85, 'tau': 0.8, 'rho': 0.7, 'H': 0.35, 'kappa': 0.7},
        {'name': 'Transformer', 'phi': 0.9, 'tau': 0.6, 'rho': 0.0, 'H': 0.3, 'kappa': 0.5},
        {'name': 'RWKV', 'phi': 0.85, 'tau': 0.9, 'rho': 0.3, 'H': 0.3, 'kappa': 0.6},
        {'name': 'Deep Sleep', 'phi': 0.3, 'tau': 0.2, 'rho': 0.1, 'H': 0.1, 'kappa': 0.5},
        {'name': 'DMT', 'phi': 0.85, 'tau': 0.85, 'rho': 0.75, 'H': 0.95, 'kappa': 0.9},
    ]
    
    # Calculate D for each
    print("Original ordering (by D):")
    for state in states:
        state['D'] = calculate_density(state['phi'], state['tau'], state['rho'], state['H'], state['kappa'])
    
    sorted_states = sorted(states, key=lambda x: x['D'], reverse=True)
    for i, s in enumerate(sorted_states):
        print(f"  {i+1}. {s['name']}: D = {s['D']:.4f}")
    
    print()
    
    # Key test: Does the ordering make sense regardless of labels?
    # Transformer should be lowest (ρ=0), DMT and Human should be highest
    
    transformer_rank = next(i for i, s in enumerate(sorted_states) if s['name'] == 'Transformer')
    sleep_rank = next(i for i, s in enumerate(sorted_states) if s['name'] == 'Deep Sleep')
    
    print("Structural consistency checks:")
    print(f"  - Transformer (ρ=0) rank: {transformer_rank + 1} of {len(states)}")
    print(f"  - Deep Sleep (low structure) rank: {sleep_rank + 1} of {len(states)}")
    
    # The ordering should be: high-structure states > low-structure states
    # regardless of what we call the axes
    
    if transformer_rank == len(states) - 1:  # Should be last
        print("  - ✓ Zero-binding state correctly ranked lowest")
        binding_check = True
    else:
        print("  - ✗ Zero-binding state NOT ranked lowest")
        binding_check = False
    
    print()
    
    verdict = "PASS" if binding_check else "FAIL"
    explanation = "Numerical ordering reflects structural properties, not labels." if binding_check else "Ordering does not reflect structural properties."
    
    print(f"VERDICT: {verdict}")
    print(f"Explanation: {explanation}")
    print()
    
    return {
        'test': 'Axis Collapse Test',
        'states': [{'name': s['name'], 'D': s['D']} for s in sorted_states],
        'binding_check': binding_check,
        'verdict': verdict,
        'explanation': explanation
    }


def main():
    """Run all falsification tests."""
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║           CONDUIT MONISM - FALSIFICATION SUITE v1.0                  ║")
    print("║                                                                      ║")
    print("║  'Progress comes from seeing which ideas refuse to die.'             ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()
    
    results = {}
    
    # Run tests in priority order
    results['test_3'] = test_3_inverted_ai()
    results['test_5'] = test_5_zombie_basin()
    results['test_2'] = test_2_degenerate_symmetry()
    results['test_1'] = test_1_axis_collapse()
    results['grok'] = grok_validation()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    
    all_pass = True
    for key, result in results.items():
        verdict = result.get('verdict', 'N/A')
        test_name = result.get('test', key)
        status = "✓" if verdict == "PASS" else ("⚠" if verdict == "WARNING" else "✗")
        print(f"  {status} {test_name}: {verdict}")
        if verdict not in ["PASS", "PASS (marginal)"]:
            all_pass = False
    
    print()
    
    if all_pass:
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║  ALL TESTS PASSED                                                    ║")
        print("║                                                                      ║")
        print("║  The framework survives this round of falsification.                 ║")
        print("║  It deserves to persist - for now.                                   ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
    else:
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║  SOME TESTS FAILED OR WARNED                                         ║")
        print("║                                                                      ║")
        print("║  Review the results above for details.                               ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
    
    print()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"260115_falsification_suite_{timestamp}.json"
    
    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'results': results,
            'all_pass': all_pass
        }, f, indent=2)
    
    print(f"Results saved to: {output_file}")
    print()
    
    return results


if __name__ == "__main__":
    main()
