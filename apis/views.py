from swift_wrapper import *
from predict import predict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    return Response("haha")

@api_view(['POST'])
def upload(request):
    file = request.FILES['file']
    send("data", file)
    return Response(status=201)

@api_view(['GET'])
def getAll(request):
    objects = map(lambda r:r['name'], listObjects("data"))
    result = []
    for o in objects:
        result.append(getMetaData("data", o))
    return Response(result,content_type="application/json")

@api_view(['GET'])
def getOne(request, pk):
    data = getMetaData("data", pk)
    return Response(data,content_type="application/json")

@api_view(['POST'])
def predict(request, model):
    data = json.loads(request.body)
    return Response(predict(model, data) ,status=201)
