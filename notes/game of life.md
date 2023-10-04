# Game of Life

**aka** _Conway's Game of Life, Life_

the [[game of life]] is a [[turing complete]] cellular automaton on an infinite two-dimensional grid of _cells_, each of which is either _alive_ or _dead_, and each of which interacts with its _neighbors_, a three-by-three grid of cells surrounding it, while obeying the following rules:

```rust
// `neighbor_count` includes the current cell
let next_state = match neighbor_count {
  3 => State::Alive,
  4 => current_state,
  _ => State::Dead,
}
```

the [[entropy]] of most starting positions in the [[game of life]] seems to reach a maximum after relatively few generations &mdash; me. if the increase in [[entropy]] could be slowed down, the [[game of life]] might reveal other fascinating results

**representation**

![[unnamed.gif]]

&mdash; <https://experiments.withgoogle.com/conway-game-of-life>
