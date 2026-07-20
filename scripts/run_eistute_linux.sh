#!/usr/bin/env bash
set -euo pipefail
mkdir -p results/eistute
./build/bin/ap_mesh --config configs/eistute/article.conf | tee results/eistute/run.log
python3 scripts/verify_eistute.py results/eistute
