parentese = input("Digite os parênteses para efetuar a verificacao:")
x = 0
pilha = []
while x < len(parentese):
    if parentese[x] == "(":
        pilha.append("(")
    if parentese[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")