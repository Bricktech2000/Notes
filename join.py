import os
import re

# assumptions: all files end with a trailing newline
joined = ''

for root, dirs, files in os.walk('./notes'):
  for file in files:
    if file.endswith('.md'):
      with open(os.path.join(root, file), 'r') as f:
        content = f.read()
        content = re.sub(r'\n<script.*\n', '', content)
        content = re.sub(r'\n<style.*\n', '', content)
        joined += f'{content}\n<hr><div style="height: 200px"></div>\n\n'
        # joined += f'{content}\n<div style="page-break-after: always;"></div>\n\n'

joined += '''
<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
'''

with open(os.path.join('./notes', 'NOTES_JOINED.md'), 'w') as f:
  f.write(joined)
