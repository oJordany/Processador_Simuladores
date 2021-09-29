def funcaoUC(inst):
    from time import sleep
    global RDM, R0, ULA, REM, stop, cont
    c_op = inst[:4]
    op = inst[4:]
    if c_op == '0000':
        stop = True
        print('\033[1;30;41m<<< FIM DO PROGRAMA >>>')
    if c_op == '0001':
        REM = op
        RDM = MP[int(REM,2)]
        R0 = RDM
    if c_op == '0010':
        REM = op
        RDM = R0
        MP[int(REM,2)] = RDM
    if c_op == '0011':
        REM = op
        RDM = MP[int(REM, 2)]
        ULA = int(RDM, 2)
        R0 = f'{(bin(int(R0, 2) + ULA)[2:]):0>12}'
    if c_op == '0100':
        REM = op
        RDM = MP[int(REM, 2)]
        ULA = int(RDM, 2)
        R0 = f'{(bin(int(R0, 2) - ULA)[2:]):0>12}'
    if c_op == '0101':
        if int(R0, 2) == 0:
            cont = int(op, 2)
    if c_op == '0110':
        if int(R0, 2) > 0:
            cont = int(op, 2)
    if c_op == '0111':
        if int(R0, 2) < 0:
            cont = int(op, 2)
    if c_op == '1000':
        cont = int(op, 2)
    if c_op == '1001':
        REM = op
        entrada = int(input('\033[1;34;40mInsira um número:\033[m '))
        MP[int(REM, 2)] = f'{bin(entrada)[2:]:0>12}'
    if c_op == '1010':
        REM = op
        sleep(0.5)
        print(f'{int(MP[int(REM, 2)], 2)} → {MP[int(REM, 2)]}')
    cicloCI()


def cicloCI():
    global cont, CI, REM, RDM, RI, UC, stop
    while True:
        if stop == True:
            break
        CI = f'{str(bin(cont)[2:]):0>8}'
        REM = CI
        cont += 1
        RDM = MP[int(REM, 2)]
        RI = RDM
        funcaoUC(RI)


#Programa principal
cont = CI = REM = RDM = RI = UC = R0 = ULA = None
stop = False
cont = 0
MP = list()
for c in range(0,256):
    MP.append(None)
MP[int('00000000', 2)] = '100110110110'
MP[int('00000001', 2)] = '101010110101'
MP[int('00000010', 2)] = '000110110110'
MP[int('00000011', 2)] = '010010110101'
MP[int('00000100', 2)] = '010100001001'
MP[int('00000101', 2)] = '000110110101'
MP[int('00000110', 2)] = '001110110100'
MP[int('00000111', 2)] = '001010110101'
MP[int('00001000', 2)] = '100000000001'
MP[int('00001001', 2)] = '000000000000'
MP[int('10110100', 2)] = '000000000001'
MP[int('10110101', 2)] = '000000000001'
cicloCI()
