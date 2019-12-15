numeric_array = [0]*330;
numeric_array[0] = 1;
for i in range(1000 ):
    carry =0;
    for j in range(len(numeric_array)):
        numeric_array[j] = numeric_array[j]*2 +carry;
        if numeric_array[j]>=10:
           carry = int(numeric_array[j]/10);
           numeric_array[j] = numeric_array[j]%10;
        else:
            carry = 0;
print(sum(numeric_array))
