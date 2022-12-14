# Você recebe uma lista de nomes, e uma lista de alturas que consiste de números inteiros positivos distintos.
# Ambas as listas são de comprimento `n`.
#
# Para cada índice `i`, `nomes[i]` e `alturas[i]` denotam o nome e a altura da i-ésima pessoa.
#
# Retorne os nomes ordenados em ordem decrescente pelas alturas das pessoas.
#
# ### Exemplo 1
#
# ```
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# ```
#
# ### Exemplo 2
#
# ```
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# ```

def q1(names, heights):
    dicionario = {}
    y = []
    for i in range(0,len(names)):
        dicionario[heights[i]] = names[i]

    heights2 = sorted(heights)
    heights2 = list(reversed(heights2))

    for i in heights2:
        y.append(dicionario[i])
    return y



if __name__ == '__main__':
    print(q1(["Mary", "John", "Emma"], [180, 165, 170]))
