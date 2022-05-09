from django.http import HttpResponse
import ssl, request
from django.shortcuts import render
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps

# Create your views here.

def index(request):
    return render(request, "index/index.html")

ssl._create_default_https_context = ssl._create_unverified_context
client = MongoClient("mongodb+srv://findimage123:findimagecapstone@cluster0.p7r2e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['2022-04-30']
collection_name = db.get_collection('패션')
cursor = collection_name.find()
list_cur = list(cursor)

@csrf_exempt
def test(request):
    json_data = dumps(list_cur)
    return HttpResponse(json_data, content_type='application/json')




