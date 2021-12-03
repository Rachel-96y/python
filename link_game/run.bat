@echo off
pyinstaller games.py --noconsole --hidden-import PySide2.QtXml --icon="yunian.ico" -F
pause > nul
