import re

def parse_receipt(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Сумма
        total = re.search(r'(?:ИТОГО|TOTAL|СУММА)[:\s]*([\d[\d\s,.]*)', content, re.IGNORECASE)
        # Дата
        date = re.search(r'(\d{2}\.\d{2}\.\d{4})', content)
        
        print(f"--- Результаты парсинга файла: {filename} ---")
        print(f"Дата: {date.group(1) if date else 'Не найдена'}")
        print(f"Сумма: {total.group(1).strip() if total else 'Не найдена'}")
        
    except FileNotFoundError:
        print("Ошибка: Файл raw.txt не найден в этой папке.")

if __name__ == "__main__":
    parse_receipt('raw.txt')