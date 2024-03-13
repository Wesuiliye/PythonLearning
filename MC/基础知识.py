import mcpi.minecraft as minecraft
#minecraft为我们导入的模块的别名，Minecraft.create()为连接游戏的方法
#()结尾代表执行一个动作，在编程中一般叫做函数或方法。
mc = minecraft.Minecraft.create()


'''
while True:
    # 获取玩家当前位置
    pop = mc.player.getTilePos()
    # 利用postToChat()方法在游戏中输出玩家的位置
    mc.postToChat(pop)
    # print(str(pop).strip('Vec3()'))
    # #判断玩家位置是否为我们设置的位置，如果是，执行子代码块
    if str(pop).strip('Vec3()') == '8,1,-70':
        mc.postToChat('welcome home!')
'''
# 直接设定玩家的位置
# 在1.19.2 里面,玩家y轴在68对应这里的0.
mc.player.setPos(0,-11,0)

