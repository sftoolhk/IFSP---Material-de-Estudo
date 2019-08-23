.data

x db ?
y db ?

.code
mov x, 165
mov y, 7
mov ch, 0
mov cl, x
mov al, x
sub1:
    cmp al, y
    jb fim
    sub al, y    
loop sub1
fim:
mov bx, ax 
mov ah, 0
mov al, x
sub ax, cx

HLT