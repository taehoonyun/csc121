import arcade

def draw_section_outlines():

    color = arcade.color.BLACK
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)
 
 
def draw_section_1():
    for row in range(30):
        for column in range(30):
             # Instead of zero, calculate the proper x location using
             # column
            x = (column * 10) + 5
 
             # Instead of zero, calculate the proper y location using row
            y = (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
 
 
def draw_section_2(sec2_x,sec2_y):
     # Below, replace "pass" with your code for the loop.
     #
     # Use the modulus operator and an if statement to select the
     # color.
     #
     # Don't loop from 30 to 60 to shift everything over, just add 300
     # to x.
    for row in range(30):
        for column in range(0,29,2):
             
             # column
            x = sec2_x + (column * 10) + 5
 
            
            y = sec2_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    for row in range(30):
        for column in range(1,30,2):
            
             # column
            x = sec2_x + (column * 10) + 5
 
             
            y = sec2_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
 
 
 
def draw_section_3(sec3_x,sec3_y):
     # Use the modulus operator and an if/else statement to select the
     # color.
     #
     # Don't use multiple 'if' statements.
    for row in range(0,29,2):
        for column in range(30):
             
             # column
            x = sec3_x + (column * 10) + 5
 
             
            y = sec3_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    for row in range(1,30,2):
        for column in range(30):
             
             # column
            x = sec3_x + (column * 10) + 5
 
             
            y = sec3_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
 
 
 
def draw_section_4(sec4_x,sec4_y):
     # Use the modulus operator and just one 'if' statement to select
     # the color.
    for row in range(0,29,2):
        for column in range(30):
            
             # column
            x = sec4_x + (column * 10) + 5
 
             
            y = sec4_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
    for row in range(1,30,2):
        for column in range(30):
            
             # column
            x = sec4_x + (column * 10) + 5
 
             
            y = sec4_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
    for row in range(0,29,2):
        for column in range(1,30,2):
            
            x = sec4_x + (column * 10) + 5
 
             
            y = sec4_y +  (row * 10) +5 
 
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
 
 
def draw_section_5(sec5_x,sec5_y):
     # Do NOT use 'if' statements to complete 5-8. Manipulate the loops
     # instead.
     for column in range(30):
        for row in range(column+1):
            x = sec5_x + (column * 10) + 5

            y = sec5_y +  (row * 10) +5 

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            print
 
def draw_section_6(sec6_x,sec6_y):
   
     for column in range(30):
        for row in range(30-column):
            x = sec6_x + (column * 10) + 5

            y = sec6_y +  (row * 10) +5 

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            print
 
 
def draw_section_7(sec7_x,sec7_y):
     for row in range(30):
        for column in range(row+1):
            x = sec7_x + (column * 10) + 5

            y = sec7_y +  (row * 10) +5 

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            print
    
 
 
def draw_section_8(sec8_x,sec8_y):
    for row in range(30):
        for column in range(30-row):
            x = sec8_x + (column * 10) + 5

            y = sec8_y +  (row * 10) +5 

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            print
 
 
def main():
      # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
  
    arcade.start_render()
  
      # Draw the outlines for the sections
    draw_section_outlines()
 
    # Draw the sections
    draw_section_1()
    draw_section_2(300,0)
    draw_section_3(600,0)
    draw_section_4(900,0)
    draw_section_5(0,300)
    draw_section_6(300,300)
    draw_section_7(600,300)
    draw_section_8(900,300)
 
    arcade.finish_render()

    arcade.run()
 
if __name__=='__main__':
    main()
arcade.open_window(600,600,"Drawing Example")


arcade.run()