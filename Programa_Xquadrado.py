def funcaoUC(inst):
    global RDM, R0, ULA, REM, stop, cont
    c_op = inst[:4]
    op = inst[4:]
    if c_op == '0000':
        print('\033[1;30;45mINSTRUÇÃO HLT')
        stop = True
        print('\033[1;30;41m<<< FIM DO PROGRAMA >>>')
    if c_op == '0001':
        print('\033[1;30;45mINSTRUÇÃO LDA')
        REM = op
        print(f'\033[mOp. = {op} ————————————————————> REM = {REM}')
        print(f'\033[mREM = {REM} ————————[BE]————————> MP')
        RDM = MP[int(REM,2)]
        print(f'\033[mMP[{REM}] = {MP[int(REM,2)]} ————————[BD]————————> RDM = {RDM}')
        R0 = RDM
        print(f'\033[mRDM = {RDM} ——————————————————> R0 = {R0}')
    if c_op == '0010':
        print('\033[1;30;45mINSTRUÇÃO STR')
        REM = op
        print(f'\033[mOp. = {op} ————————————————————> REM = {REM}')
        print(f'\033[mREM = {REM} ————————[BE]————————> MP')
        RDM = R0
        print(f'\033[mR0 = {R0} ——————————————————> RDM = {RDM}')
        MP[int(REM,2)] = RDM
        print(f'\033[mRDM = {RDM} ————————[BD]————————> MP[{REM}] = {MP[int(REM, 2)]}')
    if c_op == '0011':
        print('\033[1;30;45mINSTRUÇÃO ADD')
        REM = op
        print(f'\033[mOp. = {op} ————————————————————> REM = {REM}')
        print(f'\033[mREM = {REM} ————————[BE]————————> MP')
        RDM = MP[int(REM, 2)]
        print(f'\033[mMP[{REM}] = {MP[int(REM, 2)]} ————————[BD]————————> RDM = {RDM}')
        ULA = int(RDM, 2)
        print(f'\033[mRDM = {RDM} ————————————————————> ULA = {ULA}')
        R0 = f'{(bin(int(R0, 2) + ULA)[2:]):0>12}'
        print(f'\033[mULA + R0 ————————————————————> R0 = {R0}')
    if c_op == '0100':
        print('\033[1;30;45mINSTRUÇÃO SUB')
        REM = op
        print(f'\033[mOp. = {op} ————————————————————> REM = {REM}')
        print(f'\033[mREM = {REM} ————————[BE]————————> MP')
        RDM = MP[int(REM, 2)]
        print(f'\033[mMP[{REM}] = {MP[int(REM, 2)]} ————————[BD]————————> RDM = {RDM}')
        ULA = int(RDM, 2)
        print(f'\033[mRDM = {RDM} ————————————————————> ULA = {str(bin(ULA)[2:]):0>12}')
        if (int(R0, 2) - ULA) < 0:
            R0 = f'-{(bin(int(R0, 2) - ULA).replace("-0b", "")):0>12}'
        else:
            R0 = f'{(bin(int(R0, 2) - ULA).replace("0b", "")):0>12}'
        print(f'\033[mULA - R0 ————————————————————> R0 = {R0}')
    if c_op == '0101':
        print('\033[1;30;45mINSTRUÇÃO JZ')
        print('\033[mSE R0 = 0, ENTÃO CI ← Op.')
        print(f'\033[mR0 = {R0}')
        if int(R0, 2) == 0:
            cont = int(op, 2)
            print(f'\033[mOp. = {op} ————————————————————> CI = {str(bin(cont)[2:]):0>8}')
    if c_op == '0110':
        print('\033[1;30;45mINSTRUÇÃO JP')
        print('\033[mSE R0 > 0, ENTÃO CI ← Op.')
        print(f'\033[mR0 = {R0}')
        if int(R0, 2) > 0:
            cont = int(op, 2)
            print(f'\033[mOp. = {op} ————————————————————> CI = {str(bin(cont)[2:]):0>8}')
    if c_op == '0111':
        print('\033[1;30;45mINSTRUÇÃO JN')
        print('\033[mSE R0 < 0, ENTÃO CI ← Op.')
        print(f'\033[mR0 = {R0}')
        if int(R0, 2) < 0:
            cont = int(op, 2)
            print(f'\033[mOp. = {op} ————————————————————> CI = {str(bin(cont)[2:]):0>8}')
    if c_op == '1000':
        print('\033[1;30;45mINSTRUÇÃO JMP')
        print('\033[mCI ← Op.')
        cont = int(op, 2)
        print(f'\033[mOp. = {op} ————————————————————> CI = {str(bin(cont)[2:]):0>8}')
    if c_op == '1001':
        print('\033[1;30;45mINSTRUÇÃO GET')
        REM = op
        print(f'\033[mOp. = {op} ————————————————————> REM = {REM}')
        print(f'\033[mREM = {REM} ————————[BE]————————> MP')
        entrada = int(input('\033[1;34;40mInsira um número:\033[m '))
        MP[int(REM, 2)] = f'{bin(entrada)[2:]:0>12}'
        print(f'\033[mPorta de Entrada = {entrada} ————————[BD]—————————> MP[{REM}] = {MP[int(REM, 2)]}')
    if c_op == '1010':
        print('\033[1;30;45mINSTRUÇÃO PRT')
        REM = op
        print(f'\033[mOp. = {op} ——————————————————————> REM = {REM}')
        print(f'\033[mREM = {REM} ————————[BE]————————> MP')
        print(f'\033[mMP[{REM}] = {MP[int(REM, 2)]} ——————————[BD]————————> Porta de Saída = {MP[int(REM, 2)]}')
        print(f'\033[1;31;40mPRINT: {int(MP[int(REM, 2)], 2)} → {MP[int(REM, 2)]}')
    cicloCI()


def cicloCI():
    global cont, CI, REM, RDM, RI, UC, stop
    while True:
        if stop == True:
            break
        CI = f'{str(bin(cont)[2:]):0>8}'
        REM = CI
        print(f'\033[mCI = {CI} ————————————————————> REM = {REM}')
        cont += 1
        print(f'CI = {CI} ————————————————————> CI = {str(bin(cont)[2:]):0>8}')
        RDM = MP[int(REM, 2)]
        print(f'REM = {REM} ————————[BE]————————> MP')
        print(f'MP[{REM}] = {MP[int(REM, 2)]} ————————[BD]————————> RDM = {RDM}')
        RI = RDM
        print(f'RDM = {RDM} ————————————————————> RI = {RI}')
        funcaoUC(RI)


#Programa principal
cont = CI = REM = RDM = RI = UC = R0 = ULA = None
stop = False
cont = 0
MP = list()
for c in range(0,256):
    MP.append(None)
MP[int('00000000', 2)] = '100110110101'
MP[int('00000001', 2)] = '000110110101'
MP[int('00000010', 2)] = '001010110110'
MP[int('00000011', 2)] = '000110110110'
MP[int('00000100', 2)] = '010010110100'
MP[int('00000101', 2)] = '001010110110'
MP[int('00000110', 2)] = '011100001011'
MP[int('00000111', 2)] = '000110110101'
MP[int('00001000', 2)] = '001110110111'
MP[int('00001001', 2)] = '001010110111'
MP[int('00001010', 2)] = '100000000011'
MP[int('00001011', 2)] = '101010110111'
MP[int('00001100', 2)] = '000000000000'
MP[int('10110100', 2)] = '000000000001'
MP[int('10110111', 2)] = '000000000000'
cicloCI()
