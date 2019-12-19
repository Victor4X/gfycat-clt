# Based on https://www.geeksforgeeks.org/get-post-requests-using-python/

# importing
import requests
import time

# defining the api-endpoint  
API_ENDPOINT = "https://api.gfycat.com/v1/gfycats"

# your API key here
# API_KEY = "XXXXXXXXXXXXXXXXX"

# your source code here
external_url = input("Please input the external URL you want to create a gif of: ")

# data to be sent to api
data = {'fetchUrl':external_url}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
print(r.text)
gfyname = r.text

# Wait for the gif to process
done = False
while done is False:
    time.sleep(5)
    r = requests.post(url = "https://api.gfycat.com/v1/gfycats/fetch/status/"+gfyname, data = {})
    print(r.text)
    if r.json['task'] == 'complete':
        done = True

print("Done!")