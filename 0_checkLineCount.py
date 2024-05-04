def get_last_line_and_line_count(filename):
    line_count = 0
    with open(filename, 'r') as file:
        # Count the number of lines
        for line in file:
            line_count += 1
        
        # Move the file pointer to the end of the file
        file.seek(0, 2)
        
        # Find the position of the last newline character
        end_position = file.tell()
        position = end_position - 1
        
        while position >= 0:
            file.seek(position)
            char = file.read(1)
            if char == '\n':
                break
            position -= 1
        
        # Read the last line
        last_line = file.readline().strip()
    
    return last_line, line_count

# Example usage:
filename = 'addresses.txt'
last_line, line_count = get_last_line_and_line_count(filename)
print("Last line:", last_line)
print("Total number of lines:", line_count)
