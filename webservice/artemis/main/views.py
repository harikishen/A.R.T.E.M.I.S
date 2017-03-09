from django.http import HttpResponse
from django.shortcuts import render_to_response
from artemis.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_exempt
from utils.predict import *
from utils.vector import *
from utils.config import *
import numpy as np
import uuid

def handle_uploaded_file(f):
    filename = MEDIA_ROOT + '/' + str(uuid.uuid4())
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename

def analyze(filename):
    _vector = []
    logger.info(filename)
    temp_vector, temp_label = vectorize(filename, 0, MEDIA_ROOT)
    if temp_vector:
        _vector.append(temp_vector)
    logger.info(_vector)
    if _vector:
        logger.info(np.array(_vector, np.float32))
        result = predict(np.array(_vector, np.float32))
        if result == [0]:
            return('malware')
        else:
            return('benign')
    else:
        logger.info("Empty Vector")
        return('failed')
    return failed

def index(request):
    return render_to_response('main/index.html')

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        filename = handle_uploaded_file(request.FILES['file'])
        result = analyze(filename)
        return HttpResponse(result)
    return HttpResponse('use post')
