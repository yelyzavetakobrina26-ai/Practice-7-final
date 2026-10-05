"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.
from pathlib import Path

folder_path=Path("students_analysis")
folder_path.mkdir(exist_ok=True)
file_path=folder_path/"students.csv"
lines=[
    "name,math,python,english\n",
    "Настя,89,98,90\n",
    "Катя,90,89,95\n"
]
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print(f"Файл успішно створено за шляхом {file_path}")



# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)
INPUT_FILE=file_path
OUTPUT_FILE=folder_path/"result.txt"
total_math=0
total_python=0
total_english=0
students_count=0
best_students=""
best_average=0.0

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f,None)
    for line in f:
        parts=line.strip().split(",")
        name=parts[0]
        math=float(parts[1])
        python=float(parts[2])
        english=float(parts[3])
        total_math+=math
        total_python+=python
        total_english+=english
        students_count+=1
        students_average=(math+python+english)/3
        if students_average>best_average:
            best_average=students_average
            best_students=name
    average_math=total_math/students_count
    average_python=total_python/students_count
    average_english=total_english/students_count

# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.
results_text = f"""Середній бал по класу:
math: {average_math:.1f}
python: {average_python:.1f}
english: {average_english:.1f}

Найкращий студент: {best_students} ({best_average:.1f})"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(results_text)

print(f"Результат аналізу:\n{results_text}")




# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
