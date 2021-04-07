sales=float(input('enter the sles of the month:'))
if sales>=100000:
    basic=4000
    hra=basic*10/100
    da=basic*110/100
    conveyance=500
    incentive=sales*10/100
    bonus=1000
else :
    basic=4000
    hra=basic*10/100
    da=basic*110/100
    conveyance=500
    incentive=sales*4/100
    bonus=500
salary=basic+hra+da+bonus+conveyance+incentive
print('salary receipt by employee:',salary)
    
