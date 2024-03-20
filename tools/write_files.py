def write_files(files, content):
    with open(files, 'w', encoding='utf-8') as f:
        f.write(content)