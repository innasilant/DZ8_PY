def inp():
    mode = input ('Введите режим (импрот или экспорт): ')
    # print(mode)
    if mode == 'импорт':
        result = imp()
    else:
        result = info ()
    return result

def imp ():
    surname = input ('Введите фамилию: ')
    name = input ('Введите имя: ')
    fathername = input ('Введите отчество: ')
    phone = input ('Введите номер телефона: ')
    return surname, name, fathername, phone

def info ():
    inf = input ('Введите фамилию: ')
    return inf

    