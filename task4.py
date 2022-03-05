#Running on windows OS
import os
import platform
pid = os.getpid()
user = os.getlogin()
os_name = os.getenv("OS")
os_release = platform.win32_edition()

print("This script has the following PID:" + str(pid) + ". It was ran by " + user + " to work happily on " + os_name + "-" + os_release + ".")