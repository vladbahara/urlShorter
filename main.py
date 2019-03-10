import random as r  # Импортируем стандартный Random как r

while True: # Создаём цикл приложения чтобы не включать его постоянно 

    def urlShorter(url): # Создаём функцию urlShorter для обработки URL

        chars = [] # Создаём пустой массив для дальнейшего использования

        for x in range(4): # Создаём цикл генерации уникального адреса на 4 итерации (в итоге адрес состоит из 8 знаков)

            oneChar = chr(r.randint(97, 122))   # Создаём переменную oneChar и записываем в неё сгенерированые буквы
            oneNum = chr(r.randint(48, 57))     # То же самое только с цыфрами

            chars.append(oneNum)    # Добавляем в массив chars наши переменные
            chars.append(oneChar)   # с буквами и цыфрами, и перемешиваем их 
            r.shuffle(chars)        # с помощью shuffle

        chars = ''.join(chars) # Обьединяем элементы массива в строку
        url = '|\n| Ваша ссылка : \tpyli.com/' + str(chars) # Формируем сокращенный адрес и передаём его в переменную url

        return url # Возвращаем наш сформированный адрес

    print('+------------------------------------------------------------------+')
    url = input('|\n| Введите ссылку для сокращения : ') # Ждём и передаём ввод пользователя в переменную url
    
    print(urlShorter(url)) # Обрабатываем введённый адрес и возвращаем пользователю сокращенный
    print('|\n+------------------------------------------------------------------+')

linkFile = open('links.txt', 'w')