import os
import re

# assumptions: all files end with a trailing newline
joined = ''

for root, dirs, files in os.walk('./notes'):
  for file in sorted(files):
    if file.endswith('.md'):
      with open(os.path.join(root, file), 'r') as f:
        content = f.read()
        content = re.sub(r'\n<script.*\n', '', content)
        content = re.sub(r'\n<style.*\n', '', content)
        # joined += f'{content}\n<hr><div style="height: 200px"></div>\n\n'
        joined += f'{content}\n<div style="page-break-after: always;"></div>\n\n'

with open(os.path.join('.', 'join.md'), 'w') as f:
  f.write(joined)
