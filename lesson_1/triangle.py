from math import cos, pi #импортируем из модуля math косинус и число pi
a = int(input('Введите длину одной стороны ')) #считываем значение и 
						#превращаем его в число
b = int(input('Введите длину второй стороны '))  #считываем значение и
                                                #превращаем его в число
d = int(input('Введите угол в градусах между этими сторонами '))  #считываем значение и
                                                #превращаем его в число
c = a ** 2 + b ** 2 - 2 * a * b * cos((d * pi) / 180) #находим третью сторону
print(c) #вывод ответа