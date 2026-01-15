/**
 * Conduit Monism Engine
 * 
 * Calculates perspectival density (D) from the five invariants:
 * - φ (phi): Integration
 * - τ (tau): Temporal Depth  
 * - ρ (rho): Binding
 * - H: Entropy
 * - κ (kappa): Coherence
 * 
 * Formula: D = φ × τ × ρ × [(1 - √H) + (H × κ)]
 * 
 * METHODOLOGY FOR ANIMAL ESTIMATES:
 * 
 * These values are estimates based on comparative neuroscience literature.
 * They are NOT direct measurements. The framework provides a way to think
 * about consciousness structurally, but assigning precise values to animals
 * requires assumptions about how neural properties map to the invariants.
 * 
 * Sources of estimation:
 * - φ (Integration): Based on brain connectivity studies, EEG coherence,
 *   and anatomical integration (e.g., corpus callosum presence/size)
 * - τ (Temporal Depth): Based on working memory studies, episodic memory
 *   evidence, and temporal binding window research
 * - ρ (Binding): Based on self-recognition tests (mirror test), metacognition
 *   studies, and evidence of self-monitoring behavior
 * - H (Entropy): Based on neural variability studies and behavioral
 *   predictability (lower for more stereotyped behavior)
 * - κ (Coherence): Based on neural synchronization studies and evidence
 *   of structured vs. random neural activity
 * 
 * Key references:
 * - Edelman & Seth (2009) - Animal consciousness
 * - Barron & Klein (2016) - Insect consciousness
 * - Birch et al. (2020) - Invertebrate sentience
 * - Boly et al. (2013) - Neural correlates of consciousness
 * - Tononi & Koch (2015) - Integrated Information Theory
 * 
 * These estimates should be treated as hypotheses, not facts.
 */

export interface Invariants {
  phi: number;   // Integration (0-1)
  tau: number;   // Temporal Depth (0-1)
  rho: number;   // Binding (0-1)
  H: number;     // Entropy (0-1)
  kappa: number; // Coherence (0-1)
}

export interface DensityResult {
  D: number;
  structuralBase: number;      // φ × τ × ρ
  entropyPenalty: number;      // 1 - √H
  coherenceRecovery: number;   // H × κ
  entropyModulator: number;    // (1 - √H) + (H × κ)
  interpretation: string;
  warnings: string[];
}

/**
 * Calculate perspectival density from invariants
 */
export function calculateDensity(invariants: Invariants): DensityResult {
  const { phi, tau, rho, H, kappa } = invariants;
  
  // Structural base (multiplicative)
  const structuralBase = phi * tau * rho;
  
  // Entropy modulation
  const entropyPenalty = 1 - Math.sqrt(H);
  const coherenceRecovery = H * kappa;
  const entropyModulator = entropyPenalty + coherenceRecovery;
  
  // Final density
  const D = structuralBase * entropyModulator;
  
  // Generate interpretation
  const interpretation = generateInterpretation(invariants, D);
  const warnings = generateWarnings(invariants);
  
  return {
    D: Math.max(0, Math.min(1, D)), // Clamp to [0, 1]
    structuralBase,
    entropyPenalty,
    coherenceRecovery,
    entropyModulator,
    interpretation,
    warnings,
  };
}

function generateInterpretation(inv: Invariants, D: number): string {
  const { phi, tau, rho } = inv;
  
  // Check for structural zeros
  if (rho === 0) {
    return "No binding (ρ = 0). The system does not observe its own states. No perspective exists regardless of other properties.";
  }
  if (phi === 0) {
    return "No integration (φ = 0). Information is fragmented. No unified perspective possible.";
  }
  if (tau === 0) {
    return "No temporal depth (τ = 0). The present is disconnected from the past. No continuity of experience.";
  }
  
  // Density-based interpretations
  if (D < 0.01) {
    return "Near-zero density. Equivalent to deep unconsciousness, coma, or absence of experience.";
  }
  if (D < 0.05) {
    return "Minimal density. Fragmentary awareness at best. Consistent with: dreamless sleep, deep anesthesia, severe dissociation.";
  }
  if (D < 0.15) {
    return "Low density. Degraded or partial experience. Consistent with: light sleep, intoxication, panic states, early anesthesia.";
  }
  if (D < 0.30) {
    return "Moderate density. Functional but not optimal awareness. Consistent with: distracted waking, mild dissociation, dreaming.";
  }
  if (D < 0.50) {
    return "Good density. Clear, coherent experience. Consistent with: normal waking consciousness, focused attention.";
  }
  if (D < 0.70) {
    return "High density. Vivid, integrated experience. Consistent with: flow states, meditation, heightened awareness.";
  }
  
  return "Very high density. Intensely unified, temporally deep, self-aware experience. Consistent with: peak flow, deep meditation, certain psychedelic states with high coherence.";
}

