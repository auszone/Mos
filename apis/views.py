from config import *
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def index(request, pk):
    print(x)
    print(pk)
    print(request.data)
    print(request.data.get('test'))
    return Response({'pk': pk})


