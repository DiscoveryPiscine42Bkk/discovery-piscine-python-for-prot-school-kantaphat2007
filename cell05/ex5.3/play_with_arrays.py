#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_numbers = {num + 2 for num in numbers if num > 5}

print(numbers)
print(new_numbers)