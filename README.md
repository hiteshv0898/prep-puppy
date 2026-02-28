# prep-puppy

Learning-first interview prep CLI for data/AI engineering roles.

## Goals
- Teach fundamentals from basics to FAANG-level depth.
- Offer lessons, drills, and mock interview simulations.
- Support Data Engineer, AI Engineer, and Data Scientist tracks.
- Domains: SQL, system design, distributed systems, MLOps, LLM engineering,
  stats/probability, math for ML, Python basics, data viz, behavioral.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m preppuppy.cli.app --track data-engineer --mode learn --domain sql --level basic
```

## Modes
- **learn**: guided lessons + hints
- **drill**: practice questions + feedback
- **mock**: timed interview simulation

## Notes
This is an early scaffold. Content + engines will evolve fast.
