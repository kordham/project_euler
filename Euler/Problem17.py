
stringly = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen",
            "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","onethousand","and"];

total = "";
for k in range(10):
    hundreds = "";
    if(k!=0):
        hundreds = stringly[-3]
    for i in range(20):
        ands = stringly[-1]
        if i ==0 or k==0:
            ands = ""
        total = total + stringly [k] + hundreds + ands + stringly[i];
    for i in range(20,28):
        for j in range(10):
            total = total +  stringly [k] + hundreds + ands + stringly[i]+ stringly [j];
total = total + stringly[-2]
print(len(total))
