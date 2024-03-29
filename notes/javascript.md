# JavaScript

_[[type system]] madness_

## type system madness

```javascript
/* prettier-ignore */ {
  1 + '2'; // '12'
  +'15'; // 15
  !'word'; // false
  1 + []; // '1'
  [1] + [2]; // '12'
  typeof NaN; // 'number'
  999999999999; // 10000000000000
  Math.max(); // -Infinity
  Math.min(); // Infinity
  [] + []; // ''
  [] + {}; // '[object Object]'
  {} + []; // 0
  typeof document.all; // 'undefined'
  true + true + true === 3; // true
  true - true === 0; // true
  (!+[]+[]+![]).length; // 9
  9 + '1'; // '91'
  91 - '1'; // 90
  [] == 0; // true
  [] == ![]; // true
  ',,,' == new Array(4); // true
  'false' == ['false']; // true
  [6, -2, 2, -7].sort() // [-2, -7, 2, 6]
}
```

see <https://github.com/denysdovhan/wtfjs> for further examples

equality is **not** a [[relation#reflexive relation]] in [[javascript]] because of [[ieee 754]] **`"NaN"`**

> **proof**
>
> ```javascript
> let x = NaN;
> x === x; // false
> x == x; // false
> ```

weak equality is **not** a [[relation#transitive relation]] in [[javascript]] &mdash; <https://youtu.be/vcFBwt1nu2U?t=1290> &mdash; JavaScript: The Good Parts, by Douglas Crockford

> **proof**
>
> ```javascript
> a = '0';
> b = 0;
> c = '';
>
> a == b; // true
> b == c; // true
> a == c; // false
> ```

### &mdash;

&mdash; <https://youtu.be/5wnlYIQKPXM>

&mdash; <https://dev.to/royal_bhati/understanding-weird-parts-of-javascript-44o>

&mdash; <https://youtu.be/qC_ioJQpv4E?t=2760>

&mdash; <https://youtu.be/_CEBG_s92P8?t=646>
