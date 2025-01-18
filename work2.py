from collections import deque


def palindrome(value):
    normalized_string = ""
    for char in value:
        if char.isalnum():
            normalized_string += char.lower()
    
    char_deque = deque(normalized_string)

    while len(char_deque) > 1:
        first = char_deque.popleft()  
        last = char_deque.pop()      
        if first != last:            
            return f"Це не паліндром {value}"
    return f"Це паліндром {value}"  


print(palindrome("12345"))  
print(palindrome("123454321"))  
print(palindrome("andrii")) 
print(palindrome("Oppo")) 
