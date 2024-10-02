@echo off
pyinstaller -D _main.py --hidden-import PySide2.QtXml
pause > nul

