import os
from datetime import datetime

# Please customize the following variables
USER_NAME = "simrank"
VERSION = "1.0.0"

def say_hi(msg:str = "Hi!", file_directory:str = "/app/data/") -> None:
    # Ensure the directory exists
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Define filename with timestamp
    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)

    # Write the timestamp inside the file
    with open(file_path, "w") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

def add_numbers(a:int, b:int) -> int:
    return a + b

if __name__ == "__main__":
    say_hi()

