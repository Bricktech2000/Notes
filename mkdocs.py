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


def parse_math(string):
  string = f' {string} '
  string = re.sub(r'\\\|', r'|', string)  # when inside Markdown tables
  string = re.sub(r'&', r'&AMP', string)  # for matrices
  string = re.sub(r'&AMP&AMP', r'&BS&BS', string)  # for matrices
  string = re.sub(r'""(([^"\\]|\\"|\\\\)*)""', lambda m: f'&BStext&LBRA&DQUOT{t2e(m.group(1))}&DQUOT&RBRA', string)
  string = re.sub(r"''(([^'\\]|\\'|\\\\)*)''", lambda m: f'&BStext&LBRA&QUOT{t2e(m.group(1))}&QUOT&RBRA', string)
  string = re.sub(r'"(([^"\\]|\\"|\\\\)*)"', lambda m: f'&BStext&LBRA{t2e(m.group(1))}&RBRA', string)
  string = re.sub(r'\\\*', r'&STAR', string)  # escape sequence
  string = re.sub(r'\\\$', r'&BS&DOLLAR', string)  # escape sequence
  string = re.sub(r'\\\\', r'&BS&BS', string)  # escape sequence

  string = re.sub(r'aa', r'&BSalpha&SPACE', string)
  string = re.sub(r'AA', r'&BSmathcal&SPACEA', string)
  string = re.sub(r'bb', r'&BSbeta&SPACE', string)
  string = re.sub(r'BB', r'&BSmathcal&SPACEB', string)
  string = re.sub(r'gg', r'&BSgam&CHAR109a&SPACE', string)
  string = re.sub(r'GG', r'&BSGam&CHAR109a&SPACE', string)
  string = re.sub(r'dd', r'&BSdelta&SPACE', string)
  string = re.sub(r'DD', r'&BSDelta&SPACE', string)
  string = re.sub(r'ee', r'&BSvarepsilon&SPACE', string)
  string = re.sub(r'EE', r'&BSmathcal&SPACEE', string)
  string = re.sub(r'zz', r'&BSzeta&SPACE', string)
  string = re.sub(r'ZZ', r'&BSmathcal&SPACEZ', string)
  string = re.sub(r'hh', r'&BSeta&SPACE', string)
  string = re.sub(r'HH', r'&BSmathcal&SPACEH', string)
  string = re.sub(r'qq', r'&BStheta&SPACE', string)
  string = re.sub(r'QQ', r'&BSTheta&SPACE', string)
  string = re.sub(r'ii', r'&BSiota&SPACE', string)
  string = re.sub(r'II', r'&BSmathcal&SPACEI', string)
  string = re.sub(r'kk', r'&BSkap&CHAR112a&SPACE', string)
  string = re.sub(r'KK', r'&BSmathcal&SPACEK', string)
  string = re.sub(r'll', r'&BSlambda&SPACE', string)
  string = re.sub(r'LL', r'&BSLambda&SPACE', string)
  string = re.sub(r'mm', r'&BSmu&SPACE', string)
  string = re.sub(r'MM', r'&BSmathcal&SPACEM', string)
  string = re.sub(r'nn', r'&BSnu&SPACE', string)
  string = re.sub(r'NN', r'&BSmathcal&SPACEN', string)
  string = re.sub(r'xx', r'&BSxi&SPACE', string)
  string = re.sub(r'XX', r'&BSXi&SPACE', string)
  string = re.sub(r'oo', r'&BSomicron&SPACE', string)
  string = re.sub(r'OO', r'&BSmathcal&SPACEO', string)
  string = re.sub(r'pp', r'&BSpi&SPACE', string)
  string = re.sub(r'PP', r'&BSPi&SPACE', string)
  string = re.sub(r'rr', r'&BSrho&SPACE', string)
  string = re.sub(r'RR', r'&BSmathcal&SPACER', string)
  string = re.sub(r'ss', r'&BSsigma&SPACE', string)
  string = re.sub(r'SS', r'&BSSigma&SPACE', string)
  string = re.sub(r'tt', r'&BStau&SPACE', string)
  string = re.sub(r'TT', r'&BSmathcal&SPACET', string)
  string = re.sub(r'uu', r'&BSupsilon&SPACE', string)
  string = re.sub(r'UU', r'&BSmathcal&SPACEU', string)
  string = re.sub(r'ff', r'&BSphi&SPACE', string)
  string = re.sub(r'FF', r'&BSPhi&SPACE', string)
  string = re.sub(r'cc', r'&BSchi&SPACE', string)
  string = re.sub(r'CC', r'&BSmathcal&SPACEC', string)
  string = re.sub(r'yy', r'&BSpsi&SPACE', string)
  string = re.sub(r'YY', r'&BSPsi&SPACE', string)
  string = re.sub(r'ww', r'&BSomega&SPACE', string)
  string = re.sub(r'WW', r'&BSOmega&SPACE', string)
  string = re.sub(r'JJ', r'&BSmathcal&SPACEJ', string)
  string = re.sub(r'VV', r'&BSmathcal&SPACEV', string)

  string = re.sub(r'__', r'&BSbot&SPACE', string)
  string = re.sub(r'/\\', r'&BSland&SPACE', string)
  string = re.sub(r'\^\^', r'&BStop&SPACE', string)
  string = re.sub(r'\\/', r'&BSlor&SPACE', string)
  string = re.sub(r'_([^\s_\^\(\)\{\}\[\]\|\\\/]*)\s?', r'_&LBRA\1&RBRA', string)
  string = re.sub(r'\^([^\s_\^\(\)\{\}\[\]\|\\\/]*)\s?', r'^&LBRA\1&RBRA', string)
  string = re.sub(r'\\\./', r'&BSlfloor&BS!&BSrfloor&SPACE', string)
  string = re.sub(r'/\.\\', r'&BSlceil&BS!&BSrceil&SPACE', string)
  string = re.sub(r'\[\.\]', r'[]', string)
  string = re.sub(r'\(\.\)', r'(&BS!)', string)
  string = re.sub(r'\{\.\}', r'&BSbraket&LBRA&BS!&RBRA', string)
  string = re.sub(r'\s\\\\\s?', r'&BSlfloor&SPACE&BSlfloor&SPACE', string)
  string = re.sub(r'\s?//\s', r'&BSrfloor&SPACE&BSrfloor&SPACE', string)
  string = re.sub(r'\s\\\s?', r'&BSlfloor&SPACE', string)
  string = re.sub(r'\s?/\s', r'&BSrfloor&SPACE', string)
  string = re.sub(r'\s//', r'&BSlceil&SPACE&BSlceil&SPACE', string)
  string = re.sub(r'\\\\\s', r'&BSrceil&SPACE&BSrceil&SPACE', string)
  string = re.sub(r'\s/', r'&BSlceil&SPACE', string)
  string = re.sub(r'\\\s', r'&BSrceil&SPACE', string)
  string = re.sub(r'\.\.\.', r'&BScdots&SPACE', string)

  string = re.sub(r'#', r'&LBRA&BSsmall&BSequiv&RBRA', string)
  string = re.sub(r'\*', r'&BSsmash&BScirc&SPACE', string)
  string = re.sub(r'@@', r'&BSinfty&SPACE', string)
  string = re.sub(r'@', r'&BSsmash&BSpropto&SPACE', string)
  string = re.sub(r'\$', r'&BSint&SPACE', string)
  string = re.sub(r'\^\^', r'&BStop&SPACE', string)
  string = re.sub(r'__', r'&BSbot&SPACE', string)

  string = re.sub(r':|\s:\s', r':', string)
  string = re.sub(r'\.|\s\.\s', r'&BScdot&SPACE', string)
  string = re.sub(r"'|\s'\s", r'&BSsmash&BSshortmid&SPACE', string)
  string = re.sub(r'--|\s--\s', r'&DASH', string)
  string = re.sub(r'\[\](.*?)\[\]', r'&BSbegin&LBRAbmatrix&RBRA\1&BSend&LBRAbmatrix&RBRA', string)
  string = re.sub(r'\[', r'[', string)
  string = re.sub(r'\]', r']', string)
  string = re.sub(r'->|\s->\s', r'&BSrightarrow&SPACE', string)
  string = re.sub(r'<-|\s<-\s', r'&BSleftarrow&SPACE', string)
  string = re.sub(r'==|\s==\s', r'=&BS!=', string)
  string = re.sub(r'=|\s=\s', r'=', string)
  string = re.sub(r'\+|\s\+\s', r'+', string)
  string = re.sub(r'><|\s><\s', r'&BStimes&SPACE', string)
  string = re.sub(r'-\||\s-\|\s', r'&BSdashv&SPACE', string)
  string = re.sub(r'<|\s<\s', r'<', string)
  string = re.sub(r'\|-|\s\|-\s', r'&BSvdash&SPACE', string)
  string = re.sub(r'>|\s>\s', r'>', string)
  string = re.sub(r'{{', r'&BSbraket&LBRA&BSbraket&LBRA', string)
  string = re.sub(r'{', r'&BSbraket&LBRA', string)
  string = re.sub(r'}}', r'&RBRA&RBRA', string)
  string = re.sub(r'}', r'&RBRA', string)
  string = re.sub(r'\*|\s\*\s', r'*', string)

  string = re.sub(r'\|\||\s\|\|\s', r'&BSvert&SPACE', string)
  string = re.sub(r'\||\s\|\s', r'&BSmid&SPACE', string)
  string = re.sub(r'-|\s-\s', r'&BStext&DASH', string)
  string = re.sub(r',\s', r',', string)

  string = re.sub(r'^ | $', r'', string)
  string = re.sub(r'^&SPACE|&SPACE$', r'', string)
  string = re.sub(r' ', r'\\ ', string)  # white space is significant
  string = re.sub(r'=:', r'=\\ :', string)  # fix spacing
  string = re.sub(r'&CHAR([0-9]{,3})', lambda m: chr(int(m.group(1))), string)
  string = re.sub(r'\$', r'&BS&DOLLAR', string)  # in case of $ produced above
  string = re.sub(r'{', r'&BS&LBRA', string)  # in case of { produced above
  string = re.sub(r'}', r'&BS&RBRA', string)  # in case of } produced above
  string = re.sub(r"\\\'", r'&QUOT', string)  # in case of \' produced above
  string = re.sub(r'\\\"', r'&DQUOT', string)  # in case of \" produced above
  string = re.sub(r'\\\\', r'&BS', string)  # in case of \\ produced above
  string = re.sub(r'&BS', r'\\', string)
  string = re.sub(r'&AMP', r'&', string)
  string = re.sub(r'&DASH', r'-', string)
  string = re.sub(r'&SPACE', r' ', string)
  string = re.sub(r'&LBRA', r'{', string)
  string = re.sub(r'&RBRA', r'}', string)
  string = re.sub(r'&QUOT', r"'", string)
  string = re.sub(r'&DQUOT', r'"', string)
  string = re.sub(r'&STAR', r'*', string)
  string = re.sub(r'&DOLLAR', r'$', string)
  string = re.sub(r'&VERT', r'|', string)
  return string


for file in os.listdir(src_dir):
  if file.endswith('.md'):
    with open(os.path.join(src_dir, file), 'r') as src:
      with open(os.path.join(dst_dir, file), 'w') as dst:
        source = src.read()
        source = re.sub(r'\*\*`+ ?(.*?) ?`+\*\*', lambda m: f'${parse_math(m.group(1))}$', source)
        source = re.sub(r'\[\[([^\[\]]+?)\]\]', lambda m: f'[{h2a(m.group(1))}](/{l2e(m.group(1))})', source)
        source = re.sub(r'\[\[([^\[\]]+?)\|(.+?)\]\]', lambda m: f'[{m.group(2)}](/{l2e(m.group(1))})', source)
        source = re.sub(r'#([a-zA-Z0-9-]+[ \n])',
                        lambda m: f'<span class="tag">{m.group(1)[:-1]}</span>{m.group(1)[-1]}',
                        source)
        dst.write(source)
  else:
    shutil.copy(os.path.join(src_dir, file), dst_dir)
