# Jai Ganesh

import argparse
from pathlib import Path

from extractor import extract_iocs

# Creating parse objects
parser = argparse.ArgumentParser(
    description="IOC Extractor Static Analysis Toolkit"
)

#  Creating object to take target argument from user
parser.add_argument(
    'target',
     help="Filepath to analyze"
)

#  Taking input for output file saving option for user
parser.add_argument(
    '-o','--output',
    help="Output file to save extracted IOCs (optional)",
    default=None
)

# Converting inputs into usable Python variables
args = parser.parse_args()

# Checking given filepath by user, is correct or not
target_path = Path(args.target)

if not target_path.exists():
    print(f"[!] Error: Target file does not exist in this path ->{target_path}")
    exit (1)

if not target_path.is_file():
    print(f"[!] Error: Target is not file->{target_path}")
    exit (0)

# Read target file
try:
    content = target_path.read_text(errors="ignore")
except Exception as e:
    print(f"[!] Error: Could not read file -> {e}")
    exit (1)

print("[+] File loaded successfully.")

# Print Result
result = extract_iocs(content)
print(result)