# Adaptive Meshing of Non-Manifold Parametric Patch Complexes

Replication package for the article **“Adaptive Meshing of Non-Manifold Parametric Patch Complexes with Shared-Curve Compatibility”**, accepted in *Computers & Graphics* as part of the SIBGRAPI 2026 Journal Track (manuscript CAG-D-26-00358R2).

The package contains the C++17 implementation, the three evaluation models, the experimental configurations, archived reference results, and scripts for reproducing the representative Eistute result.

## Representative result

The default reproduction targets Eistute at stage 4:

| Metric | Reference value |
|---|---:|
| Triangles | 7,184 |
| Normalized error | 0.036712 |
| Error reduction | 96.3288% |
| Triangles with quality q >= 0.60 | 58.6303% |
| Mean shared-curve compatibility error | 0 |

## Supported environment

The reference environment is Windows 11 (64-bit), CMake with the MinGW Makefiles generator, a MinGW-w64 compiler supporting C++17, and Python 3. The experiment is sequential (`NUM_PROCESSES=1`, `NUM_THREADS=1`).

The source also compiles on Linux with GCC and CMake. Linux support is provided as a convenience; the Windows configuration is the reference configuration associated with the article.

## Reproduce on Windows

Install CMake, Python 3, and a MinGW-w64 toolchain, ensure `cmake`, `python`, and `g++` are available in `PATH`, and run from a Command Prompt:

```bat
run_grsi.bat
```

The command builds the Release executable, runs Eistute without parameters, writes outputs under `results/figure_08_eistute/`, and validates the stage-4 metrics against the archived values.

## Reproduce on Linux

```bash
./run_grsi.sh
```

For a short compilation and execution check:

```bash
./scripts/build_linux.sh
./scripts/run_smoke_linux.sh
```

## Repository organization

- `src/`, `include/`: scientific implementation.
- `libs/Eigen/`: Eigen 3.4.0 headers included in the archived snapshot.
- `input_models/`: Book, Eistute, and Decor Shelf patch complexes.
- `configs/`: article and ablation configurations.
- `reference/`: archived metrics, compatibility summaries, and representative mesh.
- `paper/`: representative image and result mapping.
- `scripts/`: build, execution, and verification utilities.
- `docs/`: installation, provenance, and reproducibility notes.

## Scope

The scientific implementation and data originate from the archived experimental snapshot recorded in `SOURCE_SNAPSHOT.txt`. Later development branches are not part of this package. Packaging additions are listed in `docs/CHANGES_FROM_ORIGINAL_SNAPSHOT.md`.

## Citation

Citation metadata are provided in `CITATION.cff`. The journal DOI should be added after publication metadata become available.
