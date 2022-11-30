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
      .replace(/\\\\/g, '\\');
  });

  // add tag support
  const main = document.querySelector('.md-content');
  main.innerHTML = main.innerHTML.replace(
    /#[a-z0-9A-Z-]+[ \n]/g,
    (tag) => `<span class="tag">${tag.trim()}</span>${tag.slice(-1)}`
  );

  // compile latex
  MathJax.typesetPromise();
});
