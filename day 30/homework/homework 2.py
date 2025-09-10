numbers = set(range(1, 11))
even_numbers = {n for n in numbers if n % 2 == 0}
even_list = list(even_numbers)
print(even_list)