from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    # echo data back to client
    print(request.GET)  # url query params if is a get request
    print(request.POST)  # url query params if is a post request
    body = request.body
    try:
        data = json.loads(body)
    except:
        data = {}
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    return JsonResponse(data)
