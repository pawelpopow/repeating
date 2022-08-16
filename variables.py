class Variables:
    def __init__(self):
        self.public = 10
        self._protected = 20
        self.__private1 = 30
        self.__private_double = self.__private1 * 2  # jest zależność między zmiennymi

    def download_private2(self):
        return self.__private_double

    def download_private1(self):
        return self.__private1

    def change_private1(self, new_value):  # zmieniamy dwie waratości
        self.__private1 = new_value
        self.__private_double = self.__private1 * 2


if __name__ == '__main__':
    zm = Variables()
    print(zm)
