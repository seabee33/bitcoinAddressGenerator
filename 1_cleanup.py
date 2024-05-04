def remove_after_tab(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            first_line = True  # Flag to indicate if it's the first line
            lines_processed = 0  # Counter to track the number of lines processed
            for line in f_in:
                if first_line:
                    first_line = False
                    continue  # Skip the first line
                if lines_processed >= 20000000:
                    break  # Exit the loop if 20 million lines have been processed
                address, _ = line.split('\t', 1)  # Split at the first tab
                address = address.strip()  # Remove any leading or trailing whitespace
                if not address.lower().startswith(('3', 'b')):
                    f_out.write(address + '\n')  # Write the address to the output file
                lines_processed += 1
    print('Done!')

# Replace 'addresses.tsv' and 'addresses.txt' with your input and output file paths
remove_after_tab('addresses.tsv', 'addresses.txt')
