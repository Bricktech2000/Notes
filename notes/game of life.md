# Game of Life

**aka** _Conway's Game of Life, Life_

the [[game of life]] is a [[turing complete]] cellular automaton on an infinite two-dimensional grid of _cells_, each of which is either _alive_ or _dead_, and each of which interacts with its _neighbors_, a three-by-three grid of cells surrounding it, while obeying the following rules:

```rust
let next_state = match current_state {
  State::Alive => match neighbor_count {
    2 | 3 => State::Alive, // if `neighbor_count` excludes current cell
    // 3 | 4 => State::Alive, // if `neighbor_count` includes current cell
    _ => State::Dead,
  },
  State::Dead => match neighbor_count {
    3 => State::Alive,
    _ => State::Dead,
  },
}
```

or equivalently:

```rust
let next_state = match neighbor_count {
  3 => State::Alive,
  2 => current_state, // if `neighbor_count` excludes current cell
  // 4 => current_state, // if `neighbor_count` includes current cell
  _ => State::Dead,
}
```

> **note** the [[entropy]] of most starting positions in the [[game of life]] seems to reach a maximum after few generations --- me. slowing the increase in [[entropy]] might lead to noteworthy results

**representation**

![[unnamed.gif]]

--- <https://experiments.withgoogle.com/conway-game-of-life>
