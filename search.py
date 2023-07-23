def search_person(person):
    with open('example.txt', 'r', encoding='utf-8') as file:
       text = file.read().splitlines()
       for i in text:
            if person in text:
                print(person)
            break

# Подумать, как вывести списком/кортежем
