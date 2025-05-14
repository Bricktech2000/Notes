# Floating-Point Number

**see** [[number]], [[logarithmic number system]], [[fixed-point number]], [[ieee 754]]

programmers overuse floats. a fundamental property of [[floating-point number]]s is their **steady relative precision**. using [[floating-point number]]s when you expect **steady absolute precision**---like with position vectors, global timers and monetary figures---is begging for trouble. when you need unbounded values, use arbitrary-precision numbers; when you need decimals, use [[fixed-point number]]s; when you need steady relative precision, and only when you need steady relative precision, use [[floating-point number]]s

> **example** Minecraft's systems begin to break down a few billion blocks out, dUE To pRecISioN LoSs --- <https://youtu.be/QIWI5wyCIcg> and <https://youtu.be/UENe51jHDw4> and <https://minecraft.wiki/w/Java_Edition_distance_effects>
