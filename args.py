import sys
import psutil

print("This process command line: ", psutil.Process().cmdline())
print("List of all processes:")

for proc in psutil.process_iter(attrs=['pid','ppid','cmdline']):
    print(proc.info)
