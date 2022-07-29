# JavaScript

_type system madness_

## type quirks

&mdash; <https://youtu.be/5wnlYIQKPXM>

&mdash; <https://dev.to/royal_bhati/understanding-weird-parts-of-javascript-44o>

see <https://github.com/denysdovhan/wtfjs> for other examples

```javascript
1 + '2'; // '12'
+'15'; // 15
!'word'; // false
1 + []; // '1'
[1] + [2]; // '12
typeof NaN; // 'number'
999999999999; // 10000000000000
Math.max(); // -Infinity
Math.min(); // Infinity
[] + []; // ''
[] + {}; // '[object Object]'
{
}
+[]; // true
true + true + true === 3; // true
true - true === 0; // true
(!+[] + [] + ![]).length; // 9
9 + '1'; // '91'
91 - '1'; // 90
[] == 0; // true
```

## properties

```javascript
a = '0';
b = 0;
c = '';

a == b; // true
b == c; // true
a == c; // false
```

&mdash; <https://youtu.be/vcFBwt1nu2U?t=1290> &mdash; JavaScript: The Good Parts, by Douglas Crockford

&mdash; weak equality is **not** transitive in [[javascript]]
