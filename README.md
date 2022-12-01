# borwell_program

install python 3

open your IDE

first create user inputs, make sure to use float data typr as your input function 
i.e width = float(input()) # just incase the user uses precise measurements

then create the calculations formulas 

#area is lenght * width 
# volume is lenght * width * height 
# formula for painting 4 walls: area = lenght * width * 4
which give you four walls

To calculate how much paint we need simply divide room size by 12 to give us how many litres of paint needed

Finally we test that all for functions and formulas are working correctly so we create a test programe 

we defien area and impute vairables to make sure that the correct value is outputed
e.g a = area(3,4)
assest a == 12  # if any output apart from 12 prints then there will be an error message

we do the same for volume
e.g # v = volume(3, 4, 10)
assesrt w == 120

we make sure we are correctly getting the size of the room correctly 
#example

cubeVolume = 120

printable_area = get_printable_area(4, 3)
assert printable_area == (4+3)n * 4
assert printable_area != cubeVolume

#we print the results to check if our formula and logic are correct 

area_computes_correctly()
volume_computes_correctly()
retrive_sucessfully_paintable_area()







