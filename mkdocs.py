import os
import re
import sys
import shutil

src_dir = os.path.join(os.path.dirname(__file__), sys.argv[1])
dst_dir = os.path.join(os.path.dirname(__file__), sys.argv[2])


def h2a(string):
  # hashtag to angle bracket
  return re.sub(r'#', r' > ', string)


for file in os.listdir(src_dir):
  if file.endswith('.md'):
    with open(os.path.join(src_dir, file), 'r') as src:
      with open(os.path.join(dst_dir, file), 'w') as dst:
        source = src.read()
        source = re.sub(r'\[\[(.+?)\]\]', lambda m: f'[{h2a(m.group(1))}](/{m.group(1)})', source)
        source = re.sub(r'\[\[(.+?)\|(.+?)\]\]', lambda m: f'[{m.group(2)}](/{m.group(1)})', source)
        source = re.sub(r'#([a-zA-Z0-9-]+[ \n])',
                        lambda m: f'<span class="tag">{m.group(1)[:-1]}</span>{m.group(1)[-1]}',
                        source)
        dst.write(source)
  else:
    shutil.copy(os.path.join(src_dir, file), dst_dir)
