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
    return split[1][:-len(split[0])] + ' < ' + split[0]
  else:
    return split[0] + ' > ' + split[1]


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

  string = re.sub(r'\\a', r'&BSalpha&SPACE', string)
  string = re.sub(r'\\b', r'&BSbeta&SPACE', string)
  string = re.sub(r'\\g', r'&BSgamma&SPACE', string)
  string = re.sub(r'\\G', r'&BSGamma&SPACE', string)
  string = re.sub(r'\\d', r'&BSdelta&SPACE', string)
  string = re.sub(r'\\D', r'&BSDelta&SPACE', string)
  string = re.sub(r'\\e', r'&BSvarepsilon&SPACE', string)
  string = re.sub(r'\\z', r'&BSzeta&SPACE', string)
  string = re.sub(r'\\h', r'&BSeta&SPACE', string)
  string = re.sub(r'\\q', r'&BStheta&SPACE', string)
  string = re.sub(r'\\Q', r'&BSTheta&SPACE', string)
  string = re.sub(r'\\i', r'&BSiota&SPACE', string)
  string = re.sub(r'\\k', r'&BSkappa&SPACE', string)
  string = re.sub(r'\\l', r'&BSlambda&SPACE', string)
  string = re.sub(r'\\L', r'&BSLambda&SPACE', string)
  string = re.sub(r'\\m', r'&BSmu&SPACE', string)
  string = re.sub(r'\\n', r'&BSnu&SPACE', string)
  string = re.sub(r'\\x', r'&BSxi&SPACE', string)
  string = re.sub(r'\\X', r'&BSXi&SPACE', string)
  string = re.sub(r'\\p', r'&BSpi&SPACE', string)
  string = re.sub(r'\\P', r'&BSPi&SPACE', string)
  string = re.sub(r'\\r', r'&BSrho&SPACE', string)
  string = re.sub(r'\\s', r'&BSsigma&SPACE', string)
  string = re.sub(r'\\S', r'&BSSigma&SPACE', string)
  string = re.sub(r'\\t', r'&BStau&SPACE', string)
  string = re.sub(r'\\u', r'&BSupsilon&SPACE', string)
  string = re.sub(r'\\f', r'&BSphi&SPACE', string)
  string = re.sub(r'\\F', r'&BSPhi&SPACE', string)
  string = re.sub(r'\\c', r'&BSchi&SPACE', string)
  string = re.sub(r'\\y', r'&BSpsi&SPACE', string)
  string = re.sub(r'\\Y', r'&BSPsi&SPACE', string)
  string = re.sub(r'\\w', r'&BSomega&SPACE', string)
  string = re.sub(r'\\W', r'&BSOmega&SPACE', string)
  string = re.sub(r'aa', r'&BSmathcal&SPACEA', string)
  string = re.sub(r'bb', r'&BSmathcal&SPACEB', string)
  string = re.sub(r'cc', r'&BSmathcal&SPACEC', string)
  string = re.sub(r'dd', r'&BSmathcal&SPACED', string)
  string = re.sub(r'ee', r'&BSmathcal&SPACEE', string)
  string = re.sub(r'ff', r'&BSmathcal&SPACEF', string)
  string = re.sub(r'gg', r'&BSmathcal&SPACEG', string)
  string = re.sub(r'hh', r'&BSmathcal&SPACEH', string)
  string = re.sub(r'ii', r'&BSmathcal&SPACEI', string)
  string = re.sub(r'jj', r'&BSmathcal&SPACEJ', string)
  string = re.sub(r'kk', r'&BSmathcal&SPACEK', string)
  string = re.sub(r'll', r'&BSmathcal&SPACEL', string)
  string = re.sub(r'mm', r'&BSmathcal&SPACEM', string)
  string = re.sub(r'nn', r'&BSmathcal&SPACEN', string)
  string = re.sub(r'oo', r'&BSmathcal&SPACEO', string)
  string = re.sub(r'pp', r'&BSmathcal&SPACEP', string)
  string = re.sub(r'qq', r'&BSmathcal&SPACEQ', string)
  string = re.sub(r'rr', r'&BSmathcal&SPACER', string)
  string = re.sub(r'ss', r'&BSmathcal&SPACES', string)
  string = re.sub(r'tt', r'&BSmathcal&SPACET', string)
  string = re.sub(r'uu', r'&BSmathcal&SPACEU', string)
  string = re.sub(r'vv', r'&BSmathcal&SPACEV', string)
  string = re.sub(r'ww', r'&BSmathcal&SPACEW', string)
  string = re.sub(r'xx', r'&BSmathcal&SPACEX', string)
  string = re.sub(r'yy', r'&BSmathcal&SPACEY', string)
  string = re.sub(r'zz', r'&BSmathcal&SPACEZ', string)
  string = re.sub(r'AA', r'&BSmathbb&SPACEA', string)
  string = re.sub(r'BB', r'&BSmathbb&SPACEB', string)
  string = re.sub(r'CC', r'&BSmathbb&SPACEC', string)
  string = re.sub(r'DD', r'&BSmathbb&SPACED', string)
  string = re.sub(r'EE', r'&BSmathbb&SPACEE', string)
  string = re.sub(r'FF', r'&BSmathbb&SPACEF', string)
  string = re.sub(r'GG', r'&BSmathbb&SPACEG', string)
  string = re.sub(r'HH', r'&BSmathbb&SPACEH', string)
  string = re.sub(r'II', r'&BSmathbb&SPACEI', string)
  string = re.sub(r'JJ', r'&BSmathbb&SPACEJ', string)
  string = re.sub(r'KK', r'&BSmathbb&SPACEK', string)
  string = re.sub(r'LL', r'&BSmathbb&SPACEL', string)
  string = re.sub(r'MM', r'&BSmathbb&SPACEM', string)
  string = re.sub(r'NN', r'&BSmathbb&SPACEN', string)
  string = re.sub(r'OO', r'&BSmathbb&SPACEO', string)
  string = re.sub(r'PP', r'&BSmathbb&SPACEP', string)
  string = re.sub(r'QQ', r'&BSmathbb&SPACEQ', string)
  string = re.sub(r'RR', r'&BSmathbb&SPACER', string)
  string = re.sub(r'SS', r'&BSmathbb&SPACES', string)
  string = re.sub(r'TT', r'&BSmathbb&SPACET', string)
  string = re.sub(r'UU', r'&BSmathbb&SPACEU', string)
  string = re.sub(r'VV', r'&BSmathbb&SPACEV', string)
  string = re.sub(r'WW', r'&BSmathbb&SPACEW', string)
  string = re.sub(r'XX', r'&BSmathbb&SPACEX', string)
  string = re.sub(r'YY', r'&BSmathbb&SPACEY', string)
  string = re.sub(r'ZZ', r'&BSmathbb&SPACEZ', string)

  string = re.sub(r'#', r'&BS#&SPACE', string)
  string = re.sub(r'\*', r'&BSsmash&BScirc&SPACE', string)
  string = re.sub(r'@@', r'&BSinfty&SPACE', string)
  string = re.sub(r'@', r'&BSvarnothing&SPACE', string)
  string = re.sub(r'\$', r'&BSint&SPACE', string)
  string = re.sub(r'\^\^', r'&BStop&SPACE', string)
  string = re.sub(r'__', r'&BSbot&SPACE', string)

  string = re.sub(r'\s__\s', r'&BSbot&SPACE ', string)
  string = re.sub(r'/\\', r'&BSland&SPACE', string)
  string = re.sub(r'\s\^\^\s', r'&BStop&SPACE', string)
  string = re.sub(r'\\/', r'&BSlor&SPACE', string)
  string = re.sub(r'\s\\\\\s?', r'&BSlfloor&SPACE&BSlfloor&SPACE', string)
  string = re.sub(r'\s?//\s', r'&BSrfloor&SPACE&BSrfloor&SPACE', string)
  string = re.sub(r'\s\\\s?', r'&BSlfloor&SPACE', string)
  string = re.sub(r'\s?/\s', r'&BSrfloor&SPACE', string)
  string = re.sub(r'\s//', r'&BSlceil&SPACE&BSlceil&SPACE', string)
  string = re.sub(r'\\\\\s', r'&BSrceil&SPACE&BSrceil&SPACE', string)
  string = re.sub(r'\s/', r'&BSlceil&SPACE', string)
  string = re.sub(r'\\\s', r'&BSrceil&SPACE', string)
  string = re.sub(r'\.\.\.', r'&BScdots&SPACE', string)
  string = re.sub(r'_([^\s_\^\)\}\]\|]*)\s?', r'_&LBRA\1&RBRA', string)
  string = re.sub(r'\^([^\s_\^\)\}\]\|]*)\s?', r'^&LBRA\1&RBRA', string)

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
