import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# 生成场地
def buildField():
    # 开辟一个99*70*15的空间
    mc.setBlocks(-49, 0, -34, 49, 15, 34, block.AIR.id)
    # 铺场地
    mc.setBlocks(-29, 0, -19, 29, 0, 19, block.WOOL.id, 0)
    mc.setBlocks(-28, 0, -18, 28, 0, 18, block.WOOL.id, 13)
    mc.setBlocks(0, 0, -19, 0, 0, 19, block.WOOL.id, 0)
    mc.setBlocks(-29, 0, -8, -18, 0, 8, block.WOOL.id, 0)
    mc.setBlocks(29, 0, -8, 18, 0, 8, block.WOOL.id, 0)
    mc.setBlocks(-28, 0, -7, -19, 0, 7, block.WOOL.id, 13)
    mc.setBlocks(28, 0, -7, 19, 0, 7, block.WOOL.id, 13)

    # 球门
    mc.setBlocks(29, 3, -5, 29, 3, 5, block.WOOL.id, 4)
    mc.setBlocks(-29, 3, -5, -29, 3, 5, block.WOOL.id, 11)



# 设置“球”的坐标，只有在这个位置上的才算是球，通过击打改变球的位置
ballPosX = 0
ballPosY = 1
ballPosZ = 0

# 球队比分
yelloScore = 0
blueScore = 0

mc.postToChat("welcome to nille's world")
# 生成场地
buildField()


while True:
    # 这个库只响应用铁剑的击打事件（击打为右键操作）。
    events = mc.events.pollBlockHits()


    # [BlockEvent(BlockEvent.HIT, -3, 0, 2, 1, 252)]
    # 里面包含了击打方块的位置信息（前3个数字）和击打的面的信息（第4个数字）。
    # print(events)

    # 将events列表中的face(面)提取出来
    # 南 3
    # 北 2
    # 东 5
    # 西 4
    # 上 1
    # 下 0

    # 实时获取“球”的信息，当“球”不见了，变成空气了就重新生成一个。也能用于程序重启来生成球
    if mc.getBlock(ballPosX, ballPosY, ballPosZ) == block.AIR.id:
        mc.setBlock(ballPosX, ballPosY, ballPosZ, block.WOOL.id, 1)

    for e in events:
        # print(e.face)

        # 判断铁剑右键的是不是 “球”
        if e.pos.x == ballPosX and e.pos.y == ballPosY and e.pos.z == ballPosZ:
            # 让方块消失
            # mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
            # 东
            if e.face == 5:
                # 当击打方块不同的面时，让方块变成不同颜色的羊毛。
                # mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.WOOL.id, 11)

                # 让当前的方块消失，然后在对应方向上偏移一格的位置上重新生成一个对应的方块。
                # 让当前方块消失
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.AIR.id)
                # 生成对应的方块
                mc.setBlock(e.pos.x - 1, e.pos.y, e.pos.z, block.WOOL.id, 11)
                # 铁剑右键是球的话，相应的坐标加 1
                ballPosX -= 1

            # 南
            if e.face == 3:
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.AIR.id)
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z - 1, block.WOOL.id, 14)
                ballPosZ -= 1

            # 西
            if e.face == 4:
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.AIR.id)
                mc.setBlock(e.pos.x + 1, e.pos.y, e.pos.z, block.WOOL.id, 10)
                ballPosX += 1

            # 北
            if e.face == 2:
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.AIR.id)
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z + 1, block.WOOL.id, 4)
                ballPosZ += 1

            if e.face == 1:
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.WOOL.id, 0)
            if e.face == 0:
                mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.WOOL.id, 15)

            # 判断球是不是出界了
            if ballPosX < -29 or ballPosX > 29 or ballPosZ < -19 or ballPosZ > 19:
                # 判断是否进球
                if ballPosZ >= -5 and ballPosZ <= 5:
                    mc.postToChat('GOAL')
                    # 判断进的是哪个门
                    if ballPosX < -29:
                        yelloScore = yelloScore + 1
                    if ballPosX > 29:
                        blueScore = blueScore + 1
                    # 比分状况
                    mc.postToChat('YELLO:' + str(yelloScore) + ' BLUE:' + str(blueScore))
                else:
                    mc.postToChat('OUT')

                # 恢复位置
                ballPosX = 0
                ballPosZ = 0
                # 重新搭建一下场地
                buildField()
