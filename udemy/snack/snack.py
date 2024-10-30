from turtle import Turtle 
STARTING_POSITION = [(0, 0),(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    
    def __init__(self) :
        self.segments = []
        self.create_snack()
        
    def create_snack(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color ("white")
            new_segment.penup() #hide the line
            new_segment.goto (position)
            self.segments.append (new_segment)
            
    def move (self):
        for seg_number in range(len(self.segments) -1, 0, -1):  #(start= , stop= , step=), #last position = len(segments) -1
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    
    
    

        
