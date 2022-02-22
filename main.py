# -*- coding: utf-8 -*-

import pyxel
from random import choice
from module import draw_mod as d, Game_msg, Enemy as eC, Bubble as bC

class APP:
  def __init__(self):
      pyxel.init(256, 256, title = "pyxel")
      pyxel.load('assets/assets.pyxres')             
      
      #Maze set
      self.data = []
      self.maze = []
      
      for i in range(32):
          self.data = []
          for i2 in range(32):
              self.data.append(pyxel.tilemap(0).pget(i2,i))
          self.maze.append(self.data)
      
      #Player status--------------------------------------------------
      #Player position
      self.pos = [1, 1]
      #Move permission tile list      
      self.move_permit = [(0, 0), (0, 1)]
      #Paint Can count
      self.paint_cnt = 5
      
      self.key_flag = False
      
      self.move_flag = False
      
      #Angle P=Player
      #    ^
      #    1
      #<4  P   2>
      #    3
      #    v
      #     
      self.pos_angle = 3
      
      #----------------------------------------------------------------
      
      #Wall set
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]
      
      for i1 in range(5):
          x1 = self.pos[1] - (1 * i1)
          if self.maze[x1][self.pos[0]] == 1:
              self.dead_end[0] = i1      
      self.dead_end = [0, (0, 0)]
      
      self.wall_list = [(1, 0), (1, 1), (2, 1),
                        (3, 1), (4, 1), (5, 1)]
      
      #Floor
      self.floor = [0, 0, 0, 0]
      
      #Bubble
      self.bubbles = [] 
      self.bubble_cnt = 0      
      #Bubble color list
      self.bub_c = (1, 5, 6, 12)
      
      #Enemy
      self.enemys = []
      self.enemy_set =[
                      (1, 10),
                      (7, 5),
                      (8, 26),
                      (24, 22),
                      (17, 17),
                      (22, 6),
                      ]
      for e in self.enemy_set:
          self.enemys.append(eC.Enemy(e[0], e[1], self.maze, self.move_permit))      
      self.enemy_pos = 9
      pyxel.mouse(True)
      
      #System
      self.game_over = False
      self.e_msg = "Enemies nearby: X"      
      self.e_msg_c = 0
      self.e_msg_F = False
      
      self.game_msg = Game_msg.GameMsg()      
      pyxel.run(self.update, self.draw)
     
  def reset(self):        
      #Player position
      self.pos = [1, 1]     
      
      self.paint_cnt = 5
      self.move_flag = False      
      self.pos_angle = 3
      self.key_flag = False
      
      #Wall set
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]
      
      for i1 in range(5):
          x1 = self.pos[1] - (1 * i1)
          if self.maze[x1][self.pos[0]] == 1:
              self.dead_end[0] = i1      
      self.dead_end = [0, (0, 0)]
      
      #Floor
      self.floor = [0, 0, 0, 0]
      
      #Bubble
      self.bubbles = [] 
      self.bubble_cnt = 0      
      #Bubble color list
      self.bub_c = (1, 5, 6, 12)
      
      #Enemy
      self.enemys = []      
      
      for e in self.enemy_set:
          self.enemys.append(eC.Enemy(e[0], e[1], self.maze, self.move_permit))            
      self.enemy_pos = 9
      
      #System
      self.game_over = False
      self.e_msg = "Enemies nearby: X"      
      self.e_msg_c = 0
      self.e_msg_F = False
      
      self.game_msg = Game_msg.GameMsg()      
      
  def update(self): 
      print(self.enemy_pos)
      print(pyxel.mouse_x, pyxel.mouse_y)
      #Bubble generate test---------------------------------------------------
      if pyxel.btnp(pyxel.KEY_B):
          c = choice(self.bub_c)
          x = pyxel.rndi(0, 256)
          y = pyxel.rndi(160, 220)
          v = pyxel.rndi(0, 2)
          s1 = pyxel.rndi(1, 2)
          s2 = pyxel.rndi(1, 9) / 10
          s = s1 + s2
          new_bubble = bC.Bubble(x, y, v, c, s)
          self.bubbles.append(new_bubble)
      #-----------------------------------------------------------------------
      
      if pyxel.btnp(pyxel.KEY_M):
          self.game_msg.update("Test M", 3)
          
      #Game Over Move---------------------------------------------------------    
      if self.game_over == True and pyxel.btnp(pyxel.KEY_R):
          self.reset()
      if self.game_over == True and pyxel.btnp(pyxel.KEY_Q):
          pyxel.quit()
      #-----------------------------------------------------------------------          

      #New bubble create------------------------------------------------------
      if self.bubble_cnt == 0:
          self.bubble_cnt = pyxel.rndi(200, 400)
          b_num = pyxel.rndi(2, 10)
          for bn in range(b_num):
              c = choice(self.bub_c)
              x = pyxel.rndi(30, 220)
              y = pyxel.rndi(160, 220)
              v = pyxel.rndi(0, 2)
              s1 = pyxel.rndi(1, 2)
              s2 = pyxel.rndi(1, 9) / 10
              s = s1 + s2
              new_bubble = bC.Bubble(x, y, v, c, s)
              self.bubbles.append(new_bubble)
              
      #Bubble update----------------------------------------------------------      
      b_mi = pyxel.rndi(1, 10)
      self.bubble_cnt -= b_mi
      for b in self.bubbles:
          b.update()
          if b.bub_y < 0:
              del b              
       #----------------------------------------------------------------------      
      if self.game_over == True:
          pass
      else:
          self.Game_update()
          
  def Game_update(self):                           
      #Wall reset
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]      
      self.floor = [0, 0, 0, 0]
      
      #Enemy reset
      self.enemy_pos = 9      
              
      #Player Controll--------------------------------------------------------
      self.move_flag = False
      #Go ahead
      if pyxel.btnp(pyxel.KEY_UP):          
          self.dead_end[0] = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1] - 1][self.pos[0]] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
              #Tile Check(Start position)
              elif self.maze[self.pos[1] - 1][self.pos[0]] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find the gold!", 10)                  
              #Tile Check(Goal position)
              elif self.maze[self.pos[1] - 1][self.pos[0]] == (2, 1):
                  self.game_msg.update("Goal position", 3)
                  self.game_msg.update("You finally found the gold!", 100)               
          elif self.pos_angle == 2:
              if self.maze[self.pos[1]][self.pos[0] + 1] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
              #Tile Check(Start position)
              elif self.maze[self.pos[1]][self.pos[0] + 1] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find the gold!", 10)                                    
              #Tile Check(Goal position)
              elif self.maze[self.pos[1]][self.pos[0] + 1] == (2, 1):
                 self.game_msg.update("Goal position", 3)
                 self.game_msg.update("You finally found the gold!", 100)                               
          elif self.pos_angle == 3:
              if self.maze[self.pos[1] + 1][self.pos[0]] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3
              #Tile Check(Start position)
              elif self.maze[self.pos[1] + 1][self.pos[0]] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find the gold!", 10)                                    
              #Tile Check(Goal position)
              elif self.maze[self.pos[1] + 1][self.pos[0]] == (2, 1):
                  self.game_msg.update("Goal position", 3)
                  self.game_msg.update("You finally found the gold!", 100)   
          elif self.pos_angle == 4:
              if self.maze[self.pos[1]][self.pos[0] - 1] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
              #Tile Check(Start position)
              elif self.maze[self.pos[1]][self.pos[0] - 1] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find the gold!", 10)                                    
              #Tile Check(Goal position)
              elif self.maze[self.pos[1]][self.pos[0] - 1] == (2, 1):
                  self.game_msg.update("Goal position", 3)
                  self.game_msg.update("You finally found the gold!", 100)   

          #Enemy action
          self.e_msg_c = 0          
          for e in self.enemys:
              if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                  self.enemy_pos = 0                  
                  self.game_over = True
                  
              if self.enemy_pos > 0:
                  if self.move_flag == True:
                      e.update()                  
                  x = abs(self.pos[0] - e.ene_x) 
                  y = abs(self.pos[1] - e.ene_y) 
                  if x < 5 and y < 5:                      
                      self.e_msg_c += 1
                  if x < 3 and y < 3:
                      self.e_msg_F = True            
                  self.e_msg = "Enemies nearby: " + str(self.e_msg_c)
                  
              if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                  self.enemy_pos = 0     
                  self.bubble_cnt = 0
                  self.game_over = True
                      
      #Turn to the back
      if pyxel.btnp(pyxel.KEY_DOWN):
          self.dead_end[0] = 0
          if self.pos_angle == 1:
              self.pos_angle = 3
          elif self.pos_angle == 2:
              self.pos_angle = 4
          elif self.pos_angle == 3:
              self.pos_angle = 1
          elif self.pos_angle == 4:
              self.pos_angle = 2
          
      #Turn to the right
      if pyxel.btnp(pyxel.KEY_RIGHT):
          self.dead_end[0] = 0
          if self.pos_angle == 1:
              self.pos_angle = 2
          elif self.pos_angle == 2:              
              self.pos_angle = 3
          elif self.pos_angle == 3:              
              self.pos_angle = 4
          elif self.pos_angle == 4:              
              self.pos_angle = 1
          
      #Turn to the left
      if pyxel.btnp(pyxel.KEY_LEFT):
          self.dead_end[0] = 0
          if self.pos_angle == 1:
              self.pos_angle = 4
          elif self.pos_angle == 2:             
              self.pos_angle = 1
          elif self.pos_angle == 3:              
              self.pos_angle = 2
          elif self.pos_angle == 4:
              self.pos_angle = 3    
      #-----------------------------------------------------------------------
  
      #Wall-Floor set & Enemy-serch-------------------------------------------      
      if self.pos_angle == 1:
          for i1 in range(4):
              if self.pos[1] - i1 < 0:
                  break           
              for i2 in range(2):
                  p1 = self.pos[1] - (1 * i1)
                  p2 = self.pos[0] - 1 + (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
                               
                  if self.maze[p1][self.pos[0]] in self.wall_list:                      
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]                                                                    
                  elif self.maze[p1][self.pos[0]] == (0, 1):
                          self.floor[i1] = 1
                          
                  for e in self.enemys:
                      if p1 == e.ene_y and self.pos[0]  == e.ene_x:
                          self.enemy_pos = i1        
                          if self.enemy_pos > i1:                            
                              self.enemy_pos = i1       
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0                  
                          self.bubble_cnt = 0
                          self.game_over = True                               
                         
                        
      elif self.pos_angle == 3:
          for i1 in range(4):
              if self.pos[1] + i1 > 31:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + (1 * i1)
                  p2 = self.pos[0] + 1 - (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[p1][self.pos[0]] in self.wall_list:                      
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]
                  elif self.maze[p1][self.pos[0]] == (0, 1):
                      self.floor[i1] = 1                          
                      
                  for e in self.enemys:
                      if p1 == e.ene_y and self.pos[0]  == e.ene_x:
                          if self.enemy_pos > i1:                                         
                              self.enemy_pos = i1         
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0        
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
                      
                      
      elif self.pos_angle == 2:
          for i1 in range(4):
              if self.pos[0] + i1 > 31:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] - 1 + (2 * i2) 
                  p2 = self.pos[0] + (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]                  
              
                  if self.maze[self.pos[1]][p2] in self.wall_list:                                            
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1             
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                  elif self.maze[self.pos[1]][p2] == (0, 1):
                      self.floor[i1] = 1                          
                          
                  for e in self.enemys:
                      if p2 == e.ene_x and self.pos[1]  == e.ene_y:
                          if self.enemy_pos > i1:                            
                              self.enemy_pos = i1              
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0        
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
                              
      elif self.pos_angle == 4:
          for i1 in range(4):
              if self.pos[0] - i1 < 0:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + 1 - (2 * i2) 
                  p2 = self.pos[0] - (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[self.pos[1]][p2] in self.wall_list:                      
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1                   
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1        
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                  elif self.maze[self.pos[1]][p2] == (0, 1):
                      self.floor[i1] = 1                       
                      
                  for e in self.enemys:
                      if p2 == e.ene_x and self.pos[1]  == e.ene_y:
                          if self.enemy_pos > i1:                            
                              self.enemy_pos = i1            
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0          
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
      #-----------------------------------------------------------------------
      
      #Paint floor action-----------------------------------------------------
      if pyxel.btnp(pyxel.KEY_SPACE):
          if self.paint_cnt > 0:
              if self.maze[self.pos[1]][self.pos[0]] == (0, 1):
                  pass
              else:
                  self.maze[self.pos[1]][self.pos[0]] = (0, 1)                        
                  self.paint_cnt -= 1
      #-----------------------------------------------------------------------
      
          

  def draw(self):
      pyxel.cls(0)                        
      
      d.draw_wall(self.wall)
      
      d.draw_paint(self.floor)

      d.draw_dead_end(self.dead_end)

      d.draw_bubble(self.bubbles, 0)
          
      #Draw Game Over text----------------------------------------------------
      if self.game_over == True:
          d.draw_game_over()
      #-----------------------------------------------------------------------                    
          
      d.draw_enemy(self.enemy_pos, self.dead_end)

      d.draw_bubble(self.bubbles, 1)
       
      d.draw_compass(self.pos, self.maze, self.wall_list,
                     self.pos_angle, self.e_msg, self.e_msg_F,
                     self.paint_cnt, self.game_msg)
      
APP()

