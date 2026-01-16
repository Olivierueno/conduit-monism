# Build Instructions

## Experiment Index Generation

The validation page requires an experiment index JSON file at `public/data/experiments_index.json`.

### Before Deployment

Run the experiment parser from the project root:

```bash
cd ..  # Go to project root (from website folder)
python3 scripts/parse_experiments.py
```

This will:
1. Parse all markdown files in `experiments/`
2. Extract individual tests from multi-test files
3. Classify experiments by status (confirmed, falsified, planned, pending)
4. Generate `website/public/data/experiments_index.json`

### For Vercel Deployment

The `experiments_index.json` file should be committed to git so it's available during build. If the file is missing, the validation page will show an error.

**Note:** Vercel builds only have access to the `website/` folder, so the parser must be run locally before committing, or the JSON file must be manually updated.

### Updating the Index

Whenever new experiments are added or existing ones are modified:

1. Run `python3 scripts/parse_experiments.py` from the project root
2. Commit the updated `website/public/data/experiments_index.json`
3. Push to trigger a new Vercel deployment
