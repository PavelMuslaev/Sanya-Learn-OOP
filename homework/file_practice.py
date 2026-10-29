from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_DIR / 'output' / 'homework' / 'file_practice'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


with open(OUTPUT_DIR / 'poem.txt', 'w', encoding='UTF-8') as f:
    f.write('У лукоморья дуб зелёный;\n')
    f.write('Златая цепь на дубе том:\n')
    f.write('И днём и ночью кот учёный\n')
    f.write('Всё ходит по цепи кругом.\n')

print('--- readline() ---')
with open(OUTPUT_DIR / 'poem.txt', 'r', encoding='UTF-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end='')

print('\n--- readlines() ---')
with open(OUTPUT_DIR / 'poem.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')

print('\n--- for line in f ---')
with open(OUTPUT_DIR / 'poem.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line, end='')

print('\n--- write() ---')
with open(OUTPUT_DIR / 'example.txt', 'w', encoding='UTF-8') as f:
    f.write('Hello World\n')
    f.write('Bye world!')
with open(OUTPUT_DIR / 'example.txt', 'r', encoding='UTF-8') as f:
    print(f.read())

print('\n--- writelines() ---')
lines = ['Первая строка\n', 'Вторая строка\n', 'Третья строка\n']
with open(OUTPUT_DIR / 'example.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
with open(OUTPUT_DIR / 'example.txt', 'r', encoding='utf-8') as f:
    print(f.read(), end='')

print('\n--- режим w ---')
with open(OUTPUT_DIR / 'mode_demo.txt', 'w', encoding='utf-8') as f:
    f.write('Старое содержимое\n')
with open(OUTPUT_DIR / 'mode_demo.txt', 'w', encoding='utf-8') as f:
    f.write('Новое содержимое (старое стёрто)\n')
with open(OUTPUT_DIR / 'mode_demo.txt', 'r', encoding='utf-8') as f:
    print(f.read(), end='')

print('\n--- режим a ---')
with open(OUTPUT_DIR / 'log.txt', 'a', encoding='utf-8') as f:
    f.write('Новая запись в логе\n')
with open(OUTPUT_DIR / 'log.txt', 'r', encoding='utf-8') as f:
    print(f.read(), end='')

print('\n--- режим x ---')
try:
    with open(OUTPUT_DIR / 'unique.txt', 'x', encoding='utf-8') as f:
        f.write('Файл создан впервые\n')
    print('Файл unique.txt создан')
except FileExistsError:
    print('Такой файл уже существует!')

print('\n--- режим r+ ---')
with open(OUTPUT_DIR / 'rplus.txt', 'w', encoding='utf-8') as f:
    f.write('Строка 1\nСтрока 2\nСтрока 3\n')

with open(OUTPUT_DIR / 'rplus.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()
    if len(lines) >= 2:
        lines[1] = 'Новая строка 2\n'
        f.seek(0)
        f.writelines(lines)
        f.truncate()
with open(OUTPUT_DIR / 'rplus.txt', 'r', encoding='utf-8') as f:
    print(f.read(), end='')

print('\n--- то же самое без r+ ---')
with open(OUTPUT_DIR / 'data.txt', 'w', encoding='utf-8') as f:
    f.write('Строка 1\nСтрока 2\nСтрока 3\n')

with open(OUTPUT_DIR / 'data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
if len(lines) >= 2:
    lines[1] = 'Новая строка 2\n'
with open(OUTPUT_DIR / 'data.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
with open(OUTPUT_DIR / 'data.txt', 'r', encoding='utf-8') as f:
    print(f.read(), end='')

print('\n--- режим w+ ---')
with open(OUTPUT_DIR / 'wplus.txt', 'w+', encoding='utf-8') as f:
    f.write('Записал и тут же прочитал\n')
    f.seek(0)
    print(f.read(), end='')

print('\n--- режим a+ ---')
with open(OUTPUT_DIR / 'aplus.txt', 'w', encoding='utf-8') as f:
    f.write('Первая строка\n')
with open(OUTPUT_DIR / 'aplus.txt', 'a+', encoding='utf-8') as f:
    f.write('Дописал в конец\n')
    f.seek(0)
    print(f.read(), end='')
