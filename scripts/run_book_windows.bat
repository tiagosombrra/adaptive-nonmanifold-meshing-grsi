@echo off
setlocal
cd /d "%~dp0.."

if exist results\book rmdir /s /q results\book
mkdir results\book || exit /b 1

build\bin\ap_mesh.exe --config configs\book\article.conf > results\book\run.log 2>&1
if errorlevel 1 (
  type results\book\run.log
  exit /b 1
)

type results\book\run.log
python scripts\verify_book.py results\book || exit /b 1
