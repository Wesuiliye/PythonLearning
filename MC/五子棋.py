import time

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# 棋盘矩阵
matrix = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]


# 清理区域
def Refresh():
    mc.setBlocks(0, 0, 0, 29, 15, 29, block.AIR.id)
    for i in range(30):
        for j in range(30):
            # mc.setBlock(i, 0, j, block.WOOL.id, matrix[i][j])
            mc.setBlock(i, 0, j, block.WOOL.id,4)


# 判断是否五子连接
def check(posX, posZ):
    # 八个方向实际就是四条正方向，四条反方向
    for k in range(5):
        # c1 正方向 c2 返方向
        # 第一步算到正方向上面
        c1 = 1
        c2 = 0

        # 正方向判断
        for x in range(0, 5):
            # 上 下
            if k == 1:
                # 依次往前面去判断
                if matrix[posX + x][posZ] == matrix[posX + x + 1][posZ]:
                    c1 += 1
                # 防止中间出现断层后还去判断
                else:
                    break
            # 右上 左下
            if k == 2:
                if matrix[posX + x][posZ + x] == matrix[posX + x + 1][posZ + x + 1]:
                    c1 += 1
                else:
                    break
            # 右 左
            if k == 3:
                if matrix[posX][posZ + x] == matrix[posX][posZ + x + 1]:
                    c1 += 1
                else:
                    break
            # 右下 左上
            if k == 4:
                if matrix[posX + x][posZ - x] == matrix[posX + x + 1][posZ - x - 1]:
                    c1 += 1
                else:
                    break
        # 反方向
        for y in range(0, 5):
            if k == 1:
                # 依次往前面去判断
                if matrix[posX - y][posZ] == matrix[posX - y - 1][posZ]:
                    c2 += 1
                # 防止中间出现断层后还去判断
                else:
                    break
            if k == 2:
                if matrix[posX - y][posZ - y] == matrix[posX - y - 1][posZ - y - 1]:
                    c2 += 1
                else:
                    break
            if k == 3:
                if matrix[posX ][posZ - y] == matrix[posX ][posZ - y - 1]:
                    c2 += 1
                else:
                    break
            if k == 4:
                if matrix[posX - y][posZ + y] == matrix[posX - y - 1][posZ + y + 1]:
                    c2 += 1
                else:
                    break
        if c1 + c2 >= 5:
            return True


mc.postToChat("welcome to nille's world")
Refresh()

# 黑棋先下
player = 0
# 标志位，表示一轮游戏一轮结束
flag = False

while True:
    # 获得击打事件
    events = mc.events.pollBlockHits()

    for e in events:
        # 击打事件在棋盘里面
        if e.pos.x >= 0 and e.pos.x <= 29 and e.pos.z >= 0 and e.pos.z <= 29 and e.pos.y == 0:
            # 改变方块的颜色
            # 判断击打事件在黄色羊毛上才生效
            if player == 0 and matrix[e.pos.x][e.pos.z] == 4:

                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.WOOL.id, 15)
                # 更改数字里面的值
                matrix[e.pos.x][e.pos.z] = 15
                if check(e.pos.x, e.pos.z):
                    mc.postToChat("black win!")
                    flag = True
                # 白棋随后
                player = 1

            elif player == 1 and matrix[e.pos.x][e.pos.z] == 4:
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.WOOL.id, 0)
                matrix[e.pos.x][e.pos.z] = 0
                if check(e.pos.x, e.pos.z):
                    mc.postToChat("white win!")
                    flag = True
                player = 0
        else:
            mc.postToChat("OUT OF RANGE")

        if flag:
            mc.postToChat("The game restarts after ten seconds")
            for i in range(11):
                mc.postToChat(f'countdown:{10-i}')
                time.sleep(1)
            flag =False
            Refresh()
