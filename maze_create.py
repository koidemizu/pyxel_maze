# -*- coding: utf-8 -*-

import random
import numpy as np
import sys
 
sys.setrecursionlimit(10**6)
 
maze_width, maze_height = 32, 32
random_seed = 4
start_pos = (1, 1)
direction = [(0, -2), (0, 2), (-2, 0), (2, 0)]
 
maze_array = np.ones((maze_height, maze_width))
 
maze_array[start_pos] = 0 # 初期位置設定
def fn_create_maze(updX, updY):
    rnd_array = list(range(random_seed))
    random.shuffle(rnd_array)
    
    for index in rnd_array:
        if updY + direction[index][1] < 1 or updY + direction[index][1] > maze_height-1:
            continue
        elif updX + direction[index][0] < 1 or updX + direction[index][0] > maze_width-1:
            continue
        elif maze_array[updY+direction[index][1]][updX+direction[index][0]] == 0:
            continue
        else:
            pass
            
        maze_array[updY+direction[index][1]][updX+direction[index][0]] = 0
        if index == 0:
            maze_array[updY+direction[index][1]+1][updX+direction[index][0]] = 0
        elif index == 1:
            maze_array[updY+direction[index][1]-1][updX+direction[index][0]] = 0
        elif index == 2:
            maze_array[updY+direction[index][1]][updX+direction[index][0]+1] = 0
        elif index == 3:
            maze_array[updY+direction[index][1]][updX+direction[index][0]-1] = 0
        else:
            pass
        
        fn_create_maze(updX+direction[index][0], updY+direction[index][1])
 
if __name__ == '__main__':
    fn_create_maze(start_pos[0], start_pos[1])
    maze_array[start_pos] = 2
 
    print("result")
    
    
    # 迷路にランダムな6つの扉を設置する(扉は10～15)、スイッチは20~25を使い、スイッチの位置は5~10の距離で設定する
    roads = []
    for i in range(maze_height):
        for j in range(maze_width):
            if maze_array[i][j] == 0:
                roads.append((i, j))
    random.shuffle(roads)
    for i in range(6):
        maze_array[roads[i]] = i + 10
        # 追加：スイッチを設定する
        for _ in range(50):
            switch_pos = (random.randint(-10, 10), random.randint(-10, 10))
            switch_dist = abs(switch_pos[0]) + abs(switch_pos[1])
            if switch_dist <= 5 or switch_dist > 10:
                continue
            wall_pos = (roads[i][0]+switch_pos[0], roads[i][1]+switch_pos[1])
            if wall_pos[0] < 0 or wall_pos[0] >= maze_height or wall_pos[1] < 0 or wall_pos[1] >= maze_width:
                continue
            if maze_array[wall_pos] == 1:
                maze_array[wall_pos] = i + 20
                break
    np.set_printoptions(threshold=10000)
    print(maze_array)
