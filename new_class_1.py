class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def introduce_yourself(self):
        print(f"Jestem {self.name} {self.surname}. Mam {self.age} lat.")

    def birthday(self):
        age1 = self.age
        self.age += 1
        return age1


def main():
    # tworzymy dwa obiekty klasy Osoba
    people = People("Jan", "Nowak", 48)
    people = People("Adam", "Mickiewicz", 220)

    # wywołujemy metodę przedstaw_sie() na każdym z nich
    people.introduce_yourself()
    people.introduce_yourself()

    age_Adam = people.birthday()
    people.introduce_yourself()
    print(f"Wiek Adama sprzed urodzin: {age_Adam}")

    # odwołujemy się do pól, modyfikujemy je
    people.name = "Stanisław"
    people.surname = "Witkiewicz"
    people.age = 133

    people.introduce_yourself()


if __name__ == "__main__":
    main()