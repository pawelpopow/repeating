def add_posfix(strg):
    # return str(strg) + '_postfix'
    # return str(strg) + '_next'
    return str(strg) + '_communication'


def mod_lista(lista):
    # return str(lista[0]) + "_" + str(lista[1][1])
    # return str(lista[0]) + " " + str(lista[1][1])
    return str(lista[0]) + "," + str(lista[1][1])


if __name__ == '__main__':
    add_posfix = add_posfix(11)
    print(add_posfix)
    # add_posfix = add_posfix("napis")
    # print(add_posfix)
    # add_posfix = add_posfix([1, 2, 3])
    # print(add_posfix)
    "###"
    lista = ["napis", ["jeden", "dwa"]]
    mod_lista = mod_lista(lista)
    print(mod_lista)
