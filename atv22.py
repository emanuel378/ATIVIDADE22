# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.

soma = 0
while True:
    n = int(input("Digite um numero"))
    
    
    if n ==0:
        break
    soma += n
print(soma)