.data

x dw ?
y dw ?
.code
mov ax, 12
sub ax, 1
mov x, ax
mov cx, ax
sub cx, 1
pmenor:
    div cx
    mov ax, x
    cmp dx, 0
    je saime
    
loop pmenor
mov x, ax
mov ax, 12
add ax, 1
mov cx, ax
add cx, 1
pmaior:
    div cx
    mov ax, y
    cmp dx, 0
    je saima
    
loop pmaior
mov bx, ax
mov ax, x
hlt  
saime:
    sub ax, 1 
    mov x, ax
    mov cx, ax
    jmp pmenor
saima:
    add ax, 1
    mov y, ax
    mov cx, ax
    jmp pmaior 