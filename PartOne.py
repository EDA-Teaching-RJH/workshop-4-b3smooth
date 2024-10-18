Ustring= input("Please input a Camel Case variable name ")
SUstring=""
for i in Ustring:
    if(i.isupper()== True):
        temp= str(i.lower())
        SUstring+=("_"+temp)
    else:
        SUstring+=i
print(SUstring)
