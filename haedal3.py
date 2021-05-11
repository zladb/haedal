
import random

class person:

    def __init__(self, name, age, height, weight):
        self.name= name
        self.age = age
        self.height= height
        self.weight= weight

    def info(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print(f'키: {self.height}')
        print(f'몸무게: {self.weight}\n')

    def go_to_gym(self):
        numbers = range(1, 3) # 1~3의 정수
        diet=random.sample(numbers, 1)[0]
        self.weight -= diet
        print(f'{self.name} worked out.')
        print(f'-{diet}kg')
        print(f'Now, {self.name} is {self.weight}kg\n')


if __name__ == '__main__':
    person1 = person('유진', 21, 160, 53)
    person2 = person('정민', 24, 188, 88)

    person1.info()
    person1.go_to_gym()
    person2.go_to_gym()

