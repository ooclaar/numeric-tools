#!/usr/bin/python3.11 env
# Usage: python3 binary-to.py value [-b] [-o] [-H] [-v]
# Versão 1.0
# Autor: ooclaar 

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-O', '--output', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decimal', action='store_true')
    group.add_argument('-o', '--octal', action='store_true')
    group.add_argument('-H', '--hexa', action='store_true')

    # Variaveis Globais

    args = parser.parse_args()
    number = str(args.number)
    debug = args.debug
    output = args.output

    if args.decimal:
        
        # Escopo quando for decimal.

        bitstring = ""
        result = 0
        vposicao = 1

        for bit in number[::-1]:
            
            bitstring = str(bit)
            
            if bit=='1':
                result=result+vposicao
            elif bit!='0':
                result=1
                break
                
            vposicao=vposicao*2

        if result!=0:
            print("The value decimal is: " + str(result))
        else:
            print("The number is not binary.")
    
    # Verifica qual a opção escolhida e define os ajustes. 
    
    if args.octal:
        factor=3
    else:
        factor=4
    
    # Escopo de variáveis locais

    resultin = 0
    resultout = ""
    vposicao = 1
    bitstring = ""
    
    while (True):
        number = "0" + str(number)
        if ((len(number) % factor)==0):
            if debug:
                print("O número passado foi modificado para: {number}.")
            break

    for i in range(0, len(number), factor):
        
        part = str(number[::-1][i:i+factor])
        
        if debug:
            print("Parte: " + part)

        for bit in part:
            
            bitstring = str(bit)
            
            if debug:
                print("Valor do Bit: " + str(bitstring))
                print("Valor da Posição:" + str(vposicao))
            
            if bit=='1':
                resultin=int(resultin) + (int(vposicao) * int(bit))
            elif bit!='0':
                result=1
                break
                
            vposicao=vposicao*2

        if debug:
            print("Soma do Bloco: " + str(resultin))
            print("------------------------------------")

        if args.octal:         
            resultout = str(resultout) + str(resultin)
        else:
            
            # Troca valores para Hexadecimal quando superior a 10.

            if resultin == 10:
                resultin = "A"
            elif resultin == 11:
                resultin = "B"
            elif resultin == 12:
                resultin = "C"
            elif resultin == 13:
                resultin = "D"
            elif resultin == 14:
                resultin = "E"
            elif resultin == 15:
                resultin = "F"

            resultout = str(resultout) + str(resultin)

        resultin = 0
        vposicao = 1

    # Verifica os dados compilados e mostra o resultado. 

    if resultout!=0:
        if args.octal:
            if output:
                print(str(resultout)[::-1])
            else:
                print("The value octal is: " + str(resultout)[::-1])
        else:
            if output:
                print(str(resultout)[::-1])
            else:
                print("The value hexa is: " + str(resultout)[::-1])
    else:
        print("The number is not binary.")
    
if __name__ == "__main__":
    main()