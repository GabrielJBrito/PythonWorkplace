print ('-=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('-=' * 30)
valor = int(input('Informe o valor que deseja sacar: R$: '))
total = valor
ced = 50
totc = 0
while True:
    if total >= ced:
        total = total - ced
        totc = totc + 1
    else:
        if totc > 0:
            print(f'Total de {totc} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced=10
        elif ced ==10:
            ced = 1
        totc = 0
        if total == 0:
            break
print('-=' * 30)
              