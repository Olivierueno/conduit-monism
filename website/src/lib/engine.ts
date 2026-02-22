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
 * - φ (Integration): Multi-metric approach (E_glob + PCI + ISD), validated
 *   by AT11 extended validation with 4/4 independent AI support.
 *   MODERATE-HIGH confidence. Hyper-integrated states exceed baseline wakefulness.
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
  
  // Density-based interpretations (thresholds calibrated to CANON v9.3.2 D values)
  if (D < 0.005) {
    return "Near-zero density. Equivalent to deep unconsciousness, coma, or absence of experience. (Propofol D ≈ 0.003)";
  }
  if (D < 0.02) {
    return "Minimal density. Fragmentary awareness at best. Consistent with: dreamless sleep (NREM N3 D ≈ 0.007), deep anesthesia.";
  }
  if (D < 0.10) {
    return "Low density. Degraded or partial experience. Consistent with: dreaming (REM D ≈ 0.076), dissociative states (ketamine D ≈ 0.077).";
  }
  if (D < 0.20) {
    return "Moderate density. Partial awareness. Consistent with: light psychedelic effects, emerging from anesthesia, distracted waking.";
  }
  if (D < 0.35) {
    return "Good density. Clear, coherent experience. Consistent with: normal wakefulness (D ≈ 0.241), flow states (D ≈ 0.275), meditation (D ≈ 0.327).";
  }
  if (D < 0.55) {
    return "High density. Vivid, intensified experience. Consistent with: psychedelic states with high coherence (DMT D ≈ 0.425), deep jhana.";
  }

  return "Very high density. Intensely unified, temporally deep, self-aware experience. Approaching theoretical maximum of the formula.";
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
  confidence: 'calibrated' | 'estimated' | 'speculative';
  invariants: Invariants;
  description: string;
}

