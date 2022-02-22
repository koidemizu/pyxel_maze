# -*- coding: utf-8 -*-
import pyxel

def draw_wall(w):
#Draw wall 1------------------------------------------------------------------      
      if w[0][0] == (1, 0):
          pyxel.line(0, 0, 50, 29, 6)
          pyxel.line(0, 0, 0, 150, 6)
          pyxel.line(0, 150, 50, 121, 6)
          pyxel.line(50, 29, 50, 121, 6)
      elif w[0][0] == (1, 1):
          pyxel.line(0, 0, 50, 29, 9)
          pyxel.line(0, 0, 0, 150, 9)
          pyxel.line(0, 150, 50, 121, 9)
          pyxel.line(50, 29, 50, 121, 9)          
      elif w[0][0] == (2, 1):
          pyxel.line(0, 0, 50, 29, 10)
          pyxel.line(0, 0, 0, 150, 10)
          pyxel.line(0, 150, 50, 121, 10)
          pyxel.line(50, 29, 50, 121, 10)               
      elif w[0][0] == (3, 1):
          pyxel.line(0, 0, 50, 29, 2)
          pyxel.line(0, 0, 0, 150, 2)
          pyxel.line(0, 150, 50, 121, 2)
          pyxel.line(50, 29, 50, 121, 2)                
      elif w[0][0] == (4, 1):
          pyxel.line(0, 0, 50, 29, 7)
          pyxel.line(0, 0, 0, 150, 7)
          pyxel.line(0, 150, 50, 121, 7)
          pyxel.line(50, 29, 50, 121, 7)                 
      elif w[0][0] == (5, 1):
          pyxel.line(0, 0, 50, 29, 7)
          pyxel.line(0, 0, 0, 150, 7)
          pyxel.line(0, 150, 50, 121, 7)
          pyxel.line(50, 29, 50, 121, 7)                           
      else:
          pyxel.line(0, 29, 50, 29, 6)
          pyxel.line(0, 121, 50, 121, 6)
          
      if w[0][1] == (1, 0):       
          pyxel.line(256, 0, 205, 29, 6)
          pyxel.line(256, 150, 205, 121, 6)      
          pyxel.line(255, 0, 255, 150, 6)
          pyxel.line(205, 29, 205, 121, 6)
      elif w[0][1] == (1, 1):       
          pyxel.line(256, 0, 205, 29, 9)
          pyxel.line(256, 150, 205, 121, 9)      
          pyxel.line(255, 0, 255, 150, 9)
          pyxel.line(205, 29, 205, 121, 9)
      elif w[0][1] == (2, 1):       
          pyxel.line(256, 0, 205, 29, 10)
          pyxel.line(256, 150, 205, 121, 10)      
          pyxel.line(255, 0, 255, 150, 10)
          pyxel.line(205, 29, 205, 121, 10)         
      elif w[0][1] == (3, 1):       
          pyxel.line(256, 0, 205, 29, 2)
          pyxel.line(256, 150, 205, 121, 2)      
          pyxel.line(255, 0, 255, 150, 2)
          pyxel.line(205, 29, 205, 121, 2)             
      elif w[0][1] == (4, 1):       
          pyxel.line(256, 0, 205, 29, 7)
          pyxel.line(256, 150, 205, 121, 7)      
          pyxel.line(255, 0, 255, 150, 7)
          pyxel.line(205, 29, 205, 121, 7)             
      elif w[0][1] == (5, 1):       
          pyxel.line(256, 0, 205, 29, 7)
          pyxel.line(256, 150, 205, 121, 7)      
          pyxel.line(255, 0, 255, 150, 7)
          pyxel.line(205, 29, 205, 121, 7)                       
      else:
          pyxel.line(256, 29, 205, 29, 6)
          pyxel.line(256, 121, 205, 121, 6)
#-----------------------------------------------------------------------------          

