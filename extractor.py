#  Impporting re for regex patterns, means reading text and find the given pattern in file
import re

# Importing IP_PATTERN from patterns.py
from patterns import IP_PATTERN

# Importing from utils.py, is_valid_ipv4
from utils import is_valid_ipv4

# ips = re.findall -> to find givem pattern in IP_PATTERN the format in target text file 
# set -> remove duplicate ips in file but can change order
# dict.fromkeys -> will remove duplicate but keep first seen order
# list -> again list all ips found in file

def extract_iocs(content):
    print("[+] Extractor received file content.")
    raw_ips = re.findall(IP_PATTERN, content)
    inorder_ips = list(dict.fromkeys(raw_ips))
    ips = [ip for ip in inorder_ips if is_valid_ipv4(ip)]


    return{
        "IPs": ips
    }
