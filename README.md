# Тестовое задание

## Описание

Это тестовое задание включает в себя четыре задачи, каждая из которых реализована в отдельном файле. Описание каждой задачи и её функционала приведены ниже.

## Файлы и их описание

### 1. `calculator.py`

Алгебраический калькулятор

**Функция:**
- `algebraic_calculator(expression)`  
  Упрощает алгебраическое выражение, возвращая эквивалентное упрощенное выражение. Поддерживаются переменные `x`, `y`, `z` и операции `+`, `-`, `*`. При неверных входных данных возвращает сообщение «Недопустимое выражение».

**Примеры использования:**
```python
from calculator import algebraic_calculator

print(algebraic_calculator("2 * (3 * x + 4 * y) - 7 * y + 9"))
print(algebraic_calculator("z + z + 2 + 3 - 2 * z"))
print(algebraic_calculator("3 * (("))
print(algebraic_calculator("5x + 4y"))
```

### 2. `shop.py`

Учёт товаров в онлайн магазине

**Классы:**
- `Product`  
  Основной класс для продуктов с атрибутами имени, цены и количества.
- `Perishable`
  Наследуется от Product, добавляет дату создания и срок годности, а также метод для проверки истечения срока годности.
- `Vitamin`
  Наследуется от Product, добавляет информацию о необходимости рецепта.
- `Cart`
  Класс для управления корзиной, добавления товаров и расчёта общей стоимости.

**Пример использования:**
```python
from shop import Product, Perishable, Vitamin, Cart
from datetime import datetime

milk = Perishable("Молоко", 100, 10, datetime.datetime(2023, 9, 12), 3)
vitamin_c = Vitamin("Витамин C", 200, 5, True)
apple = Product("Яблоко", 50, 20)

cart = Cart()
cart.add_item(milk, 2)
cart.add_item(vitamin_c, 1)
cart.add_item(apple, 5)
print(cart.calculate_total())
```

### 3. `parser_html.py`

Парсер HTML-страницы

**Функции:**
- `clean_html(html)`
  Удаляет HTML-теги из текста.
- `count_words(text)`
  Подсчитывает количество слов, состоящих минимум из 3 букв, и возвращает топ 10 наиболее часто встречающихся слов.

**Пример использования:**
```python
from parser_html import clean_html, count_words

try:
    with open("example.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    clean_text = clean_html(html_content)
    top_words = count_words(clean_text)

    print(top_words)

except FileNotFoundError:
    print("Файл 'example.html' не найден. Убедитесь, что файл находится в нужной директории.")
```

### 4. `sql.py`

SQL-запрос для создания отчёта по налогам сотрудников

**Запрос:**
```sql
SELECT Employees.name,
       Contracts.type,
       Positions.salary,
       (Positions.salary * Contracts.tax_rate / 100) AS tax_amount
FROM Employees
JOIN Positions ON Employees.position_id = Positions.id
JOIN Contracts ON Employees.contract_id = Contracts.id
WHERE Positions.salary < 50000;
```
Запрос формирует отчёт, указывающий количество денежных средств, которые нужно заплатить в качестве налогов за сотрудников с ставкой менее 50000 рублей.

___________________________________________________________________________________________________
Этот формат README.md обеспечит четкое представление о каждом файле и его функционале.