#Draw wall 2------------------------------------------------------------------                    
      if w[1][0] == (1, 0):       
          pyxel.line(50, 29, 80, 45, 12)
          pyxel.line(50, 121, 80, 105, 12)
          pyxel.line(50, 29, 50, 121, 12)
          pyxel.line(80, 45, 80, 105, 12)
      elif w[1][0] == (1, 1):       
          pyxel.line(50, 29, 80, 45, 9)
          pyxel.line(50, 121, 80, 105, 9)
          pyxel.line(50, 29, 50, 121, 9)
          pyxel.line(80, 45, 80, 105, 9)
      elif w[1][0] == (2, 1):       
          pyxel.line(50, 29, 80, 45, 10)
          pyxel.line(50, 121, 80, 105, 10)
          pyxel.line(50, 29, 50, 121, 10)
          pyxel.line(80, 45, 80, 105, 10)          
      elif w[1][0] == (3, 1):       
          pyxel.line(50, 29, 80, 45, 2)
          pyxel.line(50, 121, 80, 105, 2)
          pyxel.line(50, 29, 50, 121, 2)
          pyxel.line(80, 45, 80, 105, 2)                    
      elif w[1][0] == (4, 1):       
          pyxel.line(50, 29, 80, 45, 7)
          pyxel.line(50, 121, 80, 105, 7)
          pyxel.line(50, 29, 50, 121, 7)
          pyxel.line(80, 45, 80, 105, 7)                    
      elif w[1][0] == (5, 1):       
          pyxel.line(50, 29, 80, 45, 7)
          pyxel.line(50, 121, 80, 105, 7)
          pyxel.line(50, 29, 50, 121, 7)
          pyxel.line(80, 45, 80, 105, 7)                              
      else:          
          pyxel.line(79, 45, 51, 45, 12)
          pyxel.line(79, 105, 51, 105, 12)
          
      if w[1][1] == (1, 0):       
         pyxel.line(205, 29, 175, 45, 12)
         pyxel.line(205, 121, 175, 105, 12)
         pyxel.line(205, 29, 205, 121, 12)
         pyxel.line(175, 45, 175, 105, 12)
      elif w[1][1] == (1, 1):       
         pyxel.line(205, 29, 175, 45, 9)
         pyxel.line(205, 121, 175, 105, 9)
         pyxel.line(205, 29, 205, 121, 9)
         pyxel.line(175, 45, 175, 105, 9)
      elif w[1][1] == (2, 1):       
         pyxel.line(205, 29, 175, 45, 10)
         pyxel.line(205, 121, 175, 105, 10)
         pyxel.line(205, 29, 205, 121, 10)
         pyxel.line(175, 45, 175, 105, 10)         
      elif w[1][1] == (3, 1):       
         pyxel.line(205, 29, 175, 45, 2)
         pyxel.line(205, 121, 175, 105, 2)
         pyxel.line(205, 29, 205, 121, 2)
         pyxel.line(175, 45, 175, 105, 2)                  
      elif w[1][1] == (4, 1):       
         pyxel.line(205, 29, 175, 45, 7)
         pyxel.line(205, 121, 175, 105, 7)
         pyxel.line(205, 29, 205, 121, 7)
         pyxel.line(175, 45, 175, 105, 7)                  
      elif w[1][1] == (5, 1):       
         pyxel.line(205, 29, 175, 45, 7)
         pyxel.line(205, 121, 175, 105, 7)
         pyxel.line(205, 29, 205, 121, 7)
         pyxel.line(175, 45, 175, 105, 7)                           
      else:          
          pyxel.line(176, 45, 204, 45, 12)
          pyxel.line(176, 105, 204, 105, 12)      
#----------------------------------------------------------------------------          
      
