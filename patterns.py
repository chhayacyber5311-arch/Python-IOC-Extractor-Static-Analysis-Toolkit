# using pattern of IP addresses to extract ips in file
# pattern is : \b(?:\d{1,3}\.){3}\d{1,3}\b
# \b : making boundries
# ?:\d{1,3} : find 1 to 3 digits
# \. : dot
# {3} : do this 3 times
# \d{1,3} : last number of ip

IP_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

#  Adding URL pattern
URL_PATTERN = r"https?://[^\s]+"

# Adding domain pattern
DOMAIN_PATTERN = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"

# Adding Email pattern
EMAIL_PATTERN = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
