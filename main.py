import time
import logging

# Настройка логгера для замера времени
logging.basicConfig(level=logging.INFO, format='%(message)s')

# 1. Итеративная функция Фибоначчи
def fib_iterative(n):
    """Считает n-ное число Фибоначчи через цикл"""
    if n <= 1:
        return n

    # Первые два числа
    a, b = 0, 1

    # Считаем остальные
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# 2. Рекурсивная функция Фибоначчи
def fib_recursive(n):
    """Считает n-ное число Фибоначчи через рекурсию"""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# 3. Рекурсивная сумма всех чисел во вложенных списках
def sum_nested_list(lst):
    """Считает сумму всех чисел во вложенных списках"""
    total = 0

    for item in lst:
        if isinstance(item, list):
            # Если элемент - список, вызываем эту же функцию для него
            total += sum_nested_list(item)
        else:
            # Если элемент - число, добавляем его
            total += item
    return total

# Замеряем скорость работы функций Фибоначчи
def compare_fib_speed():
    """Сравнивает скорость итеративного и рекурсивного методов"""
    n = 35  # Берем 35, т.к. для 50 рекурсия будет очень долгой

    # Замеряем итеративную функцию
    start = time.time()
    result_iter = fib_iterative(n)
    time_iter = time.time() - start

    # Замеряем рекурсивную функцию
    start = time.time()
    result_rec = fib_recursive(n)
    time_rec = time.time() - start

    # Выводим результаты
    print(f"Итеративная функция:")
    print(f"  Число Фибоначчи F({n}) = {result_iter}")
    print(f"  Время выполнения: {time_iter:.6f} секунд")
    print()
    print(f"Рекурсивная функция:")
    print(f"  Число Фибоначчи F({n}) = {result_rec}")
    print(f"  Время выполнения: {time_rec:.6f} секунд")
    print()
    print(f"Разница в скорости: {time_rec / time_iter:.1f} раз")

    # Проверяем
    if result_iter == result_rec:
        print("Результаты совпадают!")
    else:
        print("Ошибка: результаты не совпадают!")

# Тестируем вложенные списки
def test_sum_function():
    """Тестирует функцию суммы вложенных списков"""
    test_list = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]

    print("Тест суммы вложенных списков:")
    print(f"Исходный список: {test_list}")

    result = sum_nested_list(test_list)
    print(f"Сумма всех чисел: {result}")

    # Проверяем правильность
    # 1 + 2 + 3 + 4 + 5 + 6 + (-1) + (-5) + 0 = 15
    if result == 15:
        print("Правильно! Сумма = 15")
    else:
        print(f"Ошибка! Ожидалось 15, получилось {result}")

# Основа
if __name__ == "__main__":
    print("=" * 50)
    print("СРАВНЕНИЕ ФУНКЦИЙ ФИБОНАЧЧИ")
    print("=" * 50)
    compare_fib_speed()

    print("\n" + "=" * 50)
    print("СУММА ВЛОЖЕННЫХ СПИСКОВ")
    print("=" * 50)
    test_sum_function()

    # Дополнительный тест с 50-м числом Фибоначчи (только итеративно)
    print("\n" + "=" * 50)
    print("50-Е ЧИСЛО ФИБОНАЧЧИ (только итеративно)")
    print("=" * 50)

    start = time.time()
    fib_50 = fib_iterative(50)
    time_50 = time.time() - start

    print(f"F(50) = {fib_50}")
    print(f"Время расчета: {time_50:.6f} секунд")

    # рекусрсия долго работает
    print("\n" + "=" * 50)
    print("ВАЖНО!")
    print("=" * 50)
    print("Рекурсивная функция для F(50) будет работать ОЧЕНЬ ДОЛГО")
    print("(примерно 2-3 минуты или больше в зависимости от компьютера)")
    print("Это потому что она повторяет одни и те же расчеты много раз.")
    print("\nХотите попробовать? (y/n): ", end="")

    answer = input().strip().lower()
    if answer == 'y':
        print("\nЗапускаю рекурсивную функцию для F(35)...")
        start = time.time()
        result = fib_recursive(35)
        time_taken = time.time() - start
        print(f"F(35) = {result}")
        print(f"Время: {time_taken:.2f} секунд")

        print("\nА теперь представьте, как долго считалось бы F(50)...")
