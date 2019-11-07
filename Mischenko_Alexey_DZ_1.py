#1)Переменные
a = int(input('Введите число '))
print(a)


#2)Время в секундах
time = int(input ('Введите время в секундах '))

hour = time // 3600
time = time % 3600
min = time // 60
sec = time % 60

print('%02d:%02d:%02d' % (hour, min, sec,))

#3)Сумма чисел
n = input('Введите число ')
n2 = n + n
n3 = n + n + n
n = int(n)
n2 = int(n2)
n3 = int(n3)
y = n + n2 + n3
print(y)

#4)Максимальное число

n = int(input('Введите числа: '))
m = n%10
n = n//10

while n > 0:
    if n%10 > m:
        m = n%10
    n = n//10
print('Максимальное число', m)


#5)Выручка

n = int(input('Введите выручку '))
m = int(input('Введите издержки '))
a = n - m #прибыль
z = (f'{(a * 100 / n):.2f}') #рентабельность
while True:
    if n < m:
        print('У Вас убыток', a)
        break
    else:
        print('Прибыль ', a)
        print('Рентабельность', z, '%')

    p = int(input('Введите количество сотрудников '))
    d = (f'{(a / p):.2f}')
    print ('Прибыль на 1 сотрудника', d)
    break

#6)Спортсмен

a = int(input('Введите km в 1 день '))
b = int(input('Необходимо пробежать не менее km '))
i = 1
while a < b:
    a *= 1.1
    print(i + 1, 'день - ', (f'{(a):.2f}'), 'km')
    i += 1
print('Ответ: на ',(i), 'день спортсмен пробежит не менее', (b), 'km')

