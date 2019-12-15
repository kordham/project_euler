product = 1;
side = 20;
for i in range(side+1,side*2+1):
    product = product*i/((side*2+1)-i);

print(product)
