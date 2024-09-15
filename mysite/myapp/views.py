from django.shortcuts import render
from django.http import HttpResponse
from .models import Mymodel
import threading

def create_model_instance(request):
    obj = Mymodel.objects.create(name="Test")
    print("Object created")
    print("Main thread ID:", threading.get_ident())
    return HttpResponse("Model instance created")
