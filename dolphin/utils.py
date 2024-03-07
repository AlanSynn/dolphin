# utils.py
def download_text_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def append_text_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
