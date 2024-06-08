from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .service.UserService import UserService
import json


@csrf_exempt
def user_signup(request):
    json_request = json.loads(request.body)
    res = {}
    user = UserService()
    user.add(json_request)
    res['message'] = 'User added successfully'
    return JsonResponse({"data": res})
