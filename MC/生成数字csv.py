import time

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()


# 3*5区域清空
def cleanField(baseX, baseY, baseZ):
    mc.setBlocks(baseX, baseY, baseZ, baseX, baseY + 4, baseZ + 2, block.AIR.id)


def showScore(baseX, baseY, baseZ, num):
    # 3*5区域清空
    # cleanField(baseX, baseY, baseZ)

    time.sleep(1)

    if num >= 0 and num <= 9:
        # 打开相应文件
        Fname = "CSV/" + "num" + str(num)
        f = open(Fname, 'r')

        # 从左上往左下依次判断
        offsetY = 4
        offsetZ = 0

        # 读取所有行
        for line in f.readlines():
            # 去除前后空格，换行
            # 用逗号进行切割，返回列表
            data = line.strip().split(',')
            # print(data)

            # 是 1 就在相应位置放置方块，0则是空气
            for cell in data:
                # print(cell)
                # 注意判断的是字符
                if cell == "1":
                    mc.setBlock(baseX, baseY + offsetY, baseZ + offsetZ, block.WOOL.id, 4)
                else:
                    mc.setBlock(baseX, baseY + offsetY, baseZ + offsetZ, block.AIR.id)
                offsetZ += 1

            offsetY -= 1
            offsetZ = 0
        print(num)

        f.close()


time.sleep(1)
for i in range(0,10):
    showScore(0, 1, 0, i)
