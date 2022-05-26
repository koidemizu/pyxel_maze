# -*- coding: utf-8 -*-
import pyxel

def draw_wall(w, wl, wld, wll, wll2, wlf, wlm):       
          
#Draw wall 1------------------------------------------------------------------      
      if w[0][0] in wl:
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
          
      elif w[0][0] in wld:
          cc = draw_wall_cc(w[0][0])

          pyxel.line(0, 0, 50, 29, cc)
          pyxel.line(0, 0, 0, 150, cc)
          pyxel.line(0, 150, 50, 121, cc)
          pyxel.line(50, 29, 50, 121, cc)                
          
      elif w[0][0] in wll:
          pyxel.line(0, 0, 50, 29, 7)
          pyxel.line(0, 0, 0, 150, 7)
          pyxel.line(0, 150, 50, 121, 7)
          pyxel.line(50, 29, 50, 121, 7)                 
          
      elif w[0][0] in wll2:
          pyxel.line(0, 0, 50, 29, 7)
          pyxel.line(0, 0, 0, 150, 7)
          pyxel.line(0, 150, 50, 121, 7)
          pyxel.line(50, 29, 50, 121, 7)   

      elif w[0][0] in wlf:
          pyxel.line(0, 0, 50, 29, 13)
          pyxel.line(0, 0, 0, 150, 13)
          pyxel.line(0, 150, 50, 121, 13)
          pyxel.line(50, 29, 50, 121, 13)
          
      elif w[0][0] in wlm:
          pyxel.line(0, 0, 50, 29, 2)
          pyxel.line(0, 0, 0, 150, 2)
          pyxel.line(0, 150, 50, 121, 2)
          pyxel.line(50, 29, 50, 121, 2)          
          
      else:
          pyxel.line(0, 29, 50, 29, 6)
          pyxel.line(0, 121, 50, 121, 6)
          
      if w[0][1] in wl:    
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
          
      elif w[0][1] in wld:       
          cc = draw_wall_cc(w[0][1])  
          
          pyxel.line(256, 0, 205, 29, cc)
          pyxel.line(256, 150, 205, 121, cc)      
          pyxel.line(255, 0, 255, 150, cc)
          pyxel.line(205, 29, 205, 121, cc)     
          
      elif w[0][1] in wll:
          pyxel.line(256, 0, 205, 29, 7)
          pyxel.line(256, 150, 205, 121, 7)      
          pyxel.line(255, 0, 255, 150, 7)
          pyxel.line(205, 29, 205, 121, 7)    
          
      elif w[0][1] in wll2:
          pyxel.line(256, 0, 205, 29, 7)
          pyxel.line(256, 150, 205, 121, 7)      
          pyxel.line(255, 0, 255, 150, 7)
          pyxel.line(205, 29, 205, 121, 7)   
          
      elif w[0][1] in wlf:
          pyxel.line(256, 0, 205, 29, 13)
          pyxel.line(256, 150, 205, 121, 13)      
          pyxel.line(255, 0, 255, 150, 13)
          pyxel.line(205, 29, 205, 121, 13)             

      elif w[0][1] in wlm:
          pyxel.line(256, 0, 205, 29, 2)
          pyxel.line(256, 150, 205, 121, 2)      
          pyxel.line(255, 0, 255, 150, 2)
          pyxel.line(205, 29, 205, 121, 2)  
                    
      else:
          pyxel.line(256, 29, 205, 29, 6)
          pyxel.line(256, 121, 205, 121, 6)
#-----------------------------------------------------------------------------          

