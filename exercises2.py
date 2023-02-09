def remove_vowels(string):
    vowels = "aeiou"
    new_string = ""
    for i in string:
        if i not in vowels:
            new_string += i
    return sorted(new_string)


print(remove_vowels("hello world"))
