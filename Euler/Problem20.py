numeric_array = [0]*1000;
numeric_array[0] = 1;
for i in range(1,100):
    carry =0;
    for j in range(len(numeric_array)):
        numeric_array[j] = numeric_array[j]*i +carry;
        if numeric_array[j]>=10:
           carry = int(numeric_array[j]/10);
           numeric_array[j] = numeric_array[j]%10;
        else:
            carry = 0;
        print(numeric_array)
print(sum(numeric_array))

#This worked! although it might not have, since the numeric_array could be greater than 100.
