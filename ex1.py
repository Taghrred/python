def taghreed(hrs,rate):
    if hrs>40.0:
        p = rate * 40.0
        p = p+(1.5*rate*(hrs-40))
    else:
        p = rate*hrs
    return p
hrs = float(input("enter worked hours:"))
rate = float(input("enter pay rate per hour: "))
print(taghreed(hrs,rate)) 
