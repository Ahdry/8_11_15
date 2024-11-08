import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс
        self.lock = threading.Lock()  # Объект блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайного числа
            with self.lock:  # Блокировка потока
                self.balance += amount  # Пополнение баланса
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.01)  # Увеличено для более реалистичного времени выполнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайного числа
            print(f"Запрос на {amount}")
            with self.lock:  # Блокировка потока
                if amount <= self.balance:  # Проверка на достаточность средств
                    self.balance -= amount  # Снятие средств
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            time.sleep(0.01)  # Увеличено для более реалистичного времени выполнения

# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
