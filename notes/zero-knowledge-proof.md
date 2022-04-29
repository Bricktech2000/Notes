# Zero-Knowledge Proof

_a [[proof]] that an entity knows something that does not give away any additional information_

see [[proof]]

## intuitive example

_color blind verifier_

a prover wants to show a verifier that they knows the color of two balls without revealing either color. note that the verifier cannot see the color of either ball as they are color blind.

- the verifier hides both balls behind their back and may or may not switch the balls around
- the verifier reveals the balls and asks the prover to say whether the balls were switched or not

the process above is repeated $k$ times to reduce the probability of "lucky guesses" from an untrustworthy prover

this process proves with high probability that the prover knows the color of both balls without revealing either color

## uses

Zcash and Monero are examples of [[cryptocurrency]]es that use [[zero-knowledge-proof]]s for transactions
