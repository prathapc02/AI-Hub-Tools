import os


if os.name == 'nt':
    
    command = 'echo %date% %time%'
else:
    # For Unix-like systems (Linux, Mac)
    command = 'date'

# Execute the command and capture the output
date_output = os.popen(command).read()

# Print the date and time
print("Current date and time:", date_output.strip())
