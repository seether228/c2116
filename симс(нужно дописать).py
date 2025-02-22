import random

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

    def get_home(self):
        self.home = House()

    def get_car(self):
        brands_of_car = ["Toyota", "Ford", "BMW"]  # Пример брендов машин
        self.car = Auto(random.choice(brands_of_car))

    def get_job(self):
        if self.car.drive():
            job_list = [Job("Engineer", 50, 5), Job("Doctor", 70, 3)]  # Пример профессий
            self.job = random.choice(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
                self.to_repair()
                return
        
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

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
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        
        self.days_indexes(day)
        
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()  # Добавлено, чтобы выполнить действие еды

nick = Human(name="Nick")
for day in range(1, 8):
    if not nick.live(day):
        break
