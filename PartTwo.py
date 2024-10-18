tf = False
Utotal=0
while tf==False:
    Uval=int(input("please input your cash, 5,10,20,50 pence coins are accepted "))
    if(Uval==5 or Uval==10 or Uval==20 or Uval==50):
        Utotal+=Uval
        print("total due="+str(75-Utotal))
        if(Utotal>=75):
            tf=True
    else:
        print("invalid currency")
print("Your change is "+ str(Utotal-75)+"p")