@echo off
set c1=%CD%
%~d0
cd %~d0%~p0
cd ../
pip install -r "./etc/requirements.txt"
python -u "./src/lifegame.py"
cd %c1%