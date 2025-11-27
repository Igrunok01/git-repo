from datetime import datetime
import os

os.makedirs("docs", exist_ok=True)

with open("docs/info.txt", "w", encoding="utf-8") as f:
    f.write("Документация к лабораторной работе по CI/CD\n")
    f.write("Проект: простая функция безопасного деления и тесты.\n")
    f.write(f"Последнее обновление: {datetime.utcnow().isoformat()} UTC\n")