#Draw wall 2------------------------------------------------------------------                    
      if w[1][0] in wl:    
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
          
      elif w[1][0] in wld:  
          cc = draw_wall_cc(w[1][0])
          
          pyxel.line(50, 29, 80, 45, cc)
          pyxel.line(50, 121, 80, 105, cc)
          pyxel.line(50, 29, 50, 121, cc)
          pyxel.line(80, 45, 80, 105, cc)    
                
      elif w[1][0] in wll:
          pyxel.line(50, 29, 80, 45, 7)
          pyxel.line(50, 121, 80, 105, 7)
          pyxel.line(50, 29, 50, 121, 7)
          pyxel.line(80, 45, 80, 105, 7)    
                
      elif w[1][0] in wll2:
          pyxel.line(50, 29, 80, 45, 7)
          pyxel.line(50, 121, 80, 105, 7)
          pyxel.line(50, 29, 50, 121, 7)
          pyxel.line(80, 45, 80, 105, 7)     
          
      elif w[1][0] in wlf:
          pyxel.line(50, 29, 80, 45, 13)
          pyxel.line(50, 121, 80, 105, 13)
          pyxel.line(50, 29, 50, 121, 13)
          pyxel.line(80, 45, 80, 105, 13)               
          
      elif w[1][0] in wlm:
          pyxel.line(50, 29, 80, 45, 2)
          pyxel.line(50, 121, 80, 105, 2)
          pyxel.line(50, 29, 50, 121, 2)
          pyxel.line(80, 45, 80, 105, 2)                
                         
      else:          
          pyxel.line(79, 45, 51, 45, 12)
          pyxel.line(79, 105, 51, 105, 12)
          
      if w[1][1] in wl:   
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
         
      elif w[1][1] in wld:     
         cc = draw_wall_cc(w[1][1])
          
         pyxel.line(205, 29, 175, 45, cc)
         pyxel.line(205, 121, 175, 105, cc)
         pyxel.line(205, 29, 205, 121, cc)
         pyxel.line(175, 45, 175, 105, cc)   
               
      elif w[1][1] in wll:
         pyxel.line(205, 29, 175, 45, 7)
         pyxel.line(205, 121, 175, 105, 7)
         pyxel.line(205, 29, 205, 121, 7)
         pyxel.line(175, 45, 175, 105, 7)   
               
      elif w[1][1] in wll2:
         pyxel.line(205, 29, 175, 45, 7)
         pyxel.line(205, 121, 175, 105, 7)
         pyxel.line(205, 29, 205, 121, 7)
         pyxel.line(175, 45, 175, 105, 7)   
                        
      elif w[1][1] in wlf:
         pyxel.line(205, 29, 175, 45, 13)
         pyxel.line(205, 121, 175, 105, 13)
         pyxel.line(205, 29, 205, 121, 13)
         pyxel.line(175, 45, 175, 105, 13)   
         
      elif w[1][1] in wlm:
         pyxel.line(205, 29, 175, 45, 2)
         pyxel.line(205, 121, 175, 105, 2)
         pyxel.line(205, 29, 205, 121, 2)
         pyxel.line(175, 45, 175, 105, 2)           
         
      else:          
          pyxel.line(176, 45, 204, 45, 12)
          pyxel.line(176, 105, 204, 105, 12)      
#----------------------------------------------------------------------------          
      
