# Dada uma lista de números inteiros não-negativos, organize-os de modo que formem o maior número e devolva-o.
#
# Como o resultado pode ser muito grande, é preciso devolver uma string em vez de um número inteiro.
#
# ### Exemplo 1
#
# ```
# Input: nums = [10,2]
# Output: "210"
# ```
#
# ### Exemplo 2
#
# ```
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# ```


def bonus(nums):
    # Escreva seu código aqui
    nums = [3,30,34,5,9]
    x = 0
    y=str()
    for i in nums:
        x+=1
        if int(i) >=10:
            nums.insert(x,(float(i/10)))
            nums.remove(i)
    x = 0
    lista = sorted(nums, reverse = True)
    for i in lista:
        x+=1
        if type(i) == float:
            lista.update(x,(int(i*10)))
    x = 0
    for i in lista:
        x+=1
        if type(i) == float:
            lista.update(i,(int(i))
        print(lista)
    for i in lista:
        y= y+str(i)
    print(lista,y)


if __name__ == '__main__':
    print(bonus([3, 30, 34, 5, 9]))
