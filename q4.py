# Os numerais romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M.
#
# | Símbolo | Valor |
# |---------|-------|
# | I       | 1     |
# | V       | 5     |
# | X       | 10    |
# | L       | 50    |
# | C       | 100   |
# | D       | 500   |
# | M       | 1000  |
#
# Por exemplo, 2 é escrito como II em algarismo romano, apenas dois juntos. 12 está escrito como XII,
# que é simplesmente X + II. O número 27 está escrito como XXVII, que é XX + V + II.
#
# Os numerais romanos são geralmente escritos da esquerda para a direita, do maior para a menor. Entretanto, o numeral
# para quatro não é IIII. Ao invés disso, o número quatro é escrito como IV. Porque o um está antes dos cinco,
# subtraindo-o, fazendo quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Há seis casos em que a
# subtração é utilizada:
#
# * I pode ser colocado antes de V (5) e X (10) para fazer 4 e 9.
# * X pode ser colocado antes de L (50) e C (100) para fazer 40 e 90.
# * C pode ser colocado antes de D (500) e M (1000) para fazer 400 e 900.
#
# Dado um numeral romano, converta-o para um número inteiro.

def q4(numeral):
    # Escreva seu código aqui
    numeral = 'MCMXCIV' #1994
    valores = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    lista = []
    soma = 0
    def valor(aa):
        for k, v in valores.items():
            if aa == k:
                return v
    for i in numeral:
        lista.append(i)
    for n in lista:
            soma = soma+valor(n)
    for n in lista:
        if n == "I" and n+1 == "V":
            soma = soma-1
        elif n == "I" and n+1 == "X":
            soma = soma-1
        elif n == "X" and n+1 == "L":
            soma = soma-10 
        elif n == "X" and n+1 == "C":
            soma = soma-10    
        elif n == "C" and n+1 == "D":
            soma = soma-100
        elif n == "C" and n+1 == "M":
            soma = soma-100
    print(soma)



if __name__ == '__main__':
    print(q4('MCMXCIV'))  # 1994
