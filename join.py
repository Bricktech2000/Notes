import os

# assumptions: all files end with a trailing newline
joined = ''

for root, dirs, files in os.walk('./notes'):
  for file in sorted(files):
    if file.endswith('.md'):
      with open(os.path.join(root, file), 'r') as f:
        content = f.read()
        joined += f'{content}\n\n\n'

with open(os.path.join('.', 'join.md'), 'w') as f:
  f.write(joined)
