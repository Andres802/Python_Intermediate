

def run():
    squares = []
    for i in range(1, 101):
        if i % 2 != 0:
            squares.append(i**2)

    print(squares)
def runn():
    squares = [i**2 for i in range(1, 101) if i % 2 != 0]
    print(squares)

def reto():
    squares = [i for i in range(1, 100) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squares)




if __name__ == '__main__':
    run()
    runn()
    reto()
