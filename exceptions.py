def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        if num < 0:
            raise Exception('Only positive numbers only')
        print(divisors(num))
        print("Terminó mi programa")

    except ValueError:
        print("only positive numbers can be processed")
    except Exception:
        print('Number can be negative')


if __name__ == '__main__':
    run()
