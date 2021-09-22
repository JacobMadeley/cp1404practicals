"""
1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

2. Write code that opens "name.txt" and reads the name (as above) then prints,
   "Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on
   separate lines in the file and save it:
   17
   42
   400
   Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the
   result, which should be... 59.

4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a
   file with any number of numbers.
"""

# part 1 create a file named "name.txt" and have it save an inputted name from the user.
OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()


# part 2 read the file "name.txt" as "Your name is '...'"
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print("Your name is", name)

# part 3 read file named "numbers.txt" with numbers 17\n 42\n 100 and have it add the first two number and
# print the results '59'

in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# part 4 have the programme print the total of all numbers in 'numbers.txt' or file with any number of numbers
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
