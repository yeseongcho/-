from cs1robots import *
import random
x = random.randint(1, 15)
y = random.randint(1, 15)
create_world(avenues = x, streets = y)
edit_world() # 임의로 world 구성
save_world("worlds/myworld.wld")
