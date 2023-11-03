#class Vest:

#    def __init__(self, a):
#        self.__a = a

#    def printf(self, a):
#        print(self.a)

#    def set_a(self, a):
#        self.__a = 3

# y = Vest(1)
# y.printf()
# y.set_a(3)
# y.printf()

# class Figure:
#
#     def __init__(self, coords, width, color,):
#         self.coords = coords
#         self.width = width
#         self.color = color
#
#     def draw(self):
#         print(f'рисуем фигуру цветом {self.color} и шириной {self.width}')
#
# class Line(Figure):
#     def draw(self):
#         print(f'рисуем линию цветом {self.color} и шириной {self.width}')
#
# class Rect(Figure):
#
#     def __init__(self, coords, width, color, right):
#         super().__init__(coords, width, color)
#         self.right = right
#
#     def draw(self):
#         print(f'рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')
# class Ellips(Figure):
#
#     def draw(self):
#         print(f'рисуем линию эллипс {self.color} и шириной {self.width}')
#
#
# f = Figure([1,2,4,5,7,8], 2, 'black')
# f.draw()
# l = Line([1,1,5,6], 3, 'red')
# l.draw()
# e = Ellips([5,5,2,9], 4,'yellow')
# e.draw()
# r = Rect([1,8,6,2], 6,'blue', 'неправильный')
# r.draw()

# class Publication:
#
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display(self):
#         print(f'Название {self.title}')
#         print(f'Автор {self.author}')
#         print(f'Год {self.year}')
#
#
# class Book(Publication):
#
#     def __init__(self, title, author, year, isbn):
#         super().__init__(title, author, year)
#         self.isbn = isbn
#
#     def display(self):
#         super().display()
#         print(f'ISBN: {self.isbn}')
#
# class Magazine(Publication):
#
#     def __init__(self, title, author, year, issue_number):
#         super().__init__(title, author, year)
#         self.issue_number = issue_number
#
#     def display(self):
#         super().display()
#         print(f'Номер журнала: {self.issue_number}')
#
# def info(obj):
#     obj.display()
#
# p = Publication('Название1', 'Автор1', 2015)
#
# b = Book('Название2', 'Автор2', 2015,39486528765)
#
# m = Magazine('Название3', 'Автор3', 2019,36528765)
# list = []
# list.append(p)
# list.append(b)
# list.append(m)
#
# for i in list:
#     info(m)
#     print()



#1
# import random
# class MusicAlbum:
#
#     def __init__(self,title,artist,genre,release_year,tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
#                 Название: {self.title}
#                 Исполнитель: {self.artist}
#                 Год выпуска {self.release_year}
#                 Жанр: {self.genre}
#                 Список треков: {self.tracklist}
#                 ''')
#
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
# album4 = MusicAlbum('deutschland','Rammstein', 2019, 'Neue',
#                     ['s','d','a','f','t','h','j','y','b','d'])
# album4.get_info()
# print('Воспроизводится трек: ', album4.play_random_track())

#2
# class Student:
#     def __init__(self,name,age,grade,scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def info(self):
#         print('Имя', self.name)
#         print('Возраст', self.age)
#         print('Класс', self.grade)
#         print('Оценки', self.scores)
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())

#3
# class Recipe:
#
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print(f'Ингредиенты для {self.name}:')
#         for item in self.ingredients:
#             print('- ', item)
#
#
#     def cook(self):
#         print(f'Сегодня мы готовим {self.name}.'
#               f'Выполняем инструкцию по приготовлению блюда {self.name}...'
#               f'Блюдо {self.name} готово')
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()

#4
# class Publisher:
#
#     def __init__(self,name,location,publish):
#         self.name = name
#         self.location = location
#         self.publish = publish
#
#     def get_info(self):
#         print(f'Готовим {self.publish} к публикации в {self.name} ({self.location})')
#
#
# class BookPublisher(Publisher):
#
#     def __init__(self, publish, name, location, num_authors, num_pages):
#         super().__init__(name, location, publish)
#         self.num_authors = num_authors
#         self.num_pages = num_pages
#
#     def get_info(self):
#         print(f'Передаем рукопись {self.publish}, написанную автором {self.num_authors} в издательство {self.name} ({self.location})')
#
#
# class NewspaperPublisher(Publisher):
#
#     def __init__(self, name, location, num_authors, num_pages):
#         super().__init__(name, location)
#         self.num_authors = num_authors
#         self.num_pages = num_pages
#
#     def get_info(self):
#         print(f'Печатаем свежий номер со статьей {self.publish} на главной странице в издательстве {self.name} ({self.location})')
#
#
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")
#
# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")
#
# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")
#
