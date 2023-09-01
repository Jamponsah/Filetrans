print("hello")



#   *
#  ***
# *****
# *****
# *****

def draw_christX(height):
    for i in range (1,height +1 ): # 1 - 2, 1-5
        dash = height -1
        stars = 2 * i -1
        print(" "*dash + "*"*stars)

        draw_christX(10)