#Draw wall 3-----------------------------------------------------------------                  
      if w[2][0] == (1, 0):       
          pyxel.line(80, 45, 97, 55, 5)
          pyxel.line(80, 105, 97, 95, 5)
          pyxel.line(80, 45, 80, 105, 5)
          pyxel.line(97, 55, 97, 95, 5)
      elif w[2][0] == (1, 1):       
          pyxel.line(80, 45, 97, 55, 9)
          pyxel.line(80, 105, 97, 95, 9)
          pyxel.line(80, 45, 80, 105, 9)
          pyxel.line(97, 55, 97, 95, 9)
      elif w[2][0] == (2, 1):       
          pyxel.line(80, 45, 97, 55, 10)
          pyxel.line(80, 105, 97, 95, 10)
          pyxel.line(80, 45, 80, 105, 10)
          pyxel.line(97, 55, 97, 95, 10)          
      elif w[2][0] == (3, 1):       
          pyxel.line(80, 45, 97, 55, 2)
          pyxel.line(80, 105, 97, 95, 2)
          pyxel.line(80, 45, 80, 105, 2)
          pyxel.line(97, 55, 97, 95, 2)                    
      elif w[2][0] == (4, 1):       
          pyxel.line(80, 45, 97, 55, 7)
          pyxel.line(80, 105, 97, 95, 7)
          pyxel.line(80, 45, 80, 105, 7)
          pyxel.line(97, 55, 97, 95, 7)                    
      elif w[2][0] == (5, 1):       
          pyxel.line(80, 45, 97, 55, 7)
          pyxel.line(80, 105, 97, 95, 7)
          pyxel.line(80, 45, 80, 105, 7)
          pyxel.line(97, 55, 97, 95, 7)                              
      else:
          pyxel.line(97, 55, 81, 55, 5)
          pyxel.line(97, 95, 81, 95, 5)
          
      if w[2][1] == (1, 0):       
          pyxel.line(175, 45, 158, 55, 5)
          pyxel.line(175, 105, 158, 95, 5)
          pyxel.line(175, 45, 175, 105, 5)
          pyxel.line(158, 55, 158, 95, 5)
      elif w[2][1] == (1, 1):       
          pyxel.line(175, 45, 158, 55, 9)
          pyxel.line(175, 105, 158, 95, 9)
          pyxel.line(175, 45, 175, 105, 9)
          pyxel.line(158, 55, 158, 95, 9)
      elif w[2][1] == (2, 1):       
          pyxel.line(175, 45, 158, 55, 10)
          pyxel.line(175, 105, 158, 95, 10)
          pyxel.line(175, 45, 175, 105, 10)
          pyxel.line(158, 55, 158, 95, 10)          
      elif w[2][1] == (3, 1):       
          pyxel.line(175, 45, 158, 55, 2)
          pyxel.line(175, 105, 158, 95, 2)
          pyxel.line(175, 45, 175, 105, 2)
          pyxel.line(158, 55, 158, 95, 2)                    
      elif w[2][1] == (4, 1):       
          pyxel.line(175, 45, 158, 55, 7)
          pyxel.line(175, 105, 158, 95, 7)
          pyxel.line(175, 45, 175, 105, 7)
          pyxel.line(158, 55, 158, 95, 7)                    
      elif w[2][1] == (5, 1):       
          pyxel.line(175, 45, 158, 55, 7)
          pyxel.line(175, 105, 158, 95, 7)
          pyxel.line(175, 45, 175, 105, 7)
          pyxel.line(158, 55, 158, 95, 7)                              
      else:
          pyxel.line(158, 55, 174, 55, 5)
          pyxel.line(158, 95, 174, 95, 5)
#----------------------------------------------------------------------------

