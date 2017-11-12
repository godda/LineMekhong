from cx_Freeze import setup, Executable

setup( name = "HelloWorld",
     version = "0.1",
     description = "IT Geek cx_Freeze HelloWorld",
     executables = [Executable("vodkabot.py")])
