import turtle

def turtle_sqd(n):
    i = 4
    if n < 4:
        return 1
    
    else:

        while i >= 0:
            turtle.fd(n)
            turtle.rt(90)
            i = i - 1
        turtle.up()
        turtle.rt(45)
        turtle.fd(7)
        turtle.rt(-45)
        turtle.down()
        return turtle_sqd(n - 10)


if __name__ == '__main__':

    n = 200

    turtle_sqd(n)