import ply.lex as lex
import re
import codecs
import os
import sys

resultado_lexema = []  # resultado del analisis
tokens = [
    'PSEUDOINSTRUCCIONES',
    'INSTRUCCIONES',
    'SIMBOLO',
    'REGISTRO',
    'CONSTANTE_NUMERICA_DECIMAL',
    'CONSTANTE_NUMERICA_HEXADECIMAL',
    'CONSTANTE_NUMERICA_BINARIA',

    'DOS_PUNTOS_SEPARADOR',
    'COMILLAS_DOBLES_SEPARADOR',
    'COMILLAS_SIMPLES_SEPARADOR',
    'PARENTESIS_DERECHO_SEPARADOR',
    'PARENTESIS_IZQUIERDO_SEPARADOR',
    'CORCHETE_DERECHO_SEPARADOR',
    'COMENTARIO',

    'CORCHETE_IZQUIERDO_SEPARADOR',
    'TITULO_DEL_PROGRAMA',
]

pseudoinstrucciones = {

}

instrucciones = {
    'aaa': 'AAA',
    'movsb': 'MOVSB',
    'cld': 'CLD',
    'pushf': 'PUSHF',
    'daa': 'DAA',
    'stosb': 'STOSB',
    'dec': 'DEC',
    'int': 'INT',
    'div': 'DIV',
    'pop': 'POP',
    'adc': 'ADC',
    'les': 'LES',
    'shl': 'SHL',
    'add': 'ADD',
    'ja': 'JA',
    'jnc': 'JNC',
    'loopne': 'LOOPNE',
    'jnae': 'JNAE',
    'jz': 'JZ',
    'jle': 'JLE'
}

registros = {
    'ax': 'AX', 'ah': 'AH', 'al': 'AL',
    'bx': 'BX', 'bh': 'BH', 'bl': 'BL',
    'cx': 'CX', 'ch': 'CH', 'cl': 'CL',
    'dx': 'DX', 'dh': 'DH', 'dl': 'DL',
    'cs': 'CS', 'ds': 'DS', 'es': 'ES',
    'bp': 'BP', 'sp': 'SP', 'si': 'SI', 'di': 'DI'
}

registers = ['AX', 'AH', 'AL',
             'BX', 'BH', 'BL',
             'CX', 'CH', 'CL',
             'DX', 'DH', 'DL',
             'CS', 'DS', 'ES',
             'BP', 'SP', 'SI', 'DI'
             ]

instructions = ['AAA', 'MOVSB', 'CLD', 'PUSHF', 'DAA',
                'STOSB', 'DEC', 'INT', 'DIV', 'POP',
                'ADC', 'LES', 'SHL', 'ADD', 'JA',
                'JNC', 'LOOPNE', 'JNAE', 'JZ', 'JLE']

tokens = tokens + instructions + registers

t_ignore = '\t'
t_DOS_PUNTOS_SEPARADOR = r'\:'
t_COMILLAS_DOBLES_SEPARADOR = r'\"'
t_COMILLAS_SIMPLES_SEPARADOR = r'\''
t_PARENTESIS_DERECHO_SEPARADOR = r'\)'
t_PARENTESIS_IZQUIERDO_SEPARADOR = r'\('
t_CORCHETE_DERECHO_SEPARADOR = r'\]'
t_CORCHETE_IZQUIERDO_SEPARADOR = r'\['


# def t_PSEUDOINSTRUCCIONES(t):


def t_REGISTRO(t):
    r'[a-zA-Z]{2}'
    if t.value or t.value.upper() in registers:
        # .type = t.value
        return t


def t_INSTRUCCIONES(t):
    r'[a-zA-Z]*'
    if t.value or t.value.upper() in instructions:
        # t.type = t.value
        return t


def t_COMENTARIO(t):
    r'\;.*'
    return t


# def t_simbolo(t):

def t_CONSTANTE_NUMERICA_DECIMAL(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CONSTANTE_NUMERICA_HEXADECIMAL(t):
    r'[0-9A-Fa-f][0-9A-Fa-f]*'
    return t


# def t_constante_numerica_binaria(t):


def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                                    str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")


def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")


# directorio = 'D:\Mario\Documents\Ingeniería en Computación\Sexto Semestre\Ensambladores\Ensambladores2022A\ProyectoFinal\source'
# archivo = buscarFicheros(directorio)
# test = directorio+archivo

# fp = codecs.open(test, 'r', 'utf-8')
# cadena = fp.read()
# fp.close()

# analizador.input(cadena)

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    valor = []
    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        # estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type),
        # str(tok.value), str(tok.lexpos))
        estado = " {:16} Tipo ---> {:16}  ".format(str(tok.value), str(tok.type))
        # valor.append(tok.value)
        resultado_lexema.append(estado)

    return resultado_lexema


# instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)
