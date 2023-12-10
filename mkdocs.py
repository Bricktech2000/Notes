import os
import re
import sys
import shutil

src_dir = os.path.join(os.path.dirname(__file__), sys.argv[1])
dst_dir = os.path.join(os.path.dirname(__file__), sys.argv[2])


def h2a(string):
  # hashtag to angle bracket
  split = string.split('#', 1) + ['']
  # this would replace a link like `[[function#pure function]]` with text `pure < function`
  # and would replace a link like `[[function#slope]]` with text `function > slope`
  if not split[1]:
    return split[0]
  elif split[1].endswith(split[0]):
    return split[1][:-len(split[0])] + ' &#8882; ' + split[0]
  else:
    return split[0] + ' &#8883; ' + split[1]


def l2e(string):
  # link to escaped
  split = string.split('#', 1) + ['']
  return re.sub(r' ', r'%20', split[0]) + '#' + re.sub(r' ', r'-', split[1])


def t2e(string):
  # text to escaped
  return ''.join(f'&CHAR{ord(c)}' for c in string)


def preprocess_math(source):
  source = f' {source} '
  source = re.sub(r'\\\|', r'|', source)  # when inside Markdown tables
  source = re.sub(r'&', r'&AMP', source)  # for matrices
  source = re.sub(r'&AMP&AMP', r'&BS&BS', source)  # for matrices
  source = re.sub(r'""(([^"\\]|\\"|\\\\)*)""', lambda m: f'&BStext&LBRA&DQUOT{t2e(m.group(1))}&DQUOT&RBRA', source)
  source = re.sub(r"''(([^'\\]|\\'|\\\\)*)''", lambda m: f'&BStext&LBRA&QUOT{t2e(m.group(1))}&QUOT&RBRA', source)
  source = re.sub(r'"(([^"\\]|\\"|\\\\)*)"', lambda m: f'&BStext&LBRA{t2e(m.group(1))}&RBRA', source)
  source = re.sub(r'\\\*', r'&STAR', source)  # escape sequence
  source = re.sub(r'\\\$', r'&BS&DOLLAR', source)  # escape sequence
  source = re.sub(r'\\\\', r'&BS&BS', source)  # escape sequence

  source = re.sub(r'aa', r'&BSalpha&SPACE', source)
  source = re.sub(r'AA', r'&BSmathcal&SPACEA', source)
  source = re.sub(r'bb', r'&BSbeta&SPACE', source)
  source = re.sub(r'BB', r'&BSmathcal&SPACEB', source)
  source = re.sub(r'gg', r'&BSgam&CHAR109a&SPACE', source)
  source = re.sub(r'GG', r'&BSGam&CHAR109a&SPACE', source)
  source = re.sub(r'dd', r'&BSdelta&SPACE', source)
  source = re.sub(r'DD', r'&BSDelta&SPACE', source)
  source = re.sub(r'ee', r'&BSvarepsilon&SPACE', source)
  source = re.sub(r'EE', r'&BSmathcal&SPACEE', source)
  source = re.sub(r'zz', r'&BSzeta&SPACE', source)
  source = re.sub(r'ZZ', r'&BSmathcal&SPACEZ', source)
  source = re.sub(r'hh', r'&BSeta&SPACE', source)
  source = re.sub(r'HH', r'&BSmathcal&SPACEH', source)
  source = re.sub(r'qq', r'&BStheta&SPACE', source)
  source = re.sub(r'QQ', r'&BSTheta&SPACE', source)
  source = re.sub(r'ii', r'&BSiota&SPACE', source)
  source = re.sub(r'II', r'&BSmathcal&SPACEI', source)
  source = re.sub(r'kk', r'&BSkap&CHAR112a&SPACE', source)
  source = re.sub(r'KK', r'&BSmathcal&SPACEK', source)
  source = re.sub(r'll', r'&BSlambda&SPACE', source)
  source = re.sub(r'LL', r'&BSLambda&SPACE', source)
  source = re.sub(r'mm', r'&BSmu&SPACE', source)
  source = re.sub(r'MM', r'&BSmathcal&SPACEM', source)
  source = re.sub(r'nn', r'&BSnu&SPACE', source)
  source = re.sub(r'NN', r'&BSmathcal&SPACEN', source)
  source = re.sub(r'xx', r'&BSxi&SPACE', source)
  source = re.sub(r'XX', r'&BSXi&SPACE', source)
  source = re.sub(r'oo', r'&BSomicron&SPACE', source)
  source = re.sub(r'OO', r'&BSmathcal&SPACEO', source)
  source = re.sub(r'pp', r'&BSpi&SPACE', source)
  source = re.sub(r'PP', r'&BSPi&SPACE', source)
  source = re.sub(r'rr', r'&BSrho&SPACE', source)
  source = re.sub(r'RR', r'&BSmathcal&SPACER', source)
  source = re.sub(r'ss', r'&BSsigma&SPACE', source)
  source = re.sub(r'SS', r'&BSSigma&SPACE', source)
  source = re.sub(r'tt', r'&BStau&SPACE', source)
  source = re.sub(r'TT', r'&BSmathcal&SPACET', source)
  source = re.sub(r'uu', r'&BSupsilon&SPACE', source)
  source = re.sub(r'UU', r'&BSmathcal&SPACEU', source)
  source = re.sub(r'ff', r'&BSphi&SPACE', source)
  source = re.sub(r'FF', r'&BSPhi&SPACE', source)
  source = re.sub(r'cc', r'&BSchi&SPACE', source)
  source = re.sub(r'CC', r'&BSmathcal&SPACEC', source)
  source = re.sub(r'yy', r'&BSpsi&SPACE', source)
  source = re.sub(r'YY', r'&BSPsi&SPACE', source)
  source = re.sub(r'ww', r'&BSomega&SPACE', source)
  source = re.sub(r'WW', r'&BSOmega&SPACE', source)
  source = re.sub(r'JJ', r'&BSmathcal&SPACEJ', source)
  source = re.sub(r'VV', r'&BSmathcal&SPACEV', source)

  source = re.sub(r'__', r'&BSbot&SPACE', source)
  source = re.sub(r'/\\', r'&BSland&SPACE', source)
  source = re.sub(r'\^\^', r'&BStop&SPACE', source)
  source = re.sub(r'\\/', r'&BSlor&SPACE', source)
  source = re.sub(r'_([^\s_\^\(\)\{\}\[\]\|\\\/]*)\s?', r'_&LBRA\1&RBRA', source)
  source = re.sub(r'\^([^\s_\^\(\)\{\}\[\]\|\\\/]*)\s?', r'^&LBRA\1&RBRA', source)
  source = re.sub(r'\\\./', r'&BSlfloor&BS!&BSrfloor&SPACE', source)
  source = re.sub(r'/\.\\', r'&BSlceil&BS!&BSrceil&SPACE', source)
  source = re.sub(r'\[\.\]', r'[]', source)
  source = re.sub(r'\(\.\)', r'(&BS!)', source)
  source = re.sub(r'\{\.\}', r'&BSbraket&LBRA&BS!&RBRA', source)
  source = re.sub(r'\s\\\\\s?', r'&BSlfloor&SPACE&BSlfloor&SPACE', source)
  source = re.sub(r'\s?//\s', r'&BSrfloor&SPACE&BSrfloor&SPACE', source)
  source = re.sub(r'\s\\\s?', r'&BSlfloor&SPACE', source)
  source = re.sub(r'\s?/\s', r'&BSrfloor&SPACE', source)
  source = re.sub(r'\s//', r'&BSlceil&SPACE&BSlceil&SPACE', source)
  source = re.sub(r'\\\\\s', r'&BSrceil&SPACE&BSrceil&SPACE', source)
  source = re.sub(r'\s/', r'&BSlceil&SPACE', source)
  source = re.sub(r'\\\s', r'&BSrceil&SPACE', source)
  source = re.sub(r'\.\.\.', r'&BScdots&SPACE', source)

  source = re.sub(r'#', r'&LBRA&BSsmall&BSequiv&RBRA', source)
  source = re.sub(r'\*', r'&BSsmash&BScirc&SPACE', source)
  source = re.sub(r'@@', r'&BSinfty&SPACE', source)
  source = re.sub(r'@', r'&BSsmash&BSpropto&SPACE', source)
  source = re.sub(r'\$', r'&BSint&SPACE', source)
  source = re.sub(r'\^\^', r'&BStop&SPACE', source)
  source = re.sub(r'__', r'&BSbot&SPACE', source)

  source = re.sub(r':|\s:\s', r':', source)
  source = re.sub(r'\.|\s\.\s', r'&BScdot&SPACE', source)
  source = re.sub(r"'|\s'\s", r'&BSsmash&BSshortmid&SPACE', source)
  source = re.sub(r'--|\s--\s', r'&DASH', source)
  source = re.sub(r'\[\](.*?)\[\]', r'&BSbegin&LBRAbmatrix&RBRA\1&BSend&LBRAbmatrix&RBRA', source)
  source = re.sub(r'\[', r'[', source)
  source = re.sub(r'\]', r']', source)
  source = re.sub(r'->|\s->\s', r'&BSrightarrow&SPACE', source)
  source = re.sub(r'<-|\s<-\s', r'&BSleftarrow&SPACE', source)
  source = re.sub(r'~~|\s~~\s', r'&BSsim&BS!&BSsim&SPACE', source)
  source = re.sub(r'~|\s~\s', r'&BSsim&SPACE', source)
  source = re.sub(r'==|\s==\s', r'=&BS!=', source)
  source = re.sub(r'=|\s=\s', r'=', source)
  source = re.sub(r'\+|\s\+\s', r'+', source)
  source = re.sub(r'><|\s><\s', r'&BStimes&SPACE', source)
  source = re.sub(r'-\||\s-\|\s', r'&BSdashv&SPACE', source)
  source = re.sub(r'<|\s<\s', r'<', source)
  source = re.sub(r'\|-|\s\|-\s', r'&BSvdash&SPACE', source)
  source = re.sub(r'>|\s>\s', r'>', source)
  source = re.sub(r'{{', r'&BSbraket&LBRA&BSbraket&LBRA', source)
  source = re.sub(r'{', r'&BSbraket&LBRA', source)
  source = re.sub(r'}}', r'&RBRA&RBRA', source)
  source = re.sub(r'}', r'&RBRA', source)
  source = re.sub(r'\*|\s\*\s', r'*', source)

  source = re.sub(r'\|\||\s\|\|\s', r'&BSvert&SPACE', source)
  source = re.sub(r'\||\s\|\s', r'&BSmid&SPACE', source)
  source = re.sub(r'-|\s-\s', r'&BStext&DASH', source)
  source = re.sub(r',\s', r',', source)

  source = re.sub(r'^ | $', r'', source)
  source = re.sub(r'^&SPACE|&SPACE$', r'', source)
  source = re.sub(r' ', r'\\ ', source)  # white space is significant
  source = re.sub(r'=:', r'=\\ :', source)  # fix spacing
  source = re.sub(r'&CHAR([0-9]{,3})', lambda m: chr(int(m.group(1))), source)
  source = re.sub(r'\$', r'&BS&DOLLAR', source)  # in case of $ produced above
  source = re.sub(r'{', r'&BS&LBRA', source)  # in case of { produced above
  source = re.sub(r'}', r'&BS&RBRA', source)  # in case of } produced above
  source = re.sub(r"\\\'", r'&QUOT', source)  # in case of \' produced above
  source = re.sub(r'\\\"', r'&DQUOT', source)  # in case of \" produced above
  source = re.sub(r'\\\\', r'&BS', source)  # in case of \\ produced above
  source = re.sub(r'&BS', r'\\', source)
  source = re.sub(r'&AMP', r'&', source)
  source = re.sub(r'&DASH', r'-', source)
  source = re.sub(r'&SPACE', r' ', source)
  source = re.sub(r'&LBRA', r'{', source)
  source = re.sub(r'&RBRA', r'}', source)
  source = re.sub(r'&QUOT', r"'", source)
  source = re.sub(r'&DQUOT', r'"', source)
  source = re.sub(r'&STAR', r'*', source)
  source = re.sub(r'&DOLLAR', r'$', source)
  source = re.sub(r'&VERT', r'|', source)
  return source


def preprocess_markdown(source):
  source = re.sub(r'\*\*`+ ?(.*?) ?`+\*\*', lambda m: f'${preprocess_math(m.group(1))}$', source)
  source = re.sub(r'\[\[([^\[\]]+?)\]\]', lambda m: f'[{h2a(m.group(1))}](/{l2e(m.group(1))})', source)
  source = re.sub(r'\[\[([^\[\]]+?)\|(.+?)\]\]', lambda m: f'[{m.group(2)}](/{l2e(m.group(1))})', source)
  source = re.sub(r'#([a-zA-Z0-9-]+[ \n])', lambda m: f'<small>{m.group(1)[:-1]}</small>{m.group(1)[-1]}', source)
  return source


for file in os.listdir(src_dir):
  src_file = os.path.join(src_dir, file)
  dst_file = os.path.join(dst_dir, file)
  if file.endswith('.md'):
    with open(src_file, 'r') as src:
      with open(dst_file, 'w') as dst:
        dst.write(preprocess_markdown(src.read()))
  else:
    shutil.copy(src_file, dst_dir)
