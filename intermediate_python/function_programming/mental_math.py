# # Original approach using a loop
# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#   squares.append(num ** 2)

# # Using a list comprehension to square each number
# squared_numbers = [num ** 2 for num in numbers]

# # Displaying the outcomes
# print('Original Numbers:', numbers)
# print('Squared Numbers:', squared_numbers)

numbers = [57, 10, 82, 36, 89,
           46, 13, 23, 92, 48
           ]

numbers_pars = [num for num in numbers if num % 2 == 0]
print(numbers_pars)
