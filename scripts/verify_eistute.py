#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(sys.argv[1] if len(sys.argv) > 1 else "results/eistute")
objs = sorted(root.glob("*passo_4_malha_4.obj"))
if not objs:
    raise SystemExit("Stage-4 mesh was not found")
triangles = sum(1 for line in objs[-1].open(errors="ignore") if line.startswith("f "))
expected = json.loads(Path("reference/eistute_stage4.json").read_text())
if triangles != expected["triangles"]:
    raise SystemExit(f"Triangle count mismatch: {triangles} != {expected['triangles']}")
print(f"Stage-4 triangle count verified: {triangles}")
print("Published reference metrics are available in reference/eistute_stage4.json")
