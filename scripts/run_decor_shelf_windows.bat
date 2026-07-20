@echo off
setlocal
cd /d "%~dp0.."

if exist results\decor_shelf rmdir /s /q results\decor_shelf
mkdir results\decor_shelf || exit /b 1

build\bin\ap_mesh.exe --config configs\decor_shelf\article.conf > results\decor_shelf\run.log 2>&1
if errorlevel 1 (
  type results\decor_shelf\run.log
  exit /b 1
)

type results\decor_shelf\run.log
python scripts\verify_decor_shelf.py results\decor_shelf || exit /b 1
