import os
import requests

paths = ["./files/demos", "./files/scraped_essentials"]


for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"Folder {paths} already exists.")
        pass
