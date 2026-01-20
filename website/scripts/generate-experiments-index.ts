/**
 * Generate Experiments Index
 *
 * Scans /public/experiments/*.md files and generates a JSON index
 * with metadata extracted from each file's markdown table.
 *
 * Run: npx ts-node scripts/generate-experiments-index.ts
 * Or via npm: npm run generate-experiments
 */

import * as fs from 'fs';
import * as path from 'path';

interface ExperimentMeta {
  filename: string;
  title: string;
  date: string | null;
  experimentId: string | null;
  status: 'confirmed' | 'falsified' | 'planned' | 'pending';
  priority: string | null;
  frameworkVersion: string | null;
  testType: string | null;
}

interface ExperimentsIndex {
  generated: string;
  total: number;
  byStatus: {
    confirmed: number;
    falsified: number;
    planned: number;
    pending: number;
  };
  experiments: ExperimentMeta[];
}

function extractTitle(content: string): string {
  const match = content.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : 'Untitled';
}

function extractMetadataField(content: string, field: string): string | null {
  // Match markdown table rows like: | Date | 2026.01.18 |
  const regex = new RegExp(`\\|\\s*${field}\\s*\\|\\s*([^|]+)\\|`, 'i');
  const match = content.match(regex);
  if (match) {
    // Clean up the value - remove markdown formatting
    return match[1].trim().replace(/\*\*/g, '').replace(/`/g, '');
  }
  return null;
}

function normalizeStatus(status: string | null): ExperimentMeta['status'] {
  if (!status) return 'pending';

  const lower = status.toLowerCase();

  if (lower.includes('strongly confirmed') || lower.includes('confirmed')) {
    return 'confirmed';
  }
  if (lower.includes('falsified') || lower.includes('failed')) {
    return 'falsified';
  }
  if (lower.includes('planned')) {
    return 'planned';
  }
  return 'pending';
}

function parseExperiment(filepath: string): ExperimentMeta {
  const content = fs.readFileSync(filepath, 'utf-8');
  const filename = path.basename(filepath);

  const title = extractTitle(content);
  const date = extractMetadataField(content, 'Date');
  const experimentId = extractMetadataField(content, 'Experiment ID');
  const rawStatus = extractMetadataField(content, 'Status');
  const status = normalizeStatus(rawStatus);
  const priority = extractMetadataField(content, 'Priority');
  const frameworkVersion = extractMetadataField(content, 'Framework Version');
  const testType = extractMetadataField(content, 'Test Type');

  return {
    filename,
    title,
    date,
    experimentId,
    status,
    priority,
    frameworkVersion,
    testType,
  };
}

function generateIndex(): void {
  const experimentsDir = path.join(__dirname, '../public/experiments');
  const outputPath = path.join(__dirname, '../public/data/experiments-index.json');

  // Ensure output directory exists
  const outputDir = path.dirname(outputPath);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Get all markdown files
  const files = fs.readdirSync(experimentsDir)
    .filter(f => f.endsWith('.md'))
    .sort((a, b) => b.localeCompare(a)); // Sort by date descending (newest first)

  // Parse each file
  const experiments: ExperimentMeta[] = files.map(file =>
    parseExperiment(path.join(experimentsDir, file))
  );

  // Count by status
  const byStatus = {
    confirmed: experiments.filter(e => e.status === 'confirmed').length,
    falsified: experiments.filter(e => e.status === 'falsified').length,
    planned: experiments.filter(e => e.status === 'planned').length,
    pending: experiments.filter(e => e.status === 'pending').length,
  };

  const index: ExperimentsIndex = {
    generated: new Date().toISOString(),
    total: experiments.length,
    byStatus,
    experiments,
  };

  // Write the index
  fs.writeFileSync(outputPath, JSON.stringify(index, null, 2));

  console.log(`Generated experiments index:`);
  console.log(`  Total: ${index.total}`);
  console.log(`  Confirmed: ${byStatus.confirmed}`);
  console.log(`  Falsified: ${byStatus.falsified}`);
  console.log(`  Planned: ${byStatus.planned}`);
  console.log(`  Pending: ${byStatus.pending}`);
  console.log(`  Output: ${outputPath}`);
}

// Run the script
generateIndex();
