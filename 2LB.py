import pandas as pd
import matplotlib as mb;
import sklearn as sk;
import random
import class1_

available_operation = ["Чтение", "Запись", "Модификация", "Передача прав"]
Objects = 3
Objects_files = ["CD-RW", "My_notes.txt", "Secret_file.csv"]
Users = ["Пользователь123", "Босс", "Владислав", "Станислав", "Мухаммад"]
safety_politics = class1_.relation_safety_politics(available_operation, Objects_files, Users)
A = []
A = safety_politics.identification()
safety_politics.EnterSystem(A)