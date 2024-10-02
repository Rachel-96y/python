::打包文件
@echo off
pyinstaller -F _boot.pyw --noconsole --hidden-import PySide2.QtXml
pause > nul