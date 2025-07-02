# Hungarian Notation

**definition** _systems hungarian_ is prepending onto [[variable]] names an abbreviation of their [[type]]

**definition** _apps hungarian_ is prepending onto [[variable]] names extra semantic information not available in their [[type]]

at the end of the day, both variants of [[hungarian notation]] are band-aids. most agree systems hungarian is bad idea juice. but `newtype`s and [[type-driven design]] make apps hungarian irrelevant too

> _In Excel's source code you see a lot of `rw` and `col` and when you see those you know that they refer to rows and columns. Yep, they're both integers, but it never makes sense to assign between them. In Word, I'm told, you see a lot of `xl` and `xw`, where `xl` means "horizontal coordinates relative to the layout" and `xw` means "horizontal coordinates relative to the window." Both ints. Not interchangeable._ --- <https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/>

well then use different [[type]]s? if it's this nice in [[c]], there are no good excuses anymore:

```c
typedef struct { int r; } row_t;
typedef struct { int c; } col_t;
typedef struct { int x; int y; } lay_t;
typedef struct { int x; int y; } win_t;

row_t idx = {5};
col_t col = prod((row_t){4}, idx);
col = idx; // compile error
idx.r++, col.c -= 3;
win_t button = lay2win((lay_t){8, 9});
button.x += pad, button.y += pad;
button = lay2win(button); // compile error
```
