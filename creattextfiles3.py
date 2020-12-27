# import the os module
import os
from pathlib import Path
import csv

path = r'C:\Users\sd\Desktop\titletest\celebs'

x = 'Megan Fox'
with open(path + "\\" + x + "\\"  + x + ".txt", 'w') as f:
    print(f)

print(path)