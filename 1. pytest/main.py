def task1():
    sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
    sides = sorted(sides, reverse=True)
    smax = 0
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            for k in range(j + 1, len(sides)):
                a = sides[i]
                b = sides[j]
                c = sides[k]
                if a + b > c and a + c > b and b + c > a:
                    p = (a + b + c) / 2
                    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                    if s > smax:
                        smax = s
    print("Максимальная площадь треугольника", smax)
def task2():
    coffs={"a":0,"b":0,"c":0}
    print(coffs.keys())
    for x in coffs.keys():
        text="Введите коэффициент "+str(x)+" : "
        coffs[x]=int(input(text))
    D=coffs["b"]**2-4*coffs["a"]*coffs["c"]
    print(D)
    if D<0:
        print("Корней нет")
    elif D==0:
        print("1 Корень равный: ", -coffs["b"]/2*coffs["a"])
    else:
        print("2 Корня. \n1й равен: ",(-coffs["b"]+D**(0.5))/2*coffs["a"],"\n2й равен: ",(-coffs["b"]-D**(0.5))/2*coffs["a"])
var=0
while var!=1 and var!=2:
    var=int(input("Выберите задачу:\n1. Треугольники.\n2. Нахождение квадрат.корня\n"))
if var==1:
    task1()
else:
    task2()
#2