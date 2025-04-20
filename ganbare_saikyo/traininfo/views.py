from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def saikyo_status(request):
    file_path = os.path.join(os.path.dirname(__file__), 'mock_data', 'saikyo_status.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return JsonResponse(data)
