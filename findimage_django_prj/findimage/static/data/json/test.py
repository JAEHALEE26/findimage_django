import io
import cv2
import requests
import numpy as np
import json
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
def json_detect(filename) :
    with open(filename,'r') as f:
        json_data = json.load(f)

    for i in range (0,len(json_data['posts'])) :
        json_data['posts'][i]['conf'] = []
        url = json_data['posts'][i]['img_url']
        image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
        image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
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
        with open('t1.json','r') as f:
            json_data2 = json.load(f)
        for j in range(0,len(json_data2["predictions"])) :
            json_data['posts'][i]['conf'].append((json_data2["predictions"][j]['class']))
        if(len(json_data['posts'][i]['conf'])!=0) :
            json_data['posts'][i]['detect_flag'] = True
    #print(json.dumps(json_data, indent=2))

    with open(filename,'w+', encoding='utf-8') as f:
        json.dump(json_data,f,ensure_ascii=False, indent=4)
f_name = '2022-05-11_패션.json'
json_detect(f_name)