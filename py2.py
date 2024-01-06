from py1 import Triangle

class Colored_Triange(Triangle):
    def __init__(self,a,b, color):
        super().__init__(a,b)
        self.color = color

    