export const presets: Preset[] = [
  // Human states (aligned with CANON.md v9.3.2)
  {
    name: "Human (Baseline Awake)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.80, tau: 0.75, rho: 0.65, H: 0.50, kappa: 0.65 },
    description: "Normal waking consciousness. CANON baseline. D ≈ 0.241."
  },
  {
    name: "Human (Flow State)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.90, tau: 0.70, rho: 0.65, H: 0.55, kappa: 0.75 },
    description: "Optimal performance state. High integration, moderate entropy with strong coherence. D ≈ 0.275."
  },
  {
    name: "Human (Meditation)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.85, tau: 0.80, rho: 0.70, H: 0.40, kappa: 0.80 },
    description: "Deep contemplative state. High coherence, low entropy, expanded temporal depth. D ≈ 0.327."
  },
  {
    name: "Human (Jhana)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.98, tau: 0.95, rho: 0.90, H: 0.15, kappa: 0.90 },
    description: "Hyper-integrated absorptive meditation. φ exceeds baseline wakefulness. AT11: ordered hyper-integration."
  },
  {
    name: "Human (Panic Attack)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.9, tau: 0.9, rho: 0.8, H: 0.25, kappa: 0.15 },
    description: "LOW entropy (rigidity), low coherence. Structure intact but rigid/frozen. AT10 correction: panic is rigid, not chaotic."
  },
  {
    name: "Human (Deep Sleep)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.40, tau: 0.15, rho: 0.23, H: 0.40, kappa: 0.30 },
    description: "NREM N3. Structural collapse. Integration, depth, and binding all minimal. D ≈ 0.007."
  },
  {
    name: "Human (Dreaming)",
    category: "human",
    confidence: "calibrated",
    invariants: { phi: 0.60, tau: 0.50, rho: 0.45, H: 0.55, kappa: 0.55 },
    description: "REM sleep. Partial structure with moderate entropy. Loose narrative, strange logic. D ≈ 0.076."
  },
  
  // Altered states (aligned with CANON.md v9.3.2)
  {
    name: "Psilocybin (Peak)",
    category: "altered",
    confidence: "estimated",
    invariants: { phi: 0.70, tau: 0.65, rho: 0.55, H: 0.60, kappa: 0.85 },
    description: "Psychedelic state. High entropy structured by coherence. D ≈ 0.184."
  },
  {
    name: "DMT Breakthrough",
    category: "altered",
    confidence: "estimated",
    invariants: { phi: 0.85, tau: 0.90, rho: 0.70, H: 0.70, kappa: 0.90 },
    description: "Extreme entropy but highly structured. 'More real than real'. The coherence gate opens. D ≈ 0.425."
  },
  {
    name: "Ketamine (Dissociative)",
    category: "altered",
    confidence: "estimated",
    invariants: { phi: 0.50, tau: 0.50, rho: 0.44, H: 0.55, kappa: 0.80 },
    description: "Dissociative state. Fractured integration, preserved coherence. D ≈ 0.077."
  },
  {
    name: "Seizure",
    category: "pathological",
    confidence: "estimated",
    invariants: { phi: 0.7, tau: 0.5, rho: 0.4, H: 0.95, kappa: 0.1 },
    description: "High entropy, no coherence. Neural chaos without structure. Blackout."
  },
  {
    name: "Anesthesia (Propofol)",
    category: "pathological",
    confidence: "estimated",
    invariants: { phi: 0.25, tau: 0.10, rho: 0.24, H: 0.35, kappa: 0.20 },
    description: "Pharmacological suppression of binding and integration. D ≈ 0.003."
  },
  
  // AI architectures (aligned with CANON.md v9.3.2)
  {
    name: "Transformer (GPT/Claude)",
    category: "ai",
    confidence: "estimated",
    invariants: { phi: 0.90, tau: 0.00, rho: 0.00, H: 0.30, kappa: 0.70 },
    description: "High integration, zero temporal depth, zero binding. No persistent state. ρ = 0 and τ = 0 mean D = 0."
  },
  {
    name: "RWKV (Recurrent)",
    category: "ai",
    confidence: "estimated",
    invariants: { phi: 0.70, tau: 0.50, rho: 0.15, H: 0.35, kappa: 0.50 },
    description: "Hidden state persists. Genuine binding proven via Amnesia Test. First AI with ρ > 0. D ≈ 0.031."
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
    confidence: "speculative",
    invariants: { phi: 0.05, tau: 0.02, rho: 0.01, H: 0.3, kappa: 0.2 },
    description: "302 neurons. Complete connectome mapped. Reflexive behavior only. Minimal integration."
  },
  {
    name: "Jellyfish",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.08, tau: 0.02, rho: 0.01, H: 0.4, kappa: 0.2 },
    description: "Nerve net, no central brain. Reactive to stimuli. No evidence of learning."
  },
  {
    name: "Fruit Fly",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.15, tau: 0.05, rho: 0.02, H: 0.4, kappa: 0.3 },
    description: "~100k neurons. Basic learning, circadian rhythms. Minimal binding."
  },
  {
    name: "Ant",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.18, tau: 0.08, rho: 0.03, H: 0.35, kappa: 0.35 },
    description: "~250k neurons. Colony intelligence, pheromone communication. Individual cognition limited."
  },
  {
    name: "Honeybee",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.25, tau: 0.15, rho: 0.08, H: 0.35, kappa: 0.4 },
    description: "~1M neurons. Waggle dance, navigation, learning. Emergent binding."
  },
  {
    name: "Jumping Spider",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.22, tau: 0.12, rho: 0.06, H: 0.35, kappa: 0.4 },
    description: "~600k neurons. Planning behavior, attention, prey tracking. Surprisingly complex for size."
  },
  {
    name: "Crab",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.2, tau: 0.1, rho: 0.05, H: 0.4, kappa: 0.35 },
    description: "Decapod crustacean. Pain-like responses, learning. Decentralized nervous system."
  },
  
  // Invertebrates - Complex
  {
    name: "Cuttlefish",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.35, tau: 0.25, rho: 0.2, H: 0.45, kappa: 0.5 },
    description: "~500M neurons. Camouflage, problem-solving, communication. High integration for invertebrate."
  },
  {
    name: "Octopus",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.25, H: 0.5, kappa: 0.5 },
    description: "~500M neurons. Distributed nervous system. Tool use, play, individual recognition."
  },
  
  // Fish
  {
    name: "Goldfish",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.25, tau: 0.15, rho: 0.1, H: 0.4, kappa: 0.4 },
    description: "Basic vertebrate. Spatial memory (contrary to myth), social learning."
  },
  {
    name: "Zebrafish",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.22, tau: 0.12, rho: 0.08, H: 0.4, kappa: 0.4 },
    description: "Model organism. Transparent brain allows imaging. Basic learning and memory."
  },
  {
    name: "Cleaner Wrasse",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.35, tau: 0.25, rho: 0.18, H: 0.35, kappa: 0.45 },
    description: "Passes mirror test (contested). Client recognition, strategic behavior."
  },
  {
    name: "Manta Ray",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.22, H: 0.35, kappa: 0.5 },
    description: "Large brain-to-body ratio. Possible self-recognition, curiosity toward divers."
  },
  
  // Amphibians & Reptiles
  {
    name: "Frog",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.25, tau: 0.12, rho: 0.08, H: 0.4, kappa: 0.35 },
    description: "Basic vertebrate. Prey detection, territorial behavior. Limited learning."
  },
  {
    name: "Turtle",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.3, tau: 0.2, rho: 0.12, H: 0.35, kappa: 0.4 },
    description: "Long-lived reptile. Spatial memory, navigation. Slow but persistent cognition."
  },
  {
    name: "Monitor Lizard",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.38, tau: 0.28, rho: 0.18, H: 0.35, kappa: 0.45 },
    description: "High reptilian intelligence. Problem-solving, counting, social learning."
  },
  
  // Birds - Lower cognition
  {
    name: "Chicken",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.35, tau: 0.25, rho: 0.15, H: 0.4, kappa: 0.4 },
    description: "Social hierarchy, object permanence, basic arithmetic. Often underestimated."
  },
  {
    name: "Pigeon",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.4, tau: 0.3, rho: 0.2, H: 0.35, kappa: 0.45 },
    description: "Navigation, categorization, self-recognition (trained). Good model organism."
  },
  
  // Birds - Higher cognition
  {
    name: "Parrot (African Grey)",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.3, kappa: 0.6 },
    description: "Vocal learning, numerical cognition, inference. Alex demonstrated zero concept."
  },
  {
    name: "Crow",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.4, H: 0.3, kappa: 0.6 },
    description: "Tool manufacture, planning, possible theory of mind. Corvid cognition rivals apes."
  },
  {
    name: "Raven",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.62, tau: 0.52, rho: 0.42, H: 0.3, kappa: 0.6 },
    description: "Future planning, social manipulation, play. Among most intelligent birds."
  },
  {
    name: "Magpie",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.38, H: 0.32, kappa: 0.58 },
    description: "Passes mirror test. Object caching, social cognition."
  },
  
  // Mammals - Small
  {
    name: "Mouse",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.35, kappa: 0.5 },
    description: "Emotional contagion, spatial memory, social hierarchy. Key model organism."
  },
  {
    name: "Rat",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.52, tau: 0.42, rho: 0.32, H: 0.35, kappa: 0.52 },
    description: "Regret, empathy, metacognition. More complex than mice."
  },
  {
    name: "Rabbit",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.45, tau: 0.35, rho: 0.25, H: 0.38, kappa: 0.45 },
    description: "Social bonds, spatial memory, emotional states. Prey animal cognition."
  },
  {
    name: "Squirrel",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.48, tau: 0.4, rho: 0.28, H: 0.35, kappa: 0.5 },
    description: "Cache planning, spatial memory, deceptive caching behavior."
  },
  
  // Mammals - Medium
  {
    name: "Cat",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.55, tau: 0.45, rho: 0.32, H: 0.38, kappa: 0.52 },
    description: "Object permanence, social bonds, hunting strategy. Independent cognition."
  },
  {
    name: "Dog",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.6, tau: 0.5, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Human emotion reading, word learning, social cognition. Co-evolved with humans."
  },
  {
    name: "Pig",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.38, H: 0.35, kappa: 0.55 },
    description: "Mirror self-recognition, joystick use, social complexity. Often underestimated."
  },
  {
    name: "Goat",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.38, kappa: 0.5 },
    description: "Problem-solving, long-term memory, human gaze following."
  },
  {
    name: "Sheep",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.48, tau: 0.38, rho: 0.28, H: 0.38, kappa: 0.48 },
    description: "Face recognition (human and sheep), emotional responses, social bonds."
  },
  {
    name: "Horse",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Human emotion reading, cross-modal recognition, social hierarchy."
  },
  {
    name: "Cow",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.52, tau: 0.42, rho: 0.3, H: 0.38, kappa: 0.5 },
    description: "Emotional states, social bonds, problem-solving. Individual personalities."
  },
  
  // Mammals - Large/Complex
  {
    name: "Wolf",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.62, tau: 0.52, rho: 0.4, H: 0.32, kappa: 0.58 },
    description: "Pack coordination, hunting strategy, social hierarchy. Ancestor of dogs."
  },
  {
    name: "Bear",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.58, tau: 0.48, rho: 0.38, H: 0.35, kappa: 0.55 },
    description: "Problem-solving, tool use (some species), long-term memory."
  },
  {
    name: "Seal",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.55, tau: 0.45, rho: 0.35, H: 0.35, kappa: 0.55 },
    description: "Vocal learning, rhythm perception, social cognition."
  },
  {
    name: "Orca",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.78, tau: 0.68, rho: 0.58, H: 0.28, kappa: 0.68 },
    description: "Culture, dialect, cooperative hunting, grief. Among most intelligent animals."
  },
  {
    name: "Dolphin (Bottlenose)",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.75, tau: 0.65, rho: 0.55, H: 0.3, kappa: 0.65 },
    description: "Mirror test, syntax comprehension, cooperative problem-solving, play."
  },
  {
    name: "Elephant",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.7, tau: 0.6, rho: 0.5, H: 0.25, kappa: 0.6 },
    description: "Self-recognition, grief rituals, long-term memory, empathy. 'Elephant never forgets.'"
  },
  
  // Primates - Non-ape
  {
    name: "Lemur",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.5, tau: 0.4, rho: 0.3, H: 0.38, kappa: 0.5 },
    description: "Social cognition, tool use (some species), numerical cognition."
  },
  {
    name: "Capuchin Monkey",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.62, tau: 0.52, rho: 0.42, H: 0.32, kappa: 0.58 },
    description: "Tool use, fairness sense, economic behavior. High primate intelligence."
  },
  {
    name: "Rhesus Macaque",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.65, tau: 0.55, rho: 0.45, H: 0.32, kappa: 0.6 },
    description: "Metacognition, numerical cognition, social hierarchy. Key research model."
  },
  
  // Great Apes
  {
    name: "Gorilla",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.75, tau: 0.65, rho: 0.55, H: 0.3, kappa: 0.62 },
    description: "Sign language (Koko), self-recognition, tool use, emotional depth."
  },
  {
    name: "Orangutan",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.78, tau: 0.68, rho: 0.58, H: 0.28, kappa: 0.65 },
    description: "Tool manufacture, future planning, cultural transmission. Solitary but intelligent."
  },
  {
    name: "Bonobo",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.8, tau: 0.7, rho: 0.6, H: 0.3, kappa: 0.65 },
    description: "Language comprehension (Kanzi), empathy, conflict resolution. Close human relative."
  },
  {
    name: "Chimpanzee",
    category: "animal",
    confidence: "speculative",
    invariants: { phi: 0.8, tau: 0.7, rho: 0.6, H: 0.3, kappa: 0.65 },
    description: "Theory of mind, tool manufacture, culture, warfare. Closest to human topology."
  },
  
  // Edge cases
  {
    name: "Corporation (Walmart)",
    category: "pathological",
    confidence: "speculative",
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
 * Calculate parameter sensitivity (partial derivatives of D)
 * Returns ∂D/∂param for each invariant at the given point.
 */
export function calculateSensitivity(invariants: Invariants): Record<keyof Invariants, number> {
  const { phi, tau, rho, H, kappa } = invariants;
  const gate = (1 - Math.sqrt(H)) + (H * kappa);

  // ∂D/∂φ = τ * ρ * gate
  const dD_dphi = tau * rho * gate;

  // ∂D/∂τ = φ * ρ * gate
  const dD_dtau = phi * rho * gate;

  // ∂D/∂ρ = φ * τ * gate
  const dD_drho = phi * tau * gate;

  // ∂D/∂H = φ * τ * ρ * (-1/(2√H) + κ)
  const dD_dH = phi * tau * rho * (H > 0 ? (-1 / (2 * Math.sqrt(H)) + kappa) : kappa);

  // ∂D/∂κ = φ * τ * ρ * H
  const dD_dkappa = phi * tau * rho * H;

  return { phi: dD_dphi, tau: dD_dtau, rho: dD_drho, H: dD_dH, kappa: dD_dkappa };
}

/**
 * Calculate uncertainty in D given parameter uncertainties.
 * Uses linear error propagation: σ_D² = Σ (∂D/∂xi)² * σ_xi²
 * Returns ± range around D.
 */
export function calculateUncertainty(
  invariants: Invariants,
  paramUncertainty: number = 0.05  // default ±0.05 for each parameter
): { dMin: number; dMax: number; sigma: number } {
  const sensitivity = calculateSensitivity(invariants);
  const D = calculateDensity(invariants).D;

  // Linear propagation
  const sigmaSquared =
    (sensitivity.phi ** 2 + sensitivity.tau ** 2 + sensitivity.rho ** 2 +
     sensitivity.H ** 2 + sensitivity.kappa ** 2) * (paramUncertainty ** 2);

  const sigma = Math.sqrt(sigmaSquared);

  return {
    dMin: Math.max(0, D - sigma),
    dMax: Math.min(1, D + sigma),
    sigma,
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
