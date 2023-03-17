import math

print(dir(math))

from module.func import plus as add

print(add(2, 3))


import sys
sys.path.append('C:\\Users\\saims\\OneDrive\\Desktop\\_Python_\\module_path')
import fun
print(fun.multi(1, 2))