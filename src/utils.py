import os

def write_result(text):
    data_folder = "../data"
    os.makedirs(data_folder, exist_ok=True)
    with open(f"{data_folder}/history.txt", "a") as fs:
        fs.write(f'{text}\n')
