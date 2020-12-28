import re

def validaCnpjApenasNumeros(cnpj):
    if len(cnpj) == 14 and cnpj.isdigit():
        return True
    else:
        return False

def validaCnpj(cnpj):
    expr = re.compile('\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}')
    if expr.search(cnpj) or validaCnpjApenasNumeros(cnpj):
        return 'It is a valide CNPJ'
    else:
        return 'It is not a valide CNPJ'

def validaCnpj1(cnpj):
    aux = cnpj.split('-')
    digitoVerificador = aux[1]
    aux1 = aux[0]
    aux = aux1[:2] + aux1[3:6] + aux1[7:10] + aux1[11:16]
    aux1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    digito1 = 0
    digito2 = 0
    for elemento in range(0, 12, 1):
        soma += int(aux[elemento]) * aux1[elemento]
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    aux = aux + str(digito1)
    aux1 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for elemento in range(0, 13, 1):
        soma += int(aux[elemento]) * aux1[elemento]
    resto = 0
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    dv = str(digito1) + str(digito2)
    if digitoVerificador == dv:
        return 'CNPJ is valid'
    else:
        return 'CNPJ is not valid'

def checkAndComputeIntersectionTwoRectangles(x1,y1,width1,height1,x2,y2,width2,height2):
    K = int(x1)
    L = int(y1)
    M = int(width1) + 1
    N = int(height1) + 1

    P = int(x2)
    Q = int(y2)
    R = int(width2) + 1
    S = int(height2) + 1

    left = max(K, P)
    right = min(M, R)
    bottom = max(L, Q)
    top = min(N, S)

    if left < right and bottom < top:
        intersection = (right - left) * (top - bottom)
        return [True, intersection]
    else:
        return [False, 0]