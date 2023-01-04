# Personal Tracker

## Finance

**see** [[math notation]], [[finance]]

asset tracking over [[time]] to improve [[intention]]ality in personal [[finance]]

[[python]] server responsible for all data analysis. [[javascript]] web app responsible for data visualization. using a web app is meant to be an "afterthought" that can easily be swapped out for a different data visualization tool.

### python server

- fetch [[money]] exchange rates, [[stock market]] and [[cryptocurrency]] prices, etc.
- load transaction history and asset models from a config file

### data visualization

library to use: <https://nivo.rocks/stream/> &mdash; <https://www.youtube.com/watch?v=gmLzi1w85t4>

- represent assets as a [[list]] of plots:
  1. $(t, V\ t)$ &mdash; value over [[time]]. used for net worth, total savings, etc.
  2. $(t, \delta\ V\ t - \delta t)$ &mdash; [[derivative]] of value over [[time]]. used for recurring expenses, income, savings rate, etc.
  3. $(t, [\delta\ \lceil V\ t \rceil - \delta t])$ &mdash; [[exponential derivative]] of value over [[time]]. used for [[inflation]], compound interest, [[stock market]] growth, etc.

### config file

## Habits
