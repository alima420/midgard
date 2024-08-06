from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from django.views.decorators.http import require_http_methods
from .models import Machine, LogisticsBox, Exception, ProductBox
import json
from rest_framework import viewsets
from .serializers import LogisticsBoxSerializer, ExceptionSerializer, ProductBoxSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@csrf_exempt
@require_http_methods(["GET", "POST"])
def machine_update(request, machine_name):
    machine = get_object_or_404(Machine, name=machine_name)
    
    if request.method == 'GET':
        data = {
            "name": machine.name,
            "status": machine.status,
            "program": machine.program,
            "counter": machine.counter
        }
        return JsonResponse(data)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        machine.status = data.get("status", machine.status)
        machine.program = data.get("program", machine.program)
        machine.counter = data.get("counter", machine.counter)
        machine.save()
        return JsonResponse({"message": "Machine updated successfully."})

class LogisticsBoxViewSet(viewsets.ModelViewSet):
    queryset = LogisticsBox.objects.all()
    serializer_class = LogisticsBoxSerializer

class ExceptionViewSet(viewsets.ModelViewSet):
    queryset = Exception.objects.all()
    serializer_class = ExceptionSerializer
    lookup_field = 'serial_number'


class ProductBoxViewSet(viewsets.ModelViewSet):
    queryset = ProductBox.objects.all()
    serializer_class = ProductBoxSerializer
    lookup_field = 'product_serial'

@api_view(['GET'])
def exceptions_for_box(request, box_id):
    try:
        box = LogisticsBox.objects.get(logistics_box_id=box_id)
    except LogisticsBox.DoesNotExist:
        return Response({'detail': 'Box not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    exceptions = Exception.objects.filter(logistics_box=box)
    serializer = ExceptionSerializer(exceptions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_logistics_box(request, box_id):
    try:
        box = LogisticsBox.objects.get(logistics_box_id=box_id)
    except LogisticsBox.DoesNotExist:
        return Response({'detail': 'Box not found.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    serializer = LogisticsBoxSerializer(box)
    return Response(serializer.data)