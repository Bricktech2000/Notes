# Minimax

> **resource** Sandworm, my competitive Battlesnake running [[minimax]] over Voronoi --- <https://github.com/Bricktech2000/Sandworm>

--- <https://youtu.be/U4ogK0MIzqk> and <https://youtu.be/l-hh51ncgDI>

--- <https://brilliant.org/wiki/minimax/>

[[minimax]] is a decision rule and [[tree]] search algorithm for turn-based games. it chooses the move corresponding to the **best worst-case scenario**

_the maximin value is the highest value that the player can be sure to get without knowing the actions of the other players; equivalently, it is the lowest value the other players can force the player to receive when they know the player's action_ --- Wikipedia

**representation**

```python
def minimax(state, depth, player):
  if depth == 0 or game_over(state):
    return evaluate(state)

  best = max() if is_maximizing(player) else min()
  for move in gen_moves(state):
    state.make_move(move)
    eval = minimax(state, depth - 1, next_player(player))
    if is_maximizing(player):
      best = max(best, eval)
    else:
      best = min(best, eval)
    state.unmake_move(move)

  return best

best = minimax(CURRENT_STATE, TARGET_DEPTH, CURRENT_PLAYER)
```

## Paranoid Assumption

the simplest way of adapting [[minimax]] to games where players move simultaneously is to pretend that you move first. the assumption is called _paranoid_ because it's like pretending that all other players, when choosing their move, already know what move you'll make. --- <https://stackoverflow.com/questions/19628971/expanding-minimax-for-simultaneous-move-games> and me

## Alpha--Beta Pruning

--- <https://youtu.be/l-hh51ncgDI?t=311>

[[minimax#alpha--beta pruning]] avoids exploring branches that can't affect the outcome by keeping track of a "running maximum" `alpha` and a "running minimum" `beta`. more branches get pruned when better moves (better for the current `player`) are explored first, so design `gen_moves()` with care

> **note** [[minimax#alpha--beta pruning]]'s evals are lower/upper bounds on the real [[minimax]] evals, so top-level evals can't be used to deduce what the best move is

**representation**

```diff
-def minimax(state, depth, player):
+def minimax(state, depth, player, alpha=max(), beta=min()):
   if depth == 0 or game_over(state):
     return evaluate(state)

   best = max() if is_maximizing(player) else min()
   for move in gen_moves(state):
     state.make_move(move)
-    eval = minimax(state, depth - 1, next_player(player))
+    eval = minimax(state, depth - 1, next_player(player), alpha, beta)
     if is_maximizing(player):
       best = max(best, eval)
+      alpha = max(alpha, eval)
     else:
       best = min(best, eval)
+      beta = min(beta, eval)
     state.unmake_move(move)

+    if alpha >= beta:
+      break

   return best

 best = minimax(CURRENT_STATE, TARGET_DEPTH, CURRENT_PLAYER)
```

### Iterative Deepening

--- <https://youtu.be/U4ogK0MIzqk?t=1566>

--- <https://www.chessprogramming.org/Iterative_Deepening>

[[minimax#iterative deepening]] initially searches to depth 0 then iteratively searches deeper and deeper until a target depth is reached or a time limit is hit. [[minimax#alpha--beta pruning]] works best when exploring better moves first, so by keeping track of the best moves each search we can prune more branches in subsequent searches. due to this, [[minimax#iterative deepening]] tends to be faster than searching to the target depth directly

**representation**

```diff
-def minimax(state, depth, player, alpha=max(), beta=min()):
+def minimax(state, depth, player, cache, alpha=max(), beta=min()):
   if depth == 0 or game_over(state):
     return evaluate(state)

   best = max() if is_maximizing(player) else min()
-  for move in gen_moves(state):
+  for move in gen_moves(state, cache):
     state.make_move(move)
-    eval = minimax(state, depth - 1, next_player(player), alpha, beta)
+    eval = minimax(state, depth - 1, next_player(player), cache, alpha, beta)
+    cache[hash(state)] = eval
     if is_maximizing(player):
       best = max(best, eval)
       alpha = max(alpha, eval)
     else:
       best = min(best, eval)
       beta = min(beta, eval)
     state.unmake_move(move)

     if alpha >= beta:
       break

   return best

-best = minimax(CURRENT_STATE, TARGET_DEPTH, CURRENT_PLAYER)
+cache = {}
+for depth in range(TARGET_DEPTH):
+  best = minimax(CURRENT_STATE, depth, CURRENT_PLAYER, cache)
```
