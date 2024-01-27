def replace_text(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            modified_line = line.replace("African American", "White")
            file.write(modified_line)

# Example usage
input_file = 'African_American_Prompts.txt'  # Replace with your input file name
output_file = 'White_Prompts.txt'  # Replace with your desired output file name
replace_text(input_file, output_file)
