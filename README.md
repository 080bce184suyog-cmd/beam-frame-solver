# Beam & Frame Solver
A web-based tool for analyzing beams and frames, displaying shear force, bending moment, and deflection diagrams.

## Files
- `index.html`: Main web interface with tabs for beam and frame analysis.
- `beam.py`: Python script for beam analysis (shear, moment, deflection).
- `frame.py`: Python script for frame analysis using the stiffness method.
- `.gitignore`: Specifies files to ignore in Git.

## Usage
- Open `index.html` in a browser to use the web interface (requires internet for Tailwind CSS, Chart.js, Math.js CDNs).
- Run `beam.py` or `frame.py` with Python (requires `numpy` and `matplotlib`).
- Beam analysis supports simply supported beams with point, distributed, or moment loads.
- Frame analysis supports portal frames with fixed supports and horizontal loads.

## Deployment
Hosted at: https://080bce184suyog-cmd.github.io/beam-frame-solver-test