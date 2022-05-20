import json
import requests
import numpy as np
with open('t1.json','r') as f:
    json_data = json.load(f)

#print(json.dumps(json_data, indent="\t") )
#print(len(json_data["predictions"]))
#print(json_data["predictions"])
for i in range(0,len(json_data["predictions"])) :
	print(json_data["predictions"][i]['class'])


"""
import io
import cv2
import requests
import numpy as np
import json
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder

#print(json.dumps(json_data, indent="\t") )

# !! print(len(json_data['posts']))

#print(json_data['posts'][0]['img_url'])

"""
with open('2022-05-10_패션.json','w', encoding='utf-8') as f:
    json.dumps(json_data,f, indent="\t")
"""
with open('2022-05-10_봄코디.json','r') as f:
    json_data = json.load(f)
"""
json_data['posts'][0]['conf'] = []

json_data['posts'][0]['conf'].append('leggings')
json_data['posts'][0]['conf'].append('slacks')

print(json_data['posts'][0]['conf'])
"""
for i in range (0,len(json_data['posts'])) :
    json_data['posts'][i]['conf'] = []
    url = json_data['posts'][i]['img_url']
    print(url)
    image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
    image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    #img = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilImage = Image.fromarray(image)

    # Convert to JPEG Buffer
    buffered = io.BytesIO()
    pilImage.save(buffered, quality=100, format="JPEG")

    # Build multipart form and post request
    m = MultipartEncoder(fields={'file': ("imageToUpload", buffered.getvalue(), "image/jpeg")})

    response = requests.post("https://detect.roboflow.com/images-isntv/1?api_key=8w6mM64M6BYFzHSnU57W", data=m, headers={'Content-Type': m.content_type})

    with open('t' + str(i)+ '.json','wb') as outf:
        outf.write(response.content)
    with open('t' + str(i)+ '.json','r') as f:
        json_data2 = json.load(f)
    print(json_data2["predictions"])
    for j in range(0,len(json_data2["predictions"])) :
        json_data['posts'][i]['conf'].append((json_data2["predictions"][j]['class']))
    str1 = json_data['posts'][i]['insta_id']
    print(str1 + " ",json_data['posts'][i]['conf'])

"""
# Load Image with PIL
url = "https://scontent-gmp1-1.cdninstagram.com/v/t51.2885-15/280227601_758593168882451_7347051574752086066_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=111&_nc_ohc=To_E6eswdcMAX_-GMBM&edm=ALQROFkBAAAA&ccb=7-4&ig_cache_key=MjgzMzk4NDU1MjMwNzc1ODQ2NQ%3D%3D.2-ccb7-4&oh=00_AT8nQhRDkoesG8xs5XrvOq3gMUHd4TJenDz6iV5jxmwQag&oe=627FC5F7&_nc_sid=30a2ef"

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
#img = cv2.imread(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pilImage = Image.fromarray(image)

# Convert to JPEG Buffer
buffered = io.BytesIO()
pilImage.save(buffered, quality=100, format="JPEG")

# Build multipart form and post request
m = MultipartEncoder(fields={'file': ("imageToUpload", buffered.getvalue(), "image/jpeg")})

response = requests.post("https://detect.roboflow.com/images-isntv/1?api_key=8w6mM64M6BYFzHSnU57W", data=m, headers={'Content-Type': m.content_type})

with open('t1.json','wb') as outf:
    outf.write(response.content)
"""    
#print(response)
#print(response.json())
"""