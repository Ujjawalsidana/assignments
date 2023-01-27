#Ans 1

def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "PythonGuides"
print("The original string is:",str)
print("The reverse string is:", reverse(str)) 

#Ans 2
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
#Ans 3
# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#Ans 4
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
#Ans 5
for i in range (65,70):
    # inner loop for jth columns
    for j in range(65,i+1):
        print(chr(j),end="")
        
    print()
#Ans 6
min = int(input("Enter the min : "))
max = int(input("Enter the max : "))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
#Ans 7
start_num = int(68)
  
# enter the ending range number
end_num = int(167)
  
# initialise counter with starting number
cnt = start_num
  
# check until end of the range is achieved
while cnt <= end_num:
  
    # check if number is divisible by 7 and 5
    if(cnt % 35 == 0):
        print(cnt, "is divisible by 7 and 5.")
  
    # incrementing counter
    cnt += 1
#Ans 8
for i in range(0, 10):
    num = int(input('Enter Number:'))
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")
        
#Ans 9
# Open the file in read mode
text = open("sample.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(" ")
                         
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1