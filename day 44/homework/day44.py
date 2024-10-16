def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():  
            count += 1
    return count
