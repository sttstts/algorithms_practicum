import math

def fib(n):
    t = (1 + math.sqrt(5)) / 2
    f = (1 - math.sqrt(5)) / 2

    fib_n = (t ** n - f ** n) / math.sqrt(5)

    return round(fib_n)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите число n (1 ≤ n ≤ 64) для вычисления n-го числа Фибоначчи (или 0 для выхода): "))

            if n == 0:
                print("Выход из программы.")
                break

            if 1 <= n <= 64:
                print(f"F({n}) = {fib(n)}")
            else:
                print("Пожалуйста, введите число в диапазоне от 1 до 64.")

        except ValueError:
            print("Ошибка: введите целое число.")
