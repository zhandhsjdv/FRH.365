@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================
echo   Time Capsule - Rebuild executable
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Install Python 3.8+ and check "Add Python to PATH".
    pause
    exit /b 1
)

python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing pyinstaller ...
    python -m pip install pyinstaller
)

echo Building, please wait ...
python -m PyInstaller --onefile --console --clean --name time-capsule --add-data "index.html;." --distpath dist --workpath build launcher.py

echo.
if exist "dist\time-capsule.exe" (
    echo [DONE] dist\time-capsule.exe generated.
) else (
    echo [FAILED] Build failed, see messages above.
)
pause
