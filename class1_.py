import random
import sys

class relation_safety_politics:
    def __init__(self, available_operation, Objects_files, Users):
        self.available_operation = available_operation  
        self.Objects_files = Objects_files   
        self.Users = Users

        rand_users_sprt = random.choice(self.available_operation)
        print (rand_users_sprt)

    def identification(self):
        for i in self.Objects_files:
            print(i)
        A = []
        N = len(self.Users)
        M = len(self.Objects_files)
        for i in range(N):
            A.append([0]*M)

        right_first = 0
        for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
            for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
                if right_first == i:
                    print(A[i][j], end = '  ')
                    A[0][j] = self.available_operation[0:4]
                else:
                    rand_num1 = random.randrange(1, 5)
                    rand_num2 = random.randrange(1, 100)
                    if (rand_num2 < 50):
                        A[i][j] = self.available_operation[0:rand_num1]
                        print(A[i][j], end = '  ')
                    else:
                        A[i][j] = ['']
                        print(A[i][j], end = '  ')
            print()                     # делаем переход на новую строку

        # Строка для вставки в начало
        new_row = self.Objects_files

        # Вставляем новую строку в начало
        A.insert(0, new_row)

        # Элементы для вставки в начало каждой строки
        new_column = self.Users

        # Вставляем новый элемент в начало каждой строки
        for i in range(len(A)):
            A[i].insert(0, new_column[i-1])
            
            A[0][0] = ''
        # Выводим измененный массив
        for row in A:
            print(row)
        for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
            for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
                    print(f'{str(A[i][j]):<40}', end='')
            print()                     # делаем переход на новую строку
        return A

    def EnterSystem(self, A = []):
        count_psb_acts = -1
        userId = ""
        index = -1
        index_cols = -1
        go_ = "Начать заново"
        while (go_ == "Начать заново"):
            userId = input("Введите идентификатор пользователя для получения доступа к системе:\n")
            print ("Вы ввели идентификатор " + userId + "\n")
            count = 0
            while not userId in self.Users:
                if count >= 3:
                    print("Вы трижды ввели неверный идентификатор. Программа будет остановлена")
                    sys.exit()
                
                print("Введенный идентификатор" +userId + "не существует"+"\n")
                print("Попробуйте заново")
                userId = input("Введите идентификатор пользователя для получения доступа к системе:\n")
                count = count + 1

            print("User: " + userId)
            print("Идентификация прошла успешно, добро пожаловать в систему")
            print("Перечень ваших прав:")
            for i in range (len(A)):
                if A[i][0] == userId:
                    index = i
                    break

            for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
                for j in range(len(A[i])-1):  # len(A[i]) - возвращает количество элементов в строке i
                    if i == index:
                        print(self.Objects_files[j+1]+":"+f'{str(A[i][j+1]):<40}')
                        if (str(A[i][j+1]) != ''):
                            count_psb_acts = count_psb_acts + 1
            Action = ""
            Action_object = ""
            Action_object_right = ""
            User_to_right = ""
            UserIDright=""
            index_to_right =""
            index_cols_to_rigth =""
            Action = input("Жду ваших указаний >")
            while not Action in self.available_operation:
                print("Введенная операция не соответствует ни одной из возможных")
                Action = input("Жду ваших указаний >")
                if Action == "Выход":
                    sys.exit()                         
                elif Action == "Далее":
                    break

            if Action == "Выход":
                print("Работа пользователя " + userId + " завершена. До свидания.")        
                sys.exit()
            if (Action != "Передача прав" and (Action == "Чтение" or Action == "Запись" or Action == "Модификация")):
                if (count_psb_acts > -1):
                        if (Action != "Выход" or Action_object != "Выход"):
                            while not Action in self.available_operation:
                                print("Введенная операция не соответствует ни одной из возможных")
                                Action = input("Жду ваших указаний >")
                                if Action == "Выход":
                                    sys.exit()                         
                                elif Action == "Далее":
                                    break
                            if Action_object != "Далее":
                                Action_object = input("Над каким объектом призводится операция?")

                            while not Action_object in self.Objects_files:    
                                print("Введенный объект не существует")
                                Action_object = input("Над каким объектом призводится операция?")
                                if Action_object == "Выход":
                                    sys.exit()
                                elif Action_object == "Далее":
                                    break

                            if Action == "Выход" or Action_object == "Выход":
                                print("Работа пользователя " + userId + " завершена. До свидания.")        
                                sys.exit()

                            for j in range (len(A[0])):
                                if A[0][j] == Action_object:
                                    index_cols = j
                        
                            if Action in A[index][index_cols]:
                                print("Операция над "+Action_object + " прошла успешно")
                            else:
                                print("Отказ в выполнении операции. У Вас нет прав для ее осуществления")
                        else:
                            print("Работа пользователя " + userId + " завершена. До свидания.")        
                            sys.exit()
                else:
                    print("Вы бесправны, к сожалению. Ожидайте передачи прав.")
                    print("Работа пользователя " + userId + " завершена. До свидания.")    
            else:
                for i in range (len(A)):
                    if A[i][0] == userId:
                        index = i
                        break
                Action_object = input("Право на какой объект передается?")
                if Action_object == "Выход":
                    print("Работа пользователя " + userId + " завершена. До свидания.")        
                    sys.exit()
                while not Action_object in self.Objects_files and Action_object != "Выход":    
                    print("Введенный объект не существует")
                    Action_object = input("Право на какой объект передается?")
                    if Action_object == "Выход":
                        sys.exit()
                    
                for j in range (len(A[0])):
                    if A[0][j] == Action_object:
                        index_cols = j

                Action_object_right = input("Какое право передается?")
                if Action_object_right == "Выход" or Action_object == "Выход":
                    print("Работа пользователя " + userId + " завершена. До свидания.")        
                    sys.exit()
                else:
                    while not Action_object_right in self.available_operation:    
                        print("Введенное право для передачи не существует. Введите корректное право.")
                        Action_object_right = input("Какое право передается?")
                        if Action_object_right == "Выход":
                            print("Работа пользователя" + userId + " завершена. До свидания.")
                            sys.exit()
                User_to_right = input("Какому пользователю передается право?")
                for i in range (len(A)):
                    if A[i][0] == User_to_right:
                        index_to_right = i
                        break
                if User_to_right == "Выход" or User_to_right == "Выход":
                    print("Работа пользователя " + userId + " завершена. До свидания.")        
                    sys.exit()
                else:
                    while not User_to_right in self.Users:    
                        print("Введенного пользователя для передачи права не существует. Введите корректный ID.")
                        User_to_right = input("Какому пользователю передается право?")
                        if User_to_right == "Выход":
                            print("Работа пользователя" + userId + " завершена. До свидания.")
                            sys.exit()
                    if Action_object_right in A[index][index_cols]:
                        (A[index][index_cols]).remove(Action_object_right)
                        if not Action_object_right in A[index_to_right][index_cols]:
                            if (Action_object_right == "Чтение"):
                                (A[index_to_right][index_cols]).insert(0, Action_object_right)
                            elif (Action_object_right == "Запись"):
                                (A[index_to_right][index_cols]).insert(1, Action_object_right)
                            elif (Action_object_right == "Модификация"):
                                (A[index_to_right][index_cols]).insert(2, Action_object_right)
                            elif (Action_object_right == "Модификация"):
                                (A[index_to_right][index_cols]).insert(3, Action_object_right)
                            elif (Action_object_right == "Передача прав"):
                                (A[index_to_right][index_cols]).insert(4, Action_object_right)
                        else:
                            print("Передаваемое право уже имеется у пользователя!")
                    else:
                        print("Отказ в выполнении операции. У Вас нет прав для ее осуществления или в принципе нет передаваемого права")
        

            right_first = 0 
            for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
                for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
                            print(A[i][j], end = '  ')
                print()                     # делаем переход на новую строку
            print("Хотите начать заново? Введите: Начать заново. Хотите выйти? Введите: Выход") 
            go_ = input()
