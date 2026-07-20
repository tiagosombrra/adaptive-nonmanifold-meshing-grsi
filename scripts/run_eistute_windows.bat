@echo off
setlocal
if not exist results\eistute mkdir results\eistute
build\bin\ap_mesh.exe --config configs\eistute\article.conf > results\eistute\run.log 2>&1 || exit /b 1
python scripts\verify_eistute.py results\eistute || exit /b 1
type results\eistute\run.log
