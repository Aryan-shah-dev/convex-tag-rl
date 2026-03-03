# Convex Tag RL

Convex Tag RL is a deterministic 2D continuous-control arena built to study emergent strategy in adversarial reinforcement learning systems.

The environment combines momentum-based movement, a shrinking convex storm boundary, and timing-based tagging mechanics to create a structured self-play problem.

This is not meant to be a casual game.  
It is a controlled playground for experimenting with:

- Continuous-control policies
- Multi-agent self-play
- Emergent spatial strategies
- Stability in adversarial RL training

The simulation is built from scratch with a clear separation between:
- Physics
- Game mechanics
- Rendering
- Learning logic

The objective is simple:
Create a minimal but deep environment where strategy emerges from constraints — not scripted rules.

If agents learn something surprising here, the system has done its job.

## Requirements

- Python 3.10+
- Tkinter (included with standard Python installations)
- PyTorch

## License

MIT — free to use, modify, and build upon.