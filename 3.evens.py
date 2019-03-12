# code simplified using DRY (Don't Repeat Yourself!), This is known as Pythonic code, or idiomatic Python.
def is_even(number):
     return number % 2 == 0
     
def even_number_of_evens2(numbers):
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)

# code written during test based driven coding
def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens_count = 0
    
    for number in numbers:
        if number % 2 == 0:
            evens_count += 1
            
    if evens_count == 0:
        return False
    else:
        return evens_count % 2 == 0
        
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"


print("All tests passed!")