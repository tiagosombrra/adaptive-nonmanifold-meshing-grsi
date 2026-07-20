# Adaptive Meshing of Non-Manifold Parametric Patch Complexes

Replication package for the article **Adaptive Meshing of Non-Manifold Parametric Patch Complexes with Shared-Curve Compatibility**, accepted in *Computers & Graphics* through the SIBGRAPI 2026 Journal Track (manuscript CAG-D-26-00358R2).

The package contains the C++17 implementation, the Book, Eistute and Decor Shelf evaluation models, article and ablation configurations, and scripts for executing the three representative model runs.

## Eistute reference result

| Metric | Archived value |
|---|---:|
| Triangles | 7,184 |
| Normalized error | 0.036712 |
| Error reduction | 96.3288% |
| Triangles with quality q >= 0.60 | 58.6303% |
| Recorded mean shared-curve compatibility error | 0.0 |

## Requirements

- CMake 3.15 or newer;
- C++17 compiler;
- Python 3.

The provided representative configurations use `NUM_PROCESSES=1` and `NUM_THREADS=1`.

## Run all three models

### Windows

From PowerShell, Command Prompt or a terminal with CMake and MinGW-w64 available:

```bat
.\run_grsi.bat
```

### Linux

```bash
./run_grsi.sh
```

Results are written under:

- `results/book/`;
- `results/eistute/`;
- `results/decor_shelf/`.

## Run one model

Windows:

```bat
.\scripts\run_book_windows.bat
.\scripts\run_eistute_windows.bat
.\scripts\run_decor_shelf_windows.bat
```

Linux:

```bash
./scripts/run_book_linux.sh
./scripts/run_eistute_linux.sh
./scripts/run_decor_shelf_linux.sh
```

## Verification scope

Eistute includes an archived mesh and exact metrics. Book and Decor Shelf currently have structural execution checks only; authoritative numerical targets must not be inferred from a new run.

Verify the archived Eistute reference with:

```bash
python3 scripts/verify_reference.py
```

## Repository structure

- `src/`, `include/`: scientific implementation;
- `libs/Eigen/`: Eigen headers retained from the experimental snapshot;
- `input_models/`: article evaluation models;
- `configs/`: article and ablation configurations;
- `reference/`: archived reference data;
- `scripts/`: build, execution and verification scripts;
- `docs/`: provenance and reproducibility notes.

## Provenance

The scientific source code, models and configurations were derived exclusively from the archived experimental snapshot identified in `SOURCE_SNAPSHOT.txt`. Later development branches were not incorporated.
