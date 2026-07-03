#  Impporting re for regex patterns, means reading text and find the given pattern in file
import re

# Impoeting IP_PATTERN from patterns.py
from patterns import IP_PATTERN

# ips = re.findall -> to find givem pattern in IP_PATTERN the format in target text file 
# set -> remove duplicate ips in file but can change order
# dict.fromkeys -> will remove duplicate but keep first seen order
# list -> again list all ips found in file

def extract_iocs(content):
    print("[+] Extractor received file content.")
    ips = list(dict.fromkeys(re.findall(IP_PATTERN, content)))

    return{
        "IPs": ips
    }
