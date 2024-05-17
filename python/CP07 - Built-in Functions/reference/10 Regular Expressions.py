# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# to use regular expressions, you have to import re. its part of the python standard library, so you already have it installed.
import re

# Define the regular expression pattern for an IP address
# r gets rid of the normal escape characters.
# \b is a switch between word characters and other characters
# \d{1,3} a number that has at least 1 character and at most 3
# \. just a dot (period)
ipPattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# Read the log file and extract all IP addresses
logFile = '''  [INFO] - 2023-09-26 13:45:12 - User connected from 192.168.1.2 for 5th time on current date
                    [ERROR] - 2023-09-26 13:46:14 - Connection timeout for 10.0.0.5 connection was lost
                    [INFO] - 2023-09-26 13:47:05 - User connected from 172.16.0.3 for 1st time on current date '''
    
# Find all IP addresses in the log_contents
ipAddresses = re.findall(ipPattern, logFile)

# Print the extracted IP addresses
for ip in ipAddresses:
    print(ip)
