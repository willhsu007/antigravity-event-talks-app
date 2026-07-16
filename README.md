# BigQuery Release Notes Fetcher & Tweeter 🚀

一個基於 Python Flask 與現代化前端網頁技術的 BigQuery 發布說明抓取與推文分享工具。此專案具備精美的 Glassmorphism（玻璃擬態）視覺風格，讓你可以即時追蹤 Google BigQuery 的最新更新，並能一鍵將特定的更新內容編輯並分享至 X (Twitter)。

## ✨ 功能特點

- 📡 **即時抓取**：後端代抓 Google Cloud BigQuery Release Notes RSS Feed，徹底解決前端 CORS 限制。
- 🎨 **前衛視覺設計 (Rich Aesthetics)**：採用暗黑科幻背景與半透明玻璃質感卡片，輔以細緻的懸停動畫與漸層發光邊框。
- 🔄 **手動重新整理**：提供流暢旋轉動畫 (Spinner) 的重新整理按鈕，隨時取得最新資訊。
- 🐦 **一鍵推文 (Tweet About It)**：
  - 點擊卡片可選取並高亮特定更新。
  - 整合推文編輯彈窗，具備 280 字元上限統計。
  - 使用 Twitter Web Intent API 安全地在瀏覽器中引導用戶發送推文。

## 📁 專案結構

```text
├── app.py              # Flask 後端應用程式 (負責路由與 XML 抓取解析)
├── requirements.txt    # 專案依賴套件清單
├── .gitignore          # Git 忽略檔案清單
├── README.md           # 專案說明文件 (本檔案)
└── templates/
    └── index.html      # 前端頁面 (HTML / CSS / JavaScript)
```

## 🛠️ 開發環境與安裝步驟

### 1. 複製本專案
```bash
git clone https://github.com/willhsu007/antigravity-event-talks-app.git
cd antigravity-event-talks-app
```

### 2. 建立並啟動 Python 虛擬環境
* **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. 安裝依賴套件
```bash
pip install -r requirements.txt
```

### 4. 執行 Flask 伺服器
```bash
python app.py
```

伺服器啟動後，請在瀏覽器中開啟 [http://127.0.0.1:5000](http://127.0.0.1:5000) 即可開始使用！