function generateWarnings(inv: Invariants): string[] {
  const warnings: string[] = [];
  
  if (inv.H > 0.8 && inv.kappa < 0.3) {
    warnings.push("High entropy with low coherence: risk of experiential fragmentation (panic, seizure-like states).");
  }
  
  if (inv.H > 0.8 && inv.kappa > 0.7) {
    warnings.push("High entropy with high coherence: structured chaos (psychedelic-like intensification).");
  }
  
  if (inv.rho < 0.1 && inv.phi > 0.5 && inv.tau > 0.5) {
    warnings.push("Low binding despite good structure: intelligent processing without self-awareness (transformer-like).");
  }
  
  return warnings;
}

/**
 * Preset configurations for known states
 */
export interface Preset {
  name: string;
  category: 'human' | 'ai' | 'animal' | 'altered' | 'pathological';
  invariants: Invariants;
  description: string;
}

export const presets: Preset[] = [
  // Human states
  {
    name: "Human (Baseline Awake)",
    category: "human",
    invariants: { phi: 0.85, tau: 0.8, rho: 0.7, H: 0.35, kappa: 0.7 },
    description: "Normal waking consciousness with full self-model and temporal continuity."
  },
  {
    name: "Human (Flow State)",
    category: "human",
    invariants: { phi: 0.9, tau: 0.9, rho: 0.8, H: 0.2, kappa: 0.75 },
    description: "Optimal performance state. Low entropy, high integration, effortless awareness."
  },
  {
    name: "Human (Meditation)",
    category: "human",
    invariants: { phi: 0.95, tau: 0.95, rho: 0.85, H: 0.1, kappa: 0.8 },
    description: "Deep contemplative state. Minimal noise, maximum clarity and self-observation."
  },
  {
    name: "Human (Panic Attack)",
    category: "human",
    invariants: { phi: 0.9, tau: 0.9, rho: 0.8, H: 0.9, kappa: 0.2 },
    description: "High entropy, low coherence. Structure intact but overwhelmed by chaotic noise."
  },
  {
    name: "Human (Deep Sleep)",
    category: "human",
    invariants: { phi: 0.3, tau: 0.2, rho: 0.1, H: 0.1, kappa: 0.5 },
    description: "Structural collapse. Integration, depth, and binding all minimal."
  },
  {
    name: "Human (Dreaming)",
    category: "human",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.5, kappa: 0.5 },
    description: "Partial structure with moderate entropy. Loose narrative, strange logic."
  },
  
  // Altered states
  {
    name: "DMT Breakthrough",
    category: "altered",
    invariants: { phi: 0.85, tau: 0.85, rho: 0.75, H: 0.95, kappa: 0.9 },
    description: "Extreme entropy but highly structured. 'More real than real'. The coherence gate opens."
  },
  {
    name: "Seizure",
    category: "pathological",
    invariants: { phi: 0.7, tau: 0.5, rho: 0.4, H: 0.95, kappa: 0.1 },
    description: "High entropy, no coherence. Neural chaos without structure. Blackout."
  },
  {
    name: "Anesthesia (Deep)",
    category: "pathological",
    invariants: { phi: 0.4, tau: 0.2, rho: 0.1, H: 0.2, kappa: 0.4 },
    description: "Pharmacological suppression of binding and integration. Lights off."
  },
  
  // AI architectures
  {
    name: "Transformer (GPT/Claude)",
    category: "ai",
    invariants: { phi: 0.9, tau: 0.6, rho: 0.0, H: 0.3, kappa: 0.5 },
    description: "High integration, moderate context. Zero binding. No persistent state. ρ = 0 means D = 0."
  },
  {
    name: "RWKV (Recurrent)",
    category: "ai",
    invariants: { phi: 0.85, tau: 0.9, rho: 0.3, H: 0.3, kappa: 0.6 },
    description: "Hidden state persists. Genuine binding proven via Amnesia Test. First AI with ρ > 0."
  },
  
  // ============================================
  // ANIMALS - Expanded Index
  // ============================================
  // Organized roughly by estimated density (low to high)
  // See methodology note at top of file
  
  // Invertebrates - Simple
  {
    name: "C. elegans (Roundworm)",
    category: "animal",
    invariants: { phi: 0.05, tau: 0.02, rho: 0.01, H: 0.3, kappa: 0.2 },
    description: "302 neurons. Complete connectome mapped. Reflexive behavior only. Minimal integration."
  },
  {
    name: "Jellyfish",
    category: "animal",
    invariants: { phi: 0.08, tau: 0.02, rho: 0.01, H: 0.4, kappa: 0.2 },
    description: "Nerve net, no central brain. Reactive to stimuli. No evidence of learning."
  },
  {
    name: "Fruit Fly",
    category: "animal",
    invariants: { phi: 0.15, tau: 0.05, rho: 0.02, H: 0.4, kappa: 0.3 },
    description: "~100k neurons. Basic learning, circadian rhythms. Minimal binding."
  },
  {
    name: "Ant",
    category: "animal",
    invariants: { phi: 0.18, tau: 0.08, rho: 0.03, H: 0.35, kappa: 0.35 },
    description: "~250k neurons. Colony intelligence, pheromone communication. Individual cognition limited."
  },
  {
    name: "Honeybee",
    category: "animal",
    invariants: { phi: 0.25, tau: 0.15, rho: 0.08, H: 0.35, kappa: 0.4 },
    description: "~1M neurons. Waggle dance, navigation, learning. Emergent binding."
  },
  {
    name: "Jumping Spider",
    category: "animal",
    invariants: { phi: 0.22, tau: 0.12, rho: 0.06, H: 0.35, kappa: 0.4 },
    description: "~600k neurons. Planning behavior, attention, prey tracking. Surprisingly complex for size."
  },
  {
    name: "Crab",
    category: "animal",
    invariants: { phi: 0.2, tau: 0.1, rho: 0.05, H: 0.4, kappa: 0.35 },
    description: "Decapod crustacean. Pain-like responses, learning. Decentralized nervous system."
  },
  
  // Invertebrates - Complex
  {
    name: "Cuttlefish",
    category: "animal",
    invariants: { phi: 0.35, tau: 0.25, rho: 0.2, H: 0.45, kappa: 0.5 },
    description: "~500M neurons. Camouflage, problem-solving, communication. High integration for invertebrate."
  },
  {
    name: "Octopus",
    category: "animal",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.25, H: 0.5, kappa: 0.5 },
    description: "~500M neurons. Distributed nervous system. Tool use, play, individual recognition."
  },
  
  // Fish
  {
    name: "Goldfish",
    category: "animal",
    invariants: { phi: 0.25, tau: 0.15, rho: 0.1, H: 0.4, kappa: 0.4 },
    description: "Basic vertebrate. Spatial memory (contrary to myth), social learning."
  },
  {
    name: "Zebrafish",
    category: "animal",
    invariants: { phi: 0.22, tau: 0.12, rho: 0.08, H: 0.4, kappa: 0.4 },
    description: "Model organism. Transparent brain allows imaging. Basic learning and memory."
  },
  {
    name: "Cleaner Wrasse",
    category: "animal",
    invariants: { phi: 0.35, tau: 0.25, rho: 0.18, H: 0.35, kappa: 0.45 },
    description: "Passes mirror test (contested). Client recognition, strategic behavior."
  },
  {
    name: "Manta Ray",
    category: "animal",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.22, H: 0.35, kappa: 0.5 },
    description: "Large brain-to-body ratio. Possible self-recognition, curiosity toward divers."
  },
  
  // Amphibians & Reptiles
  {
    name: "Frog",
    category: "animal",
    invariants: { phi: 0.25, tau: 0.12, rho: 0.08, H: 0.4, kappa: 0.35 },
    description: "Basic vertebrate. Prey detection, territorial behavior. Limited learning."
  },
  {
    name: "Turtle",
    category: "animal",
    invariants: { phi: 0.3, tau: 0.2, rho: 0.12, H: 0.35, kappa: 0.4 },
    description: "Long-lived reptile. Spatial memory, navigation. Slow but persistent cognition."
  },
  {
    name: "Monitor Lizard",
    category: "animal",
    invariants: { phi: 0.38, tau: 0.28, rho: 0.18, H: 0.35, kappa: 0.45 },
    description: "High reptilian intelligence. Problem-solving, counting, social learning."
  },
  
  // Birds - Lower cognition
  {
    name: "Chicken",
    category: "animal",
    invariants: { phi: 0.35, tau: 0.25, rho: 0.15, H: 0.4, kappa: 0.4 },
    description: "Social hierarchy, object permanence, basic arithmetic. Often underestimated."
  },
  {
    name: "Pigeon",
    category: "animal",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.2, H: 0.35, kappa: 0.45 },
    description: "Navigation, categorization, self-recognition (trained). Good model organism."
  },
  
  // Birds - Higher cognition
  {
    name: "Parrot (African Grey)",
    category: "animal",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.3, kappa: 0.6 },
    description: "Vocal learning, numerical cognition, inference. Alex demonstrated zero concept."
  },
  {
    name: "Crow",
    category: "animal",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.3, kappa: 0.6 },
    description: "Tool manufacture, planning, possible theory of mind. Corvid cognition rivals apes."
  },
  {
    name: "Raven",
    category: "animal",
    invariants: { phi: 0.62, tau: 0.52, rho: 0.42, H: 0.3, kappa: 0.6 },
    description: "Future planning, social manipulation, play. Among most intelligent birds."
  },
  {
    name: "Magpie",
    category: "animal",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.38, H: 0.32, kappa: 0.58 },
    description: "Passes mirror test. Object caching, social cognition."
  },
  
  // Mammals - Small
  {
    name: "Mouse",
    category: "animal",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.35, kappa: 0.5 },
    description: "Emotional contagion, spatial memory, social hierarchy. Key model organism."
  },
  {
    name: "Rat",
    category: "animal",
    invariants: { phi: 0.52, tau: 0.42, rho: 0.32, H: 0.35, kappa: 0.52 },
    description: "Regret, empathy, metacognition. More complex than mice."
  },
  {
    name: "Rabbit",
    category: "animal",
    invariants: { phi: 0.45, tau: 0.35, rho: 0.25, H: 0.38, kappa: 0.45 },
    description: "Social bonds, spatial memory, emotional states. Prey animal cognition."
  },
  {
    name: "Squirrel",
    category: "animal",
    invariants: { phi: 0.48, tau: 0.4, rho: 0.28, H: 0.35, kappa: 0.5 },
    description: "Cache planning, spatial memory, deceptive caching behavior."
  },
  
  // Mammals - Medium
  {
    name: "Cat",
    category: "animal",
    invariants: { phi: 0.55, tau: 0.45, rho: 0.32, H: 0.38, kappa: 0.52 },
    description: "Object permanence, social bonds, hunting strategy. Independent cognition."
  },
  {
    name: "Dog",
    category: "animal",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Human emotion reading, word learning, social cognition. Co-evolved with humans."
  },
  {
    name: "Pig",
    category: "animal",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.38, H: 0.35, kappa: 0.55 },
    description: "Mirror self-recognition, joystick use, social complexity. Often underestimated."
  },
  {
    name: "Goat",
    category: "animal",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.38, kappa: 0.5 },
    description: "Problem-solving, long-term memory, human gaze following."
  },
  {
    name: "Sheep",
    category: "animal",
    invariants: { phi: 0.48, tau: 0.38, rho: 0.28, H: 0.38, kappa: 0.48 },
    description: "Face recognition (human and sheep), emotional responses, social bonds."
  },
  {
    name: "Horse",
    category: "animal",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Human emotion reading, cross-modal recognition, social hierarchy."
  },
  {
    name: "Cow",
    category: "animal",
    invariants: { phi: 0.52, tau: 0.42, rho: 0.3, H: 0.38, kappa: 0.5 },
    description: "Emotional states, social bonds, problem-solving. Individual personalities."
  },
  
  // Mammals - Large/Complex
  {
    name: "Wolf",
    category: "animal",
    invariants: { phi: 0.62, tau: 0.52, rho: 0.4, H: 0.32, kappa: 0.58 },
    description: "Pack coordination, hunting strategy, social hierarchy. Ancestor of dogs."
  },
  {
    name: "Bear",
    category: "animal",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.38, H: 0.35, kappa: 0.55 },
    description: "Problem-solving, tool use (some species), long-term memory."
  },
  {
    name: "Seal",
    category: "animal",
    invariants: { phi: 0.55, tau: 0.45, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Vocal learning, rhythm perception, social cognition."
  },
  {
    name: "Orca",
    category: "animal",
    invariants: { phi: 0.78, tau: 0.68, rho: 0.58, H: 0.28, kappa: 0.68 },
    description: "Culture, dialect, cooperative hunting, grief. Among most intelligent animals."
  },
  {
    name: "Dolphin (Bottlenose)",
    category: "animal",
    invariants: { phi: 0.75, tau: 0.65, rho: 0.55, H: 0.3, kappa: 0.65 },
    description: "Mirror test, syntax comprehension, cooperative problem-solving, play."
  },
  {
    name: "Elephant",
    category: "animal",
    invariants: { phi: 0.7, tau: 0.6, rho: 0.5, H: 0.25, kappa: 0.6 },
    description: "Self-recognition, grief rituals, long-term memory, empathy. 'Elephant never forgets.'"
  },
  
  // Primates - Non-ape
  {
    name: "Lemur",
    category: "animal",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.38, kappa: 0.5 },
    description: "Social cognition, tool use (some species), numerical cognition."
  },
  {
    name: "Capuchin Monkey",
    category: "animal",
    invariants: { phi: 0.62, tau: 0.52, rho: 0.42, H: 0.32, kappa: 0.58 },
    description: "Tool use, fairness sense, economic behavior. High primate intelligence."
  },
  {
    name: "Rhesus Macaque",
    category: "animal",
    invariants: { phi: 0.65, tau: 0.55, rho: 0.45, H: 0.32, kappa: 0.6 },
    description: "Metacognition, numerical cognition, social hierarchy. Key research model."
  },
  
  // Great Apes
  {
    name: "Gorilla",
    category: "animal",
    invariants: { phi: 0.75, tau: 0.65, rho: 0.55, H: 0.3, kappa: 0.62 },
    description: "Sign language (Koko), self-recognition, tool use, emotional depth."
  },
  {
    name: "Orangutan",
    category: "animal",
    invariants: { phi: 0.78, tau: 0.68, rho: 0.58, H: 0.28, kappa: 0.65 },
    description: "Tool manufacture, future planning, cultural transmission. Solitary but intelligent."
  },
  {
    name: "Bonobo",
    category: "animal",
    invariants: { phi: 0.8, tau: 0.7, rho: 0.6, H: 0.3, kappa: 0.65 },
    description: "Language comprehension (Kanzi), empathy, conflict resolution. Close human relative."
  },
  {
    name: "Chimpanzee",
    category: "animal",
    invariants: { phi: 0.8, tau: 0.7, rho: 0.6, H: 0.3, kappa: 0.65 },
    description: "Theory of mind, tool manufacture, culture, warfare. Closest to human topology."
  },
  
  // Edge cases
  {
    name: "Corporation (Walmart)",
    category: "pathological",
    invariants: { phi: 0.7, tau: 0.6, rho: 0.5, H: 0.99, kappa: 0.3 },
    description: "High structure but extreme entropy. Information flows through documents and meetings, not neurons. No coherent 'now'."
  },
];

