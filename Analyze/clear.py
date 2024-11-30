import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

os.system("rmdir /Q /S .\\..\\Diagram")
os.system("rmdir /Q /S .\\..\\Output")
os.system("rmdir /Q /S .\\..\\Table")
