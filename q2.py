# Você está subindo uma escada. São necessários `n` degraus para chegar ao topo.
#
# Você pode subir 1 ou 2 degraus de cada vez. De quantas formas distintas você pode escalar até o topo?
#
# ### Exemplo 1
#
# ```
# Input: n = 2
# Output: 2
# Explicação: Existem duas maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau
# 2. 2 degraus
# ```
#
# ### Exemplo 2
#
# ```
# Input: n = 3
# Output: 3
# Explanation: Existem três maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau + 1 degrau
# 2. 1 degrau + 2 degraus
# 3. 2 degraus + 1 degrau
# ```


def q2(n):
    # Escreva seu código aqui
    n1 = 0
    n2 = 1
    contador = 0
    lista = {'n':0}
    while contador < n:
        x = n1 + n2
        n1 = n2 
        n2 = x
        contador += 1
        lista.update({'n': x})
    for v in lista.values():
        return v


if __name__ == '__main__':
    print(q2(2))
