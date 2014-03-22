@echo off

echo Py to EXE using Pyinstaller!!
echo.
REM set /p fileName="Enter Script Name[default:1st .py file in directory]:"
REM echo %fileName%
for /r %%i in (..\*.py) do ..\..\..\PyInstaller-2.1\pyinstaller.py --onefile ..\%%~nxi
echo done!
echo Removing build directory...
rmdir /S /Q build
echo done!
REM c:\Apps\PyInstaller-2.1\pyinstaller.py --onefile %fileName%
pause