number = int(input("Run loop times? "))

for i in range(number):
    print("Item in for loop: " + str(i))

j = 0
while j < number:
    print("Item in while loop: " + str(j))
    j += 1

my_array = ['car', 'python', 'dog']

for a in my_array:
    print("Item in array: " + a)

print("2-nd element is: " + my_array[1])

# last item
print("Last item is: " + my_array[-1])
