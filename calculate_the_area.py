# Calculate the area, and perimeter of a circle, triangle, and rectangle
import math

# Circle

print('Hello world! Let\'s do some calculations')
print() # Format

print('let\'s start with the cercle')
print()

radius = (float(input('Enter the radius of your cercle: ')))
area_of_circle = math.pi*(radius**2)
area_result = "{:.3f}".format(area_of_circle)


print('if the circle\'s radius is: ', radius, 'then the area of the cercle is: ', area_result)
circumference = math.pi * (radius*2)  
circumference_result = "{:.3f}".format(circumference)

print('and the circumference is: ', circumference_result)

area_of_circle = round(area_of_circle)
circumference = round(circumference)
print()
print('Or if we round the results:')
print('Area = ', area_of_circle)
print('Circumference = ', circumference)

print()
print('Be aware that rounded results are not as precise as float ones.')

# Format 
print()
print()

# Triangle

print('Now let\'s calculate the area of a triangle')
print()

triangle_base = float(input('Triangle\'s base: '))
triangle_height = float(input('Triangle\'s height: '))
triangle_area = 0.5*triangle_base*triangle_height
tr_area_result = '{:.3f}'.format(triangle_area)

print('The area for a triangle with base: ', triangle_base, 'and height: ', triangle_height, 'is:', tr_area_result)

print()
print('Now, let\'s calculate the perimeter.')

lado_a = float(input("Side A: "))
lado_b = float(input("Side B: "))
lado_c = float(input("Side C: "))

perimeter = lado_a+lado_b+lado_c

print('Perimeter for a triangle with sides: ', lado_a,',', lado_b, 'and ', lado_c, 'is: ', perimeter)

print()

# Rectangle

print('Lastly, we will calculate the area of a rectangle.')
print()

print("Ejercicios para calcular en base a RECTANGULO")

rectangle_height = float(input("Rectangle height: "))
rectangle_long = float(input("Rectagle long: "))

rectangle_area = rectangle_height*rectangle_long
print('If the height of the rectangle is ', rectangle_height, 'and the long of the rectangle is ', rectangle_long) 
print('then the area is: ', rectangle_area)
rectangle_perimeter = 2*rectangle_height*rectangle_long
print('and the perimeter is: ', rectangle_perimeter)