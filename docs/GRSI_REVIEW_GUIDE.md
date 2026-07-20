# GRSI reviewer guide

## Scope

The representative result selected for the Graphics Replicability Stamp
Initiative review is **Figure 7**, Section 4.3, “Eistute model”.

The paper figure presents five saved states numbered 0–4. The GRSI script
reproduces these data and verifies the final stage-4 triangular mesh.

## Primary review platform

- Windows 10/11, 64-bit;
- MSYS2 UCRT64;
- GCC/MinGW-w64;
- CMake;
- Python 3.

Complete clean-machine instructions are in `INSTALL_WINDOWS.txt`.

## One-command reproduction

From the repository root:

```powershell
.\reproduce_eistute_windows.bat
```

When using the MSYS2 UCRT64 terminal:

```bash
cmd.exe /c reproduce_eistute_windows.bat
```

No parameters are required.

## Expected outputs

The run creates:

```text
results/eistute/
```

The representative mesh name ends with:

```text
passo_4_malha_4.obj
```

The OBJ is a standard text triangular mesh. The verifier requires:

- configured final stage: 4;
- no stage greater than 4;
- final mesh contains triangular faces;
- final triangle count: 7,184.

The run log is written to:

```text
results/eistute/run.log
```

## Archived evidence

The repository includes:

- `reference/eistute_stage4.obj`;
- `reference/eistute_metrics.csv`;
- `reference/eistute_stage4.json`.

Run:

```powershell
python scripts\verify_reference.py
```

to check consistency among the archived files.

## Additional models

Book and Decor Shelf execution scripts are included, but they are not required
for the representative GRSI review. Their current verifiers check output
structure rather than archived numerical targets.

## Integrity

Before submission, the authors regenerate `MANIFEST.sha256`. Reviewers may
validate it with `sha256sum -c MANIFEST.sha256` in Git Bash or MSYS2.
