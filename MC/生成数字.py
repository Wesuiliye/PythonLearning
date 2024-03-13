import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()


# 3*5区域清空
def cleanField(baseX, baseY, baseZ):
    mc.setBlocks(baseX, baseY, baseZ, baseX, baseY + 4, baseZ + 2, block.AIR.id)

'''
# 生成分数
def showScore(baseX, baseY, baseZ, num):
    # 3*5区域清空
    cleanField(baseX, baseY, baseZ)

    # A1
    if num != 1:
        mc.setBlock(baseX, baseY + 4, baseZ, block.WOOL.id, 4)
    # b1
    if num != 4:
        mc.setBlock(baseX, baseY + 4, baseZ + 1, block.WOOL.id, 4)
    # c1
    if num != 1:
        mc.setBlock(baseX, baseY + 4, baseZ + 2, block.WOOL.id, 4)
    # a2
    if (num == 1 or num == 0) or (num > 3 and num <= 10) and num != 7:
        mc.setBlock(baseX, baseY + 3, baseZ, block.WOOL.id, 4)
    # b2
    if num == 1:
        mc.setBlock(baseX, baseY + 3, baseZ + 1, block.WOOL.id, 4)
    # c2
    if num == 0 or (num > 1 and num < 5) or (num > 6 and num <= 9):
        mc.setBlock(baseX, baseY + 3, baseZ + 2, block.WOOL.id, 4)
    # a3
    if (num == 2 or num == 0) or (num > 3 and num <= 10) and num != 7:
        mc.setBlock(baseX, baseY + 2, baseZ, block.WOOL.id, 4)
    # b3
    if num != 7 and num != 0:
        mc.setBlock(baseX, baseY + 2, baseZ + 1, block.WOOL.id, 4)
    # c3
    if num != 1:
        mc.setBlock(baseX, baseY + 2, baseZ + 2, block.WOOL.id, 4)
    # a4
    if num == 0 or num == 2 or num == 6 or num == 8:
        mc.setBlock(baseX, baseY + 1, baseZ, block.WOOL.id, 4)
    # b4
    if num == 1:
        mc.setBlock(baseX, baseY + 1, baseZ + 1, block.WOOL.id,4 )
    # c4
    if num != 1 and num != 2:
        mc.setBlock(baseX, baseY + 1, baseZ + 2, block.WOOL.id, 4)
    # a5
    if num != 4 and num != 7:
        mc.setBlock(baseX, baseY, baseZ, block.WOOL.id, 4)  # a5 基点
    # b5
    if num != 4 and num != 7:
        mc.setBlock(baseX, baseY, baseZ + 1, block.WOOL.id, 4)
    # c5
    if num != None:
        mc.setBlock(baseX, baseY, baseZ + 2, block.WOOL.id, 4)

'''
def showScore(baseX, baseY, baseZ, num):
    # 3*5区域清空
    cleanField(baseX, baseY, baseZ)

    # A1
    # c1
    # c3
    if num != 1:
        mc.setBlock(baseX, baseY + 4, baseZ, block.WOOL.id, 4)
        mc.setBlock(baseX, baseY + 4, baseZ + 2, block.WOOL.id, 4)
        mc.setBlock(baseX, baseY + 2, baseZ + 2, block.WOOL.id, 4)
    # b1
    if num != 4:
        mc.setBlock(baseX, baseY + 4, baseZ + 1, block.WOOL.id, 4)
    # a2
    if (num == 1 or num == 0) or (num > 3 and num <= 10) and num != 7:
        mc.setBlock(baseX, baseY + 3, baseZ, block.WOOL.id, 4)
    # b2
    # b4
    if num == 1:
        mc.setBlock(baseX, baseY + 3, baseZ + 1, block.WOOL.id, 4)
        mc.setBlock(baseX, baseY + 1, baseZ + 1, block.WOOL.id,4 )
    # c2
    if num == 0 or (num > 1 and num < 5) or (num > 6 and num <= 9):
        mc.setBlock(baseX, baseY + 3, baseZ + 2, block.WOOL.id, 4)
    # a3
    if (num == 2 or num == 0) or (num > 3 and num <= 10) and num != 7:
        mc.setBlock(baseX, baseY + 2, baseZ, block.WOOL.id, 4)
    # b3
    if num != 7 and num != 0:
        mc.setBlock(baseX, baseY + 2, baseZ + 1, block.WOOL.id, 4)
    # a4
    if num == 0 or num == 2 or num == 6 or num == 8:
        mc.setBlock(baseX, baseY + 1, baseZ, block.WOOL.id, 4)
    # c4
    if num != 1 and num != 2:
        mc.setBlock(baseX, baseY + 1, baseZ + 2, block.WOOL.id, 4)
    # a5
    # b5
    if num != 4 and num != 7:
        mc.setBlock(baseX, baseY, baseZ, block.WOOL.id, 4)  # a5 基点
        mc.setBlock(baseX, baseY, baseZ + 1, block.WOOL.id, 4)
    # c5
    if num != None:
        mc.setBlock(baseX, baseY, baseZ + 2, block.WOOL.id, 4)

# 生成黄色初始分数
showScore(0, 1, 0, 9)

# 清除空间
# cleanField(0,1,0)
