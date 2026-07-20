@echo off
setlocal
cd /d "%~dp0.."

if exist results\eistute rmdir /s /q results\eistute
mkdir results\eistute || exit /b 1

build\bin\ap_mesh.exe --config configs\eistute\article.conf > results\eistute\run.log 2>&1
if errorlevel 1 (
  type results\eistute\run.log
  exit /b 1
)

type results\eistute\run.log
python scripts\verify_eistute.py results\eistute || exit /b 1
