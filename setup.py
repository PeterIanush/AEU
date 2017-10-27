from cx_Freeze import setup, Executable

target = Executable(
    script="WareHouseAEU.py",
    base="Win32GUI",
    )

setup(
    name="WHT",
    version="1.0",
    description="for warehouse",
    author="Peter&Yevhen",
    executables=[target]
    )