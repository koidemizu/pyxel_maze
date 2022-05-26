# -*- coding: utf-8 -*-

class GameMsg:
  def __init__(self):
      self.msg = [
                 ["",3],
                 ["",5],
                 ["",6],
                 ["",7],
                 ["",8],
                 ["",9],
                 ["",10],
                 ["You have entered the maze.",3],
                 ["Find the gold!",10],                 
                 ]    
      
  def update(self, msg, c):
      self.msg.pop(0)
      self.msg.append([msg, c])
