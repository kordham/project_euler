
sum = 0;
num_prev = 1;
num_curr = 2;

while(num_prev<=4000000):
    if num_prev%2 ==0:
        sum = sum + num_prev;
    temp = num_curr;
    num_curr = num_prev + num_curr;
    num_prev = temp;
print(sum)
