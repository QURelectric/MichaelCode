start = 1
end = 100
winningTotal = 0
winningMultiplier = 0

#Read the number on that line
def read_numbers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and convert to float
            yield float(line.strip())

#File path
file_path = '/Users/michaelwhitwam/Desktop/MichaelCode/untitled3.txt'  # Replace with your file's path

for i in range(int((end - start) / 0.01) + 1):
    multiplier = start + i * 0.01
    total = 0
    
    
    for number in read_numbers(file_path):
       if multiplier <= number:
           total += multiplier
            
    if winningTotal < total:
        winningTotal = total
        winningMultiplier = multiplier

print("The winning number is " + str(winningMultiplier) + " and the winnign total is " + str(winningTotal))
            