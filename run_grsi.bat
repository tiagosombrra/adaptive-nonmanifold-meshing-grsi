@echo off
call scripts\build_windows.bat || exit /b 1
call scripts\run_eistute_windows.bat || exit /b 1
