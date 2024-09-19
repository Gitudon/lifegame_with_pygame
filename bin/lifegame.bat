@echo off
set c1=%CD%
%~d0
cd %~d0%~p0
cd ../
pip install -r "./bin/requirements.txt"
python -u "./src/lifegame.py"
cd %c1%