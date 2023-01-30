# Python function that accepts a string and calculate the number of upper case letters and lower case letters

string=input("enter any statement : ")
lower,upper = 0,0
for i in string:
    if (i>='a'and i<='z'):
         
        # counting lower case
        lower=lower+1               
    if (i>='A'and i<='Z'):
         
        #counting upper case
        upper=upper+1
         
print('Lower case characters: ',lower)
print('Upper case characters: ',upper)