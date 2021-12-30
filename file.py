import re

userID = []
open("Teamcenter_*", "r") as f:
    for line in f:
        userID += re.findall("\+44\d{10}", line)
         
