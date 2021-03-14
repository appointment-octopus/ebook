import glob

pattern = '<pre><code class="language-bash">$ '
fixed_pattern = pattern.replace('$ ', '<span style="user-select: none">$ </span>')
for f in glob.glob("**/*.html", recursive=True):
    fixed_content = ''
    with open(f, 'r') as file:
        content = file.read()
        fixed_content = content.replace(pattern, fixed_pattern)
    with open(f, 'w') as file:
        file.write(fixed_content)
