def palindrome(string):
    string = string.lower()
    reversed_string = string[::-1]

    if string == reversed_string:
        return True
    else:
        return False
    
string = input()
if palindrome(string):
  print(True)
else:
  print(False)
