from django.http import HttpResponse
import request, pymongo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps
from .Connect import collection_Instagram
from .Save import save_img


# Create your views here.


save_img()

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def search_result(request):
    return render(request, "dashboard/search_result.html")

@csrf_exempt
def display_table(request):
    table_cursor = collection_Instagram.find({'confs': {'$exists': 'true'}}).sort('likes', pymongo.DESCENDING).limit(25)
    list_table = list(table_cursor)
    table_string = dumps(list_table)
    return HttpResponse(table_string, content_type='application/json')


def display_today(request):
    today_cursor = collection_Instagram.find_one(sort=[('date', pymongo.DESCENDING)])
    today_dict = today_cursor['dir']
    real_dir = str("/static") + today_dict[1:]
    return HttpResponse(real_dir, content_type='application/json')


def search(request):
    payload = []
    if request.method == 'GET':
        searched = request.GET['searched']
        add_result = collection_Instagram.aggregate([
            {
                "$match": {"confs": searched}
            },
            {
                "$sort": {"date": 1}
            }
        ])

        for i in add_result:
            payload.append(i['dir'])
        search_dir = []
        for j in payload:
            search_dir.append(j[2:])
    return render(request, 'dashboard/searched.html', {'data': search_dir})



