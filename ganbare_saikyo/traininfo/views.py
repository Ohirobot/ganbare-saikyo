import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import TrainStatus
from django.conf import settings
import os
from datetime import datetime

def index(request):
    status_list = TrainStatus.objects.all().order_by('-timestamp')
    return render(request, 'traininfo/index.html', {
        'status_list': status_list
    })

def about(request):
    return render(request, 'traininfo/about.html')

def load_mock_data(request):
    json_path = os.path.join(settings.BASE_DIR, 'traininfo/static/mock/train_status.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    TrainStatus.objects.all().delete()  # リセット（開発中のみ）
    for item in data:
        TrainStatus.objects.create(
            line_name=item["line_name"],
            status=item["status"],
            message=item["message"],
            timestamp=datetime.fromisoformat(item["timestamp"])
        )
    return render(request, 'traininfo/index.html', {
    'status_list': TrainStatus.objects.all().order_by('-timestamp')
})

def train_status_api(request):
    status_list = TrainStatus.objects.all().order_by('-timestamp')[:10]

    data = []
    for status in status_list:
        data.append({
            "line_name": status.line_name,
            "status": status.status,
            "message": status.message,
            "timestamp": status.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return JsonResponse(data, safe=False)
