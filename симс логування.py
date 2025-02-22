import random
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Job:
    def __init__(self, job_name, salary, gladness_less):
        self.job = job_name
        self.salary = salary
        self.gladness_less = gladness_less

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.fuel = 100
        self.strength = 100

    def drive(self):
        if self.fuel > 0 and self.strength > 0:
            self.fuel -= 10
            return True
        return False

class House:
    def __init__(self):
        self.food = 50
        self.mess = 0

class City:
    def __init__(self, city_list):
        self.city_list = city_list
        self.current_city = random.choice(city_list)  # случайно выбираем текущий город

    def change_city(self):
        self.current_city = random.choice(self.city_list)  # изменяем город на случайный

    def get_current_city(self):
        return self.current_city

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, city_list=["Kiev", "Warsaw", "Paris"]):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.city = City(city_list)  # Создаем объект City с переданным списком городов

        logging.info(f"{self.name} created with initial money: {self.money}, gladness: {self.gladness}, satiety: {self.satiety}")

    def get_home(self):
        self.home = House()
        logging.info(f"{self.name} settled in a new house.")

    def get_car(self):
        brands_of_car = ["Toyota", "Ford", "BMW"]  # Пример брендов машин
        self.car = Auto(random.choice(brands_of_car))
        logging.info(f"{self.name} bought a car: {self.car.brand}")

    def get_job(self):
        if self.car.drive():
            job_list = [Job("Engineer", 50, 5), Job("Doctor", 70, 3)]  # Пример профессий
            self.job = random.choice(job_list)
            logging.info(f"{self.name} got a job as {self.job.job} with salary {self.job.salary}")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            logging.info(f"{self.name} ate food. Satiety: {self.satiety}, Food left: {self.home.food}")

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
            logging.info(f"{self.name} worked and earned {self.job.salary}. Money: {self.money}, Gladness: {self.gladness}, Satiety: {self.satiety}")
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
                self.to_repair()
                return
        
        if manage == "fuel":
            logging.info(f"{self.name} bought fuel.")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            logging.info(f"{self.name} bought food.")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            logging.info(f"{self.name} bought delicacies.")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logging.info(f"{self.name} is chilling. Gladness: {self.gladness}, Mess: {self.home.mess}")

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logging.info(f"{self.name} cleaned the house. Mess: {self.home.mess}, Gladness: {self.gladness}")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logging.info(f"{self.name} repaired the car. Strength: {self.car.strength}, Money: {self.money}")

    def days_indexes(self, day):
        day_str = f" Today the {day} of {self.name}'s life "
        print(f"{day_str:=^50}")
        human_indexes = f"{self.name}'s indexes"
        print(f"{human_indexes:^50}")
        print(f"Current City – {self.city.get_current_city()}")  # Вывод текущего города
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            logging.warning(f"{self.name} is in depression...")
            return False
        if self.satiety < 0:
            logging.warning(f"{self.name} is dead...")
            return False
        if self.money < -500:
            logging.warning(f"{self.name} is bankrupt...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        
        if self.home is None:
            logging.info(f"{self.name} settled in the house")
            self.get_home()
        
        if self.car is None:
            self.get_car()
        
        if self.job is None:
            self.get_job()
        
        self.days_indexes(day)
        
        if self.satiety < 20:
            logging.info(f"{self.name} is going to eat")
            self.eat()  # Добавлено, чтобы выполнить действие еды

nick = Human(name="Nick")
for day in range(1, 8):
    if not nick.live(day):
        break
