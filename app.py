# Validador de CPF

import re

def primeiroDigito(cpf):
    i=10
    cpf=re.sub(r'[^0-9]',"",cpf)
    soma=0
    cpf=list(cpf)
    del cpf[-1:-2]
    ints = [eval(x) for x in cpf]
    for numero in ints:
        soma+=(numero*i)
        i-=1
    mult=soma*10
    mult=mult%11
    if mult<9:
        return numero
    else:
        return 0

def segundoDigito(cpf):
    i=11
    soma=0
    cpf=re.sub(r'[^0-9]',"",cpf)
    cpf=list(cpf)
    del cpf[-1]
    ints = [eval(x) for x in cpf]
    for numero in ints:
        soma+=(numero*i)
        i-=1
    mult=soma*10
    mult=mult%11
    if mult<9:
        return numero
    else:
        return 0

def verificarCpf(cpf):
    cpf=re.sub(r'[^0-9]',"",cpf)
    ints = [eval(x) for x in cpf]
    if primeiroDigito(cpf) == ints[-1] and segundoDigito(cpf)==ints[-2]:
        print("CPF válido")
    else:
        print("CPF inválido")
        

verificarCpf("119.527.246-43")