s = '1aba23'
def validarSimbolo(string):  # Solo etiquetas
    primerChar = string[0]
    print(primerChar)
    if primerChar.isdigit() == False and len(string) < 10 and string.endswith(':') == False:
        return True
    else:
        return False


if __name__ == '__main__':
    print(validarSimbolo(s))
