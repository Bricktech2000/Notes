window.MathJax = {
  loader: { load: ['[tex]/braket'] },
  tex: {
    packages: { '[+]': ['braket'] },
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: '.*|',
    processHtmlClass: 'arithmatex',
  },
};

document$.subscribe(() => {
  // fixup obsidian-export
  const math = document.querySelectorAll('.arithmatex');
  math.forEach((m) => {
    m.innerHTML = m.innerHTML
      .replace(/\\\[/g, '[')
      .replace(/\\\]/g, ']')
      .replace(/\\\*/g, '*')
      .replace(/\\&lt;/g, '&lt;')
      .replace(/\\_/g, '_')
      .replace(/!/g, '\\!')
      // .replace(/,/g, '\\,')
      .replace(/\\\\/g, '\\');
  });
  const code = document.querySelectorAll('code');
  code.forEach((c) => {
    c.innerHTML = c.innerHTML.replace(/\\&lt;/g, '&lt;');
  });

  // add tag support
  const items = document
    .querySelector('.md-content')
    .querySelectorAll('p, li, h1, h2, h3, h4, h5, h6, th, td');
  items.forEach((item) => {
    item.innerHTML = (item.innerHTML + ' ').replace(
      /#[a-z0-9A-Z-]+[ \n]/g,
      (tag) => `<span class="tag">${tag.trim()}</span>${tag.slice(-1)}`
    );
  });

  // compile latex
  MathJax.typesetPromise();
});
