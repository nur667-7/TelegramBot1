# Business Card Telegram Bot

Интерактивный Telegram-бот визитка разработчика с кнопками и ссылками на соцсети.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-v20+-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Функционал

- `/start` — приветствие и меню доступных команд.
- `/about` — краткая информация о разработчике и стеке технологий.
- `/social` — интерактивные Inline-кнопки со ссылками на социальные сети и профили (Telegram, Instagram, LinkedIn).

---

## 🚀 Быстрый старт

### 1. Клонирование и виртуальное окружение

```bash
git clone https://github.com/nur667-7/TelegramBot1.git
cd TelegramBot1
python -m venv venv
# Linux / macOS:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка токена

Получите токен у [@BotFather](https://t.me/BotFather) и задайте переменную окружения `TOKEN`:

**Windows (PowerShell):**
```powershell
$env:TOKEN="ваш_токен_бота"
```

**Linux / macOS:**
```bash
export TOKEN="ваш_токен_бота"
```

### 4. Запуск бота

```bash
python bot.py
```
