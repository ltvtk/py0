# py0 : python zero
Simple python-like scripting language for kids 
# description
This is very simple scripting language which compile to python from file *.py0 to *.py and run them
# installation on windows only, open your powershell as Admin
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

iex "& {$(irm get.scoop.sh)} -RunAsAdmin"

scoop install python

pip install git+https://github.com/ltvtk/py0.git
# usage
py0 <filename.py0>
# use togther with our Vditor
https://github.com/ltvtk/py0/releases/download/1.0/vditor.Setup.1.0.0.exe
