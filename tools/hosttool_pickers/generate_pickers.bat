@echo off
rem Edit these two paths, then double-click this file.
set "MOD=C:\path\to\your\SPT mod folder"
set "GAME=C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"

python "%~dp0generate_pickers.py" --mod "%MOD%" --game "%GAME%"
pause
