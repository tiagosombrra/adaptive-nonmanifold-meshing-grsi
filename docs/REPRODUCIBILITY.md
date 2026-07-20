# Reproducibility protocol

The package builds the project in Release mode and provides article configurations for Book, Eistute and Decor Shelf. All three representative runs use one process and one thread.

## Stage numbering

Saved meshes are indexed from stage 0. Consequently, an `ADAPTIVE_MAX_STEPS` value of 5 produces the five states 0, 1, 2, 3 and 4. The Eistute target reported in the accepted manuscript is stage 4; a stage 5 output is not part of that target sequence.

## Validation levels

### Eistute

Eistute has an archived numerical reference. The principal stage-4 target is:

- 7,184 triangles;
- normalized error 0.036712;
- total error reduction 96.3288%;
- 58.6303% of triangles with quality at least 0.60;
- recorded mean shared-curve compatibility error 0.0.

`python scripts/verify_reference.py` checks the archived OBJ and CSV against the JSON target. After execution, `scripts/verify_eistute.py` checks the configured final stage and triangle count.

### Book and Decor Shelf

The repository includes their input models and article configurations. Their current execution verifiers are structural: they require the configured final-stage OBJ to exist, prohibit stages beyond the configured limit and require at least one triangular face.

Authoritative numerical reference JSON/CSV/OBJ files for Book and Decor Shelf are not bundled in this patch because no unambiguous archived targets were established during the audit. They should be added only from verified experimental records.

## Commands

### Windows

```bat
run_grsi.bat
```

### Linux

```bash
./run_grsi.sh
```

Runtime depends on the compiler and hardware. Numerical claims should be based on archived or explicitly verified metrics rather than wall-clock time.
