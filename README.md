# CSV Report Tool

Генератор отчетов из CSV файлов с данными разработчиков. Выполнено в соответствии с приложенным техническим заданием.

## Основной функционал
- Чтение одного или нескольких CSV файлов
- Генерация отчета "performance" - средняя эффективность по должностям
- Сортировка результатов по убыванию эффективности
- Красивый табличный вывод в консоль

## Стек
- Python 3.13
- argparse - парсинг аргументов
- csv - чтение CSV файлов  
- tabulate - форматирование таблиц
- pytest - тестирование

## Установка
- Создать вирутуальное окружение и установить зависимости:
```bash
pip install -r requirements.txt
```

## Если необходимо провести тестирование:
```bash
pip install -r requirements-dev.txt
```

## Использование
```bash
python -m csv_tool.main --files examples/employees1.csv examples/employees2.csv --report performance
```
## Пример такого результата
[examples/employees1.csv examples/employees2.csv](output_example.png)

## Тестирование
```bash
pytest
```
