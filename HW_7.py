import pickle
import openpyxl as openpyxl


"""Task 1
У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст складається з  міток часу і репліки яка була сказана в той момент часу.
Причому репліка знаходиться в наступному рядку після мітки часу.
Результатом виконнання завдання повинно бути:
1. словник елементами якого буде пара ключ:значення де ключ - мітка часу, значення - репліка в даний момент часу
2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі субтитри повинні мати вигляд простого тексту.
Це означає що окрім видалення міток часу, вам потрібно видалити переноси рядків
"""


dict = {}
with open("sub.txt") as file:
    content = file.readlines()
    for line in range(len(content)):
        content[line] = content[line].replace('\n', '')
    dict = {content[line]: content[line + 1] for line in range(0, len(content), 2)}
    print(dict)  # 1
    del content[0:len(content):2]
    print(content)  # 2

    

""" Task 2
в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і 
знайдіть середнє арифметичне чисел що знаходяться в списку"""


with open("task2", "rb") as file:
    list_1 = pickle.load(file)
    arithmetic_mean = sum(list_1) / len(list_1)
    print(arithmetic_mean)



"""Task 3
Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку), напишіть контекстний менеджер для роботи з ексель.
Даний менеджер повинен бути аналогом методу open()"""


class Create_Excel:
    def __init__(self, name):
        self.file_obj = openpyxl.load_workbook(name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with Create_Excel('task3.xlsx') as file:
    file.active['A1'].value = "HW 7"
    file.active['B1'].value = "is in process"
    file.save("task3.xlsx")
    print(file.active['A1'].value, file.active['B1'].value)
