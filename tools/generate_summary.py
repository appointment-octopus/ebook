import glob

result = '# Summary\n\n'
for f in glob.glob("src/**/*.md", recursive=True):
    if 'SUMMARY' not in f:
        tokens = f.split('/')
        filename = tokens[-1]
        name = (filename.strip('.md') if filename != 'README.md' else tokens[-2]).title()
        path = f.split('src/')[-1].replace(' ', '%20')
        indent = (len(tokens)-2)*2
        if 'README' in f:
            indent -= 2
        result += f'{" "*indent}- [{name}](./{path})\n'

with open('src/SUMMARY.md', 'w') as file:
    file.write(result)
