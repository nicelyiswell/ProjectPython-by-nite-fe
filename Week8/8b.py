def del_non_char(string):
    result=""
    for char in string:
        if char.isalpha():
            result+=char
    return result
    
user_input=input()
output = del_non_char(user_input)
print(output) 


