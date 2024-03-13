import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()


# 在一个范围中输出对应方块材质到文件里面
def BlockRange(x1, z1, z2, y1, y2, flag):
    # 选出 一个正范围
    Z_Max = z1 if z1 > z2 else z2
    Z_Min = z1 if z1 < z2 else z2

    Y_Max = y1 if y1 > y2 else y2
    Y_Min = y1 if y1 < y2 else y2

    w = open("CSV/test.txt", 'w')

    # 左上角到右下角
    while Y_Max != Y_Min - 1:
        i = Y_Max
        j = Z_Max
        while j != Z_Min - 1:
            # x不动
            if flag == 1:
                Block = mc.getBlockWithData(x1, i, j)
            # z 不动
            else:
                Block = mc.getBlockWithData(j, i, x1)
            print(f'{Block.id}' + ',' + f'{Block.data}', end=' ')
            w.write(f'{Block.id}' + ',' + f'{Block.data}')
            w.write(' ')
            j -= 1
        Y_Max -= 1
        w.write('\n')
        print('')

    # for j in range(Z_Min ,Z_Max + 1):
    #     for i in range(Y_Min, Y_Max + 1):
    #         Block = mc.getBlockWithData(x1, i, j)
    #         print(f'{Block.id}' + ',' + f'{Block.data}', end=' ')
    #         # print(Block.id,Block.data,end='')
    #     print('')
    # with open("CSV/test.csv",'w') as w:
    #     w.write()


# 选定范围
def Range():
    posLB = posRT = None
    x1 = x2 = z1 = z2 = y1 = y2 = 0
    print('请选择第一个点')
    while True:
        # 获得击打事件
        events = mc.events.pollBlockHits()
        posLB = events
        if posLB != []:
            x1 = posLB[0].pos.x
            y1 = posLB[0].pos.y
            z1 = posLB[0].pos.z
            break
    print('请选择第二个点')
    while True:
        # 获得击打事件
        events = mc.events.pollBlockHits()
        posRT = events
        if posRT != []:
            x2 = posRT[0].pos.x
            y2 = posRT[0].pos.y
            z2 = posRT[0].pos.z
            break
    return [posLB, posRT, x1, x2, y1, y2, z1, z2]


# 扫描菜单，其中包括“选定左下角方块”“选定右上角方块”“开始扫描”以及“返回主菜单”
def scan():
    listScan = Range()
    print(listScan)
    # posLB和posRT，用来保存左下角方块的坐标和右上角方块的坐标
    posLB = listScan[0]
    posRT = listScan[1]
    x1 = listScan[2]
    x2 = listScan[3]
    y1 = listScan[4]
    y2 = listScan[5]
    z1 = listScan[6]
    z2 = listScan[7]

    # 判断是否同一平面
    # 同一 x 下：
    print(posLB[0])
    print(posRT[0])
    if x1 == x2:
        BlockRange(x1, z1, z2, y1, y2, 1)
        # print('x')
        return
    # 同一 z 下：
    if z1 == z2:
        if x1 == x2:
            return
        BlockRange(z1, x1, x2, y1, y2, 0)
        # print('z')
        return

    print('Not on the same plane, please try again!')


# 返回文件所对应的方块材质
def RetrunBlockID(X_Max, X_Min, Y_Max, Y_Min, Z_Max, Z_Min, flag):
    i = j = 0

    r = open("CSV/test.txt", 'r')
    lines = r.readlines()
    for line in lines:
        i += 1
        line = line.strip().split(' ')
        # 只需要记录一次就行
        if j == 0:
            for l in line:
                j += 1

    for y in range(0, i):
        line = lines[y].split()
        # 重置min
        s1 = Z_Min
        s2 = X_Min
        for x in range(0, j):
            L = line[x].split(',')[0]
            R = line[x].split(',')[1]
            # print(L,' ',R)
            if flag == 1:
                mc.setBlock(X_Min, Y_Max, s1, int(L), int(R))
                s1 += 1
            else:
                mc.setBlock(s2, Y_Max, Z_Min, int(L), int(R))
                s2 += 1

        Y_Max -= 1


# 复印菜单
def copy():
    listCopy = Range()
    # 判断 复印在哪一面
    x1 = listCopy[2]
    x2 = listCopy[3]
    z1 = listCopy[6]
    z2 = listCopy[7]

    y1 = listCopy[4]
    y2 = listCopy[5]

    # 选出 一个正范围
    Z_Max = z1 if z1 > z2 else z2
    Z_Min = z1 if z1 < z2 else z2

    Y_Max = y1 if y1 > y2 else y2
    Y_Min = y1 if y1 < y2 else y2

    X_Max = x1 if x1 > x2 else x2
    X_Min = x1 if x1 < x2 else x2

    # 如果 x1 = x2 说明放置这一面
    if x1 == x2:
        RetrunBlockID(X_Max, X_Min, Y_Max, Y_Min, Z_Max, Z_Min, 1)
    else:
        RetrunBlockID(X_Max, X_Min, Y_Max, Y_Min, Z_Max, Z_Min, 0)


# 显示主菜单，等待用户选择
def menu():
    while True:
        print("This is a menu")
        print("1.扫描菜单")
        print("2.复印菜单")
        buff = input("Please choose: ")
        if buff == "1":
            print("You select 1")
            scan()
        elif buff == "2":
            print("You select 2")
            copy()
        else:
            print("You Input error!!!")
        print("")


# while True:
#     scan()
while True:
    menu()
