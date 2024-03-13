import datetime
import time

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def showNum(baseX, baseY, baseZ, num):
    # 3*5区域清空
    # cleanField(baseX, baseY, baseZ)

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

preTime = ''

while True:
    timeNow = datetime.datetime.now()
    # 只有时间变化了才刷新
    if preTime != timeNow.minute:
        preTime = timeNow.minute
        # 如果小时十位上的数为0时，把它那片区域清空，便于识别
        if timeNow.hour//10 != 0:
            # 小时十位数
            showNum(0, 1, 0, timeNow.hour//10)
        else:
            mc.setBlocks(0,1,0,0,4,2,block.AIR.id)
        # 小时个位数
        showNum(0, 1, 4, timeNow.hour%10)
        # 分隔符 :
        mc.setBlock(0,2,8, block.WOOL.id, 4)
        mc.setBlock(0,4,8, block.WOOL.id, 4)
        # 分钟十位数
        showNum(0, 1, 10, timeNow.minute//10)
        # 分数个位数
        showNum(0, 1, 14, timeNow.minute%10)

        # showNum()
        # print(timeNow.hour//10)
        # print(timeNow.hour%10)
        # print(timeNow.minute//10)
        # print(timeNow.minute%10)


# showNum(0, 1, 0,)