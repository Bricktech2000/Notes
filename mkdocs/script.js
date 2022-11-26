window.MathJax = {
  tex: {
    inlineMath: [['$', '$']],
  },
  svg: {
    fontCache: 'global',
  },
  messageStyle: 'none',
};

var script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
script.async = true;
document.head.appendChild(script);

// fixup obsidian-export
const main = document.querySelector('.md-main');
// const main = document.body; // breaks search feature in material theme
main.innerHTML = main.innerHTML
  .replace(/\n([^\n\$]*?(\$.*?\$)*?\$[^\n\$]*?)#/g, '$1\\#')
  .replace(/\n([^\n\$]*?(\$.*?\$)*?\$[^\n\$]*?)!/g, '$1\\!')
  .replace(/\\&lt;/g, '&lt;');

console.log('MathJax loaded');
