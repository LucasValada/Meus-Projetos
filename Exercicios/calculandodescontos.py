n1 = float(input("Qual o preço do produto?"))
x = n1-(n1 * 5 / 100)
print("O produto que custava R${:.2f}, na promoção está com desconto de 5%, vai custar R${:.2f} ".format(n1, x))

