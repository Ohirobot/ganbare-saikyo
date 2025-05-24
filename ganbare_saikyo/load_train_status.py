import os
import requests
import django
import json
from datetime import datetime

# Djangoの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ganbare_saikyo.settings')
django.setup()

from traininfo.models import TrainStatus


def fetch_train_status_from_api():
    # 例: 駅すぱあとの運行情報APIのURL（要実際のエンドポイントで確認）
    api_url = "https://api.ekispert.jp/v1/json/operationLine"
    api_key = "YOUR_API_KEY"  # ← 本番は settings.py や環境変数から取得が推奨

    params = {
        'key': api_key,
        'line': 'JR.Saikyo'  # 埼京線のコード（実際はAPI仕様書で確認）
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()

    return response.json()


def save_train_status(data):
    TrainStatus.objects.all().delete()

    # これは仮の構造（実際は駅すぱあとAPIのレスポンスに合わせて修正）
    for item in data.get("Result", {}).get("OperationLine", []):
        TrainStatus.objects.create(
            line_name=item.get("Name", "不明"),
            status=item.get("Status", "未設定"),
            message=item.get("Text", "詳細なし"),
            timestamp=datetime.now()  # or APIから取得できる場合はそれ
        )


def main():
    data = fetch_train_status_from_api()
    save_train_status(data)
    print("✅ 駅すぱあとAPIから運行情報を更新しました")


if __name__ == '__main__':
    main()
