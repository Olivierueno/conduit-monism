'use client';

import { useState, useEffect } from 'react';
import MarkdownRenderer from '@/components/MarkdownRenderer';

interface Experiment {
  id: string;
  title: string;
  content: string;
  parent_file: string;
  test_number: number | null;
  status: 'confirmed' | 'falsified' | 'pending' | 'planned';
  type: string;
  date: string | null;
  filename: string;
}

interface ExperimentsIndex {
  confirmed: Experiment[];
  falsified: Experiment[];
  pending: Experiment[];
  planned: Experiment[];
  all: Experiment[];
}

export default function ValidationPage() {
  const [experiments, setExperiments] = useState<ExperimentsIndex | null>(null);
  const [selectedExperiment, setSelectedExperiment] = useState<Experiment | null>(null);
  const [filter, setFilter] = useState<'all' | 'confirmed' | 'falsified' | 'planned'>('all');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/data/experiments_index.json')
      .then(res => res.json())
      .then(data => {
        setExperiments(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load experiments:', err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <main className="min-h-screen py-12 px-6">
        <div className="max-w-5xl mx-auto">
          <p className="text-neutral-500">Loading experiments...</p>
        </div>
      </main>
    );
  }

  if (!experiments) {
    return (
      <main className="min-h-screen py-12 px-6">
        <div className="max-w-5xl mx-auto">
          <p className="text-red-500">Failed to load experiments.</p>
        </div>
      </main>
    );
  }

  const getFilteredExperiments = () => {
    if (filter === 'all') return experiments.all;
    return experiments[filter];
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'confirmed': return 'bg-green-900/50 text-green-400 border-green-900/50';
      case 'falsified': return 'bg-red-900/50 text-red-400 border-red-900/50';
      case 'planned': return 'bg-yellow-900/50 text-yellow-400 border-yellow-900/50';
      case 'pending': return 'bg-blue-900/50 text-blue-400 border-blue-900/50';
      default: return 'bg-neutral-800 text-neutral-400 border-neutral-800';
    }
  };

  const getStatusLabel = (status: string) => {
    switch (status) {
      case 'confirmed': return 'CONFIRMED';
      case 'falsified': return 'FALSIFIED';
      case 'planned': return 'PLANNED';
      case 'pending': return 'PENDING';
      default: return status.toUpperCase();
    }
  };

  return (
    <main className="min-h-screen py-12 px-6">
      <div className="max-w-5xl mx-auto">
        <div className="mb-12">
          <h1 className="text-2xl font-mono mb-4">Validation</h1>
          <p className="text-neutral-500">
            Experiments conducted to test and falsify the framework. 
            Failures are documented alongside successes.
          </p>
        </div>

        {/* Summary Stats */}
        <section className="mb-12">
          <div className="grid grid-cols-4 gap-4 mb-6">
            <div className="p-4 border border-neutral-800 text-center">
              <div className="text-2xl font-mono">{experiments.all.length}</div>
              <div className="text-xs text-neutral-500">Total Experiments</div>
            </div>
            <div className="p-4 border border-green-900/50 text-center">
              <div className="text-2xl font-mono text-green-500">{experiments.confirmed.length}</div>
              <div className="text-xs text-neutral-500">Confirmed</div>
            </div>
            <div className="p-4 border border-red-900/50 text-center">
              <div className="text-2xl font-mono text-red-500">{experiments.falsified.length}</div>
              <div className="text-xs text-neutral-500">Falsified</div>
            </div>
            <div className="p-4 border border-yellow-900/50 text-center">
              <div className="text-2xl font-mono text-yellow-500">{experiments.planned.length}</div>
              <div className="text-xs text-neutral-500">Planned</div>
            </div>
          </div>
        </section>

        {/* Filter Tabs */}
        <section className="mb-8">
          <div className="flex gap-2 border-b border-neutral-800">
            <button
              onClick={() => setFilter('all')}
              className={`px-4 py-2 text-sm font-mono transition-colors ${
                filter === 'all'
                  ? 'text-neutral-300 border-b-2 border-neutral-300'
                  : 'text-neutral-500 hover:text-neutral-400'
              }`}
            >
              All ({experiments.all.length})
            </button>
            <button
              onClick={() => setFilter('confirmed')}
              className={`px-4 py-2 text-sm font-mono transition-colors ${
                filter === 'confirmed'
                  ? 'text-green-400 border-b-2 border-green-400'
                  : 'text-neutral-500 hover:text-neutral-400'
              }`}
            >
              Confirmed ({experiments.confirmed.length})
            </button>
            <button
              onClick={() => setFilter('falsified')}
              className={`px-4 py-2 text-sm font-mono transition-colors ${
                filter === 'falsified'
                  ? 'text-red-400 border-b-2 border-red-400'
                  : 'text-neutral-500 hover:text-neutral-400'
              }`}
            >
              Falsified ({experiments.falsified.length})
            </button>
            <button
              onClick={() => setFilter('planned')}
              className={`px-4 py-2 text-sm font-mono transition-colors ${
                filter === 'planned'
                  ? 'text-yellow-400 border-b-2 border-yellow-400'
                  : 'text-neutral-500 hover:text-neutral-400'
              }`}
            >
              Planned ({experiments.planned.length})
            </button>
          </div>
        </section>

        {/* Experiments List */}
        <section className="mb-12">
          <div className="space-y-4">
            {getFilteredExperiments().map((exp) => (
              <details
                key={exp.id}
                className={`border ${getStatusColor(exp.status)} group`}
              >
                <summary className="p-4 cursor-pointer hover:bg-neutral-900/50 transition-colors">
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <span className={`text-xs font-mono px-2 py-0.5 ${getStatusColor(exp.status)} mr-2`}>
                        {getStatusLabel(exp.status)}
                      </span>
                      <span className="text-neutral-300">{exp.title}</span>
                      {exp.test_number && (
                        <span className="text-xs text-neutral-600 ml-2">(Test {exp.test_number})</span>
                      )}
                    </div>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setSelectedExperiment(exp);
                      }}
                      className="text-xs text-neutral-500 hover:text-neutral-300 ml-4"
                    >
                      View Full →
                    </button>
                  </div>
                  <div className="mt-2 text-xs text-neutral-600 font-mono">
                    {exp.filename}
                  </div>
                </summary>
                <div className="p-4 border-t border-neutral-800/50">
                  <div className="text-sm text-neutral-400 max-h-96 overflow-y-auto">
                    <MarkdownRenderer content={exp.content.substring(0, 2000)} />
                    {exp.content.length > 2000 && (
                      <p className="text-neutral-600 text-xs mt-4">
                        ... (truncated, click "View Full" to see complete content)
                      </p>
                    )}
                  </div>
                </div>
              </details>
            ))}
          </div>
        </section>

        {/* Tools Section */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Testing Tools</h2>
          <div className="grid md:grid-cols-2 gap-4">
            <div className="p-4 border border-neutral-800">
              <h3 className="font-mono text-neutral-300 mb-2">Interactive Engine</h3>
              <p className="text-sm text-neutral-500 mb-4">
                Web-based calculator for testing the density formula with real-time visualization.
              </p>
              <a
                href="/engine"
                className="text-xs text-neutral-400 hover:text-neutral-300 underline"
              >
                Open Engine →
              </a>
            </div>
            <div className="p-4 border border-neutral-800">
              <h3 className="font-mono text-neutral-300 mb-2">RWKV Cloud Server</h3>
              <p className="text-sm text-neutral-500 mb-4">
                GPU-accelerated RWKV instance for binding tests (Amnesia Test, decay measurements).
              </p>
              <p className="text-xs text-neutral-600 font-mono">
                Setup: notebooks/RWKV_Colab_Server.ipynb
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <h3 className="font-mono text-neutral-300 mb-2">Python Engine</h3>
              <p className="text-sm text-neutral-500 mb-4">
                Local state space exploration with vector database and operators.
              </p>
              <p className="text-xs text-neutral-600 font-mono">
                scripts/conduit_engine.py
              </p>
            </div>
            <div className="p-4 border border-neutral-800">
              <h3 className="font-mono text-neutral-300 mb-2">Falsification Scripts</h3>
              <p className="text-sm text-neutral-500 mb-4">
                Automated tests designed to break the framework.
              </p>
              <p className="text-xs text-neutral-600 font-mono">
                scripts/run_falsification_tests.py
              </p>
            </div>
          </div>
        </section>

        {/* Methodology */}
        <section className="mb-12">
          <h2 className="text-sm font-mono text-neutral-500 mb-4 uppercase tracking-wide">Methodology</h2>
          <div className="p-4 border border-neutral-800 text-sm text-neutral-500">
            <p className="mb-4">
              All experiments follow adversarial testing principles. The goal is falsification, not confirmation.
            </p>
            <p className="mb-4">
              <strong className="text-neutral-400">Falsification criteria:</strong> Each claim has explicit break conditions. 
              If the break condition is met, the claim is rejected.
            </p>
            <p className="mb-4">
              <strong className="text-neutral-400">Stealth eviction:</strong> For binding tests, content is embedded without 
              framing cues ("memory", "state", "persistent"). If the effect requires framing, it is instruction compliance, 
              not geometric binding.
            </p>
            <p>
              <strong className="text-neutral-400">Placebo controls:</strong> Fake summaries, shuffled tokens, and numeric-only 
              vectors test whether effects survive degraded channels.
            </p>
          </div>
        </section>
      </div>

      {/* Full Experiment Modal */}
      {selectedExperiment && (
        <div
          className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-6"
          onClick={() => setSelectedExperiment(null)}
        >
          <div
            className="bg-neutral-950 border border-neutral-800 max-w-4xl w-full max-h-[90vh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="sticky top-0 bg-neutral-950 border-b border-neutral-800 p-4 flex items-center justify-between">
              <div>
                <h2 className="text-lg font-mono text-neutral-300">{selectedExperiment.title}</h2>
                <p className="text-xs text-neutral-600 font-mono mt-1">{selectedExperiment.filename}</p>
              </div>
              <button
                onClick={() => setSelectedExperiment(null)}
                className="text-neutral-500 hover:text-neutral-300 text-xl"
              >
                ×
              </button>
            </div>
            <div className="p-6">
              <MarkdownRenderer content={selectedExperiment.content} />
            </div>
          </div>
        </div>
      )}
    </main>
  );
}
