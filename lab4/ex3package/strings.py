def reverse_string(string):
    return string[::-1]

def count_vowels(string):
    vowels = ['a','e','i','o','u','y','а','е','ё','о','у','ы','э','ю','я']
    return sum(1 for char in string.lower() if char in vowels)