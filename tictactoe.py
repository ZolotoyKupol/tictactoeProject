field = [['-'] * 3 for _ in range (3)]
count = 0

def win(f,user):
    f_list=[]
    print(f)
    for l in f:
        f_list+=l
    print(f_list)
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False


def show_field(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])

def user_input(f):
    while True:
        place = input("Write your coordinates in field: ").split()
        if len(place) != 2:
            print('Write two coordinates!')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Write numbers!')
            continue
        x = int(place[0])
        y = int(place[1])
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('You are out of range!')
            continue
        if field[x][y] != '-':
            print('The cage is occupied!')
            continue
        break
    return x, y

while True:
    if count == 9:
        print("It's draw")
        break
    if count % 2 == 0:
        user = "X"
    else:
        user = "O"
    show_field(field)
    x, y = user_input(field)
    field[x][y] = user
    if win(field, user):
        print(f" {user} is winner!!!")
        show_field(field)
        break
    count += 1
