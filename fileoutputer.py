import os

# Open the input file for reading
with open('input.txt', 'r') as input_file:

    # Initialize a counter for the output files
    file_counter = 1

    # Initialize a flag to indicate whether we are inside a Text block
    inside_text = False

    # Loop through each line of the input file
    for line in input_file:

        # Check if we are inside a Text block
        if inside_text:
            # Append the current line to the text block
            text_block.append(line)
            
            # Check if we have reached the end of the Text block
            if '[/Text]' in line:
                # We have reached the end of the Text block
                inside_text = False
                
                # Write the text block to a new output file
                output_file_name = f'output_file{file_counter}.MD'
                with open(output_file_name, 'w') as output_file:
                    output_file.write(''.join(text_block))
                
                # Increment the counter for the output files
                file_counter += 1

        else:
            # Check if we have found the start of a Text block
            if '[Text]' in line:
                # We have found the start of a Text block
                inside_text = True
                text_block = []
        
        # Check if we need to write the line to the output file
        if not inside_text:
            # Do not write Text block lines to the input file
            with open('temp_file.MD', 'a') as temp_file:
                temp_file.write(line)

# Rename the temporary file to the input file name
os.remove('input.txt')
os.rename('temp_file.MD', 'input.txt')