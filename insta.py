#!/usr/bin/env python
# python libs: pip install instaloader os ; os requirements: xzcat w3m browser
import instaloader
import os
input=input("input profile:\n")
print(instaloader.Instaloader().download_profile(str(input),profile_pic_only=True))
os.system("xzcat "+input+"/"+input+"*.json.xz | sed -z -e 's.,.\\n.g' | sed -e 's.\". .g'  ; xdg-open \"fb.com/$(xzcat "+input+"/"+input+"*.json.xz | awk  -F 'fbid' '{print $2}' | awk -F ',' '{print $1}' | sed 's/,\|\"\|://g')\" ; w3m "+input+"/*.jpg")
