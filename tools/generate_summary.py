import glob

result = '# Summary\n\n'
folders = set()
for f in sorted(glob.glob("src/**/*.md", recursive=True)):
    tokens = f.split('/')
    print(tokens)
    filename = tokens[-1]
    print(filename)
    name = filename.replace('.md', '').replace('_', '. ').title()
    print('------------------------')
    path = f.split('src/')[-1]
    directory = '/'.join(path.split('/')[:-1])
    indent = (len(tokens)-2)*2

    if directory and directory not in folders:
        dir_name = directory.split('/')[-1].title().replace('_', '. ')
        result += f'{" "*(indent-2)}- [{dir_name}](./{directory.replace(" ", "%20")}/README.md)\n'            
        folders.add(directory)

    if 'SUMMARY' not in f and 'README' not in f:
        result += f'{" "*indent}- [{name}](./{path.replace(" ", "%20")})\n'


with open('src/SUMMARY.md', 'w') as file:
    file.write(result)
