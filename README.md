# WeHelp Weather Team 5

本專案為 WeHelp 第二階段第八週之團隊合作作業，目標為合作開發一個氣象資訊的網站，包含後端 API 與前端展示，並整合Discord Webhook，在Discord channel進行即時推播。

---

## 👥 團隊分工

本專案採取前後端分工進行開發，並透過 GitHub Pull Request 進行整合與 code review。

### 成員與負責項目

- **組員 張瑀珊(組長)**
  - 前端資料 API 串接
  - 前端版面樣式
  - 前端推播按鈕串接
  - 擔任 host Repository，負責整合並合併 GitHub Pull Request。

- **組員 林庭安**
  - 前端頁面設計與實作
  - 天氣資訊視覺化呈現
  - 報告 PPT 實作

- **組員 林冠宇**
  - 實作後端 API
  - weather資料庫結構設計 
  - 與氣象站串接 API
  - 協助前後端串接debug
  
- **組員 何珮璇**
  - Discord Webhook 六都天氣推播功能後端設計與實作
  - README.md撰寫
  - EC2部署



---

## 🔗 成果展示連結

- **專案前端展示網站**  
  👉 http://43.213.29.230:8000/

---

## 🛠 使用技術

- Backend：FastAPI、Python
- Database：MySQL
- Frontend：HTML / CSS / JavaScript
- Third-party Service：中央氣象署 API、Discord Webhook
- Deployment：AWS EC2

---

## 📂 Repository 說明

- 本 Repository 為 **Host Repository**
- 各組員透過 fork 專案進行開發
- 完成功能後以 Pull Request 方式合併至 `develop` branch
