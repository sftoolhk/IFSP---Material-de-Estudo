.data

x dw ?
z dw ?

.code
mov x, 12322
mov ax, x
mov cx, 10
div cx
mov z, ax
mov ax, dx
mul cx
mov bx, ax
mov ax, z
div cx
mov z, ax
add bx, dx
mov ax, bx
mul cx
mov bx, ax
mov ax, z
div cx
mov z, ax
add bx, dx
mov ax, bx
mul cx
mov bx, ax
mov ax, z
div cx
mov z, ax
add bx, dx
mov ax, bx
mul cx
add ax, z
sub ax, x
cmp ax, 0
jnz nao_palindromo
    mov ax, 1
    jmp fim
nao_palindromo:
    mov ax, 0
fim:
HLT
