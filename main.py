# -*- coding: utf-8 -*-

import pyxel
from random import choice, sample
from module import draw_mod as d, Game_msg, Enemy as eC, Bubble as bC

class APP:
  def __init__(self):         
      pyxel.init(236, 340, title = "maze", fps = 30)      
      pyxel.camera(9, 0)
      pyxel.load('assets/assets.pyxres')                               
      
      self.status_set()       
      pyxel.run(self.update, self.draw)      
     
  def status_set(self):        
      #Maze set
      self.data = []
      self.maze = []
      self.aisle = []
      self.a_count = 0
      self.e_ig = [
          (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
          (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
          (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
          (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
          (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),          
          ]
      
      mi = pyxel.rndi(0, 2)
      #mi = 0
      for i in range(32):
          self.data = []
          for i2 in range(32):
              self.data.append(pyxel.tilemaps[0].pget(i2, i + mi * 32))
          self.maze.append(self.data)
          
      self.d_pos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
      self.caves = [[(0, 0), (0, 0)], [(0, 0), (0, 0)], [(0, 0), (0, 0)]]
      for m1 in range(32):
          for m2 in range(32):
              m = self.maze[m1][m2]
              if m == (3, 1):
                  self.d_pos[0] = (m1, m2)
              elif m == (3, 2):
                  self.d_pos[1] = (m1, m2)                  
              elif m == (3, 3):
                  self.d_pos[2] = (m1, m2)                  
              elif m == (3, 4):
                  self.d_pos[3] = (m1, m2)                                    
              elif m == (3, 5):
                  self.d_pos[4] = (m1, m2)                                    
              elif m == (3, 6):
                  self.d_pos[5] = (m1, m2) 
              elif m == (7, 1):
                  self.caves[0][0] = (m1, m2) 
              elif m == (8, 1):
                  self.caves[0][1] = (m1, m2)                   
              elif m == (7, 2):
                  self.caves[1][0] = (m1, m2) 
              elif m == (8, 2):
                  self.caves[1][1] = (m1, m2)   
              elif m == (7, 3):
                  self.caves[2][0] = (m1, m2) 
              elif m == (8, 3):
                  self.caves[2][1] = (m1, m2)                                    

              elif m == (0, 0):
                  self.a_count += 1
                  mii = (m1, m2)
                  if mii in self.e_ig:
                      pass
                  else:
                      self.aisle.append((m1, m2))
      
      #Player status--------------------------------------------------
      #Player position
      self.pos = [1, 1]
      self.pos_history = [(1, 1)]
      #Move permission tile list      
      self.move_permit = [(0, 0), (0, 1)]
      #Paint Can count
      self.paint_cnt = 5
      #Scan count
      self.scan_cnt = 9
      self.scan_cnt_f = 0
      self.scan_flug = False
      #Fence count
      self.fence_cnt = 8
      self.fence_flag = False
      
      self.key_flag = False
      
      self.move_flag = False
      self.key_koutyoku_flag = False
      self.key_koutyoku = 0

      self.other_action_flag = False
      self.other_action_num = 0
      self.other_action_col = 0
      
      #Angle P=Player
      #    ^
      #    1
      #<4  P   2>
      #    3
      #    v
      #     
      self.pos_angle = 3
      
      self.step_num = 0
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
      
      self.wall_list = [(1, 0), (3, 0), (4, 0), (5, 0), (6, 0), 
                        (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
                        (3, 2), (4, 2), (5, 2),
                        (3, 3), (4, 3), (5, 3),
                        (3, 4), (4, 4), (5, 4),
                        (3, 5), (4, 5), (5, 5),
                        (3, 6), (4, 6), (5, 6),
                        (0, 2),
                        (6, 1),
                        (7, 1), (7, 2),(7, 3),
                        (8, 1), (8, 2),(8, 3),
                        ]
      
      self.wall_list_n = [(1, 0), (3, 0), (4, 0), (5, 0), (6, 0),]
      self.wall_list_d = [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),]
      self.wall_list_l = [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),]
      self.wall_list_l2 = [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),]
      self.wall_list_f = [(0, 2),]
      self.wall_list_m = [(6, 1),]
                        
      
      #Floor
      self.floor = [0, 0, 0, 0]
      
      #Bubble
      self.bubbles = [] 
      self.bubble_cnt = 0      
      #Bubble color list
      self.bub_c = (1, 5, 6, 12)
      
      #Enemy
      self.enemys = []
      self.enemys_num1 = 10            
      self.enemy_set1 = sample(self.aisle, self.enemys_num1)      
      
      for e in self.enemy_set1:
          self.enemys.append(eC.Enemy(e[0], e[1], self.maze, 
                                      self.move_permit, pyxel.rndi(1, 2)))
          
             
      self.enemy_pos = 9
      self.enemy_col = 1
      pyxel.mouse(True)
      
      #System
      self.game_over = False
      self.e_msg = "Enemies nearby: X"      
      self.e_msg_c = 0
      self.e_msg_F = False
      self.key_ipt = False
      self.key_ipt_num = (0, 0)
      self.game_start = False
      self.game_end = False
      self.start_move = False
      self.end_move = False
      self.start_bubble = True
      self.screen = 250
      self.screen_s = 0
      self.game_msg = Game_msg.GameMsg()      
      self.ver = "1.20"
      self.map_h_ctl = 0
      self.buttons = []
      self.buttons.append(Button(50, 259, 30, 27, 6, 1, "UP"))
      self.buttons.append(Button(50, 298, 30, 27, 6, 2, "DOWN"))
      self.buttons.append(Button(15, 280, 30, 27, 6, 3, "LEFT"))
      self.buttons.append(Button(85, 280, 30, 27, 6, 4, "RIGHT"))
      self.buttons.append(Button(135, 260, 45, 35, 8, 5, "NO"))
      self.buttons.append(Button(195, 260, 45, 35, 11, 6, "YES"))
      self.buttons.append(Button(135, 300, 65, 25, 7, 7, "CHANGE ACTION"))
      self.hit_button = 0
      self.view_mode = 2
      pyxel.screen_mode(self.view_mode)

  def update(self):               
      self.bubble_update()           
      
      if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
          #if self.view_mode == 2:
          #    self.view_mode = 0
          #else:
          #    self.view_mode += 1
          #pyxel.screen_mode(self.view_mode)
          self.chk_button()

      if self.end_move == True:                      
          if self.screen < 255:
              self.screen += 6
          else:
              self.screen_s += 1
              if self.screen_s == 30:
                  ep1 = int(len(list(set(self.pos_history))))
                  ep2 = int(self.a_count)
                  for mi in range(9):
                      self.game_msg.update("", 3)
                  self.game_msg.update("Congratulations", 8)
                  self.game_msg.update("You've cleared the game!", 6)
                  self.game_msg.update("Thank you for playing!", 10)
                  self.game_msg.update("----------------------------", 13)
                  self.game_msg.update("Number of steps: "+str(self.step_num),
                                       7)
                  self.game_msg.update("Exploration Progress: " + 
                                       str('{:.0%}'.format(ep1 / ep2)),
                                       7)
                  self.game_msg.update("", 10)                    
                  self.game_msg.update("Press R key or GamePad Button.", 11)  
                  self.screen_s = 0
                  self.game_end = True
                  self.end_move = False
                  self.key_ipt = True
                  self.key_ipt_num = (99, 99)
      elif self.start_move == True:                      
          if self.screen < 255:
              self.screen += 6
          else:
              self.screen_s += 1
              if self.screen_s == 30:                  
                  self.start_move = False   
                  self.screen_s = 0
      elif self.game_over == True:
          for go in range(8):
              self.game_msg.update("", 3)                    
          self.game_msg.update("The path you followed.", 8)
          self.game_msg.update("Press R key or GamePad Button.", 11)            
          for go2 in range(7):
              self.game_msg.update("", 3)
          
          if (pyxel.btnp(pyxel.KEY_R) or
             pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or
             pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) or
             pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or
             pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B)):
              self.status_set()
          
      elif self.game_start == False:
             if (pyxel.btnp(pyxel.KEY_S) or 
                self.hit_button > 0
             ):
              self.game_start = True
              self.start_move = True
              self.screen = 0
              self.bubble_cnt = -1
              self.hit_button = 0
      else:
          if self.screen > 0:
              if self.game_end == False:
                  self.screen -= 4
              else:
                  self.screen -= 6
              
          if self.key_ipt == True:
              #Key input------------------------------------------------------
              #Lever------------------------------------------------------
              if self.key_ipt_num in self.wall_list_l:                  
                  if pyxel.btnp(pyxel.KEY_Y) or self.hit_button == 6:
                      self.hit_button = 0
                      self.game_msg.update("Yes", 3)
                      self.game_msg.update("Somewhere a door opened.", 9)
                      ip = self.key_ipt_num[1]
                      if self.pos_angle == 1:
                          self.maze[self.pos[1] - 1][self.pos[0]] = (5, ip)
                      elif self.pos_angle == 2:
                          self.maze[self.pos[1]][self.pos[0] + 1] = (5, ip)
                      elif self.pos_angle == 3:
                          self.maze[self.pos[1] + 1][self.pos[0]] = (5, ip)
                      elif self.pos_angle == 4:
                          self.maze[self.pos[1]][self.pos[0] - 1] = (5, ip) 
                      self.dead_end[1] = (5, ip)
                      self.key_ipt = False
                      self.key_ipt_num = (0, 0)
                      
                      if ip == 1:
                          self.maze[self.d_pos[0][0]][self.d_pos[0][1]]=(0, 0)
                      elif ip == 2:
                          self.maze[self.d_pos[1][0]][self.d_pos[1][1]]=(0, 0)
                      elif ip == 3:
                          self.maze[self.d_pos[2][0]][self.d_pos[2][1]]=(0, 0)
                      elif ip == 4:
                          self.maze[self.d_pos[3][0]][self.d_pos[3][1]]=(0, 0)
                      elif ip == 5:
                          self.maze[self.d_pos[4][0]][self.d_pos[4][1]]=(0, 0)
                      elif ip == 6:
                          self.maze[self.d_pos[5][0]][self.d_pos[5][1]]=(0, 0)
                          
                  elif pyxel.btnp(pyxel.KEY_N) or self.hit_button == 5:
                      self.hit_button = 0
                      self.game_msg.update("No", 3)
                      self.key_ipt = False
                      self.key_ipt_num = (0, 0)
              #Fence------------------------------------------------------
              elif self.key_ipt_num in self.wall_list_f:
                  if pyxel.btnp(pyxel.KEY_Y) or self.hit_button == 6:
                      self.hit_button = 0
                      self.game_msg.update("Yes", 3)
                      self.game_msg.update("Fence removed.", 9)
                      ip = self.key_ipt_num[1]
                      if self.pos_angle == 1:
                          self.maze[self.pos[1] - 1][self.pos[0]] = (0, 0)
                      elif self.pos_angle == 2:
                          self.maze[self.pos[1]][self.pos[0] + 1] = (0, 0)
                      elif self.pos_angle == 3:
                          self.maze[self.pos[1] + 1][self.pos[0]] = (0, 0)
                      elif self.pos_angle == 4:
                          self.maze[self.pos[1]][self.pos[0] - 1] = (0, 0)                       
                      self.key_ipt = False
                      self.key_ipt_num = (0, 0)           
                      self.dead_end[0] = 0
                      self.wall_update()
                      
                  elif pyxel.btnp(pyxel.KEY_N) or self.hit_button == 5:
                      self.hit_button = 0
                      self.game_msg.update("No", 3)
                      self.key_ipt = False
                      self.key_ipt_num = (0, 0)     
              #Cave------------------------------------------------------
              elif (self.key_ipt_num == (7, 1) or self.key_ipt_num == (8, 1) or 
                   self.key_ipt_num == (7, 2)  or self.key_ipt_num == (8, 2) or
                   self.key_ipt_num == (7, 3)  or self.key_ipt_num == (8, 3)):
                  if pyxel.btnp(pyxel.KEY_Y) or self.hit_button == 6:
                      self.hit_button = 0
                      self.game_msg.update("Yes", 3)
                      self.key_ipt = False                      
                      if self.key_ipt_num == (7, 1):
                          self.pos[0] = self.caves[0][1][1]
                          self.pos[1] = self.caves[0][1][0] + 1
                      elif self.key_ipt_num == (8, 1):
                          self.pos[0] = self.caves[0][0][1]
                          self.pos[1] = self.caves[0][0][0] + 1
                      elif self.key_ipt_num == (7, 2):
                          self.pos[0] = self.caves[1][1][1]
                          self.pos[1] = self.caves[1][1][0] + 1
                      elif self.key_ipt_num == (8, 2):
                          self.pos[0] = self.caves[1][0][1]
                          self.pos[1] = self.caves[1][0][0] + 1                                                
                      elif self.key_ipt_num == (7, 3):
                          self.pos[0] = self.caves[2][1][1]
                          self.pos[1] = self.caves[2][1][0] + 1
                      elif self.key_ipt_num == (8, 3):
                          self.pos[0] = self.caves[2][0][1]
                          self.pos[1] = self.caves[2][0][0] + 1                          
                      
                      self.pos_angle = 3
                      self.pos_history.append((self.pos[0], self.pos[1]))
                      self.key_ipt_num = (0, 0)     
                      self.dead_end[0] = 0
                      self.wall_update()                      
                  elif pyxel.btnp(pyxel.KEY_N) or self.hit_button == 5:
                      self.hit_button = 0
                      self.game_msg.update("No", 3)
                      self.key_ipt = False
                      self.key_ipt_num = (0, 0)                                    
              #---------------------------------------------------------------
              elif self.key_ipt_num == (2, 1):
                  if (pyxel.btnp(pyxel.KEY_S) or
                     self.hit_button > 0):
                      self.hit_button = 0
                      self.start_bubble = True
                      self.bubble_cnt = -1
                      self.bubble_update()
                      self.key_ipt = False
                      self.key_ipt_num = (0, 0)       
                      self.end_move = True
                      self.screen = 0

              elif self.key_ipt_num == (99, 99) and self.screen < 10:
                  if (pyxel.btnp(pyxel.KEY_R) or
                     self.hit_button > 0):
                      self.hit_button = 0
                      self.status_set()                      
          else:
              self.Game_update()
          
  def chk_button(self):
      self.hit_button = 0
      if pyxel.MOUSE_BUTTON_LEFT:
          for b in self.buttons:
              if b.check_hit(pyxel.mouse_x, pyxel.mouse_y):
                  self.hit_button = b.check_hit(pyxel.mouse_x, pyxel.mouse_y)
              else:
                  if self.hit_button > 0:
                      pass
                  else:
                      self.hit_button = 0
      print(self.hit_button)

  def Game_update(self):                           
      #Wall reset
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]      
      self.floor = [0, 0, 0, 0]
      
      #Enemy reset
      self.enemy_pos = 9      
      self.enemy_col = 1
      
      if self.other_action_flag == False:
          self.Player_update()

      #Wall-Floor set & Enemy-serch-------------------------------------------
      self.wall_update()          

      #Other action-----------------------------------------------------------
      if (pyxel.btnp(pyxel.KEY_SPACE) or
          self.hit_button == 7 ):
          if self.other_action_flag == False:
              self.other_action_flag = True
          else:
              self.other_action_flag = False
          self.hit_button = 0
      if self.other_action_flag == True:
          self.other_action()          

  def Player_update(self):
      #Player Controll--------------------------------------------------------
      if self.key_koutyoku_flag == True:
          self.key_koutyoku += 1
          if self.key_koutyoku > 5:
              self.key_koutyoku_flag = False
              self.key_koutyoku = 0
      else:
          self.move_flag = False
          #Go ahead
          if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W) or self.hit_button == 1:
              self.hit_button = 0
              self.key_koutyoku_flag = True
              self.dead_end[0] = 0
              if self.pos_angle == 1:
                  tile = self.maze[self.pos[1] - 1][self.pos[0]]
                  if tile in self.move_permit:
                      self.move_flag = True
                      self.e_msg_F = False
                      self.pos[1] = self.pos[1] - 1
                      self.enemys_update()
                      self.pos_history.append((self.pos[0], self.pos[1]))
                      self.step_num += 1
                      self.pos_angle = 1
                      self.scan_update()
                  else:
                      self.chk_other_tile(tile)
              elif self.pos_angle == 2:
                  tile = self.maze[self.pos[1]][self.pos[0] + 1]
                  if tile in self.move_permit:
                      self.move_flag = True
                      self.e_msg_F = False
                      self.pos[0] = self.pos[0] + 1
                      self.enemys_update()
                      self.step_num += 1
                      self.pos_history.append((self.pos[0], self.pos[1]))
                      self.pos_angle = 2
                      self.scan_update()
                  else:
                      self.chk_other_tile(tile)
              elif self.pos_angle == 3:
                  tile = self.maze[self.pos[1] + 1][self.pos[0]]
                  if tile in self.move_permit:
                      self.move_flag = True
                      self.e_msg_F = False
                      self.pos[1] = self.pos[1] + 1
                      self.enemys_update()
                      self.step_num += 1
                      self.pos_history.append((self.pos[0], self.pos[1]))
                      self.pos_angle = 3
                      self.scan_update()
                  else:
                      self.chk_other_tile(tile)
              elif self.pos_angle == 4:
                  tile = self.maze[self.pos[1]][self.pos[0] - 1] 
                  if tile in self.move_permit:
                      self.move_flag = True
                      self.e_msg_F = False
                      self.pos[0] = self.pos[0] - 1     
                      self.enemys_update()
                      self.step_num += 1
                      self.pos_history.append((self.pos[0], self.pos[1]))
                      self.pos_angle = 4
                      self.scan_update()
                  else:
                      self.chk_other_tile(tile)
                      
          #Turn to the back
          elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S) or self.hit_button == 2:
              self.hit_button = 0
              self.key_koutyoku_flag = True
              self.dead_end[0] = 0
              if self.pos_angle == 1:
                  self.pos_angle = 3
              elif self.pos_angle == 2:
                  self.pos_angle = 4
              elif self.pos_angle == 3:
                  self.pos_angle = 1
              elif self.pos_angle == 4:
                  self.pos_angle = 2
              #self.move_flag = True
              #self.enemys_update()
          
          #Turn to the right
          elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D) or self.hit_button == 4:
              self.hit_button = 0
              self.key_koutyoku_flag = True
              self.dead_end[0] = 0
              if self.pos_angle == 1:
                  self.pos_angle = 2
              elif self.pos_angle == 2:              
                  self.pos_angle = 3
              elif self.pos_angle == 3:              
                  self.pos_angle = 4
              elif self.pos_angle == 4:              
                  self.pos_angle = 1
              #self.move_flag = True
              #self.enemys_update()
          
          #Turn to the left
          elif pyxel.btnp(pyxel.KEY_LEFT)or pyxel.btnp(pyxel.KEY_A) or self.hit_button == 3:
              self.hit_button = 0
              self.key_koutyoku_flag = True
              self.dead_end[0] = 0
              if self.pos_angle == 1:
                  self.pos_angle = 4
              elif self.pos_angle == 2:             
                  self.pos_angle = 1
              elif self.pos_angle == 3:              
                  self.pos_angle = 2
              elif self.pos_angle == 4:
                  self.pos_angle = 3   
              #self.move_flag = True 
              #self.enemys_update()
          #-----------------------------------------------------------------------  
      
      
  def enemys_update(self):
      #Enemy action
      self.e_msg_c = 0          
      for e in self.enemys:
          if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
              self.enemy_pos = 0                  
              self.enemy_col = e.coller
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


  def other_action(self):
      if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W) or self.hit_button == 1:
          self.hit_button = 0
          if self.other_action_num > 0:
              self.other_action_num -= 1
        
      if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S) or self.hit_button == 2:
          self.hit_button = 0
          if self.other_action_num < 2:
              self.other_action_num += 1              
      
      if (pyxel.btnp(pyxel.KEY_Y) or
          self.hit_button == 6 ):        
          self.hit_button = 0  
          if self.other_action_num == 0:              
              self.other_action_flag = False
              #Paint floor action-----------------------------------------------------      
              if self.paint_cnt > 0:
                  if self.maze[self.pos[1]][self.pos[0]] == (0, 1):
                      pass
                  else:
                      self.maze[self.pos[1]][self.pos[0]] = (0, 1)                        
                      self.paint_cnt -= 1
          elif self.other_action_num == 1:              
              self.other_action_flag = False
              #Scan action-----------------------------------------------------
              if self.scan_flug == False:
                 if self.scan_cnt > 0:
                      self.game_msg.update("Scanning start.", 9)
                      self.scan_flug = True
                      self.scan_cnt -= 1
                      self.scan_cnt_f = 30
          elif self.other_action_num == 2:      
              #Fence action-----------------------------------------------------      
                  self.other_action_flag = False            
                  self.fence_flag = 0
                  if self.fence_cnt > 0:
                      if self.pos_angle == 1:
                          tile = self.maze[self.pos[1] - 1][self.pos[0]]
                          for e in self.enemys:
                              if e.ene_y == self.pos[1] - 1 and e.ene_x == self.pos[0]:
                                  self.game_msg.update("The enemy is too close.", 9)
                                  self.game_msg.update("Fence could not be set up.", 9)
                                  self.fence_flag = 3
                                  break
                          if tile in self.move_permit and self.fence_flag == 0:
                              self.maze[self.pos[1] - 1][self.pos[0]] = (0, 2)
                              self.fence_cnt -= 1
                              self.game_msg.update("You have set up a fence.", 9)                              
                              
                      elif self.pos_angle == 2:
                          tile = self.maze[self.pos[1]][self.pos[0] + 1]
                          for e in self.enemys:                     
                              if e.ene_y == self.pos[1] and e.ene_x == self.pos[0]+1:
                                  self.game_msg.update("The enemy is too close.", 9)
                                  self.game_msg.update("Fence could not be set up.", 9)
                                  self.fence_flag = 3
                                  break                      
                          if tile in self.move_permit and self.fence_flag == 0:
                              self.maze[self.pos[1]][self.pos[0]+1] = (0, 2)
                              self.fence_cnt -= 1
                              self.game_msg.update("You have set up a fence.", 9)                      
                      
                      elif self.pos_angle == 3:
                          tile = self.maze[self.pos[1] + 1][self.pos[0]]
                          for e in self.enemys:
                              if e.ene_y == self.pos[1] + 1 and e.ene_x == self.pos[0]:
                                  self.game_msg.update("The enemy is too close.", 9)
                                  self.game_msg.update("Fence could not be set up.", 9)
                                  self.fence_flag = 3
                                  break                    
                          if tile in self.move_permit and self.fence_flag == 0:
                              self.maze[self.pos[1] + 1][self.pos[0]] = (0, 2)
                              self.fence_cnt -= 1
                              self.game_msg.update("You have set up a fence.", 9)                                    
                      
                      elif self.pos_angle == 4:
                          tile = self.maze[self.pos[1]][self.pos[0] - 1] 
                          for e in self.enemys: 
                              if e.ene_y == self.pos[1] and e.ene_x == self.pos[0]-1:
                                  self.game_msg.update("The enemy is too close.", 9)
                                  self.game_msg.update("Fence could not be set up.", 9)
                                  self.fence_flag = 3
                                  break
                          if tile in self.move_permit and self.fence_flag == 0:
                              self.maze[self.pos[1]][self.pos[0]-1] = (0, 2)
                              self.fence_cnt -= 1
                              self.game_msg.update("You have set up a fence.", 9)                      
                              
              #-----------------------------------------------------------------------      
      
  def scan_update(self):
      if self.scan_flug == True:          
          self.scan_cnt_f -= 1
          if self.scan_cnt_f < 1:
              self.scan_flug = False
              self.game_msg.update("Scanning end.", 9)
      
      
  def chk_other_tile(self, t):
      #Tile Check(Start position)
      if t == (1, 1):
          self.game_msg.update("You have entered the maze.", 3)
          self.game_msg.update("Find the gold!", 10)                                    
      #Tile Check(Goal position)
      elif t == (2, 1):
          self.game_msg.update("Goal position", 3)
          self.game_msg.update("You finally found the gold!", 10)             
          self.game_msg.update("Congratulations!", 10)  
          self.game_msg.update("Press S key or ", 10)  
          self.game_msg.update("Any GamePad Button.", 10)  
          self.key_ipt = True
          self.key_ipt_num = t
      #Tile Check(Cave)
      elif (t == (7, 1)  or t == (8, 1) or t == (7, 2)  or t == (8, 2) or
            t == (7, 3)  or t == (8, 3)):
          self.game_msg.update("You have found a cave.", 3)          
          self.game_msg.update("Do you want to enter?", 11)   
          self.game_msg.update("Y = Yes,  N = No", 11, 1)     
          self.key_ipt = True
          self.key_ipt_num = t        
      #Tile Check(Door)
      elif t in self.wall_list_d:
          self.game_msg.update("Door is locked.", 3)
      #Tile Check(Lever)
      elif t in self.wall_list_l:
          self.game_msg.update("You have found the lever.", 3)
          self.game_msg.update("Do you want to activate", 11)
          self.game_msg.update("the lever?", 11)   
          self.game_msg.update("Y = Yes,  N = No", 11, 1)   
          self.key_ipt = True
          self.key_ipt_num = t
      #Tile Check(Fence)
      elif t in self.wall_list_f:          
          self.game_msg.update("Do you want to remove ", 11)
          self.game_msg.update("the fence?", 11)   
          self.game_msg.update("Y = Yes,  N = No", 11)   
          self.key_ipt = True
          self.key_ipt_num = t          
      #Tile Check(monitor)
      elif t in self.wall_list_m:          
          self.game_msg.update("You found an old monitor.", 11)
          
  def wall_update(self):
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
                              self.enemy_col = e.coller
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0   
                          self.enemy_col = e.coller
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
                              self.enemy_col = e.coller
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0     
                          self.enemy_col = e.coller
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
                              self.enemy_col = e.coller
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0       
                          self.enemy_col = e.coller
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
                              self.enemy_col = e.coller
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0          
                          self.enemy_col = e.coller
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
      #-----------------------------------------------------------------------      


  def bubble_update(self):      
      #New bubble create------------------------------------------------------
      if self.bubble_cnt < 0:
          self.bubble_cnt = pyxel.rndi(1200, 2400)
          if self.game_start == True:
              if self.start_bubble == True:
                  b_num = 10
                  self.start_bubble = False
              else:
                  b_num = pyxel.rndi(2, 10)
          else:
              b_num = pyxel.rndi(20, 30)             
          for bn in range(b_num):
              c = choice(self.bub_c)              
              if self.game_start == True:
                  x = pyxel.rndi(10, 230)
                  y = pyxel.rndi(160, 230)
              else:
                  x = pyxel.rndi(0, 250)
                  y = pyxel.rndi(256, 286)
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

  def draw(self):
      pyxel.cls(0)                        
      
      #Game start information
      if self.game_start == False or self.start_move == True:
          pyxel.blt(10, 10, 2, 0, 0, 232, 40, 14)
          
          y = 50
          pyxel.rect(50, 29 + y, 156, 93, 0)
              
          pyxel.circb(128, 60 + y, 25, 7)
          pyxel.circb(128, 93 + y, 25, 7)
          pyxel.rect(103, 50 + y, 51, 54, 0)
          pyxel.rectb(103, 50 + y, 51, 54, 7)
              
          pyxel.line(106, 50 + y, 150, 50 + y, 0)
          pyxel.line(106, 103 + y, 150, 103 + y, 0)
              
          pyxel.line(107, 50 + y, 107, 103 + y, 7)
              
          pyxel.rectb(103, 59 + y, 10, 5, 7)
          pyxel.rectb(103, 89 + y, 10, 5, 7)
              
          #pyxel.circ(128, 58, 10, 7)
          pyxel.circb(128, 58 + y, 10, 7)
              
          pyxel.circb(145, 78 + y, 6, 7)
          pyxel.line(139, 78 + y, 150, 78 + y, 7)
          pyxel.line(145, 73 + y, 145, 84 + y, 7)                    
          
          d.draw_bubble(self.bubbles, 1)
          
          pyxel.text(59, 202, "Press S key or Any Button to start.", 1)
          pyxel.text(58, 201, "Press S key or Any Button to start.", 5)
          pyxel.text(57, 200, "Press S key or Any Button to start.", 7)
          
          pyxel.text(205, 55, "Ver." + self.ver, 7)
          
          #Game Start Door Movie----------------------------------------------
          if self.start_move == True:
              if self.screen > 0:                                    
                  #YOKO KAN-NON
                  pyxel.rect(0, 0, self.screen / 2, 254, 0)
                  pyxel.rectb(0, 0, self.screen / 2, 254, 13)
                  pyxel.rect(128+(128-self.screen/2), 0, self.screen / 2,
                             254, 0)
                  pyxel.rectb(128+(128-self.screen/2), 0,self.screen / 2,
                              254, 13)               
          
      else:          
          d.draw_wall(self.wall, self.wall_list_n,
                      self.wall_list_d, self.wall_list_l, self.wall_list_l2,
                      self.wall_list_f, self.wall_list_m)
      
          d.draw_paint(self.floor)

          d.draw_dead_end(self.dead_end, self.wall_list_n, 
                          self.wall_list_d, self.wall_list_l, 
                          self.wall_list_l2, self.wall_list_f, 
                          self.wall_list_m,
                          self.maze, self.pos, self.enemys)

          if self.game_end == True:
              if pyxel.frame_count % 5 == 0:
                  if self.map_h_ctl + 1 < len(self.pos_history):
                      self.map_h_ctl += 1
                  else:
                      self.map_h_ctl = 0                  
              d.draw_map_history(self.maze, 95, 35, self.pos, 
                                 self.pos_history, self.map_h_ctl,
                                 self.enemys)          

          d.draw_bubble(self.bubbles, 0)
          
          #Draw Game Over text------------------------------------------------
          if self.game_over == True:
              d.draw_game_over()
          #-------------------------------------------------------------------
          
          d.draw_enemy(self.enemy_pos, self.dead_end, self.enemy_col)

          d.draw_bubble(self.bubbles, 1)
       
          d.draw_compass(self.pos, self.maze, self.wall_list,
                         self.pos_angle, self.e_msg, self.e_msg_F,
                         self.paint_cnt, self.game_msg, self.wall_list_n,
                         self.scan_flug, self.scan_cnt, self.fence_cnt)
          
          if self.screen > 0:     
              if self.game_end == True:                              
                  #YOKO KAN-NON
                  pyxel.rect(0, 0, self.screen / 2, 254, 0)
                  pyxel.rectb(0, 0, self.screen / 2, 254, 13)
                  pyxel.rect(128+(128-self.screen/2), 0, self.screen / 2,
                             254, 0)
                  pyxel.rectb(128+(128-self.screen/2), 0,self.screen / 2,
                              254, 13)               
              else:
                  #YOKO KAN-NON
                  pyxel.rect(0, 0, self.screen / 2, 254, 0)
                  pyxel.rectb(0, 0, self.screen / 2, 254, 13)
                  pyxel.rect(128+(128-self.screen/2), 0, self.screen / 2,
                             254, 0)
                  pyxel.rectb(128+(128-self.screen/2), 0,self.screen / 2,
                              254, 13)                                                                      
           
          if self.other_action_flag == True:
              if pyxel.frame_count % 45 == 0:
                  if self.other_action_col == 0:
                      self.other_action_col = 1
                  else:
                      self.other_action_col = 0
             
              if self.other_action_col == 0:
                  colk = 10
              else:
                  colk = 9

              pyxel.rectb(10, 151, 100, 104, colk)
              on = self.other_action_num * 18              
              pyxel.tri(71, 167 + on, 71, 173 + on, 77, 170 + on, colk)
         
      #Map window dev    
      #Draw Game Over Map------------------------------------------------
      if self.game_over == True or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
          if pyxel.frame_count % 5 == 0:
              if self.map_h_ctl + 1 < len(self.pos_history):
                  self.map_h_ctl += 1
              else:
                  self.map_h_ctl = 0                          
          d.draw_map_history(self.maze, 121, 182, self.pos, 
                             self.pos_history, self.map_h_ctl, self.enemys)          
      else:
          pass
          #self.map_h_ctl = 0

      #Draw Controller--------------------------------------------------------
      pyxel.rect(0, 255, 256, 100, 0)
      pyxel.rectb(9, 255, 236, 74, 1)
      #Draw Controller Button-------------------------------------------------
      for b in self.buttons:
          b.draw()



class Button:
  def __init__(self, x, y, w, h, c, t, cap=""):
      self.x = x
      self.y = y
      self.w = w
      self.h = h      
      self.c = c
      self.type = t
      self.col_cng_time = 0
      self.caption = cap
      
  def update(self):
      if self.col_cng_time > 0:
          self.col_cng_time -= 1
  
  def check_hit(self, x, y):
      if self.x <= x and (self.x + self.w) >= x:
          if self.y <= y and (self.y + self.h) >= y:
              self.col_cng_time = 7
              return self.type          
  
  def draw(self):
      self.update()
      c = self.c
      if self.col_cng_time > 0:
          if c == 11:
              c = 3
          elif c == 8:
              c = 2                
          elif c == 6:
              c = 5                
          elif c == 7:
              c = 13                

      pyxel.rect(self.x, self.y, self.w, self.h, c)
      pyxel.rectb(self.x, self.y, self.w, self.h, 1)
      pyxel.text(self.x + 5, self.y + (self.h/2-3), self.caption, 0)
      


      
APP()

