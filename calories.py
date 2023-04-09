from temperature import Temperature

class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10*self.weight + 6.5*self.height - self.temperature*10
        return result


# if __name__ == '__main__':
#     temperature = Temperature(country='uk', city='london').get()
#     calorie = Calorie(temperature=temperature, weight= 91, height=180, age=28)
#
#     print(calorie.calculate())


