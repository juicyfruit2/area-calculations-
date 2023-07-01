# This program will calculate the area of a foundation of a building cover

# user needs to enter a shape in given options
user_input = input("Enter shape of building,square,rectangular or a round ?:")
print(user_input)
opt1 = "square"
opt2 = "rectangular" 
opt3 = "round"

# line 12 - 23 used if statements to calcuate area of the different shapes

if user_input == opt1:
    length = int(input("Enter the length of the square:"))
    area_of_sqaure = length ** 2
    print(area_of_sqaure)

if user_input == opt2:
    length_rectangular = int(input("Enter the length of the rectangular:"))
    width_rectangular = int(input("Enter the Width of the rectangular:"))
    area_rectangular = length_rectangular * width_rectangular
    print(area_rectangular)

if user_input == opt3:
    pi = 3.14
    raduis = int(input("Enter the raduis of round:"))
    area_round = pi * raduis**2
    print(area_round)

   
   
 



  

       




