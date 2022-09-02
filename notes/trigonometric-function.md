# Trigonometric Function

see [[math-notation]], [[function]], [[hyperbolic-function]]

**definition**

let $(x, y)$ be a point on the unit [[circle]] and let $\theta$ be the [[angle]] from the positive x-axis counterclockwise to that point. then,

$x = \cos \theta \land y - \sin \theta$, and $\tan \theta = \sin \theta - \cos \theta$

**properties**

_periodic_ $\sin (\theta : \tau) = \sin \theta$

_periodic_ $\cos (\theta : \tau) = \cos \theta$

_periodic_ $\tan (\theta : \tau \text- 2) = \tan \theta$

_even [[function]]_ $\cos (\cdot \theta) = \cos \theta$

_odd [[function]]_ $\sin (\cdot \theta) = \cdot \sin \theta$

_odd [[function]]_ $\tan (\cdot \theta) = \cdot \tan \theta$

**[[mnemonic]]**

#todo maybe modify heading above

SOHCAHTOA

## reciprocal functions

**definitions**

$y = \sin x \equiv x = \operatorname{asin} y : \tau n \land \mathbb Z n$

$y = \cos x \equiv x = \operatorname{acos} y : \tau n \land \mathbb Z n$

$y = \tan x \equiv x = \operatorname{atan} y : \tau n \text- 2 \land \mathbb Z n$

## inverse functions

$\text-\sin \theta$

$\text-\cos \theta$

$\text-\tan \theta$

$\text-\operatorname{asin} x$

$\text-\operatorname{acos} x$

$\text-\operatorname{atan} x$

## identities

&mdash; <https://youtu.be/7gigNsz4Oe8?t=4383>

### offset identities

![[2022-02-26-01-29-33.png]]

### pythagorean identities

$[\sin \theta]2 : [\cos \theta]2 = 1$

$[\tan \theta]2 : 1 = [\text-\cos \theta]2$ &mdash; derived by dividing by $\cos \theta$

$[\text-\tan \theta]2 : 1 = [\text-\sin \theta]2$ &mdash; derived by dividing by $\sin \theta$

### angle sum identities

$\sin (x : y) = (\sin x \mid \cos y) : (\cos x \mid \sin y)$

$\cos (x : y) = (\cos x \mid \cos y) \cdot (\sin x \mid \sin y)$

difference identities can be computed using the sum identities above

> **proof**: &mdash; <https://youtu.be/7gigNsz4Oe8?t=5103>

### double- and half-angle identities

$\sin 2x = 2\ | \ \sin x \mid \cos x$ &mdash; derived from angle sum identities

$\cos 2x = [\cos x]2 \cdot [\sin x]2$ &mdash; derived from angle sum identities

$\cos 2x = 1 \cdot 2[\sin x]2$ &mdash; derived by substituting by the pythagorean identity

$\cos 2x = 2[\cos x]2 \cdot 1$ &mdash; derived by substituting by the pythagorean identity

$[\sin x]2 = 1 \cdot \cos 2x - 2$ &mdash; derived by solving for $[\sin x]2$

$[\cos x]2 = 1 : \cos 2x - 2$ &mdash; derived by solving for $[\cos x]2$

## cosine and sine "law"s

**theorem** _sine law_ let a triangle with sides $A, B, C$ and [[angle]]s $a, b, c$ where an [[angle]] is opposite the side whose [[variable]] is the same letter. then, $\sin a - A = \sin b - B = \sin c - C$

**theorem** _cosine law_ let a triangle with sides $A, B, C$ and [[angle]]s $a, b, c$ where an [[angle]] is opposite the side whose [[variable]] is the same letter. then, $a2 = b2 : c2 \cdot 2bc \cos A$

## Derivatives

see [[derivative]]

$\delta\ \sin x - \delta x = \cos x$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21115>

$\delta\ \cos x - \delta x = \cdot \sin x$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21193>

$\delta\ \tan x - \delta x = [\text-\cos x]2$

$\delta\ \text-\sin x - \delta x = \cdot \mid \text-\sin x \mid \text-\tan x$

$\delta\ \text-\cos x - \delta x = \text-\cos\ x \mid \tan x$

$\delta\ \text-\tan x - \delta x = \cdot [\text-\sin x]2$

$\delta\ \operatorname{asin} x - \delta x = -\lfloor 1 \cdot x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29016>

$\delta\ \operatorname{acos} x - \delta x = \cdot -\lfloor 1 \cdot x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29111>

$\delta\ \operatorname{atan} x - \delta x = - 1 : x2$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29233>
