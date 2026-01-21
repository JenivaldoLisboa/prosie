import math
import data

faraday = 96500

def mols(i,t):
    #Converte valores de corrente em número de mols de elétrons.
    return (i * t) / faraday

def corrente(n,nox,t):
    return (n*nox*faraday) / t

def tempo(n,nox,i):
    return (n*nox*faraday) / i

def massa(n,nox,MM):
    return (n/nox) * MM

def massa_mol(m,MM):
    return m/MM

def resposta_corrosao01 (n,MM,nox):
    print(f'\nNúmero de mols de elétrons envolvidos: {n} mol(s)')
    print(f'Massa molar: {MM} g/mol')
    print(f'Número de oxidação: {nox}')
    print(f'\nVariação de massa: {massa(n,nox,MM)} g')

def resposta_nmols(dm):
    print(f'\nNúmero de mols:')
    print(f' - Alumínio: {massa_mol(dm,27)} mol(s)')
    print(f' - Ferro: {massa_mol(dm,56)} mol(s)')
    print(f' - Zinco: {massa_mol(dm,65)} mol(s)')

def lista_especies():
    print()
    i = 1
    while i != (len(data.especies_quimicas) + 1):
        print(f'[{i}] {data.especies_quimicas[i]['especie']}')
        i += 1
    print()


def eletro_cations():
    print(f'\nEscolha o cátion:')
    print()
    x = 1
    while x != (len(data.cations) + 1):
        print(f'[{x}] {data.cations[x]['especie']}')
        x += 1
    print()

def eletro_anions():
    print(f'\nEscolha o ânion:')
    y = 1
    while y != (len(data.anions) + 1):
        print(f'[{y}] {data.anions[y]['especie']}')
        y += 1
    print()

def resposta_tabelacom2(x,y):
    print('--------------------------------------------')
    print('Potencial do ânodo','\t','Potencial do cátodo')
    print('--------------------------------------------')
    print(f'{x:>10,.2f} V {y:>22,.2f} V')

def resposta_tabelacom3(x,y,z):
    print('-----------------------------------------------------------------------')
    print('Potencial do ânodo','\t','Potencial do cátodo','\t','Diferença de potencial')
    print('-----------------------------------------------------------------------')
    print(f'{x:>10,.2f} V {y:>22,.2f} V {z:>20,.2f} V')

