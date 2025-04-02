import time
import sys
import os

print("-" *60)
print("|" " Привет это тестовая программа которая выполняет команды! " "|")
print("-" *60)
time.sleep(2)
print("\t\t\t↓")
print("Подаждите 5 секунд что бы запустилась программа!")
print("\t\t\t↓")
def loading_animation(duration=5, length=20):
    for i in range(length + 1):  
        bar = "#" * i + "-" * (length - i)  
        sys.stdout.write(f"\rЗагрузка: [{bar}] {int((i / length) * 100)}%")  
        sys.stdout.flush()
        time.sleep(duration / length)  
    sys.stdout.write("\nПрограмма запустилась\n")  
loading_animation(5)
print("\t↓")
time.sleep(1)
print("Выберайте вариант!")
print("↓")
1 == print("1. Ping")
2 == print("2. Tracert")
3 == print("3. Netstat")
4 == print("4. Ipconfig")
5 == print("5. Exit\n")
time.sleep (2)
f = input("Введите номер команды: ")
if f == "1":
    os.system("ping google.com")
elif f == "2":
    os.system("tracert google.com")
elif f == "3":
    os.system("netstat -an")
elif f == "4":
    os.system("ipconfig /all")
elif f == "5":
    os.system("exit")
else:
    print("Такой команды нет!")
    time.sleep(2)
    os.system("exit")
