from borewell import get_paintable_area, volume, get_estimated_litres_needed_to_paint

#User input
print("please enter the dimensions of the room, firstly enter the width of the room: ")
width = float(input())

print("please enter the dimensions of the room, firstly enter the height of the room: ")
height = float(input())

print("please enter the dimensions of the room, firstly enter the lenght of the room: ")
lenght = float(input())

# area and volume
print(f'the area of the room is: {area(lenght, width)}')
print (f'the volume of the room is: {volume(lenght, width, height)}')

#paintable and the amount of paint required:
paintable_area = get_paintable_area(lenght, width)
estimated_litres_of_paint_required = get_estimated_litres_needed_to_paint(paintable_area)

print(f'you need enough paint to cover the following area (in sq metres) {paintable_area}')
print(f'we estimate 1 litre of paint covers 12m^2, so you will need: {estimated_litres_to_paint(paintable_area)


