# -*- coding: utf-8 -*-
import pyxel

class Enemy:
  def __init__(self, x, y, m, p):
      self.ene_x = x
      self.ene_y = y      
      self.ene_m = 1
      self.maze = m
      self.move_permit = p
      self.move_c = 0
      
  def update(self):
      if self.maze[self.ene_y - 1][self.ene_x] in self.move_permit:
          self.move_c += 1
      if self.maze[self.ene_y + 1][self.ene_x] in self.move_permit:
          self.move_c += 1
      if self.maze[self.ene_y][self.ene_x + 1] in self.move_permit:
          self.move_c += 1
      if self.maze[self.ene_y][self.ene_x - 1] in self.move_permit:
          self.move_c += 1
          
      if self.move_c > 2:
          self.ene_m = pyxel.rndi(1, 4)
          
      #ene_m = Angle E=Enemy
      #    ^
      #    1
      #<4  E   2>
      #    3
      #    v
      #     
      if self.ene_m == 1:
          if self.maze[self.ene_y - 1][self.ene_x] in self.move_permit:
              self.ene_y = self.ene_y - 1
              self.ene_m = 1
          else:
              self.ene_m = pyxel.rndi(1, 4)
      elif self.ene_m == 3:
          if self.maze[self.ene_y + 1][self.ene_x] in self.move_permit:
              self.ene_y = self.ene_y + 1
              self.ene_m = 3
          else:
              self.ene_m = pyxel.rndi(1, 4)
      if self.ene_m == 2:
          if self.maze[self.ene_y][self.ene_x + 1] in self.move_permit:
              self.ene_x = self.ene_x + 1
              self.ene_m = 2
          else:
              self.ene_m = pyxel.rndi(1, 4)
      if self.ene_m == 4:
          if self.maze[self.ene_y][self.ene_x - 1] in self.move_permit:
              self.ene_x = self.ene_x - 1
              self.ene_m = 4
          else:
              self.ene_m = pyxel.rndi(1, 4)           
              
      self.move_c = 0


