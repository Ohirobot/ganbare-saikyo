document.addEventListener('DOMContentLoaded', () => {

  async function fetchTrainStatus() {
    try {
      const response = await fetch('/api/train-status/');
      const data = await response.json();

      const container = document.getElementById('status-container');
      if (!container) return;

      const html = data.map(status => {
        const isDelay = status.status.includes('遅延');

        const message = status.message?.trim()
          ? status.message
          : '詳細情報はありません';

        return `
          <div class="col">
            <div class="card h-100 shadow-sm">
              <div class="card-header d-flex justify-content-between">
                <span class="text-muted small">
                  ${status.timestamp}
                </span>
                <span class="badge ${isDelay ? 'bg-danger' : 'bg-success'}">
                  ${isDelay ? '遅延' : '正常'}
                </span>
              </div>

              <div class="card-body">
                <h5 class="card-title">
                  ${isDelay ? '⚠' : '✔'} ${status.status}
                </h5>
                <p class="card-text">
                  ${message}
                </p>
              </div>
            </div>
          </div>
        `;
      }).join('');

      container.innerHTML = html;

    } catch (error) {
      console.error('データ取得失敗:', error);
    }
  }

  fetchTrainStatus();
  setInterval(fetchTrainStatus, 30000);

});
