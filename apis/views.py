from swift_wrapper import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    return Response("haha")

@api_view(['POST'])
def upload(request):
    file = request.FILES['file']
    send(file)
    return Response(status=201)