#Draw wall 3-----------------------------------------------------------------                  
      if w[2][0] in wl:
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
          
      elif w[2][0] in wld:   
          cc = draw_wall_cc(w[2][0])
          
          pyxel.line(80, 45, 97, 55, cc)
          pyxel.line(80, 105, 97, 95, cc)
          pyxel.line(80, 45, 80, 105, cc)
          pyxel.line(97, 55, 97, 95, cc)   
                 
      elif w[2][0] in wll:
          pyxel.line(80, 45, 97, 55, 7)
          pyxel.line(80, 105, 97, 95, 7)
          pyxel.line(80, 45, 80, 105, 7)
          pyxel.line(97, 55, 97, 95, 7)  
                  
      elif w[2][0] in wll2:
          pyxel.line(80, 45, 97, 55, 7)
          pyxel.line(80, 105, 97, 95, 7)
          pyxel.line(80, 45, 80, 105, 7)
          pyxel.line(97, 55, 97, 95, 7)   
          
      elif w[2][0] in wlf:
          pyxel.line(80, 45, 97, 55, 13)
          pyxel.line(80, 105, 97, 95, 13)
          pyxel.line(80, 45, 80, 105, 13)
          pyxel.line(97, 55, 97, 95, 13)             
          
      elif w[2][0] in wlm:
          pyxel.line(80, 45, 97, 55, 2)
          pyxel.line(80, 105, 97, 95, 2)
          pyxel.line(80, 45, 80, 105, 2)
          pyxel.line(97, 55, 97, 95, 2)                 
                           
      else:
          pyxel.line(97, 55, 81, 55, 5)
          pyxel.line(97, 95, 81, 95, 5)
          
      if w[2][1] in wl:  
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
          
      elif w[2][1] in wld:
          cc = draw_wall_cc(w[2][1])
             
          pyxel.line(175, 45, 158, 55, cc)
          pyxel.line(175, 105, 158, 95, cc)
          pyxel.line(175, 45, 175, 105, cc)
          pyxel.line(158, 55, 158, 95, cc)    
                
      elif w[2][1] in wll:
          pyxel.line(175, 45, 158, 55, 7)
          pyxel.line(175, 105, 158, 95, 7)
          pyxel.line(175, 45, 175, 105, 7)
          pyxel.line(158, 55, 158, 95, 7)   
                 
      elif w[2][1] in wll2:
          pyxel.line(175, 45, 158, 55, 7)
          pyxel.line(175, 105, 158, 95, 7)
          pyxel.line(175, 45, 175, 105, 7)
          pyxel.line(158, 55, 158, 95, 7)   

      elif w[2][1] in wlf:
          pyxel.line(175, 45, 158, 55, 13)
          pyxel.line(175, 105, 158, 95, 13)
          pyxel.line(175, 45, 175, 105, 13)
          pyxel.line(158, 55, 158, 95, 13)   

      elif w[2][1] in wlm:
          pyxel.line(175, 45, 158, 55, 2)
          pyxel.line(175, 105, 158, 95, 2)
          pyxel.line(175, 45, 175, 105, 2)
          pyxel.line(158, 55, 158, 95, 2)   
                           
      else:
          pyxel.line(158, 55, 174, 55, 5)
          pyxel.line(158, 95, 174, 95, 5)
#----------------------------------------------------------------------------

#Draw wall 4-----------------------------------------------------------------                  
      if w[3][0] in wl:   
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
          
      elif w[3][0] in wld:
          cc = draw_wall_cc(w[3][0])
          
          pyxel.line(97, 55, 108, 60, cc)
          pyxel.line(97, 95, 108, 90, cc)
          pyxel.line(97, 55, 97, 95, cc)
          pyxel.line(108, 60, 108, 90, cc) 
          
      elif w[3][0] in wll:
          pyxel.line(97, 55, 108, 60, 7)
          pyxel.line(97, 95, 108, 90, 7)
          pyxel.line(97, 55, 97, 95, 7)
          pyxel.line(108, 60, 108, 90, 7) 
                    
      elif w[3][0] in wll2:
          pyxel.line(97, 55, 108, 60, 7)
          pyxel.line(97, 95, 108, 90, 7)
          pyxel.line(97, 55, 97, 95, 7)
          pyxel.line(108, 60, 108, 90, 7)                     
          
      elif w[3][0] in wlf:
          pyxel.line(97, 55, 108, 60, 13)
          pyxel.line(97, 95, 108, 90, 13)
          pyxel.line(97, 55, 97, 95, 13)
          pyxel.line(108, 60, 108, 90, 13)                       
          
      elif w[3][0] in wlm:
          pyxel.line(97, 55, 108, 60, 2)
          pyxel.line(97, 95, 108, 90, 2)
          pyxel.line(97, 55, 97, 95, 2)
          pyxel.line(108, 60, 108, 90, 2)
          
      if w[3][1] in wl:  
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
         
      elif w[3][1] in wld:
         cc = draw_wall_cc(w[3][1])
           
         pyxel.line(158, 55, 148, 60, cc)
         pyxel.line(158, 95, 148, 90, cc)
         pyxel.line(158, 55, 158, 95, cc)
         pyxel.line(148, 60, 148, 90, cc)  
         
      elif w[3][1] in wll:
         pyxel.line(158, 55, 148, 60, 7)
         pyxel.line(158, 95, 148, 90, 7)
         pyxel.line(158, 55, 158, 95, 7)
         pyxel.line(148, 60, 148, 90, 7)  
          
      elif w[3][1] in wll2:
         pyxel.line(158, 55, 148, 60, 7)
         pyxel.line(158, 95, 148, 90, 7)
         pyxel.line(158, 55, 158, 95, 7)
         pyxel.line(148, 60, 148, 90, 7)                     
         
      elif w[3][1] in wlf:
         pyxel.line(158, 55, 148, 60, 13)
         pyxel.line(158, 95, 148, 90, 13)
         pyxel.line(158, 55, 158, 95, 13)
         pyxel.line(148, 60, 148, 90, 13)                      
         
      elif w[3][1] in wlm:
         pyxel.line(158, 55, 148, 60, 2)
         pyxel.line(158, 95, 148, 90, 2)
         pyxel.line(158, 55, 158, 95, 2)
         pyxel.line(148, 60, 148, 90, 2)                           
