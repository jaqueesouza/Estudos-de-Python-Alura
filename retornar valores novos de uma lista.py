# lista de numeros, sendo o 3 o numero que quero usar para mudar a lista
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
qualitativo = 3

# o "map" ajuda a dar uma função para cada elemento da lista e retorna outro map com o resultado
# a "lambda" permite a criação de funções sem precisar dar nome a elas
# eles juntos funcionam ''''''assim map(<lambda function>, <iterador>)''''''''
# o x diz dos numeros da lista = aos mesmos vezes o qualitativo (3) escolhido a cima e a lista
# atualizei para mostrar os numeros em formato de lista como os antigos valores
# print da nova lista 
lista_atualizada = map(lambda  x: x * qualitativo, lista)
lista_atualizada = list(lista_atualizada)
print(lista_atualizada)