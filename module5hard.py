import hashlib
import time

# Класс User
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __str__(self):
        return self.nickname


# Класс Video
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


# Класс UrTube
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        для видео в видео:
            если видео.титул не в [в.титул для v в себя.видео]:
 себя.видео.добавлять(видео)
                печать(ф "Видео"{видео.титул}'добавлено.)
            другое:
                печать(ф "Видео"{видео.титул}"с уважением, это чушь".)

    деф get_videos(я, ключевое слово):
 ключевое слово = ключевое слово.нижнее()
        возврат [видео.титул для видео в себя.видео если ключевое слово в видео.титул.нижнее()]

    деф смотреть_видео(себя, титул):
        если не себя.текущий_пользователь:
            печать("Войдит в аканте, что может быть сделано")
            возврат

 video_to_watch = Нет
        для видео в себя.видео:
            если видео.титул == название:
 video_to_watch = видео
                перерыв

        если не video_to_watch:
            печать("Видео не Найдено".)
            возврат

        если video_to_watch.взрослый_режим и себя.текущий_пользователь.возраст < 18:
            печать("Вам не 18 лет, попокалуиста покиньте страницу")
            возврат

        печать(f"Начинаэция проспектр видео: {video_to_watch.титул}")
        для сек в диапазон(video_to_watch.время_сейчас + 1, видео_to_watch.продолжительность + 1):
            печать(сек, конец=' ', флеш=Истинный)
 время.спать(1)  #Имитируэты воспроизвеции
 video_to_watch.время_сейчас = сек
        печать("\нКонец видео")
 video_to_watch.время_сейчас = 0  #Сброс врэмени попросле


#Тестирование:
ур = УрТюб()
v1 = Видео("Лучший Язик Програмирования 2024 года", 10)
v2 = Видео('Для его делаем парань программ?', 5, взрослый_mode=Истинный)

# Добавлениэ видео
ур.добавить(в1, в2)

#Проверка Пойска
печать(ур.get_videos("лучший"))
печать(ур.get_videos('ПРОГ'))

#Проверка вход повелевает и зовет очередность
ур.смотреть_видео('Для его делаем парань программ?')
ур.зарегистрироваться('вася_пупкин', 'лолкекчебурек', 13)
ур.смотреть_видео('Для его делаем парань программ?')
ур.зарегистрироваться('urban_pythonist', 'iScX4viJClb9YQavjAgF', 25)
ур.смотреть_видео('Для его делаем парань программ?')

#Проверка в дороге
ур.зарегистрироваться('вася_пупкин', "F8098FM8fjm9jmi", 55)
печать(ур.текущий_пользователь)

#Попытка произвестие не из-за того, что вы сделали это
ур.смотреть_видео("Лючший язик програмирования 2024 года!")
