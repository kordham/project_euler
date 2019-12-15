def is_palindrome(number):
    reverse = ""
    for i in range(len(str(number))):
        reverse = reverse + str(number)[len(str(number))-i-1];
    if reverse==str(number):
        return True;
    else:
        return False;

def find_max():
    MAX =0;
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            if(is_palindrome(i*j)):
                if(MAX<i*j):
                    MAX =i*j;
    return MAX;
print(find_max())
