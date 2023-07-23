def add_person(person):
    with open('example.txt', 'a', encoding='utf-8') as file:
        for word in person:
            file.write(word + '\n')
        file.write('\n')
    
   