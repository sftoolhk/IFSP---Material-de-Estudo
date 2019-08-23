.data

n dw ?
f dw ?

.code

mov n, 0
mov ax, 0
mov cx,n
cmp cx, 0
je fim
sub cx, 1
mov f, cx
fato:
    add ax, n
loop fato
mov n, ax
mov cx, f
sub cx, 1
mov f, cx
mov ax, 0
cmp cx, 1
jg fato
mov ax, n
HLT
fim:
    mov n, 1
    mov ax, n
    HLT



