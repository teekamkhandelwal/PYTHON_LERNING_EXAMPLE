def calculate_compound_interest(p,n,r):
    print('start balance\t','interest   ','endingbalance')
    total=0
    x=r/100
    tot=0
    for i in range (1,n+1):
        z_new=p*(1+x)**i-p
        z_old=p*(1+x)**(i-1)-p
        tot=tot+(z_new-z_old)
        if(i==1):
            print('{0:.2f}\t'.format(p),end=" ")
            print('{0:.2f}\t'.format(z_new-z_old),end=" ")
            print('{0:.2f}\t'.format(z_new+p))
        else:
            print('{0:.2f}\t'.format(p+z_old),end=" ")
            print('{0:.2f}\t'.format(z_new-z_old),end=" ")
            print('{0:.2f}\t'.format(z_new+p))
    print('total interest deposited :rs{0:.2f}'.format(tot))
p=int(input('enter the principal amount'))
r=int(input('enter the rate of the interest'))
n=int(input('enter number of year '))
calculate_compound_interest(p,n,r)

            
