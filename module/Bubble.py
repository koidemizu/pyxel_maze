# -*- coding: utf-8 -*-

class Bubble:
  def __init__(self, x, y, v, c, s):
      self.bub_x = x
      self.bub_y = y
      self.bub_v = v
      self.bub_c = c      
      self.bub_s = s
      
  def update(self):
      self.bub_y -= self.bub_s  
