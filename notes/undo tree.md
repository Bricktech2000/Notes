# Undo Tree

**see** [[tree]], [[version control]]

> **resource** [[vim]] `:h undo-tree` and `:h usr_32` --- <https://vimdoc.sourceforge.net/htmldoc/undo.html#undo-tree> and <https://vimdoc.sourceforge.net/htmldoc/usr_32.html>

> **resource** my _jumptree.vim_ plugin, provides [[undo tree]] semantics for the jumplist --- <https://github.com/Bricktech2000/jumptree.vim>

[[undo tree]]s are so much more than "restoring overwritten undos". they turn your undo history into a mini [[version control]] system complete with feature branches and give you superpowers like the ability to seamlessly try out different ideas in parallel on the same file

the way [[vim]] does [[undo tree]]s is particularily clever: the two additional bindings it introduces---_earlier_ `g-` and _later_ `g+`, atop the usual _undo_ `u` and _redo_ `<c-r>`---are all that's needed to freely navigate the entire tree. for more information, see `:h undo-tree` and `:h usr_32`. I also like to abuse `==` to "[[git]] commit" the current text state onto the top of the tree, which works because it always creates a new undo block while generally being a no-op

some plugins visualize [[undo tree]]s for you, but really that's unnecessary; after a bit of practice you get pretty good at holding a mental model of the tree, and navigating it becomes [[muscle memory]]. [[undo tree]]s are gamechangers and I'm never writing an undo system that doesn't support them
