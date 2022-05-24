import shutil
from datetime import date
import requests
from pathlib import Path
from .Connect import collection_Instagram


def save_img():
    imgList = collection_Instagram.distinct("img_url")

    for img_url in imgList:
        a = collection_Instagram.find_one({"img_url": img_url})
        query = a['query']

    try:
        today = str(date.today())
        if Path('static/data/images/' + today + '/').exists() != True:
            Path('static/data/images/' + today + '/').mkdir()

        for i, img_url in enumerate(imgList):
            findquery = collection_Instagram.find_one({"img_url": img_url})
            query = findquery['query']
            resp = requests.get(img_url, stream=True)
            local_file = open('static/data/images/' + today + '/' + query + str(i + 1) + '.jpg', 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            del resp

        print("end")

    except Exception as e:
        print("Problem while saving photos inside image list..")
        print(e)

save_img()