echo off
MODE 75,50
Set I_Dir=includes
Set C_Dir=src
Set O_Dir=bin

echo "Running simulator.."
g++ %C_Dir%/simulate.cpp %C_Dir%/localizer.cpp %C_Dir%/debugging_helpers.cpp %C_Dir%/helpers.cpp -I %I_Dir% -o %O_Dir%/simulator.exe
if %ERRORLEVEL% NEQ 0 (
    pause
    exit
) else (
    cd %O_Dir%
    simulator.exe
    cd /D  %~dp0
)

echo "Running tests.."
g++ %C_Dir%/tests.cpp %C_Dir%/localizer.cpp %C_Dir%/debugging_helpers.cpp %C_Dir%/helpers.cpp -I %I_Dir% -o %O_Dir%/tests.exe
if %ERRORLEVEL% NEQ 0 (
    pause
    exit
) else (
    cd %O_Dir%
    tests.exe
    pause
)

