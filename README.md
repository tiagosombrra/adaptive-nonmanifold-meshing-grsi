# Adaptive Meshing of Non-Manifold Parametric Patch Complexes

Replication package for the article **Adaptive Meshing of Non-Manifold Parametric Patch Complexes with Shared-Curve Compatibility**, accepted in *Computers & Graphics* through the SIBGRAPI 2026 Journal Track (manuscript CAG-D-26-00358R2).

The package contains the C++17 implementation, the Book, Eistute and Decor Shelf evaluation models, article and ablation configurations, and scripts for executing the three representative model runs.

![Representative Eistute result](assets/grsi_representative.png)

## GRSI representative result

The GRSI reproduction target is **Figure 7**, Section 4.3, “Eistute model”. The figure presents five saved mesh states numbered 0, 1, 2, 3 and 4. In the configuration files, `ADAPTIVE_MAX_STEPS` denotes the highest saved stage index; therefore, the Eistute value `4` produces states 0–4.

The representative target is the saved **stage-4 candidate mesh** used in Figure 7. The implementation saves rejected candidates for analysis; in the tested workflow, the transition to stage 4 is rejected by the hybrid acceptance criterion but the stage-4 OBJ is intentionally retained and verified against the archived paper target.

| Metric | Archived value |
|---|---:|
| Triangles | 7,184 |
| Normalized error | 0.036712 |
| Error reduction | 96.3288% |
| Triangles with quality q >= 0.60 | 58.6303% |
| Recorded mean shared-curve compatibility error | 0.0 |

The reproduction scripts run without parameters, compile the implementation, execute the Eistute configuration and verify the generated stage-4 OBJ against the archived triangle-count target.

## Supported platform for GRSI review

The primary supported review platform is:

- Windows 10 or Windows 11, 64-bit;
- MSYS2 UCRT64 toolchain;
- CMake;
- GCC/MinGW-w64 with C++17 support;
- Python 3.

Eigen headers required by the implementation are bundled under `libs/Eigen/`. On MinGW, the build links the compiler runtime statically to avoid accidental loading of incompatible `libgcc` or `libstdc++` DLLs from another toolchain in `PATH`.

For a clean Windows installation, follow [`INSTALL_WINDOWS.txt`](INSTALL_WINDOWS.txt).

## Quick reproduction — Figure 7

### Windows

Open PowerShell in the repository root and run:

```powershell
.\reproduce_eistute_windows.bat
```

From MSYS2 UCRT64 or Git Bash, use:

```bash
cmd.exe //c reproduce_eistute_windows.bat
```

### Linux

Linux execution is provided as an additional convenience but is not the primary GRSI review platform:

```bash
./reproduce_eistute_linux.sh
```

Expected final output:

```text
Eistute final stage verified: 4
Triangles: 7184
Published Eistute target triangle count verified.
Representative Eistute result reproduced successfully.
```

Generated data are written under:

```text
results/eistute/
```

The representative triangular mesh is an OBJ file whose name ends with:

```text
passo_4_malha_4.obj
```

The OBJ is the standard text-format mesh data selected for the representative paper figure.

## Verify the archived reference

This validation does not execute the meshing algorithm. It verifies the archived OBJ and CSV against the JSON target:

```powershell
python scripts\verify_reference.py
```

## Run all three models

### Windows

```powershell
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

Book and Decor Shelf currently have structural execution checks. The archived exact numerical target used for GRSI validation is the Eistute stage-4 result.

## Run one model

Windows:

```powershell
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

## Numerical diagnostics

The run log reports `FindUV` calls that reach the configured iteration limit. This counter is retained as a numerical diagnostic and is not used by the GRSI triangle-count verifier.

The implementation also prints legacy internal timing fields. These fields are not used as reproducibility targets. Use an external wall-clock measurement when execution time must be reported.

## Article publication status

The article is fully accepted and is currently in the publisher's production
process. No manuscript or publisher-formatted PDF is distributed in this
repository. The DOI or public article-page link should be added to the GRSI
metadata when it becomes available.

## GRSI submission files

- `GRSI_SUBMISSION.txt`: paper, authors, supported OS and representative result;
- `GRSI_LIABILITY.txt`: authorization for review and public advertisement after approval;
- `INSTALL_WINDOWS.txt`: clean-machine installation and compilation instructions;
- `DATA_PROVENANCE.md`: input-model provenance and redistribution declaration;
- `GRSI_FORM_VALUES.txt`: values prepared for the online submission form;
- `docs/GRSI_REVIEW_GUIDE.md`: reviewer-oriented workflow;
- `assets/grsi_representative.png`: 250 × 250 representative image;
- `paper/README.md`: publication-status note; no manuscript PDF is bundled while the article is in production.

## Environment report

After installing the dependencies and completing the final representative run, generate the tested-environment record:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\collect_environment_windows.ps1
```

This creates `TESTED_ENVIRONMENT.txt`.

## Package validation

Run:

```powershell
python .\scripts\validate_grsi_package.py
```

Before the final commit, regenerate and validate `MANIFEST.sha256` using the scripts under `scripts/`.

## Repository structure

- `src/`, `include/`: scientific implementation;
- `libs/Eigen/`: bundled Eigen headers retained from the experimental snapshot;
- `input_models/`: article evaluation models;
- `configs/`: article and ablation configurations;
- `reference/`: archived Eistute reference data;
- `scripts/`: build, execution and verification scripts;
- `assets/`: representative submission image;
- `paper/`: publication-status information;
- `docs/`: provenance and reproducibility notes.

## License

The source code is distributed under the MIT License. Third-party notices are documented in `THIRD_PARTY_LICENSES.md`. Input-model provenance and redistribution terms are documented in `DATA_PROVENANCE.md`.

## Provenance

The scientific source code, models and configurations were derived exclusively from the archived experimental snapshot identified in `SOURCE_SNAPSHOT.txt`. Later development branches were not incorporated.
