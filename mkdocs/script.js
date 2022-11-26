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
      .replace(/\\&lt;/g, '&lt;')
      .replace(/\\_/g, '_');
  });

  MathJax.typesetPromise();
});
