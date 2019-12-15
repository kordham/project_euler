
#Method 1
def is_prime(integer):
    for i in range(2,integer+1):

        if(integer%i==0):
           if(i != integer):
               is_prime(int(integer/i));
               break;
           elif(i == integer):
               print(i)

is_prime(600851475143)
