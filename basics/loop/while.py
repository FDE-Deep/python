#lets create the following pattern using while loop

#   *   
#  * * 
# * * * 

stars = 15
rows = 1
fixedStars = stars
while(stars > 0):
    leftSpace = 1;
    #printStars = 1;
    while(leftSpace <= int(fixedStars - rows)):
        print(" ",end="")
        leftSpace = leftSpace + 1
    tempPrintStar = 1
    while(tempPrintStar <= rows):
        print("* ",end="")
        tempPrintStar = tempPrintStar + 1
    #printStars = printStars + 1
    rows = rows + 1
    stars = stars - 1
    print()