#-----------------------------------------------------------------------------   

def draw_wall_cc(w):
      if w[1] == 1:
        cc = 2
      elif w[1] == 2:
        cc = 8
      elif w[1] == 3:
        cc = 4
      elif w[1] == 4:
        cc = 9
      elif w[1] == 5:
        cc = 12       
      elif w[1] == 6:
        cc = 3          
      else:
        cc = 12            
     
      return cc

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

def draw_dead_end(d, wl, wld, wll, wll2, wlf, wlm, mz, pos):
#Draw Dead-End----------------------------------------------------------------
      if d[1][1] == 1:
          cc = 2
      elif d[1][1] == 2:
          cc = 8
      elif d[1][1] == 3:
          cc = 4
      elif d[1][1] == 4:
          cc = 9
      elif d[1][1] == 5:
          cc = 12       
      elif d[1][1] == 6:
          cc = 3 
          
      if d[0] == 0:
          pass
      elif d[0] == 1:
          if d[1] in wl:
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 6)
              
          elif d[1] in wlf:
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 13)              
              for f in range(12):
                 pyxel.rectb(50 + f * 13, 29, 156 - f *13, 93, 13)          
                 
          elif d[1] in wlm:
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 2)
              pyxel.rectb(89, 29, 78, 93, 2)
              pyxel.rectb(50, 102, 156, 20, 2)
              pyxel.rectb(50, 29, 156, 5, 2)
              draw_map_window(mz, 95, 35, pos)
                              
              
          elif d[1] == (1, 1):
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 36, 93, 9)              
              pyxel.rectb(150, 29, 70, 93, 9)
              
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
              
          elif d[1] in wld:              
              
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, cc)   
              
              pyxel.circb(128, 60, 25, 7)
              pyxel.circb(128, 93, 25, 7)
              pyxel.rect(103, 50, 51, 54, 0)
              pyxel.rectb(103, 50, 51, 54, 7)
              
              pyxel.line(106, 50, 150, 50, 0)
              pyxel.line(106, 103, 150, 103, 0)
              
              pyxel.line(107, 50, 107, 103, 7)
              
              pyxel.rectb(103, 59, 10, 5, 7)
              pyxel.rectb(103, 89, 10, 5, 7)
              
              #pyxel.circ(128, 58, 10, 7)
              pyxel.circb(128, 58, 10, 7)
              
              pyxel.circb(145, 78, 6, 7)
              pyxel.line(139, 78, 150, 78, 7)
              pyxel.line(145, 73, 145, 84, 7)              
              
          elif d[1] in wll:         
              
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 7)                                                        
              
              pyxel.rect(122, 68, 15, 25, 3)                          
              pyxel.rectb(122, 68, 15, 25, 7)                          
              
              pyxel.rect(125, 70, 9, 20, 0)                          
              pyxel.rectb(125, 70, 9, 20, 1)                          
              
              pyxel.rect(127, 60, 5, 15, 0)
              pyxel.rectb(127, 60, 5, 15, 7)
              
              pyxel.rect(122, 60, 15, 5, 8)
              pyxel.rectb(122, 60, 15, 5, 7)                            
              
              pyxel.rect(103, 50, 5, 54, 10)
              pyxel.rectb(103, 50, 5, 54, 13)                            
              pyxel.rect(113, 50, 5, 54, 10)
              pyxel.rectb(113, 50, 5, 54, 13)                            

              pyxel.rect(149, 50, 5, 54, 10)
              pyxel.rectb(149, 50, 5, 54, 13)                                          
              pyxel.rect(140, 50, 5, 54, 10)
              pyxel.rectb(140, 50, 5, 54, 13)                                                        
              
              pyxel.rectb(103, 50, 51, 54, 13)      
              
              pyxel.fill(110, 76, cc)
              pyxel.fill(146, 76, cc)
              

          elif d[1] in wll2:    
              
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 7)                                                        
              
              pyxel.rect(122, 68, 15, 25, 3)                          
              pyxel.rectb(122, 68, 15, 25, 7)                          
              
              pyxel.rect(125, 70, 9, 20, 0)                          
              pyxel.rectb(125, 70, 9, 20, 1)                          
              
              pyxel.rect(127, 83, 5, 15, 0)
              pyxel.rectb(127, 83, 5, 15, 7)
              
              pyxel.rect(122, 95, 15, 5, 8)
              pyxel.rectb(122, 95, 15, 5, 7)                            
              
              pyxel.rect(103, 50, 5, 54, 10)
              pyxel.rectb(103, 50, 5, 54, 13)                            
              pyxel.rect(113, 50, 5, 54, 10)
              pyxel.rectb(113, 50, 5, 54, 13)                            

              pyxel.rect(149, 50, 5, 54, 10)
              pyxel.rectb(149, 50, 5, 54, 13)                                          
              pyxel.rect(140, 50, 5, 54, 10)
              pyxel.rectb(140, 50, 5, 54, 13)                                                        
              
              pyxel.rectb(103, 50, 51, 54, 13)      
              
              pyxel.fill(110, 76, cc)
              pyxel.fill(146, 76, cc)
              
      elif d[0] == 2:
          if d[1] in wl:
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 12)
              
          elif d[1] in wlf:
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 13)
              for f in range(12):
                  pyxel.rectb(80 + f * 8, 45, 96 - f * 8, 61, 13)
                  
          elif d[1] == (1, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 20, 61, 9)              
              pyxel.rectb(150, 45, 25, 61, 9)              
              
          elif d[1] == (2, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 10)          
              pyxel.rectb(106, 54, 44, 42, 9)
              
          elif d[1] in wld:
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, cc)          
              
              pyxel.circb(128, 61, 13, 7)
              pyxel.circb(128, 88, 13, 7)
              pyxel.rect(115, 55, 27, 40, 0)
              pyxel.rectb(115, 55, 27, 40, 7)           
              
              pyxel.line(116, 55, 140, 55, 0)
              pyxel.line(116, 94, 140, 94, 0)
              
          elif d[1] in wll:
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 7)          
              
              pyxel.rectb(114, 60, 30, 30, 13)      
              
          elif d[1] in wll2:
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 7)          
              
              pyxel.rectb(114, 60, 30, 30, 13)        
              
          elif d[1] in wlm:
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 2)
              pyxel.rectb(80, 49, 96, 44, 2)
              
      elif d[0] == 3:
          if d[1] in wl:
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 5)
              
          elif d[1] in wlf:
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 13)
              for f in range(12):
                  pyxel.rectb(97 + 5 * f, 55, 62 - 5 * f, 41, 13)
              
          elif d[1] == (1, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 10, 41, 9)          
              pyxel.rectb(143, 55, 15, 41, 9)          
              
          elif d[1] == (2, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 10)           
              pyxel.rectb(115, 62, 28, 25, 9)
              
          elif d[1] in wld:
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, cc)           
              
              pyxel.rectb(119, 59, 20, 32, 7)       
              
          elif d[1] in wll:
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 7)           
              pyxel.rectb(120, 67, 17, 17, 13)
              
          elif d[1] in wll2:
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 7)           
              pyxel.rectb(120, 67, 17, 17, 13)      
              
          elif d[1] in wlm:
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 2)
              pyxel.rectb(97, 58, 62, 31, 2)
              
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

