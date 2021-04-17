from functools import reduce

my_list = [1, 2, 3, 4, 5]
my_list2 = [2, 2, 2, 2, 2]

# Map
squares = list(map(lambda x: x**2, my_list))

print(squares)

# Filter 
odd = list(filter(lambda x: x % 2 != 0, my_list))
print(odd)

# Reduce
all_multiplied  = reduce(lambda a, b: a * b, my_list2)
print(all_multiplied)


#if __name__ == '__main__':
