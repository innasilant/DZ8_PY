from user import inp, imp, info
from write import add_person
from search import search_person

def run():
    result = inp()
    # add_person(result)
    search_person(result)

    # как корректно написать, чтобы вызывалась или одна, или другая ф-ция