#Draw wall 4-----------------------------------------------------------------                  
      if w[3][0] == (1, 0):       
          pyxel.line(97, 55, 108, 60, 1)
          pyxel.line(97, 95, 108, 90, 1)
          pyxel.line(97, 55, 97, 95, 1)
          pyxel.line(108, 60, 108, 90, 1)    
      elif w[3][0] == (1, 1):       
          pyxel.line(97, 55, 108, 60, 9)
          pyxel.line(97, 95, 108, 90, 9)
          pyxel.line(97, 55, 97, 95, 9)
          pyxel.line(108, 60, 108, 90, 9)              
      elif w[3][0] == (2, 1):       
          pyxel.line(97, 55, 108, 60, 10)
          pyxel.line(97, 95, 108, 90, 10)
          pyxel.line(97, 55, 97, 95, 10)
          pyxel.line(108, 60, 108, 90, 10)    
      elif w[3][0] == (3, 1):       
          pyxel.line(97, 55, 108, 60, 2)
          pyxel.line(97, 95, 108, 90, 2)
          pyxel.line(97, 55, 97, 95, 2)
          pyxel.line(108, 60, 108, 90, 2)           
      elif w[3][0] == (4, 1):       
          pyxel.line(97, 55, 108, 60, 7)
          pyxel.line(97, 95, 108, 90, 7)
          pyxel.line(97, 55, 97, 95, 7)
          pyxel.line(108, 60, 108, 90, 7)                     
      elif w[3][0] == (5, 1):       
          pyxel.line(97, 55, 108, 60, 7)
          pyxel.line(97, 95, 108, 90, 7)
          pyxel.line(97, 55, 97, 95, 7)
          pyxel.line(108, 60, 108, 90, 7)                     
          
      if w[3][1] == (1, 0):       
         pyxel.line(158, 55, 148, 60, 1)
         pyxel.line(158, 95, 148, 90, 1)  
         pyxel.line(158, 55, 158, 95, 1)
         pyxel.line(148, 60, 148, 90, 1)      
      elif w[3][1] == (1, 1):       
         pyxel.line(158, 55, 148, 60, 9)
         pyxel.line(158, 95, 148, 90, 9)  
         pyxel.line(158, 55, 158, 95, 9)
         pyxel.line(148, 60, 148, 90, 9)      
      elif w[3][1] == (2, 1):       
         pyxel.line(158, 55, 148, 60, 10)
         pyxel.line(158, 95, 148, 90, 10)
         pyxel.line(158, 55, 158, 95, 10)
         pyxel.line(148, 60, 148, 90, 10)    
      elif w[3][1] == (3, 1):       
         pyxel.line(158, 55, 148, 60, 2)
         pyxel.line(158, 95, 148, 90, 2)
         pyxel.line(158, 55, 158, 95, 2)
         pyxel.line(148, 60, 148, 90, 2)            
      elif w[3][1] == (4, 1):       
         pyxel.line(158, 55, 148, 60, 7)
         pyxel.line(158, 95, 148, 90, 7)
         pyxel.line(158, 55, 158, 95, 7)
         pyxel.line(148, 60, 148, 90, 7)            
      elif w[3][1] == (5, 1):       
         pyxel.line(158, 55, 148, 60, 7)
         pyxel.line(158, 95, 148, 90, 7)
         pyxel.line(158, 55, 158, 95, 7)
         pyxel.line(148, 60, 148, 90, 7)                     
#-----------------------------------------------------------------------------     

def draw_paint (p):
#Draw Floor paint-------------------------------------------------------------
      if p[0] == 1:
          pyxel.line(67, 145, 178, 130, 8)
          pyxel.line(70, 130, 178, 145, 8)
      if p == 1:
          pyxel.line(95, 117, 155, 107, 8)
          pyxel.line(95, 107, 155, 117, 8)
      if p == 1:
          pyxel.line(110, 104, 140, 97, 1)
          pyxel.line(110, 97, 140, 104, 1)        
      if p == 1:
          pyxel.line(115, 92, 135, 95, 1)
          pyxel.line(115, 95, 135, 92, 1)          
#-----------------------------------------------------------------------------   

