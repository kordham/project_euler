def lin_search(list,item):
    for i in range(len(list)):
        if(list[i]==item):
            return False;

    return True;

def divisors(num,integer,list):
    for i in range(2,integer+1):

        if(integer%i==0):
           if(i != integer):
               if(lin_search(list,i)):
                   list.append(i);
               divisors(num,int(integer/i),list);

           elif(i == integer and i!=num):
               break;
           elif(i==num):
               list.append(num)
               return len(list);

number = 2;
i= 2;
while(divisors(number,number,[1])<30):
    number = int(i*(i+1)/2);
    i=i+1;
print(number)
