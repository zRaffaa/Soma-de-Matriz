matriz = []
somaCol = 0
for li in range (0,3):
    linha = []

    for co in range(0,3):
        linha.append(int(input(f'Inf. Numero da lin={li} col={co}')))
        matriz.append(linha)

print ('-=' * 30)
print ()

for li in range (0,3):
    for co in range (0,3):
        print (f'[{matriz[li][co]:^3}]',end = '')
        somaCol += matriz[li][2]
    print (f'soma da coluna 3 => {somaCol}')       
        
                               