def draw_dead_end(d):
#Draw Dead-End----------------------------------------------------------------
      
      if d[0] == 0:
          pass
      elif d[0] == 1:
          if d[1] == (1, 0):
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 6)
          elif d[1] == (1, 1):
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 9)              
          elif d[1] == (2, 1):             
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 10)        
                                                 
              gw = 10
              gx1 = 100
              gx2 = 150
              gx3 = gx1 - gw
              gx4 = gx2 + gw
              gx5 = 115
              gx6 = gx5 + gw
              gx7 = gx6 + gw
              gx8 = 106
              gx9 = gx8 + gw
              gx10 = 137
              gx11 = 144
              
              gy1 = 90
              gy2 = 70
              gy3 = 50
              
              pyxel.rectb(gx1 - 15, gy3 - 15, 80, 75, 9) 
              pyxel.rect(gx1 - 13, gy1 + 1, 76, 17, 13) 
              
              pyxel.line(gx3, gy1, gx4, gy1, 1)
              pyxel.line(gx1, gy2, gx2, gy2, 1)
              pyxel.line(gx1, gy2, gx3, gy1, 1)
              pyxel.line(gx2, gy2, gx4, gy1, 1)
              pyxel.line(gx5, gy2, gx6, gy1, 1)
              pyxel.line(gx7, gy2, gx6, gy1, 1)
              pyxel.line(gx8, gy2, gx9, gy3, 1)
              pyxel.line(gx11, gy2, gx10, gy3, 1)
              pyxel.line(gx9, gy3, gx10, gy3, 1)
              pyxel.fill(gx5 + 1, gy3 + 1, 10)
              pyxel.fill(gx1 + 1, gy2 + 1, 10)
              pyxel.fill(gx11 + 1, gy2 + 1, 10)
              pyxel.line(gx2, gy2, gx4, gy1 - 1, 7)
              pyxel.line(gx11, gy2, gx10 - 1, gy3, 7)
              pyxel.line(gx5, gy2, gx6, gy1 - 1, 7)
              
              lp = 2
              pyxel.line(gx2 - lp, gy2 + lp, gx4 - lp*2, gy1 - 1 - lp, 7)
              pyxel.line(gx11 + 1 - lp*2, gy2 - lp, gx10 - lp, gy3 - 1 + lp, 7)
              pyxel.line(gx5 - lp, gy2 + lp, gx6 - lp*2, gy1 - 1 - lp, 7)
              
              pyxel.line(gx1 + 65, gy3 - 15, 204, 31, 9)
              pyxel.line(gx1 + 65, gy3 + 60, 204, 120, 9)
              pyxel.line(190, 33, 190, 115, 9)
              pyxel.line(186, 33, 186, 114, 9)
              pyxel.line(205, 31, 205, 121, 9)
              
          elif d[1] == (3, 1):             
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 2)                    

          elif d[1] == (4, 1):             
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 7)      

          elif d[1] == (5, 1):             
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 7)      
              
      elif d[0] == 2:
          if d[1] == (1, 0):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 12)
          elif d[1] == (1, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 9)              
          elif d[1] == (2, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 10)          
              pyxel.rectb(106, 54, 44, 42, 9)
          elif d[1] == (3, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 2)          
              #pyxel.rectb(106, 54, 44, 42, 9)
          elif d[1] == (4, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 7)          
              #pyxel.rectb(106, 54, 44, 42, 9)
          elif d[1] == (5, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 7)          
              #pyxel.rectb(106, 54, 44, 42, 9)              
              
      elif d[0] == 3:
          if d[1] == (1, 0):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 5)
          elif d[1] == (1, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 9)              
          elif d[1] == (2, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 10)           
              pyxel.rectb(115, 62, 28, 25, 9)
          elif d[1] == (3, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 2)           
              #pyxel.rectb(115, 62, 28, 25, 9)
          elif d[1] == (4, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 7)           
              #pyxel.rectb(115, 62, 28, 25, 9)
          elif d[1] == (5, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 7)           
              #pyxel.rectb(115, 62, 28, 25, 9)              
      else:
          pass
#-----------------------------------------------------------------------------   

def draw_bubble(b, n):
#Bubble draw 1--------------------------------------------------------------     
      bn = len(b)
      for bi in range(bn) :
          bx = b[bi].bub_x
          by = b[bi].bub_y
          bc = b[bi].bub_c
          bv = b[bi].bub_v
          
          if bi % 2 == n:
              if bv == 0:
                  pyxel.circb(bx, by, 10, bc)
                  pyxel.circb(bx - 5, by - 5, 3, bc)
                  pyxel.circb(bx - 6, by - 6, 1, 7)
              elif bv == 1:     
                  pyxel.circb(bx, by, 7, 6)
                  pyxel.circb(bx - 3, by - 3, 2, bc)
                  pyxel.circb(bx - 4, by - 4, 1, bc)      
              elif bv == 2:
                  pyxel.circb(bx, by, 5, 6)
                  pyxel.circb(bx - 3, by - 1, 1, bc)
                  pyxel.circb(bx - 4, by - 2, 1, bc)            
#------------------------------------------------------------------------------      

def draw_game_over():
      pyxel.circ(124, 87, 45, 0)
      pyxel.text(105, 70, "GAME OVER!!", 8)
      pyxel.text(105, 90, "R: RETRY", 8)
      pyxel.text(105, 100, "Q: QUIT", 8)    
#------------------------------------------------------------------------------      

