from django.db import models

class TrainStatus(models.Model):
    line_name = models.CharField(max_length=100)  # 例: 埼京線
    status = models.CharField(max_length=200)     # 例: 平常運転, 遅延, etc
    message = models.TextField(blank=True, null=True)  # 詳細メッセージ
    timestamp = models.DateTimeField(auto_now_add=True)  # 取得日時

    def __str__(self):
        return f"{self.line_name} - {self.status} ({self.timestamp})"
