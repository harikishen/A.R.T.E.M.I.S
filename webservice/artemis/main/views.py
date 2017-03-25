from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from artemis.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_exempt
from utils.predict import *
from utils.vector import *
from utils.config import *
import numpy as np
import uuid
import os
import json

def handle_uploaded_file(f):
    filename = MEDIA_ROOT + '/' + str(uuid.uuid4())
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename

def analyze(filename):
    _vector = []
    result_list = {}
    folderindex = filename.split('/')[-1]
    logger.info(folderindex)
    temp_vector, temp_label, permissions, api, actions = vectorize(filename, folderindex, MEDIA_ROOT)
    if temp_vector:
        _vector.append(temp_vector)
    logger.info(_vector)
    os.system('rm ' + filename)
    result_list['permissions'] = permissions
    result_list['api'] = api
    result_list['actions'] = actions
    if _vector:
        logger.info(np.array(_vector, np.float32))
        result = predict(np.array(_vector, np.float32))
        if result == [0]:
            result_list['result'] = 'malware'
        else:
            result_list['result'] = 'benign'
    else:
        logger.info("Empty Vector")
        result_list['result'] = 'extractionfailed'
    return JsonResponse(result_list)
def index(request):
    return render_to_response('main/index.html')

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        filename = handle_uploaded_file(request.FILES['file'])
        request.session['filename'] = filename
        return HttpResponse(filename)
    return HttpResponse('usepost')

@csrf_exempt
def analyze_file(request):
    if request.method == 'POST':
        result = analyze(request.session.get('filename',''))
        return HttpResponse(result)
    return HttpResponse('usepost')
