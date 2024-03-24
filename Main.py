import sys
import os
import subprocess

# Task 1
Executing os.getlogin()
Executing os.get_exec_path()

user = os.getlogin()
execPath = os.get_exec_path()

print (user)
print (execPath)
#
# End Task 1

# Task 2
# Execute sys.path
# Execute sys.byteorder

##path = sys.path
##byteOrder = sys.byteorder

##print (path)
##print (byteOrder)

# End Task 2

# Task 3
# Executing os.listdir on the C:\ drive
##dirPath = "C:\\"
##dir_list = os.listdir(dirPath)

##path = ("C:\\tempPython")

# Using os.mkdir to make a new directory on the C:\ drive names tempPython
##os.mkdir (path)

##print (dir_list)

# End Task 3

# Task 4
# Using subprocess.Popen to execute the Windows dir command and have its output placed in a text file named pythonOut.txt
##subprocess.Popen('C:\\Windows\\System32\\cmd.exe "/c dir C:\\>>C:\\tempPython\\pythonOut.txt"')

# End Task 4

# Task 5
# Using subprocess.Popen to open Windows calc.exe utility
##subprocess.Popen('calc.exe')

# End Task 5