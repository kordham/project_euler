
#Method 1
def is_prime(integer):
    for i in range(2,integer+1):

        if(integer%i==0):
           if(i != integer):
               is_prime(integer/i);
               break;
           elif(i == integer):
               print(i)

is_prime(13195)


#Method 2
number = 600851475143;
MAX = 0;
for i in range(2,number+1):
    if(number%i==0):
        for j in range(2,i+1):
            if(i%j==0):
                if(i==j):
                    MAX = i;
                elif(i!=j):
                    break;
print(MAX)
