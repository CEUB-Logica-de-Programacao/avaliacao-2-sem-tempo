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
    # Escreva seu código aqui
    dict = {}
    lista1 = []
    for i in range(0,len(names)):
        if names[i] in dict and x == None:
            dict[names[i]+'1'] = heights[i]
            x = i
        dict[names[i]] = heights[i]
    def aaa():
        dict1 = {}
        lista = []
        dict2 = sorted(dict.values(), reverse= True)
        for i in dict2:
            for k in dict.keys():
                if dict[k] == i:
                    dict1[k] = dict[k]
        for k in dict1.keys():
            lista.append(k)
        for i in range(0,len(names)):
            if names[i]+"1" in lista:
                lista.insert(x-2, names[i])
                lista.remove(names[i]+"1")
        return lista
    return aaa()


if __name__ == '__main__':
    print(q1(["Mary", "John", "Emma"], [180, 165, 170]))
