#!/usr/bin/env python3
"""
Corpus Expansion - Conduit Engine v0.1

Expand the state corpus from 6 to 50+ mental states.

Goal: Create comprehensive mapping of consciousness space including:
- Normal variations
- Sleep states
- Altered states
- Pathological states
- Transitional states
- Peak experiences
- Impaired states
- Clinical states
- Non-human states
- Edge cases
"""

import numpy as np
from src.database import ConduitDB
from src.encoder import encode, compute_density
from src.density_models import density_entropy_modulated_v3
from datetime import datetime
import json
import os


def print_header(title: str):
    """Print formatted header."""
    print("\n" + "="*80)
    print(title.center(80))
    print("="*80 + "\n")


def print_subheader(title: str):
    """Print formatted subheader."""
    print("\n" + "-"*80)
    print(title)
    print("-"*80)


class CorpusExpansion:
    """
    Systematic expansion of mental state corpus.

    Target: 50+ states covering full consciousness space.
    """

    def __init__(self):
        self.db = ConduitDB()
        self.states = []
        self.output_dir = "./research_output/corpus"
        os.makedirs(self.output_dir, exist_ok=True)

    def create_comprehensive_corpus(self):
        """Create comprehensive corpus of 50+ states."""

        print_header("CORPUS EXPANSION - 50+ MENTAL STATES")
        print("Building comprehensive mapping of consciousness space")
        print()

        # Category 1: Normal Waking States (8 states)
        print_subheader("CATEGORY 1: Normal Waking States (8 states)")
        self.normal_waking_states()

        # Category 2: Sleep States (8 states)
        print_subheader("CATEGORY 2: Sleep States (8 states)")
        self.sleep_states()

        # Category 3: Altered States (8 states)
        print_subheader("CATEGORY 3: Altered States (8 states)")
        self.altered_states()

        # Category 4: Pathological States (6 states)
        print_subheader("CATEGORY 4: Pathological States (6 states)")
        self.pathological_states()

        # Category 5: Transitional States (6 states)
        print_subheader("CATEGORY 5: Transitional States (6 states)")
        self.transitional_states()

        # Category 6: Peak Experiences (5 states)
        print_subheader("CATEGORY 6: Peak Experiences (5 states)")
        self.peak_experiences()

        # Category 7: Impaired States (5 states)
        print_subheader("CATEGORY 7: Impaired States (5 states)")
        self.impaired_states()

        # Category 8: Clinical States (6 states)
        print_subheader("CATEGORY 8: Clinical States (6 states)")
        self.clinical_states()

        # Category 9: Non-Human States (6 states)
        print_subheader("CATEGORY 9: Non-Human States (6 states)")
        self.non_human_states()

        # Category 10: Edge Cases (6 states)
        print_subheader("CATEGORY 10: Edge Cases (6 states)")
        self.edge_cases()

        # Generate summary
        self.generate_summary()

    def add_state(self, name: str, phi: float, tau: float, rho: float, entropy: float, category: str, notes: str = ""):
        """Add a state to the corpus and database."""

        # Encode and compute density
        vector = encode(phi, tau, rho, entropy)
        density = density_entropy_modulated_v3(phi, tau, rho, entropy)

        # Store state data
        state_data = {
            'name': name,
            'category': category,
            'phi': phi,
            'tau': tau,
            'rho': rho,
            'entropy': entropy,
            'density': float(density),
            'vector': vector,
            'notes': notes
        }

        self.states.append(state_data)

        # Seed to database (using original signature)
        description = f"[{category}] {notes}" if notes else category
        self.db.seed_state(
            name=name,
            phi=phi,
            tau=tau,
            rho=rho,
            entropy=entropy,
            description=description
        )

        print(f"  ✓ {name:<40} | φ={phi:.2f} τ={tau:.2f} ρ={rho:.2f} H={entropy:.2f} | D={density:.4f}")

    def normal_waking_states(self):
        """Normal waking consciousness variations."""

        self.add_state(
            name="Healthy Awake (Alert)",
            phi=0.90, tau=0.90, rho=0.90, entropy=0.10,
            category="Normal Waking",
            notes="Baseline healthy consciousness, high alertness"
        )

        self.add_state(
            name="Relaxed Awake",
            phi=0.85, tau=0.85, rho=0.85, entropy=0.15,
            category="Normal Waking",
            notes="Calm, relaxed waking state"
        )

        self.add_state(
            name="Focused Concentration",
            phi=0.90, tau=0.85, rho=0.90, entropy=0.08,
            category="Normal Waking",
            notes="Deep focus on task, low entropy"
        )

        self.add_state(
            name="Mind Wandering",
            phi=0.75, tau=0.70, rho=0.75, entropy=0.30,
            category="Normal Waking",
            notes="Default mode network active, higher entropy"
        )

        self.add_state(
            name="Boredom",
            phi=0.70, tau=0.60, rho=0.70, entropy=0.35,
            category="Normal Waking",
            notes="Low engagement, moderate entropy"
        )

        self.add_state(
            name="Engaged Conversation",
            phi=0.85, tau=0.80, rho=0.85, entropy=0.20,
            category="Normal Waking",
            notes="Social interaction, moderate dynamics"
        )

        self.add_state(
            name="Reading (Absorbed)",
            phi=0.88, tau=0.82, rho=0.88, entropy=0.12,
            category="Normal Waking",
            notes="Absorbed in narrative, low entropy"
        )

        self.add_state(
            name="Daydreaming",
            phi=0.65, tau=0.55, rho=0.65, entropy=0.40,
            category="Normal Waking",
            notes="Imaginative wandering, higher entropy"
        )

    def sleep_states(self):
        """Sleep and dream states."""

        self.add_state(
            name="REM Dream (Vivid)",
            phi=0.60, tau=0.40, rho=0.50, entropy=0.70,
            category="Sleep",
            notes="High entropy, fragmented integration"
        )

        self.add_state(
            name="REM Dream (Lucid)",
            phi=0.75, tau=0.65, rho=0.70, entropy=0.35,
            category="Sleep",
            notes="Awareness in dream, moderate control"
        )

        self.add_state(
            name="NREM Stage 1 (Drowsy)",
            phi=0.50, tau=0.40, rho=0.50, entropy=0.50,
            category="Sleep",
            notes="Light sleep, transitional"
        )

        self.add_state(
            name="NREM Stage 2 (Light Sleep)",
            phi=0.40, tau=0.30, rho=0.40, entropy=0.60,
            category="Sleep",
            notes="Spindles and K-complexes"
        )

        self.add_state(
            name="NREM Stage 3 (Deep Sleep)",
            phi=0.20, tau=0.15, rho=0.20, entropy=0.30,
            category="Sleep",
            notes="Slow-wave sleep, low entropy, low integration"
        )

        self.add_state(
            name="NREM Stage 4 (Deepest Sleep)",
            phi=0.10, tau=0.08, rho=0.10, entropy=0.20,
            category="Sleep",
            notes="Deepest non-REM, minimal consciousness"
        )

        self.add_state(
            name="Hypnagogic Hallucinations",
            phi=0.55, tau=0.45, rho=0.50, entropy=0.75,
            category="Sleep",
            notes="Falling asleep imagery, high entropy"
        )

        self.add_state(
            name="Sleep Paralysis (Aware)",
            phi=0.70, tau=0.60, rho=0.65, entropy=0.55,
            category="Sleep",
            notes="Conscious but paralyzed, moderate entropy"
        )

    def altered_states(self):
        """Meditation, psychedelics, and other altered states."""

        self.add_state(
            name="Meditation (Beginner)",
            phi=0.80, tau=0.75, rho=0.80, entropy=0.25,
            category="Altered",
            notes="Early meditation, some mind wandering"
        )

        self.add_state(
            name="Meditation (Deep Samadhi)",
            phi=0.95, tau=0.90, rho=0.95, entropy=0.05,
            category="Altered",
            notes="One-pointed focus, very low entropy"
        )

        self.add_state(
            name="Meditation (Open Awareness)",
            phi=0.85, tau=0.80, rho=0.85, entropy=0.15,
            category="Altered",
            notes="Choiceless awareness, relaxed alertness"
        )

        self.add_state(
            name="LSD (Moderate Dose)",
            phi=0.65, tau=0.50, rho=0.60, entropy=0.80,
            category="Altered",
            notes="High entropy, moderate structure"
        )

        self.add_state(
            name="Psilocybin (Moderate)",
            phi=0.60, tau=0.45, rho=0.55, entropy=0.75,
            category="Altered",
            notes="Psychedelic state, elevated entropy"
        )

        self.add_state(
            name="DMT Breakthrough",
            phi=0.40, tau=0.20, rho=0.30, entropy=0.95,
            category="Altered",
            notes="Extreme entropy, collapsed temporal depth"
        )

        self.add_state(
            name="Ketamine Dissociation",
            phi=0.30, tau=0.20, rho=0.25, entropy=0.85,
            category="Altered",
            notes="Dissociative, reduced binding"
        )

        self.add_state(
            name="MDMA Empathy State",
            phi=0.80, tau=0.70, rho=0.75, entropy=0.40,
            category="Altered",
            notes="Enhanced social binding, moderate entropy"
        )

    def pathological_states(self):
        """Clinical pathological states."""

        self.add_state(
            name="Schizophrenia (Acute)",
            phi=0.50, tau=0.40, rho=0.45, entropy=0.85,
            category="Pathological",
            notes="Fragmented integration, very high entropy"
        )

        self.add_state(
            name="Severe Depression",
            phi=0.60, tau=0.50, rho=0.55, entropy=0.60,
            category="Pathological",
            notes="Reduced binding, elevated entropy"
        )

        self.add_state(
            name="Mania (Acute)",
            phi=0.70, tau=0.50, rho=0.65, entropy=0.75,
            category="Pathological",
            notes="Elevated activity, high entropy"
        )

        self.add_state(
            name="Dementia (Moderate)",
            phi=0.40, tau=0.25, rho=0.35, entropy=0.70,
            category="Pathological",
            notes="Degraded temporal depth and integration"
        )

        self.add_state(
            name="Alzheimer's (Advanced)",
            phi=0.25, tau=0.10, rho=0.20, entropy=0.65,
            category="Pathological",
            notes="Severe temporal and integrative deficits"
        )

        self.add_state(
            name="Autism (High-Functioning)",
            phi=0.75, tau=0.70, rho=0.70, entropy=0.30,
            category="Pathological",
            notes="Intact but different integration patterns"
        )

    def transitional_states(self):
        """States between major categories."""

        self.add_state(
            name="Falling Asleep (Early)",
            phi=0.65, tau=0.55, rho=0.60, entropy=0.45,
            category="Transitional",
            notes="Onset of sleep, increasing entropy"
        )

        self.add_state(
            name="Waking Up (Groggy)",
            phi=0.60, tau=0.50, rho=0.55, entropy=0.50,
            category="Transitional",
            notes="Sleep inertia, rebuilding coherence"
        )

        self.add_state(
            name="Microsleep",
            phi=0.35, tau=0.25, rho=0.30, entropy=0.55,
            category="Transitional",
            notes="Brief sleep intrusion while awake"
        )

        self.add_state(
            name="Coming Out of Anesthesia",
            phi=0.40, tau=0.30, rho=0.35, entropy=0.65,
            category="Transitional",
            notes="Recovering integration, high entropy"
        )

        self.add_state(
            name="Psychedelic Peak to Plateau",
            phi=0.55, tau=0.40, rho=0.50, entropy=0.80,
            category="Transitional",
            notes="Transitioning from peak effects"
        )

        self.add_state(
            name="Hypnopompic State",
            phi=0.60, tau=0.50, rho=0.55, entropy=0.60,
            category="Transitional",
            notes="Waking from dream, reality anchoring"
        )

    def peak_experiences(self):
        """Flow, awe, mystical experiences."""

        self.add_state(
            name="Flow State (Athletic)",
            phi=0.95, tau=0.90, rho=0.95, entropy=0.03,
            category="Peak",
            notes="Optimal performance, minimal entropy"
        )

        self.add_state(
            name="Flow State (Creative)",
            phi=0.90, tau=0.85, rho=0.90, entropy=0.08,
            category="Peak",
            notes="Creative absorption, very low entropy"
        )

        self.add_state(
            name="Awe Experience",
            phi=0.85, tau=0.80, rho=0.85, entropy=0.25,
            category="Peak",
            notes="Vastness perception, moderate entropy"
        )

        self.add_state(
            name="Mystical Experience (Unitive)",
            phi=0.90, tau=0.85, rho=0.90, entropy=0.10,
            category="Peak",
            notes="Sense of unity, low entropy"
        )

        self.add_state(
            name="Orgasm",
            phi=0.80, tau=0.60, rho=0.75, entropy=0.45,
            category="Peak",
            notes="Intense but brief, moderate entropy"
        )

    def impaired_states(self):
        """Intoxication, fatigue, hypoxia."""

        self.add_state(
            name="Alcohol Intoxication (Moderate)",
            phi=0.60, tau=0.50, rho=0.55, entropy=0.55,
            category="Impaired",
            notes="Reduced integration and binding"
        )

        self.add_state(
            name="Alcohol Intoxication (Severe)",
            phi=0.35, tau=0.25, rho=0.30, entropy=0.70,
            category="Impaired",
            notes="Heavily impaired, high entropy"
        )

        self.add_state(
            name="Extreme Fatigue",
            phi=0.55, tau=0.45, rho=0.50, entropy=0.60,
            category="Impaired",
            notes="Degraded performance, elevated entropy"
        )

        self.add_state(
            name="Hypoxia (Moderate)",
            phi=0.50, tau=0.40, rho=0.45, entropy=0.65,
            category="Impaired",
            notes="Oxygen deprivation effects"
        )

        self.add_state(
            name="Concussion (Acute)",
            phi=0.45, tau=0.35, rho=0.40, entropy=0.70,
            category="Impaired",
            notes="Traumatic brain injury, confusion"
        )

    def clinical_states(self):
        """Anesthesia, coma, vegetative states."""

        self.add_state(
            name="Light Sedation",
            phi=0.50, tau=0.40, rho=0.45, entropy=0.50,
            category="Clinical",
            notes="Drowsy but arousable"
        )

        self.add_state(
            name="Deep Sedation",
            phi=0.30, tau=0.20, rho=0.25, entropy=0.40,
            category="Clinical",
            notes="Difficult to arouse"
        )

        self.add_state(
            name="General Anesthesia",
            phi=0.05, tau=0.03, rho=0.04, entropy=0.15,
            category="Clinical",
            notes="Surgical anesthesia, minimal consciousness"
        )

        self.add_state(
            name="Coma (Light)",
            phi=0.15, tau=0.10, rho=0.12, entropy=0.35,
            category="Clinical",
            notes="Unresponsive, some brain activity"
        )

        self.add_state(
            name="Vegetative State",
            phi=0.08, tau=0.05, rho=0.06, entropy=0.25,
            category="Clinical",
            notes="Wakefulness without awareness"
        )

        self.add_state(
            name="Minimally Conscious State",
            phi=0.25, tau=0.15, rho=0.20, entropy=0.45,
            category="Clinical",
            notes="Some awareness, inconsistent responses"
        )

    def non_human_states(self):
        """Animal consciousness (various species)."""

        self.add_state(
            name="Chimpanzee",
            phi=0.80, tau=0.75, rho=0.75, entropy=0.20,
            category="Non-Human",
            notes="Great ape cognition, high complexity"
        )

        self.add_state(
            name="Dolphin",
            phi=0.70, tau=0.60, rho=0.70, entropy=0.25,
            category="Non-Human",
            notes="Marine mammal, echolocation"
        )

        self.add_state(
            name="Crow",
            phi=0.60, tau=0.50, rho=0.55, entropy=0.30,
            category="Non-Human",
            notes="Avian intelligence, tool use"
        )

        self.add_state(
            name="Octopus",
            phi=0.55, tau=0.40, rho=0.50, entropy=0.35,
            category="Non-Human",
            notes="Distributed nervous system"
        )

        self.add_state(
            name="Mouse",
            phi=0.40, tau=0.30, rho=0.35, entropy=0.40,
            category="Non-Human",
            notes="Small mammal, moderate complexity"
        )

        self.add_state(
            name="Bee",
            phi=0.25, tau=0.15, rho=0.20, entropy=0.35,
            category="Non-Human",
            notes="Insect, simple but organized"
        )

    def edge_cases(self):
        """Unusual and extreme states."""

        self.add_state(
            name="Sensory Deprivation (Extended)",
            phi=0.60, tau=0.50, rho=0.55, entropy=0.65,
            category="Edge Case",
            notes="Reduced external input, hallucinations possible"
        )

        self.add_state(
            name="Locked-In Syndrome",
            phi=0.85, tau=0.80, rho=0.85, entropy=0.20,
            category="Edge Case",
            notes="Conscious but paralyzed, intact awareness"
        )

        self.add_state(
            name="Seizure (Absence)",
            phi=0.20, tau=0.10, rho=0.15, entropy=0.50,
            category="Edge Case",
            notes="Brief loss of consciousness"
        )

        self.add_state(
            name="Seizure (Tonic-Clonic)",
            phi=0.10, tau=0.05, rho=0.08, entropy=0.70,
            category="Edge Case",
            notes="Generalized seizure, very low density"
        )

        self.add_state(
            name="Syncope (Fainting)",
            phi=0.15, tau=0.08, rho=0.10, entropy=0.45,
            category="Edge Case",
            notes="Brief unconsciousness from blood flow"
        )

        self.add_state(
            name="Near-Death Experience",
            phi=0.70, tau=0.55, rho=0.65, entropy=0.60,
            category="Edge Case",
            notes="Reported experiences at edge of death"
        )

    def generate_summary(self):
        """Generate comprehensive summary of corpus."""

        print_header("CORPUS EXPANSION SUMMARY")

        # Count by category
        categories = {}
        for state in self.states:
            cat = state['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(state)

        print(f"Total States: {len(self.states)}")
        print(f"Categories: {len(categories)}")
        print()

        print("States by Category:")
        for cat, states in sorted(categories.items()):
            print(f"  {cat:<20} : {len(states):2d} states")
        print()

        # Density statistics
        densities = [s['density'] for s in self.states]
        print("Density Statistics:")
        print(f"  Min:    {min(densities):.6f}")
        print(f"  Max:    {max(densities):.6f}")
        print(f"  Mean:   {np.mean(densities):.6f}")
        print(f"  Median: {np.median(densities):.6f}")
        print(f"  Std:    {np.std(densities):.6f}")
        print()

        # Density ranges
        very_low = sum(1 for d in densities if d < 0.05)
        low = sum(1 for d in densities if 0.05 <= d < 0.3)
        moderate = sum(1 for d in densities if 0.3 <= d < 0.6)
        high = sum(1 for d in densities if d >= 0.6)

        print("Density Distribution:")
        print(f"  Very Low (< 0.05):  {very_low:2d} states ({very_low/len(self.states)*100:.1f}%)")
        print(f"  Low (0.05-0.3):     {low:2d} states ({low/len(self.states)*100:.1f}%)")
        print(f"  Moderate (0.3-0.6): {moderate:2d} states ({moderate/len(self.states)*100:.1f}%)")
        print(f"  High (>= 0.6):      {high:2d} states ({high/len(self.states)*100:.1f}%)")
        print()

        # Top 10 highest density
        sorted_states = sorted(self.states, key=lambda s: s['density'], reverse=True)
        print("Top 10 Highest Density States:")
        for i, state in enumerate(sorted_states[:10], 1):
            print(f"  {i:2d}. {state['name']:<40} | D={state['density']:.4f} | {state['category']}")
        print()

        # Bottom 10 lowest density
        print("Bottom 10 Lowest Density States:")
        for i, state in enumerate(sorted_states[-10:][::-1], 1):
            print(f"  {i:2d}. {state['name']:<40} | D={state['density']:.6f} | {state['category']}")
        print()

        # Save to JSON
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"corpus_expansion_{timestamp}.json")

        output_data = {
            'timestamp': datetime.now().isoformat(),
            'total_states': len(self.states),
            'categories': {cat: len(states) for cat, states in categories.items()},
            'statistics': {
                'min_density': float(min(densities)),
                'max_density': float(max(densities)),
                'mean_density': float(np.mean(densities)),
                'median_density': float(np.median(densities)),
                'std_density': float(np.std(densities))
            },
            'distribution': {
                'very_low': very_low,
                'low': low,
                'moderate': moderate,
                'high': high
            },
            'states': self.states
        }

        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)

        print(f"✓ Corpus saved to: {output_file}")
        print()
        print("="*80)
        print("CORPUS EXPANSION COMPLETE".center(80))
        print("="*80)


def main():
    """Main execution."""
    expander = CorpusExpansion()
    expander.create_comprehensive_corpus()


if __name__ == "__main__":
    main()
