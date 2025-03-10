# Атрибуты классов — это переменные, определенные внутри класса, но вне любых методов.
# Эти атрибуты являются общими для всех экземпляров (объектов) этого класса.
# Они принадлежат самому классу, а не конкретному объекту.

# Атрибуты объектов — это переменные, которые принадлежат конкретному экземпляру класса.
# Они определяются внутри методов, обычно внутри метода __init__,
# который является конструктором класса.
from icecream import ic as print
class Car:
    wheels = 4  # атрибут класса

    def __init__(self, color, model):
        self.color = color  # атрибут объекта
        self.model = model  # атрибут объекта


def main():
    # Создаем два объекта класса Car
    car1 = Car('red', 'Toyota')
    car2 = Car('blue', 'Honda')

    # Доступ к атрибутам объекта
    print(f'Доступ к атрибуту объекта car1.color: {car1.color}')  # Output: red

    print(f'Доступ к атрибуту объекта car2.model: {car2.model}')  # Output: Honda

    # Доступ к атрибуту класса
    print(f'Доступ к атрибуту класса Сar.wheels: {Car.wheels}') # Output: 4
    print(car1.wheels)
    print(car2.wheels)
    Car.wheels = 6
    print(car1.wheels)
    print(car2.wheels)
    car1.color = 'black'
    print(car1.color)
    print(car2.color)

if __name__ == '__main__':
    main()
