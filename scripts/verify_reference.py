#!/usr/bin/env python3
from pathlib import Path
import json
expected = json.loads(Path('reference/eistute_stage4.json').read_text())
mesh = Path('reference/eistute_stage4.obj')
triangles = sum(1 for line in mesh.open(errors='ignore') if line.startswith('f '))
if triangles != expected['triangles']:
    raise SystemExit(f"Archived reference mismatch: {triangles} != {expected['triangles']}")
quality = Path('reference/eistute_stage4_quality.log').read_text(errors='ignore')
for token in ('elements_total=7184', 'error_normalized=0.036712', 'error_total_reduction_pct=96.3288'):
    if token not in quality:
        raise SystemExit(f'Missing archived metric: {token}')
print('Archived Eistute reference verified.')
