import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

# 在一个 3*3*3 的空间里面就单射60m
while True:
    pop = mc.player.getTilePos()
    if pop.x < 3 and pop.x > -3 and pop.y < 3 and pop.y > -3 \
        and pop.z < 3 and pop.z > -3:
        mc.player.setPos(pop.x,pop.y+60,pop.z)


