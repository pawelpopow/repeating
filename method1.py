class MyList:
    def __init__(self, np1, np20, np21, np22):
        self.list = [np1, [np20, np21, np22]]  # zbudowanie listy
        self.np1 = np1
        self.np2 = 2
        self.np22 = 3

    def mod_lista(self):  # żadnych dodatkowych argumentów!
        # return str(self.list[0]) + "_" + str(self.list[1][0])
        # return str(self.list[0]) + "_" + str(self.list[1][1])
        # return str(self.list[0]) + "_" + str(self.list[1][2])
        # return str(self.list[0]) + "  " + str(self.list[1][0])
        # return str(self.list[0]) + "  " + str(self.list[1][1])
        # return str(self.list[0]) + "  " + str(self.list[1][2])
        # return str(self.list[0]) + "," + str(self.list[1][0])
        # return str(self.list[0]) + "," + str(self.list[1][1])
        return str(self.list[0]) + "," + str(self.list[1][2])


if __name__ == '__main__':
    lst = MyList("slowo1", "slowo2", "slowo3", "słowo4")
    print(lst.mod_lista())
