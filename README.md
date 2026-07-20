# Adaptive Meshing of Non-Manifold Parametric Patch Complexes

Replication package for the article **Adaptive Meshing of Non-Manifold Parametric Patch Complexes with Shared-Curve Compatibility**, accepted in *Computers & Graphics* through the SIBGRAPI 2026 Journal Track (manuscript CAG-D-26-00358R2).

The package contains the C++17 implementation, the Book, Eistute and Decor Shelf evaluation models, the article configurations, ablation configurations, and scripts for reproducing the representative Eistute experiment.

## Representative result

The default reproduction targets Eistute at stage 4.

| Metric | Published value |
|---|---:|
| Triangles | 7,184 |
| Normalized error | 0.0367 |
| Error reduction | 96% |
| Triangles with quality q >= 0.60 | 59% |
| Mean shared-curve compatibility error | 0 |

## Requirements

- CMake 3.15 or newer
- C++17 compiler
- Python 3

The reference experiment is sequential (`NUM_PROCESSES=1`, `NUM_THREADS=1`).

## Linux

```bash
./run_grsi.sh
```

## Windows

From a Developer Command Prompt or a terminal with CMake and MinGW-w64 available:

```bat
run_grsi.bat
```

Results are written under `results/eistute/`.

## Repository structure

- `src/`, `include/`: scientific implementation.
- `libs/Eigen/`: Eigen headers retained from the experimental snapshot.
- `input_models/`: evaluation models used in the article.
- `configs/`: article and ablation configurations.
- `reference/`: published target values.
- `scripts/`: build, execution and verification scripts.
- `docs/`: provenance and reproducibility notes.

## Provenance

The scientific source code, models and configurations were derived exclusively from the archived experimental snapshot identified in `SOURCE_SNAPSHOT.txt`. Later development branches were not incorporated.