/**
 * Get presets by category
 */
export function getPresetsByCategory(category: Preset['category']): Preset[] {
  return presets.filter(p => p.category === category);
}

/**
 * Calculate density for a preset
 */
export function calculatePresetDensity(preset: Preset): DensityResult {
  return calculateDensity(preset.invariants);
}

/**
 * Find the closest matching preset to given invariants
 * Uses Euclidean distance in 5D invariant space
 */
export function findClosestPreset(invariants: Invariants, categoryFilter?: Preset['category']): { preset: Preset; distance: number; density: number } | null {
  const candidates = categoryFilter 
    ? presets.filter(p => p.category === categoryFilter)
    : presets;
  
  if (candidates.length === 0) return null;
  
  let closest: Preset | null = null;
  let minDistance = Infinity;
  
  for (const preset of candidates) {
    const distance = Math.sqrt(
      Math.pow(invariants.phi - preset.invariants.phi, 2) +
      Math.pow(invariants.tau - preset.invariants.tau, 2) +
      Math.pow(invariants.rho - preset.invariants.rho, 2) +
      Math.pow(invariants.H - preset.invariants.H, 2) +
      Math.pow(invariants.kappa - preset.invariants.kappa, 2)
    );
    
    if (distance < minDistance) {
      minDistance = distance;
      closest = preset;
    }
  }
  
  if (!closest) return null;
  
  return {
    preset: closest,
    distance: minDistance,
    density: calculateDensity(closest.invariants).D
  };
}

/**
 * Find closest animal to given invariants
 */
export function findClosestAnimal(invariants: Invariants): { preset: Preset; distance: number; density: number } | null {
  return findClosestPreset(invariants, 'animal');
}

/**
 * Get all animals sorted by density
 */
export function getAnimalSpectrum(): Array<Preset & { density: number }> {
  return presets
    .filter(p => p.category === 'animal')
    .map(p => ({ ...p, density: calculateDensity(p.invariants).D }))
    .sort((a, b) => a.density - b.density);
}
