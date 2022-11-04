class Biblioteka(): #Создание библиотеки с переменными: отдел, кол-во книг, кол-во газет, кол-во журналов
    def __init__(self, chapter, book_in, newspapers_in, journal_in):
        if  isinstance(chapter, str):
            self.chapter = chapter
        else:                                   
            raise InvalidNameError()        
        self.book_in = book_in
        self.newspapers_in = newspapers_in
        self.journal_in = journal_in

    def nn(self): 
        self.__number_of_newspapers_in_chapter()
        self.__number_of_journal_in_chapter()
    def __number_of_newspapers_in_chapter(self): #кол-во газет в отделе с приватным доступом
        print("В отделе " + self.chapter + " находится " + str(self.newspapers_in) + " газет.")
    def __number_of_journal_in_chapter(self): #кол-во журналов в отделе с приватным доступом
        print("В отделе " + self.chapter + " находится " + str(self.journal_in) + " журналов.")

#Класс для вывода ошибки
class InvalidNameError(Exception):
    def __str__(self):
        return f"Неправильное название! Название состоит из цифр, а должно из букв! Проверка"

#Начало проверки на ошибки
try:
    b1 = Biblioteka(8, 115, 22, 34)
    #b1.nn() 
    #b1.otdel()
except InvalidNameError as e:
    print(e)
#Конец проверки на ошибки
