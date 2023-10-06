# Задание 1
a = int(input('Введите число от 1 до 100 '))
if a >= 101:
    print('Ошибка')
elif a <= 0:
    print('Ошибка')
elif a % 3 == 0 and a % 5 == 0:
    print('Fizz Buzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
elif a % 3 != 0 and a % 5 != 0:
    print(a)
# Задание 2
a = int(input('Введите число '))
b = int(input('Выберите степень в которую возвести число от 0 до 7 '))
if b == 0:
    print(a**0)
elif b == 1:
    print(a**1)
elif b == 2:
    print(a**2)
elif b == 3:
    print(a**3)
elif b == 4:
    print(a**4)
elif b == 5:
    print(a**5)
elif b == 6:
    print(a**6)
elif b == 7:
    print(a**7)
# Задание 4
a = int(input('Введите продажи 1 менеджера: '))
b = int(input('Введите продажи 2 менеджера: '))
c = int(input('Введите продажи 3 менеджера: '))
oklad = 200
if a>1000:
   zp1 = oklad+a*0.08
else:
   if a <500:
       zp1 = oklad+a*0.03
   else:
       zp1 = oklad+a*0.05
if b>1000:
   zp2 = oklad+b*0.08
else:
   if b <500:
       zp2 = oklad+b*0.03
   else:
       zp2 = oklad+b*0.05
if c>1000:
   zp3 = oklad+c*0.08
else:
   if c <500:
       zp3 = oklad+c*0.03
   else:
       zp3 = oklad+c*0.05
if zp1 > zp2 and zp1 > zp3:
   print('Лучший по продажам - 1 менеджер!')
   zp1 += 200
if zp2 > zp1 and zp2 > zp3:
   print('Лучший по продажам - 2 менеджер!')
   zp2 += 200
if zp3 > zp1 and zp3 > zp2:
   print('Лучший по продажам - 3 менеджер!')
   zp3 +=200
print('Зарплата 1 менеджера ',zp1)
print('Зарплата 2 менеджера ',zp2)
print('Зарплата 3 менеджера ',zp3)