def draw_enemy(ep, d, c):
#Draw enemy------------------------------------------------------------------
      if c == 1:
          ci1 = 9
          ci2 = 10
          ct1 = 1
          ct2 = 7
      elif c == 2:  
          ci1 = 2
          ci2 = 8
          ct1 = 1
          ct2 = 11
      
      if ((ep == 3 and ep < d[0])
         or (ep == 3 and d[0] == 0)) : 
       #Pos 1------------------------------------------------------------------
          ex = 117
          ey = 75
          pyxel.circ(ex, ey, 1, ci1)
          pyxel.circ(ex - 1, ey + 1, 1, ci1)
          pyxel.circ(ex + 16, ey, 1, ci1)
          pyxel.circ(ex + 16 + 1, ey + 1, 1, ci1)
          
      elif ((ep == 2 and ep < d[0])
            or (ep == 2 and d[0] == 0)): 
       #Pos 2------------------------------------------------------------------
          ex = 114
          ey = 70
          pyxel.circ(ex, ey, 2, ci1)
          pyxel.circ(ex - 1, ey + 1, 2, ci1)
          pyxel.circ(ex + 26, ey, 2, ci1)
          pyxel.circ(ex + 26 + 1, ey + 1, 2, ci1)      
          
      elif ((ep == 1 and ep < d[0])
            or (ep == 1 and d[0] == 0)):
      #Pos 3-------------------------------------------------------------------
          ex = 109
          ey = 65
          pyxel.circ(ex, ey, 3, ci1)
          pyxel.circ(ex - 1, ey + 1, 3, ci1)
          pyxel.circ(ex + 36, ey, 3, ci1)
          pyxel.circ(ex + 36 + 1, ey + 1, 3, ci1)
          pyxel.circ(ex - 1, ey + 1, 2, ci2)
          pyxel.circ(ex + 36 + 1, ey + 1, 2, ci2)
      
      #teeth 1----------------------------------------------------------------
          x = 105
          x2 = 110
          y = 100
          x3 = x + ((x2 - x) / 2)
          y3 = 90
            
          for i in range(5):
              vx =  i * 4.3
              vy =  i * 5
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct1)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct2)    
      
      #teeth 2-----------------------------------------------------------------
          x = 145
          x2 = 150
          y = 100
          x3 = x + ((x2 - x) / 2)
          y3 = 90
       
          for i in range(5):
              vx =  i * 4.3
              vy =  i * 5
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct1)              
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct2)              
      
      #teeth 3----------------------------------------------------------------
          x = 105
          x2 = 110
          y = 87
          x3 = x + ((x2 - x) / 2)
          y3 = 97
      
          for i in range(5):
              vx =  i * 4.3
              vy =  i * -5          
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct2)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct1)     
      
      #teeth 4----------------------------------------------------------------
          x = 145
          x2 = 150
          y = 87
          x3 = x + ((x2 - x) / 2)
          y3 = 97
      
          for i in range(5):
              vx =  i * 4.3
              vy =  i * -5
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct2)      
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct1)      
     #------------------------------------------------------------------------
      elif ep == 0:
      #Pos 4-------------------------------------------------------------------
          ex = 85
          ey = 30
          pyxel.circ(ex, ey, 4, ci1)
          pyxel.circ(ex - 1, ey + 1, 4, ci1)
          pyxel.circ(ex + 80, ey, 4, ci1)      
          pyxel.circ(ex + 80 + 1, ey + 1, 4, ci1)
          pyxel.circ(ex + 80 + 1, ey + 1, 3, ci2)
          pyxel.circ(ex - 1, ey + 1, 3, ci2)  
      
      #teeth 1----------------------------------------------------------------
          x = 75
          x2 = 85
          y = 110
          x3 = x + ((x2 - x) / 2)
          y3 = 90
            
          for i in range(5):
              vx =  i * 10
              vy =  i * 8
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct1)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct2)    
      
      #teeth 2-----------------------------------------------------------------
          x = 165
          x2 = 175
          y = 110
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * 8
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct1)              
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct2)              
      
      #teeth 3----------------------------------------------------------------
          x = 75
          x2 = 85
          y = 50
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * - 8          
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct2)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, ct1)     
      
      #teeth 4----------------------------------------------------------------
          x = 165
          x2 = 175
          y = 50
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * - 8
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct2)      
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, ct1)      
#-----------------------------------------------------------------------------    

