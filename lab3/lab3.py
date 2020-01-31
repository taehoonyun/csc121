
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing With Functions Example"
arcade.open_window(600,600, "Drawing Example")
radius=10



def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)

def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.BRITISH_RACING_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)
    draw_pine_apple(x,y-100,radius)
    draw_pine_apple(x+20,y-130,radius)
#arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.set_background_color((0,150,0)
 #arcade.color.SKY_BLUE
 )
def draw_pine_apple(x, y,radius):
    arcade.draw_circle_filled(x+30,y+50,radius,arcade.color.RED)
    arcade.draw_arc_outline(x+30, y+55, 3, 10, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x+30, y+55, 8, 5, arcade.color.BLACK, 190, 350)


def draw_mountin(x,y):
    arcade.draw_triangle_filled(x+10,y+SCREEN_HEIGHT* (1 / 3),x-SCREEN_WIDTH/4,y,x+SCREEN_WIDTH/4,y,
    arcade.color.DARK_GREEN)


def draw_house(x,y):
    arcade.draw_lrtb_rectangle_filled(x+10,x+210,y+100,y,
                                      arcade.color.BROWN)
    #roof
    arcade.draw_polygon_filled([[x-40, y+100],[x+10, y+200],[x+210, y+200],[x+260, y+100]],arcade.color.RED)
    arcade.draw_arc_outline(x+20, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+40, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+60, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+80, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+100, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+120, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+140, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+160, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+180, y+200, 10, 10, (219,199,83), 180, 360)
    arcade.draw_arc_outline(x+200, y+200, 10, 10, (219,199,83), 180, 360)
    #Chimney
    arcade.draw_lrtb_rectangle_filled(x+190,x+210,y+250,y+200,
                                      arcade.color.BROWN)
    
    arcade.draw_line(x+10, y, x+210, y, arcade.color.BISQUE, 5)
    #left top window
    arcade.draw_rectangle_filled(x+50, y+150, 40, 40, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x+50, y+150, 35 , 35, arcade.color.SKY_BLUE)
    arcade.draw_line(x+50, y+132, x+50,y+168, arcade.color.BISQUE, 2)
    arcade.draw_line(x+30,  y+125, x+70, y+125, arcade.color.BISQUE, 10)
    #right top window
    arcade.draw_rectangle_filled(x+170, y+150, 40, 40, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x+170, y+150, 35 ,35, arcade.color.SKY_BLUE)
    arcade.draw_line(x+170,  y+132, x+170, y+168, arcade.color.BISQUE, 2)
    arcade.draw_line(x+150,  y+125, x+190, y+125, arcade.color.BISQUE, 10)
    #right bottom window
    arcade.draw_rectangle_filled(x+150, y+50, 40, 40, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x+150, y+50, 35 ,35, arcade.color.SKY_BLUE)
    arcade.draw_line(x+150,  y+32, x+150, y+68, arcade.color.BISQUE, 2)
    arcade.draw_line(x+130,  y+25, x+170, y+25, arcade.color.BISQUE, 10)
    #door
    arcade.draw_lrtb_rectangle_filled(x+30,x+80,y+70,y+5,
                                      (100,88,17))
    arcade.draw_rectangle_outline(x+45, y+53,15,23, arcade.color.BONE, 1)
    arcade.draw_rectangle_outline(x+65, y+53,15,23, arcade.color.BONE, 1)
    arcade.draw_rectangle_outline(x+45, y+20,15,23, arcade.color.BONE, 1)
    arcade.draw_rectangle_outline(x+65, y+20,15,23, arcade.color.BONE, 1)
    arcade.draw_circle_filled(x+35,y+35, 3, arcade.color.BLACK)

def draw_lake(x,y):
    arcade.draw_circle_filled(x, y, 200, arcade.color.SKY_BLUE)

arcade.start_render()   #I'm about to draw from now on. ready for that!

# draw a tree
arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT * (1 / 3),arcade.color.SKY_BLUE)
#arcade.draw_triangle_filled(x,y,x-y,x+y,h,i,arcade.color.GREEN,)
draw_mountin(SCREEN_WIDTH* (1/4), SCREEN_HEIGHT* (1 / 3))
draw_mountin(SCREEN_WIDTH* (3/4), SCREEN_HEIGHT* (1 / 3))
draw_bird(70, 500)
draw_bird(470, 550)
draw_pine_tree(50, 250)
draw_pine_tree(250, 320)
draw_house(350,50)
draw_lake(20,-100)



arcade.finish_render()  #I'm doen my drawing. You don't need to get ready for drawing anymore.

arcade.start_render()

arcade.run()