from swift_wrapper import *
from predict import predict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import httplib
import requests
import urllib
from urlparse import parse_qs
# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    return Response("haha")

@api_view(['POST'])
def upload(request):
    # trigger the train
    h1 = httplib.HTTPConnection('172.17.183.181')
    model = parse_qs(request.META['QUERY_STRING'])['model'][0]
    print model
    file = request.FILES['file']
    print 'upload... ' + file.name
    send("data", file)
    r = requests.get('http://172.17.183.181/?data='+file.name+'&model='+model)
    #params = urllib.urlencode({'model': 'default', 'data': file.name})
    #print params
    #h1.request('GET', '/', params)
    return Response(status=201)

@api_view(['GET'])
def getAll(request):
    objects = map(lambda r:r['name'], listObjects("models"))
    return Response(objects,content_type="application/json")

@api_view(['GET'])
def getOne(request, pk):
    data = getMetaData("data", pk)
    return Response(data,content_type="application/json")

@api_view(['POST'])
def predict_model(request, model):
    print 'predict...'
    data = json.loads(request.body)
    result = predict(model, data)
    print result
    return Response(result ,status=201, content_type="application/json")
