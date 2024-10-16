def separate_even_odd(numbers):
    evens = []
    odds = []
    
    for num in numbers:
        if num % 2 == 0:
            evens.append(num) 
            odds.append(num)   
    
    return evens, odds
