import arcade
  
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
color = (0,0,0)

def Flowerpot(x,y):
    arcade.draw_lrtb_rectangle_filled(x,x+400,y+20,y-50, arcade.color.BROWN)
    arcade.draw_polygon_filled([[x+100,y-250],
                             [x+50, y-50],
                             [x+350, y-50],
                             [x+300, y-250]],
                             arcade.color.BROWN)
    arcade.draw_line(x,y-50,x+400,y-50,arcade.color.BLACK,2)

def Plants(x,y,color):
    arcade.draw_triangle_filled(x+50, y+100, x+35, 320, x+65, 320, color)

def Spray(x,y,anlge):
    arcade.draw_rectangle_filled(x+50,y-100,200,200, (0,128,200),anlge)
    arcade.draw_rectangle_filled(x-100,y-100,100,50, (0,128,200),anlge)
    """arcade.draw_polygon_filled([[x-150,y-100],
                             [x-150, y],
                             [x-100, y-30],
                             [x-100, y-60]],
                             (0,128,200))"""

def Water(x,y,stream_Water):
     arcade.draw_arc_outline(x-100, y-120-stream_Water, 100, stream_Water, arcade.color.BLUE, 120, 180,5)

def Snail(x,y):
    #body
    arcade.draw_arc_outline(x,y,100,50,arcade.color.BONE,170,330,50)
    #head
    arcade.draw_circle_filled(x-97,y+16,25, arcade.color.BONE)
    arcade.draw_circle_filled(x-105,y+24,5, arcade.color.BLACK)
    arcade.draw_circle_filled(x-85,y+18,5, arcade.color.BLACK)
    arcade.draw_arc_outline(x-97,y+10,10,10,arcade.color.BLACK,170,330,2)
    #house
    arcade.draw_circle_filled(x,y+10,60,(222,136,32))
    arcade.draw_circle_outline(x,y+10,45,arcade.color.BLACK,2)
    arcade.draw_circle_outline(x,y+10,30,arcade.color.BLACK,2)
    arcade.draw_circle_outline(x,y+10,15,arcade.color.BLACK,2)

def on_draw(delta_time):

    arcade.start_render()

    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, (210,175,0))

    Flowerpot(200,300)
    Spray(700,600,on_draw.spray_angle)
    Snail(on_draw.snail_move,100)
    
    if on_draw.spray_angle == 30 :
        Water(700,600,on_draw.Water)
        Water(680,580,on_draw.Water)
        Water(720,620,on_draw.Water)
        
        if on_draw.Water == 140:
            #plants
            Plants(200,on_draw.plant_growing_y,(0,178,22))
            Plants(250,on_draw.plant_growing_y,(0,178,22))
            Plants(300,on_draw.plant_growing_y,(0,178,22))
            Plants(350,on_draw.plant_growing_y,(0,178,22))
            Plants(400,on_draw.plant_growing_y,(0,178,22))
            Plants(450,on_draw.plant_growing_y,(0,178,22))
            Plants(500,on_draw.plant_growing_y,(0,178,22))
            if on_draw.plant_growing_y > 350 :
                Plants(200,on_draw.plant_growing_y-100,(189,248,183))
                Plants(250,on_draw.plant_growing_y-100,(189,248,183))
                Plants(300,on_draw.plant_growing_y-100,(189,248,183))
                Plants(350,on_draw.plant_growing_y-100,(189,248,183))
                Plants(400,on_draw.plant_growing_y-100,(189,248,183))
                Plants(450,on_draw.plant_growing_y-100,(189,248,183))
                Plants(500,on_draw.plant_growing_y-100,(189,248,183))
            on_draw.Water = 139
            on_draw.plant_growing_y +=1

        on_draw.spray_angle = 29
        on_draw.Water += 1
        
    
    on_draw.spray_angle += 1
    on_draw.snail_move -=1

on_draw.spray_angle = 0
on_draw.plant_growing_y = 300
on_draw.Water = 100
on_draw.snail_move = 700

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    
    arcade.schedule(on_draw,1/200)

    
    arcade.run()
main()