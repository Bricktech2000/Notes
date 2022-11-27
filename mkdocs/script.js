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

  /*
  // add admonition support
  
  note: this is broken because of the way the markdown is parsed

  ```
  > a

  > b
  ```

  is parsed as

  ```
  > a
  >
  > b
  ```

  const admonitions = document
    .querySelector('.md-content')
    .querySelectorAll('blockquote');

  const admonitionExpandMap = {
    note: true,
    example: false,
    examples: false,
    procedure: true,
    proof: false,
    '[[mnemonic]]': true,
    constant: true,
    equivalence: false,
  };

  admonitions.forEach((a) => {
    const firstLine = a?.querySelector('p');
    const type = firstLine?.querySelector('strong');
    const title = firstLine?.querySelector('em');

    if (!type) return;
    details = document.createElement('details');
    summary = document.createElement('summary');
    details.appendChild(summary);
    details.classList.add('quote');
    details.open = admonitionExpandMap[type.textContent] ?? true;
    summary.appendChild(document.createTextNode(type.textContent));
    firstLine.removeChild(type);
    while (a.firstChild) details.appendChild(a.firstChild);
    a.parentNode.insertBefore(details, a);
    a.remove();

    if (!title) return;
    firstLine.removeChild(title);
    if (['', ' '].includes(firstLine.textContent)) firstLine.remove();
    summary.appendChild(document.createTextNode(' '));
    summary.appendChild(title);
    title.style.fontWeight = 'normal';
  });
  */

  // add tag support
  const main = document.querySelector('.md-content');
  main.innerHTML = main.innerHTML.replace(
    /#[a-z0-9A-Z-]+[ \n]/g,
    (tag) => `<span style="
      display: inline-block;
      padding: 0.25em 0.75em;
      margin: 0 0.25em;
      border-radius: 0.5em;
      background-color: hsla(0,0%,62%,.1); /* amonition quote background */
    ">${tag.trim()}</span>${tag.slice(-1)}`
  );

  MathJax.typesetPromise();
});
