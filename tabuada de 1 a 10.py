# Aqui o codigo está pedindo para o usuario falar um numero.
tabuada=int(input("Tabuada do numero: "))

# o count in range vai fazer essa sequencia de 1 a 10.
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )

# o "%d" é um marcador de posição e serve para reservar um valor(inteiro) em um vetor.
# diferente do "%s" que mostra valores flutuantes também.