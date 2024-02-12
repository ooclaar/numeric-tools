#!/usr/bin/python3.11 env
# Usage: python3 binary-to.py value [-b] [-o] [-H] [-v]
# Versão 1.0
# Autor: ooclaar 

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decimal', action='store_true')
    group.add_argument('-o', '--octal', action='store_true')
    group.add_argument('-H', '--hexa', action='store_true')

    args = parser.parse_args()
    number = str(args.number)
    
    if args.decimal:
        
        result = 0
        vposicao = 1

        for bit in number[::-1]:
            if bit=='1':
                result=result+vposicao
            elif bit=='0':
                continue
            else:
                result=1
                break
            vposicao=vposicao*2
        if result!=0:
            print("The value decimal is: " + str(result))
        else:
            print("The number is not binary.")
    
    if args.octal:
        
        resultin = 0
        resultout = ""
        vposicao = 1
        bitstring = ""
        rest = 0
        diff = 0

        rest = len(number) % 3
        while (True):
            number = "0" + str(number)
            if ((len(number) % 3)==0):
                print("A string foi modificada para: " + str(number))
                break

        for i in range(0, len(number), 3):
            
            part = str(number[::-1][i:i+3])
            print("Parte: " + part)

            for bit in part:
                
                bitstring = str(bit)
                
                print("BIT: " + str(bitstring))
                print("VPO:" + str(vposicao))
                
                if bit=='1':
                    resultin=int(resultin) + (int(vposicao) * int(bit))
                elif bit!='0':
                    result=1
                    break
                    
                vposicao=vposicao*2

            print("Soma do Bloco: " + str(resultin))
            print("------------------------------------")
            
            vposicao = 1
            resultout = str(resultout) + str(resultin)
            resultin = 0

        if resultout!=0:
            print("The value octal is: " + str(resultout)[::-1])
        else:
            print("The number is not binary.")    
    
if __name__ == "__main__":
    main()