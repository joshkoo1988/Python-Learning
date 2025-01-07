def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

print(f"sword_length = {sword_length}")
print(f"spear_length = {spear_length}")
print(f"The area of a sword attack is {sword_area}")
print(f"The area of a spear attack is {spear_area}")
