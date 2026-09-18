# Парсер каталога компаний

Собирает данные о компаниях (название, адрес, телефон, часы работы) и сохраняет в Excel.

## Что умеет
- Парсинг каталога
- Чистка телефонов (убирает всё, кроме цифр)
- Удаление дублей
- Сохранение в Excel

## Стек
- Python
- requests (для реальных сайтов)
- BeautifulSoup
- pandas
- re

## Как запустить
1. Установи зависимости:
   pip install requests beautifulsoup4 pandas openpyxl
2. Запусти:
   python companies_parser.py
3. Результат: baza.xlsx
