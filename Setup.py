import cx_Freeze
import os

executables = [cx_Freeze.Executable("Game.py")]



os.environ['TCL_LIBRARY'] = r"F:\Python 3.6\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"F:\Python 3.6\tcl\tk8.6"

cx_Freeze.setup(
    name = "Setup",
    options = { "build_exe": { "packages": ["pygame"], "include_files": ["download.jpg", "SnakeHead.png"] } },
    description = "Snake game project",
    executables = executables
    )
