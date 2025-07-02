mixed_list = [42, 'apple', False, 'cat', 3.14]

for item in mixed_list:
    if isinstance(item, str):
        result.append(item.upper()[-3:])

print(result)
