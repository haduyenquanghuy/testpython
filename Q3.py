import re
countNumber = 0
countAlphabet = 0
value = str(input()) 
for g in value:         
    if re.match("^[0-9]",str(g)):  
        countNumber +=1             
    elif re.match("^[A-Za-z]",str(g)):  
        countAlphabet +=1          
print("Số lượng ký tự số là: ", countNumber) 
print("Số lượng ký tự là chữ là: ", countAlphabet)