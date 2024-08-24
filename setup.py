import sys
from cx_Freeze import setup, Executable

sys.setrecursionlimit(10000)  # Set an appropriate limit according to your needs

build_exe_options = {"packages": ["os","pickle","customtkinter",'numpy','sklearn','ttkthemes','tkinter'],"include_files":["images/","model.pkl"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="WATER PREDICTOR",
    version="1.0",
    description="Water portability Checker",
    options={"build_exe": build_exe_options},
    author="Eli Usheunepa Yunana",
    executables=[Executable("app.py", base=base,icon='images/logo_w.ico')],
)