def start():
    print('Escolha o módulo que será iniciado:')
    print(f'\n  [1] Básico')
    print(f'  [2] Avançado\n')
    print()
    a = 0
    while a < 1 or a > 2:
        a = int(input('Digite um número: '))

    #Inicia o módulo básico.
    if a == 1:
        print(f'\nEscolha a simulação que deseja iniciar:')
        print(f'\n  [1] Pilha') #Determina a voltagem de uma pilha a partir da escolha das substâncias participantes.
        print('  [2] Eletrólise') #Apresenta os módulos ígnea e aquosa e determina o potencial e as espécies envolvidas no processo.
        print(f'  [3] Variação de massa\n') #Realiza cálculos simples de perda de massa para um determinado material escolhido - inserir opção comparativa.
        mod1 = 0
        while mod1 < 1 or mod1 > 3:
            mod1 = int(input('Digite um número: '))

    #Inicia o módulo básico para cálculo do potencial de uma pilha.
        if mod1 == 1:
            print(f'\nEscolha o ânodo:')
            print(' - A espécie que sofre oxidação.')
            lista_especies()
            anodo = 0
            while anodo < 1 or anodo > 9:
                anodo = int(input('Digite um número: '))
            print(f'\nEscolha o cátodo:')
            print(' - A espécie que sofre redução.')
            lista_especies()
            catodo = 0
            while catodo < 1 or catodo > 9:
                catodo = int(input('Digite um número: '))
            pcat = float(data.especies_quimicas[catodo]['potencial'])
            pand = float(data.especies_quimicas[anodo]['potencial'])
            potencial = pcat - pand
            if potencial < 0:
                print(f'\nPotencial: {potencial:.2f} V, tratando-se de um processo não espontâneo (eletrólise).')
            else:
                resposta_tabelacom3(pand,pcat,potencial)

    #Inicia o módulo básico de eletrólise.
        if mod1 == 2:
            print(f'\nEscolha o tipo de eletrólise.')
            print(f'\n  [1] Ígnea')
            print(f'  [2] Aquosa\n')
            eletro01 = 0
            while eletro01 < 1 or eletro01 > 2:
                eletro01 = int(input('Digite um número: '))
            print()

    #Realiza os cálculos para eletrólise ígnea.
            if eletro01 == 1:
                print(f'\nEscolha o ânodo:')
                print(' - A espécie que sofre oxidação.')
                lista_especies()
                anodo = 0
                while anodo < 1 or anodo > 9:
                    anodo = int(input('Digite um número: '))
                print(f'\nEscolha o cátodo:')
                print(' - A espécie que sofre redução.')
                lista_especies()
                catodo = 0
                while catodo < 1 or catodo > 9:
                    catodo = int(input('Digite um número: '))
                print()
                pcat = float(data.especies_quimicas[catodo]['potencial'])
                pand = float(data.especies_quimicas[anodo]['potencial'])
                potencial = pcat - pand
                if potencial > 0:
                    resposta_tabelacom2(pand,pcat)
                    print(f'\n Potencial: {potencial:.2f} V, indicando tratar-se de um processo espontâneo (pilha).')
                else:
                    resposta_tabelacom3(pand,pcat,potencial)

    #Realiza os cálculos para eletrólise aquosa.
            if eletro01 == 2:
                eletro_cations()
                cation = 0
                while cation < 1 or cation > 9:
                    cation = int(input('Digite um número: '))
                eletro_anions()
                anion = 0
                while anion < 1 or anion > 5:
                    anion = int(input('Digite um número: '))
                if 1 < cation < 8 and 1 < anion < 4:
                    print(f'\nCom base nas espécies selecionadas o ânion e cátion que irão descarregar durante a eletrólise serão aqueles indicados por você, seguem os dados do processo eletroquímico:\n')
                    potencial = float(data.cations[cation]['potencial']) - float(data.anions[anion]['potencial'])                
                    if potencial > 0:
                        resposta_tabelacom2(float(data.anions[anion]['potencial']),data.cations[cation]['potencial'])
                        print(f'\nO valor do potencial resultou em {potencial:.2f} V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha.')
                    else:
                        resposta_tabelacom3(float(data.anions[anion]['potencial']),float(data.cations[cation]['potencial']),potencial)
                if cation >= 8 and 1 < anion < 4:
                    print(f'\nCom base nas espécies selecionadas apenas o ânion que você indicou irá descarregar, enquanto o cátion que participará da reação será o H+ (neste caso haverá a autoionização da água), seguem os dados do processo eletroquímico:\n')
                    pot_cation = 0.00
                    potencial = pot_cation - float(data.anions[anion]['potencial'])
                    if potencial > 0:
                        resposta_tabelacom2(float(data.anions[anion]['potencial']),pot_cation)
                        print(f'\nPotencial: {potencial:.2f} V, indicando que trata-se de um processo espontâneo (pilha).')
                    else:
                        resposta_tabelacom3(float(data.anions[anion]['potencial']),pot_cation,potencial)
                if 1 < cation < 8 and anion >= 4:
                    print(f'\nCom base nas espécies selecionadas apenas o cátion que você indicou irá descarregar, enquanto o ânion que participará da reação será o OH-(neste caso haverá a autoionização da água), seguem os dados do processo eletroquímico:\n')
                    pot_anion = 0.40
                    potencial = data.cations[cation]['potencial'] - pot_anion
                    if potencial > 0:
                        resposta_tabelacom2(pot_anion,data.cations[cation]['potencial'])
                        print(f'\nO valor do potencial resultou em {potencial:.2f} V, indicando que neste sentido o processo é espontâneo e, consequentemente, representa uma pilha.')
                    else:
                        resposta_tabelacom3(pot_anion,data.cations[cation]['potencial'],potencial)
                if cation >=8 and anion >=4:
                    pot_cation = 0.00
                    pot_anion = 0.40
                    potencial = pot_cation - pot_anion
                    print(f'\nNenhuma das espécies selecionadas irá descarregar durante a eletrólise, havendo a participação apenas dos íons H+ (cátion) e OH- (ânion) (neste caso não necessita representar a dissociação do sal), seguem os dados do processo eletroquímico:\n')
                    resposta_tabelacom3(pot_anion,pot_cation,potencial)

    #Inicia o módulo para testes de variação de massa.
        if mod1 == 3:
            print(f'\nEscolha o tipo de teste:\n')
            print('  [1] Simples')
            print('  [2] Comparativo\n')
            corrosao = 0
            while corrosao < 1 or corrosao > 2:
                corrosao = int(input('Digite um número: '))
            
    #Inicia o cálculo da variação de massa em um determinado metal sob as condições de corrente elétrica (A) e tempo (s) estipulados.
            if corrosao == 1:
                print('Avaliação da variação de massa de um metal durante um processo eletrolítico.')
                print()
                print('Escolha o metal a ser utilizado na simulação:')
                print()
                for w in data.metais:
                    print(f'{[w]} {data.metais[w]['especie']}')
                print()
                metal = 0
                while metal < 1 or metal > 4:
                    metal = int(input('Digite um número: '))
                print()
                print('Determine o tempo e a corrente elétrica aplicada ao sistema.')
                print()
                i = int(input('Corrente elétrica (A): '))
                t = int(input('Tempo (s): '))
                n = mols(i,t)
                resposta_corrosao01(n,data.metais[metal]['MM'],data.metais[metal]['nox'])

    #Permite realizar comparações de variação de massa, corrente elétrica e tempo em um processo de corrosão.
            if corrosao == 2:
                print('Defina a variável de comparação:')
                print()
                print('  [1] Metal') #Compara a variação de massa para diferentes metais.
                print('  [2] Corrente elétrica') #Compara a corrente elétrica relacionada a uma variação de massa em diferentes metais em um tempo determinado.
                print('  [3] Tempo') #Compara o tempo necessário para que haja uma variação de massa em diferentes metais para um dado valor de corrente elétrica.
                print()
                variavel = 0
                while variavel < 1 or variavel > 3:
                    variavel = int(input('Digite um número: '))
                if variavel == 1:
                    i = int(input('Corrente elétrica (A): '))
                    t = int(input('Tempo (s): '))
                    n = mols(i,t)
                    print()
                    print(f'Número de mols de elétrons envolvidos: {n:.2f} mol(s)')
                    print('Variação de massa:')
                    print()
                    for x in data.metais:
                        print(f'{data.metais[x]['especie']}\t==> {massa(n,data.metais[x]['nox'],data.metais[x]['MM']):.5f} g')

                if variavel == 2:
                    dm = float(input('Variação de massa (g): '))
                    t = int(input('Tempo (s): '))
                    resposta_nmols(dm)
                    print('Corrente elétrica:')
                    for x in data.metais:
                        print(f'{data.metais[x]['especie']}\t==> {corrente(massa_mol(dm,data.metais[x]['MM']),data.metais[x]['nox'],t):.5f} A')

                if variavel == 3:
                    dm = float(input('Variação de massa: '))
                    i = int(input('Corrente elétrica (A): '))
                    resposta_nmols(dm)
                    print('Tempo:')
                    for x in data.metais:
                        print(f'{data.metais[x]['especie']}\t==> {corrente(massa_mol(dm,data.metais[x]['MM']),data.metais[x]['nox'],i):.5f} s')

    #Inicia o módulo avançado.   
    if a == 2:
        print()
        print('Escolha a simulação que deseja iniciar:')
        print('  [1] Pilha')
        print()
        mod2 = 0
        while mod2 != 1:
            mod2 = int(input('Digite um número: '))
        print()
        if mod2 == 1:
            print()
            print('Escolha o ânodo:')
            lista_especies()
            anodo = 0
            while anodo < 1 or anodo > 9:
                anodo = int(input('Digite um número: '))
            print()
            print('Escolha o cátodo:')
            lista_especies()
            catodo = 0
            while catodo < 1 or catodo > 9:
                catodo = int(input('Digite um número: '))
            print()
            potencial_pad = float(data.especies_quimicas[catodo]['potencial']) - float(data.especies_quimicas[anodo]['potencial'])
            if potencial_pad < 0:
                print(f'Potencial padrão: {potencial_pad:.5f} V | O processo não corresponde a uma pilha.')
            else:
                temp = int(input('Temperatura (K): '))
                conc_anodo = float(input('Concentração molar do ânodo (mol/L): '))
                conc_catodo = float(input('Concentração molar do cátodo (mol/L): '))
                eano = int(data.especies_quimicas[anodo]['eletrons'])
                ecat = int(data.especies_quimicas[catodo]['eletrons'])
                if eano == 1 and ecat == 1:
                    neletro = 1
                    quociente = conc_anodo/conc_catodo
                if eano == 2 and ecat == 2:
                    neletro = 2
                    if anodo == 3:
                        quociente = (conc_anodo ** 2)/conc_catodo
                    if catodo == 3:
                        quociente = conc_anodo/(conc_catodo ** 2)
                    else:
                        quociente = conc_anodo/conc_catodo
                if eano == 1 and ecat == 2:
                    neletro = 2
                    if catodo == 3:
                        quociente = (conc_anodo ** 2)/(conc_catodo ** 2)
                    else:
                        quociente = (conc_anodo ** 2)/conc_catodo
                if eano == 2 and ecat == 1:
                    neletro = 2
                    if anodo == 3:
                        quociente = (conc_anodo ** 2)/(conc_catodo ** 2)
                    else:
                        quociente = conc_anodo/(conc_catodo ** 2)
                potencial = potencial_pad - ((8.31447 * temp)/(neletro * 96485.3))*math.log(quociente)
                print(' ')
                print('-----------------------------------------------------------------------------------')
                print('Potencial padrão','\t','Número de elétrons','\t','Quociente','\t','Potencial da pilha')
                print('-----------------------------------------------------------------------------------')
                print(f'{potencial_pad:>8,.2f} V {neletro:>20} mol(s) {quociente:>16,.2f} {potencial:>20,.2f} V')
    restart()

def restart():
    print(f'\nDeseja continuar usando o programa?\n')
    print(' [1] Sim;','\n','[2] Não.')
    reinicio = 0
    while reinicio < 1 or reinicio > 2:
        reinicio = int(input('Digite sua opção: '))
    if reinicio == 1:
        print('=====================================================================')
        print('/////////////////////////////////////////////////////////////////////')
        print('=====================================================================')
        start()
    else:
        print('=================================FIM=================================')

print()
print('██████╗░██████╗░░█████╗░░██████╗██╗███████╗')
print('██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██╔════╝')
print('██████╔╝██████╔╝██║░░██║╚█████╗░██║█████╗░░')
print('██╔═══╝░██╔══██╗██║░░██║░╚═══██╗██║██╔══╝░░')
print('██║░░░░░██║░░██║╚█████╔╝██████╔╝██║███████╗')
print('╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝╚══════╝')
print('PROGRAMA PARA CÁLCULOS DE PROCESSOS ELETROQUÍMICOS - v. 1.0')
#Versão 1.0
print('Produzido por: Jenivaldo Lisboa')
print()

start()