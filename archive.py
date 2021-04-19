def read():
        numbers = []
        with open('./archivos/numbers.txt', 'r', encoding="utf-8") as f:
            for line in f:
                numbers.append(int(line))
            print(numbers)

def write():
    names = ['Andres', 'Julian', 'Juan', 'Oscar', 'Santiago', 'Alex']
    with open('./archivos/name.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')



def run1():
    write()

def run():
    read()

if __name__ == '__main__':

    run()
    run1()

