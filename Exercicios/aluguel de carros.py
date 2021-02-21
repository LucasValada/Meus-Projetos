n1 = float(input("Quantos dias alugados? "))
n2 = float(input("Quantos KM rodados? "))
x = n1*60 + (n2*0.15)
print("o total a pagar é de R$:{:.2f} ".format(x))