def draw_enemy(ep, d):
#Draw enemy------------------------------------------------------------------
       
      if ((ep == 3 and ep < d[0])
         or (ep == 3 and d[0] == 0)) : 
       #Pos 1------------------------------------------------------------------
          ex = 117
          ey = 75
          pyxel.circ(ex, ey, 1, 9)
          pyxel.circ(ex - 1, ey + 1, 1, 9)
          pyxel.circ(ex + 16, ey, 1, 9)
          pyxel.circ(ex + 16 + 1, ey + 1, 1, 9)
          
      elif ((ep == 2 and ep < d[0])
            or (ep == 2 and d[0] == 0)): 
       #Pos 2------------------------------------------------------------------
          ex = 114
          ey = 70
          pyxel.circ(ex, ey, 2, 9)
          pyxel.circ(ex - 1, ey + 1, 2, 9)
          pyxel.circ(ex + 26, ey, 2, 9)
          pyxel.circ(ex + 26 + 1, ey + 1, 2, 9)      
          
      elif ((ep == 1 and ep < d[0])
            or (ep == 1 and d[0] == 0)):
      #Pos 3-------------------------------------------------------------------
          ex = 109
          ey = 65
          pyxel.circ(ex, ey, 3, 9)
          pyxel.circ(ex - 1, ey + 1, 3, 9)
          pyxel.circ(ex + 36, ey, 3, 9)
          pyxel.circ(ex + 36 + 1, ey + 1, 3, 9)
          pyxel.circ(ex - 1, ey + 1, 2, 10)
          pyxel.circ(ex + 36 + 1, ey + 1, 2, 10)
      
      #teeth 1----------------------------------------------------------------
          x = 105
          x2 = 110
          y = 100
          x3 = x + ((x2 - x) / 2)
          y3 = 90
            
          for i in range(5):
              vx =  i * 4.3
              vy =  i * 5
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)    
      
      #teeth 2-----------------------------------------------------------------
          x = 145
          x2 = 150
          y = 100
          x3 = x + ((x2 - x) / 2)
          y3 = 90
       
          for i in range(5):
              vx =  i * 4.3
              vy =  i * 5
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)              
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)              
      
      #teeth 3----------------------------------------------------------------
          x = 105
          x2 = 110
          y = 87
          x3 = x + ((x2 - x) / 2)
          y3 = 97
      
          for i in range(5):
              vx =  i * 4.3
              vy =  i * -5          
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)     
      
      #teeth 4----------------------------------------------------------------
          x = 145
          x2 = 150
          y = 87
          x3 = x + ((x2 - x) / 2)
          y3 = 97
      
          for i in range(5):
              vx =  i * 4.3
              vy =  i * -5
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)      
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)      
     #------------------------------------------------------------------------
      elif ep == 0:
      #Pos 4-------------------------------------------------------------------
          ex = 85
          ey = 30
          pyxel.circ(ex, ey, 4, 9)
          pyxel.circ(ex - 1, ey + 1, 4, 9)
          pyxel.circ(ex + 80, ey, 4, 9)      
          pyxel.circ(ex + 80 + 1, ey + 1, 4, 9)
          pyxel.circ(ex + 80 + 1, ey + 1, 3, 10)
          pyxel.circ(ex - 1, ey + 1, 3, 10)  
      
      #teeth 1----------------------------------------------------------------
          x = 75
          x2 = 85
          y = 110
          x3 = x + ((x2 - x) / 2)
          y3 = 90
            
          for i in range(5):
              vx =  i * 10
              vy =  i * 8
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)    
      
      #teeth 2-----------------------------------------------------------------
          x = 165
          x2 = 175
          y = 110
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * 8
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)              
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)              
      
      #teeth 3----------------------------------------------------------------
          x = 75
          x2 = 85
          y = 50
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * - 8          
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)     
      
      #teeth 4----------------------------------------------------------------
          x = 165
          x2 = 175
          y = 50
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * - 8
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)      
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)      
#-----------------------------------------------------------------------------    

