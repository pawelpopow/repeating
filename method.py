class Writing:
    def __init__(self, np1, value):
        self.writing1 = np1
        self.number = value  # pomijamy sprawdzanie typów
        self.list = [1, 0, 2]


if __name__ == '__main__':
    obj = Writing("napis", 10)  # pomijamy argument self
    print(obj.writing1)
    print(obj.number)
    print(obj.list)