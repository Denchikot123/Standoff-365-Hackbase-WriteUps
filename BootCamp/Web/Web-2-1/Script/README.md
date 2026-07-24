# Web-2-1 Autocomplete Script

## ⚙️ Техническое описание и стек

Скрипт разработан для автоматического получения флага стенда **Web-2-1** в категории **BootCamp** на ИБ-полигоне **Standoff 365 Hackbase**

### 🧰 Инструменты и библиотеки
* **Язык**: Python
* **Пакеты**:
  * `Requests` — работа с вэб-запросами.

### 🔄 Процесс работы скрипта

```mermaid
graph LR
    A["⚙️ Старт<br>(main)"] --> B["📝 Формирование payload<br>(file=/etc/pt.flag)"]
    B --> C["🌐 HTTP GET запрос<br>(requests.get)"]
    C --> D{"Проверка связи?"}
    
    D -->|Успешно| E["📄 Вывод содержимого<br>(print flag)"]
    D -->|Ошибка сети| F["❌ Вывод ошибки<br>(print Exception)"]
```

### 🚀 Запуск скрипта

1. **Установите зависимости**:
   ```bash
   pip install requests
   ```
2. **Запустите скрипт**:
   ```bash
   python Web-2-1-autocomplete.py
   ```
