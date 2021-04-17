from math import sqrt

def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print(my_dict)


def run2():
    
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print (my_dict)


def reto2():
    squares = {i : sqrt(i) for i in range(1, 10)}
    print(squares)


def reto3():
    squares = {i : i**0.5 for i in range(1, 10)}
    print(squares)

if __name__ == '__main__':
    run()
    run2()
    reto2()
    reto3()
