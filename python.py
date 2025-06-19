#1
num=int(input("Enter a number:"))
sum=0
while num > 0:
  digit = num % 10
  sum = sum + digit
  num = num // 10
print("Sum",sum)

#2
def even(numbers):
  even_numbers = [num for num in numbers if num % 2 == 0]
  return even_numbers
num=[1,2,3,4,5,6,7,8,9,10]
print(even(num))

#3
try:
  num=int(input("Enter a number:"))
  print("Entered value:",num)
except Exception as e:
  print("Error\n",e)

#4
for i in range(1,5):
  for j in range(1,i+1):
    print(3*j,end=" ")
  print()

#5
radius=float(input("Enter radius "))
area=(22/7)*radius*radius
print("Area:",area)