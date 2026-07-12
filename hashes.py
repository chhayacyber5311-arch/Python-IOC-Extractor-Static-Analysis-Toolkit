import re
from patterns import MD5_PATTERN, SHA1_PATTERN, SHA256_PATTERNS

def extract_hashes(content):
    md5_hash = list(dict.fromkeys(re.findall(MD5_PATTERN, content)))
    sha1_hash = list(dict.fromkeys(re.findall(SHA1_PATTERN, content)))
    sha256_hash = list(dict.fromkeys(re.findall(SHA256_PATTERNS, content)))

    return{

        "MD5": md5_hash,
        "SHA1": sha1_hash,
        "SHA256": sha256_hash
    }