def draw_compass(po, m, wl, pa, em, emf, pc, gm):
#Draw Compass-----------------------------------------------------------------
      pyxel.ellib(-50, -10, 360, 170, 5)
      pyxel.fill(0, 1, 0)
      pyxel.rect(3, 2, 15, 7, 0)
      pyxel.fill(0, 140, 0)
      pyxel.rect(0, 141, 17, 15, 0)
      pyxel.fill(255, 9, 0)
      pyxel.rect(242, 0, 15, 9, 0)
      pyxel.fill(255, 141, 0)
      pyxel.rect(242, 141, 15, 9, 0)
      
      pyxel.rectb(0, 0, 256, 151, 1)      
      
      pyxel.rect(0, 150, 256, 106, 0)
      pyxel.rectb(0, 150, 256, 106, 1)     
      pyxel.rectb(110, 150, 146, 106, 1)           
      pyxel.rectb(114, 154, 137, 97, 5)       
        
      #Wall
      for d0 in range(5):
          if (po[1]-1 < 0 or 
              po[0]-2+d0 < 0 or po[0]-2+d0 > 31):
              pyxel.rect(17+10*d0, 167, 9, 9, 7)
          elif m[po[1]-1][po[0]-2+d0] in wl:
              pyxel.rect(17+10*d0, 167, 9, 9, 7)
          elif m[po[1]-1][po[0]-2+d0] == (2, 0):
              pyxel.rect(17+10*d0, 167, 9, 9, 3)              
          elif m[po[1]-1][po[0]-2+d0] == (0, 1):
              pyxel.rectb(17+10*d0, 167, 9, 9, 8)              
      for d1 in range(5):
          if po[0]-2+d1 < 0 or po[0]-2+d1 > 31:
              pyxel.rect(17+10*d1, 177, 9, 9, 7)
          elif m[po[1]][po[0]-2+d1] in wl:
              pyxel.rect(17+10*d1, 177, 9, 9, 7)
          elif m[po[1]][po[0]-2+d1] == (2, 0):
              pyxel.rect(17+10*d1, 177, 9, 9, 3)              
          elif m[po[1]][po[0]-2+d1] == (0, 1):
              pyxel.rectb(17+10*d1, 177, 9, 9, 8)              
      for d2 in range(5):
          if (po[1]+1 > 31 or
              po[0]-2+d2 < 0 or po[0]-2+d2 > 31):
              pyxel.rect(17+10*d2, 187, 9, 9, 7)
          elif m[po[1]+1][po[0]-2+d2] in wl:
              pyxel.rect(17+10*d2, 187, 9, 9, 7)
          elif m[po[1]+1][po[0]-2+d2] == (2, 0):
              pyxel.rect(17+10*d2, 187, 9, 9, 3)              
          elif m[po[1]+1][po[0]-2+d2] == (0, 1):
              pyxel.rectb(17+10*d2, 187, 9, 9, 8)              
      for d3 in range(5):
          if (po[1]+2 > 31 or
              po[0]-2+d3 < 0 or po[0]-2+d3 > 31):
              pyxel.rect(17+10*d3, 197, 9, 9, 7)      
          elif m[po[1]+2][po[0]-2+d3] in wl:
              pyxel.rect(17+10*d3, 197, 9, 9, 7)              
          elif m[po[1]+2][po[0]-2+d3] == (2, 0):
              pyxel.rect(17+10*d3, 197, 9, 9, 3)                            
          elif m[po[1]+2][po[0]-2+d3] == (0, 1):
              pyxel.rectb(17+10*d3, 197, 9, 9, 8)                            
            
      #Prayer
      if pa == 1:
          pyxel.tri(41, 178, 37, 185, 45, 185, 1)
      elif pa == 2:
          pyxel.tri(45, 181, 37, 178, 37, 185, 1)
      elif pa == 3:
          pyxel.tri(41, 185, 37, 178, 45, 178, 1)
      elif pa == 4:
          pyxel.tri(37, 183, 45, 178, 45, 186, 1)
          
      pyxel.circb(40, 185, 27, 5)   
      pyxel.circb(40, 185, 32, 1)   
      pyxel.fill(18, 168, 0)
      pyxel.fill(64, 168, 0)
      pyxel.fill(63, 202, 0)
      pyxel.fill(18, 204, 0)
      
      #Enemy message
      pyxel.ellib(12, 220, 90, 20, 5)
      pyxel.rectb(12, 220, 90, 20, 1)
      #pyxel.fill(42, 228, 3)
      if emf == False:
          c = 3
      else:
          c = 8
      pyxel.text(23, 228, em, c)            
      
      #Paint count
      pyxel.blt(74, 160, 1, 0, 0, 16, 16, 15)
      pyxel.text(90, 170, "x  " + str(pc), 7)
      
      #Message
      for m in range(len(gm.msg)):
          if gm.msg[m][1] == 100:
              pyxel.text(120, 160 + m*10, gm.msg[m][0], pyxel.frame_count % 16)
          else:
              pyxel.text(120, 160 + m * 10, gm.msg[m][0], gm.msg[m][1])
                
#-----------------------------------------------------------------------------          
     
 