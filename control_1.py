
def rast(usk):
    def wrapper(v, v0, t):
        try:
            if t ==0:
                print("Время не может быть равно 0")

            a=usk(v,v0,t)

            s=(v*v-v0*v0)/(2*a)
            print(s)
            return s
        except ValueError:
            print("Ошибка")
    return wrapper

@rast

def usk(v, v0, t):
    a=(v-v0)/t
    print(a)
    return a

def main():

    v0=float(input("Введите начальную скорость"))
    v=float(input("Введите конечную скорость"))
    t=int(input("Введите время"))
    usk(v, v0, t)

main()




