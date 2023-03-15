# Open the input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:

    # Flag to indicate whether we are inside a Code block
    inside_code = False

    # Loop through each line of the input file
    for line in input_file:

        # Check if we are inside a Code block
        if inside_code:
            # Replace the [Code] and [/Code] tags with the appropriate markup
            line = line.replace('[Code]', ''''').replace('[/Code]', ''''')
            
            # Check if we have reached the end of the Code block
            if '[/Code]' in line:
                # We have reached the end of the Code block
                inside_code = False

                # Write the code block to the output file using Github quoting code tags
                output_file.write("'''\n")
                output_file.write(line)
                output_file.write("'''\n\n")

        else:
            # Check if we have found the start of a Text block
            if '[Text]' in line:
                # We have found the start of a Text block
                inside_code = False
                text_lines = []
                
                # Loop through the lines of the Text block
                for text_line in input_file:
                    # Check if we have reached the end of the Text block
                    if '[/Text]' in text_line:
                        # We have reached the end of the Text block
                        output_file.write(''.join(text_lines))
                        break
                    else:
                        # Add the line to the list of Text block lines
                        text_lines.append(text_line)
            
            # Check if we have found the start of a Code block
            elif '[Code]' in line:
                # We have found the start of a Code block
                inside_code = True
        
        # Check if we need to write the line to the output file
        if not inside_code:
            output_file.write(line)
