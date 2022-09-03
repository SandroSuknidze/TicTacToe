
print(f'''---------
|       |
|       |
|       |
---------''')

Matrix = [[" " for x in range(3)] for y in range(3)]
c = "X"


def fun(Matrix):
    if Matrix[0][0] == Matrix[0][1] == Matrix[0][2] != " ":
        print(f'{"".join(Matrix[0][0])} wins')
        return 0
    elif Matrix[1][0] == Matrix[1][1] == Matrix[1][2] != " ":
        print(f'{"".join(Matrix[1][0])} wins')
        return 0
    elif Matrix[2][0] == Matrix[2][1] == Matrix[2][2] != " ":
        print(f'{"".join(Matrix[2][0])} wins')
        return 0
    elif Matrix[0][0] == Matrix[1][0] == Matrix[2][0] != " ":
        print(f'{"".join(Matrix[0][0])} wins')
        return 0
    elif Matrix[0][1] == Matrix[1][1] == Matrix[2][1] != " ":
        print(f'{"".join(Matrix[0][1])} wins')
        return 0
    elif Matrix[0][2] == Matrix[1][2] == Matrix[2][2] != " ":
        print(f'{"".join(Matrix[0][2])} wins')
        return 0
    elif Matrix[0][0] == Matrix[1][1] == Matrix[2][2] != " ":
        print(f'{"".join(Matrix[0][0])} wins')
        return 0
    elif Matrix[0][2] == Matrix[1][1] == Matrix[2][0] != " ":
        print(f'{"".join(Matrix[0][2])} wins')
        return 0
    elif Matrix[0][0] != " " and Matrix[1][0] != " " and Matrix[2][0] != " " and Matrix[0][1] != " "\
            and Matrix[1][1] != " " and Matrix[2][1] != " " and Matrix[0][2] != " " and Matrix[1][2] != " " and Matrix[2][2] != " ":
        print("Draw")
        return 0


def Tic(Matrix, c):
    print(">", end=" ")


    while True:
        try:
            a, b = map(int, input().split())
            a -= 1
            b -= 1

            if 3 <= a or a < 0 or 3 <= b or b < 0:
                print("Coordinates should be from 1 to 3!")
                print(">", end=" ")
            elif Matrix[a][b] != " ":
                print("This cell is occupied! Choose another one!")
                print(">", end=" ")
            else:
                break
        except ValueError:
            print("You should enter numbers!")
            print(">", end=" ")




    Matrix[a][b] = c
    print(f'''---------
| {Matrix[0][0]} {Matrix[0][1]} {Matrix[0][2]} |
| {Matrix[1][0]} {Matrix[1][1]} {Matrix[1][2]} |
| {Matrix[2][0]} {Matrix[2][1]} {Matrix[2][2]} |
---------''')

    if c == "X":
        c = "O"
    else:
        c = "X"

    if fun(Matrix) == 0:
        quit()

    Tic(Matrix, c)



Tic(Matrix, c)