def draw_compass(po, m, wl, pa, em, emf, pc, gm, wln, sf, sc, fc):
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
              cw = m[po[1]-1][po[0]-2+d0]
              if cw in wln or sf == False:
                  ccw = 7
              else:
                  ccw = 9
              pyxel.rect(17+10*d0, 167, 9, 9, ccw)
          elif m[po[1]-1][po[0]-2+d0] == (2, 0):
              pyxel.rect(17+10*d0, 167, 9, 9, 3)              
          elif m[po[1]-1][po[0]-2+d0] == (0, 1):
              pyxel.rectb(17+10*d0, 167, 9, 9, 8)        
              
      for d1 in range(5):
          if po[0]-2+d1 < 0 or po[0]-2+d1 > 31:
              pyxel.rect(17+10*d1, 177, 9, 9, 7)
          elif m[po[1]][po[0]-2+d1] in wl:
              cw = m[po[1]][po[0]-2+d1]
              if cw in wln or sf == False:
                  ccw = 7
              else:
                  ccw = 9  
              pyxel.rect(17+10*d1, 177, 9, 9, ccw)
          elif m[po[1]][po[0]-2+d1] == (2, 0):
              pyxel.rect(17+10*d1, 177, 9, 9, 3)              
          elif m[po[1]][po[0]-2+d1] == (0, 1):
              pyxel.rectb(17+10*d1, 177, 9, 9, 8)    
              
      for d2 in range(5):
          if (po[1]+1 > 31 or
              po[0]-2+d2 < 0 or po[0]-2+d2 > 31):
              pyxel.rect(17+10*d2, 187, 9, 9, 7)
          elif m[po[1]+1][po[0]-2+d2] in wl:
              cw = m[po[1]+1][po[0]-2+d2]
              if cw in wln or sf == False:
                  ccw = 7
              else:
                  ccw = 9                
              pyxel.rect(17+10*d2, 187, 9, 9, ccw)
          elif m[po[1]+1][po[0]-2+d2] == (2, 0):
              pyxel.rect(17+10*d2, 187, 9, 9, 3)              
          elif m[po[1]+1][po[0]-2+d2] == (0, 1):
              pyxel.rectb(17+10*d2, 187, 9, 9, 8)  
              
      for d3 in range(5):
          if (po[1]+2 > 31 or
              po[0]-2+d3 < 0 or po[0]-2+d3 > 31):
              pyxel.rect(17+10*d3, 197, 9, 9, 7)      
          elif m[po[1]+2][po[0]-2+d3] in wl:
              cw = m[po[1]+2][po[0]-2+d3]
              if cw in wln or sf == False:
                  ccw = 7
              else:
                  ccw = 9                
              pyxel.rect(17+10*d3, 197, 9, 9, ccw)                                     
          elif m[po[1]+2][po[0]-2+d3] == (2, 0):
              pyxel.rect(17+10*d3, 197, 9, 9, 3)                            
          elif m[po[1]+2][po[0]-2+d3] == (0, 1):
              pyxel.rectb(17+10*d3, 197, 9, 9, 8)                            
            
      #Prayer
      if pa == 1:
          pyxel.tri(41, 178, 37, 185, 45, 185, 6)
      elif pa == 2:
          pyxel.tri(45, 181, 37, 178, 37, 185, 6)
      elif pa == 3:
          pyxel.tri(41, 185, 37, 178, 45, 178, 6)
      elif pa == 4:
          pyxel.tri(37, 183, 45, 178, 45, 186, 6)
          
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
      pyxel.text(72, 170, "(P)", 7)
      pyxel.blt(83, 160, 1, 0, 0, 16, 16, 15)
      pyxel.text(98, 170, "x " + str(pc), 7)
      
      #Scan count
      if sf == True:
          pyxel.text(72, 188, "(O)", 9)
          pyxel.blt(83, 178, 1, 16, 0, 16, 16, 15)
          pyxel.text(98, 188, "x " + str(sc), 9)      
          pyxel.circb(40, 183, pyxel.frame_count % 16 + 5, 9)   
      else:
          pyxel.text(72, 188, "(O)", 7)
          pyxel.blt(83, 178, 1, 16, 0, 16, 16, 15)
          pyxel.text(98, 188, "x " + str(sc), 7)                
      
      #Wall count
      pyxel.text(72, 206, "(I)", 7)
      pyxel.blt(83, 196, 1, 32, 0, 16, 16, 15)
      pyxel.text(98, 206, "x " + str(fc), 7)            
      
      #Message
      for m in range(len(gm.msg)):
          if gm.msg[m][1] == 100:
              pyxel.text(120, 160 + m*10, gm.msg[m][0], pyxel.randi(2, 14))
          else:
              pyxel.text(120, 160 + m * 10, gm.msg[m][0], gm.msg[m][1])
                
