# area computation 
def area (lenght, width):
  return lenght * width

# volume of the room 
def volume(lenght, width, height):
  return lenght * width * height

# amount of paint required to paint just the walls 
# since there are just four walls:
# we can simply times the area of one face of the cube by 4

def get_paint_area(lenght, width):
  paintable_area = (area(lenght, width) * 4)
  return paintable_area

# assuming that the room is equally spaced and 1 litre of paint covers 12^2
def get_estimated_litres_need_to_paint(paintable_area):
  return paintable_area / 12
