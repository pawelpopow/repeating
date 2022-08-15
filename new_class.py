class People:
    def __init__(self, name, number, birtday):
        self.name = name
        self.number = number
        self.birtday = birtday


if __name__ == '__main__':
    people = People(name='Jan', number='656464905', birtday=2022 - 1970)
    print(people.name)
    print(people.number)
    print(people)
    print(people.birtday)
