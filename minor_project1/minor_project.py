cp=float(input('entter the cost of product'))
cgst=float(input('entter the % of cgst'))
sgst=float(input('entter the % of sgst'))
total=0
amount_cgst=((cgst/100)*cp)
amount_sgst=((sgst/100)*cp)
total=cp+amount_cgst+amount_sgst
print('toatal cost of product is:',total)
