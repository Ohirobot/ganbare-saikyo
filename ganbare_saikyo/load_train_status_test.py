# cronやタスクスケジューラによって定期実行する「データ更新処理」を実装する予定
# APIで取得したデータをDBに格納する

# load_train_status.py
import os
import django
import json
from datetime import datetime

# Djangoの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ganbare_saikyo.settings')
django.setup()

from traininfo.models import TrainStatus

def main():
    json_path = os.path.join('traininfo', 'static', 'mock', 'train_status.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    TrainStatus.objects.all().delete()
    for item in data:
        TrainStatus.objects.create(
            line_name=item["line_name"],
            status=item["status"],
            message=item["message"],
            timestamp=datetime.fromisoformat(item["timestamp"])
        )
    print("✅ データの更新が完了しました")

if __name__ == '__main__':
    main()
