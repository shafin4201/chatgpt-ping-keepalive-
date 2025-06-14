# 🟢 ChatGPT Ping Keepalive

This is a simple Python + Selenium script to keep your ChatGPT session alive by automatically pinging [chat.openai.com](https://chat.openai.com) every 7 minutes.

Deployed on [Render](https://render.com) as a **background worker**.

---

## ⚙️ Features

- ✅ Keeps ChatGPT session active using headless Chrome
- ✅ Loads cookies from `cookies.json`
- ✅ Runs every 7 minutes via `schedule`
- ✅ Deployed seamlessly on Render's free plan

---

## 🛠️ Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/yourusername/chatgpt-ping-keepalive.git
cd chatgpt-ping-keepalive