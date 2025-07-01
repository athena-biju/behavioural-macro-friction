# The Hidden Friction: ψ as a Behavioural Macroeconomic Distortion

This repository introduces `ψ`, a norm-induced wage suppression parameter representing post-marital labor market frictions unrelated to fertility. We embed ψ into a dynamic Overlapping Generations (OLG) macroeconomic model to simulate growth, welfare, and fiscal implications.
 
 ## Core Contributions
 - Definition and empirical estimation of ψ across countries.
 - Structural integration of ψ into general equilibrium simulations.
 - Simulation of GDP losses, labor force participation shifts, and fiscal drag.
 - Foundational framing of "behavioural macrofrictions".
 
 ## Repository Structure
 - `/code/`: Jupyter notebooks for empirical and simulation logic.
 - `/data/`: Placeholder for PHF, SHP, SOEP, WVS, etc. (access instructions only).
 - `/docs/`: Theoretical notes on embedding ψ into macroeconomic systems.
 
## Setup

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda.
2. Create and activate the environment with the `jupyterlab` package:

   ```bash
   conda create -n macrofriction python=3.11 jupyterlab
   conda activate macrofriction
   ```
3. Verify the environment and JupyterLab installation:

   ```bash
   conda env list | grep macrofriction
   jupyter lab --version
   ```

## Running the Notebooks

Launch JupyterLab:

```bash
jupyter lab
```

Run the notebooks sequentially:

- `01-macro-model-structure.ipynb` – establishes the baseline model structure.
- `02-psi-output-loss-simulation.ipynb` – simulates output losses from ψ.
- `03-psi-dynamic-path.ipynb` – traces the dynamic adjustment path.
- `04-lfp-welfare-simulation.ipynb` – evaluates labor force and welfare shifts.
- `05-policy-simulation-scenarios.ipynb` – explores policy scenarios.

 ## Citation
 Athena Biju (2025). *The Hidden Friction: Marriage, Gender Norms, and the Macroeconomics of Labor Market Divergence.* Jacobs University Bremen.
 
 ## License
 MIT License (for code), CC-BY 4.0 (for paper).
 
 ## Disclosure
 AI-assisted for select technical implementations. All theoretical and conceptual content by Athena Biju.
