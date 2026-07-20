@echo off
setlocal
cmake -S . -B build -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DAP_MESH_USE_MPI=OFF -DAP_MESH_USE_OPENMP=OFF -DAP_MESH_ENABLE_LTO=OFF || exit /b 1
cmake --build build --parallel || exit /b 1
