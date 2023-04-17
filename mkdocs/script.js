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
  MathJax.typesetPromise();
});
