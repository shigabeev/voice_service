def write_result(text):
    with open("data/history.txt", "a") as fs:
        fs.write(f'{text}\n')