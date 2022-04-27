data segment
    
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:

    mov ax, data
    mov ds, ax 
    
    MOV AX,15 
    AAA
    RET
    
    PUSHF
    
    MOV AL, 0Fh
    DAA
    RET
    
    ORG 100h
    LEA DI,a1
    MOV AL, 12h
    MOV CX,5
    
    REP STOBS
    
    ORG 100h
    CLD
    LEA SI,a1
    LEA DI,a2
    MOV CX,5
    REP MOVSB
    
    RET
    
    MOV AL,255
    DEC AL
    RET
    
    MOV AH,0Fh
    MOV AL,'A'
    INT 10h
    RET
    
    MOV AX,203
    MOV BL,4
    DIV BL
    RET
    
    MOV AX,1234h
    PUSH AX
    POP DX
    RET
    
    STC
    MOV AL,5
    ADC AL,1
    RET
    
    LES AX,m
    RET 
    
    MOV AL, 1110000b
    SHL AL, 1
    RET
    
    MOV AL,250
    CMP AL,5
    JA label1
    
    MOV AL,2
    ADD AL,3
    JNC label1 
    
    MOV AL,2
    MCP AL,5
    JNAE label1
    
    MOV AL,5
    CMP AL,5
    JZ label1
    
    MOV AL,-2
    CMP AL,5
    JLE label1
    
    MOV SI,0
    MOV CX,5
    label1:
    PUTC 'a'
    MOV AL,v[SI]
    INC SI
    CMP AL,7
    LOOPNE label1
    RET
       
ends

end start 
