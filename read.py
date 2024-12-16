f = open('myfile3.txt', 'r')  # Open the file in read mode
i = 0
while True:
    i = i + 1  # Increment the student counter
    line = f.readline()  # Read the next line from the file
    if not line:
        break  # Exit the loop if no more lines are left

    line = line.strip()  # Remove any trailing whitespace or newline characters
    
    # Split the line into components, assuming it contains exactly three values
    parts = line.split(",")
    
    if len(parts) < 3:
        print(f"Error: Line {i} does not contain enough values: {line}")
        continue  # Skip this line and proceed to the next one
    
    m1 = parts[0]
    m2 = parts[1]
    m3 = parts[2]
    
    print(f"marks of student {i} in maths is : {m1}")
    print(f"marks of student {i} in science is : {m2}")
    print(f"marks of student {i} in english is : {m3}")
    print(line)  # Print the original line for reference

f.close()  # Don't forget to close the file