#-----------------------------------------------------------------------------          

def draw_map_window(mz, x, y, p):
#Map Window-------------------------------------------------------------------
      mw = []
      for m in range(len(mz)):
          mw2 = []
          for m2 in range(len(mz)):
              if mz[m][m2] == (0, 0):
                  mw2.append(0)
              else:
                  mw2.append(1)
          mw.append(mw2)
      b_pos = (x, y)
      pyxel.rect(b_pos[0], b_pos[1], 66, 66, 3)
      pyxel.rectb(b_pos[0], b_pos[1], 66, 66, 13)
      pyxel.rectb(b_pos[0] - 2, b_pos[1] - 2, 70, 70, 1)
      pyxel.rectb(b_pos[0] - 6, b_pos[1] + 30, 5, 36, 1)
      pyxel.rectb(b_pos[0] - 6, b_pos[1] , 5, 36, 1)
      pyxel.rectb(b_pos[0] + 67, b_pos[1] + 30, 5, 36, 1)
      pyxel.rectb(b_pos[0] + 67, b_pos[1] , 5, 36, 1)
      
      for m3 in range(len(mw)):
          for m4 in range(len(mw[m3])):
              if mw[m3][m4] == (1):
                  c = pyxel.rndi(0, 500)
                  if c == 0:
                      pyxel.rect(b_pos[0] + 1 + m4 * 2,
                                 b_pos[1] + 1 + m3 * 2,
                                 2, 2, 11)
                  elif c < 10:
                      pyxel.rect(b_pos[0] + 1 + m4 * 2,
                                 b_pos[1] + 1 + m3 * 2,
                                 2, 2, 1)
                  else:
                      pyxel.rect(b_pos[0] + 1 + m4 * 2,
                                 b_pos[1] + 1 + m3 * 2,
                                 2, 2, 0)
              else:
                  cc = pyxel.rndi(0, 1000)
                  if cc == 0:
                      pyxel.rect(b_pos[0] + 1 + m4 * 2,
                                 b_pos[1] + 1 + m3 * 2,
                                 2, 2, 11)
                  elif cc < 10:
                      pyxel.rect(b_pos[0] + 1 + m4 * 2,
                                 b_pos[1] + 1 + m3 * 2,
                                 2, 2, 1)
                          
              if p[0] == m4 and p[1] == m3:
                     pyxel.rect(b_pos[0] + 1 + m4 * 2,
                                 b_pos[1] + 1 + m3 * 2,
                                 2, 2, 8)
#-----------------------------------------------------------------------------










     
 