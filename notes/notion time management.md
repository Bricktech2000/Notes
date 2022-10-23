# Notion Time Management

## Day View

used for events that generally happen within a single day (friend meetups, classes, etc.)

> **filter**
>
> - _where_
>   - _where_ Status is not Completed, Archive, Revisit
>   - _and_ Date is not empty
> - _and_
>   - _where_ END_DATE is within the next week
>   - _or_ END_DATE is on or before today
>   - _or_ START_DATE is within the next week
>   - _or_ Status is Next Up, Work On

> **sort**
>
> 1. Status ascending
> 2. DDONE_OVER_DT descending

> **properties**
>
> 1. Category
> 2. Name

page load limit: 100

## Month View

used for long-term events (assignments, reports, deadlines, etc.). allows me to have a global view of everything going on at a glance

> **filter**
>
> - _where_
>   - _where_ Status is not Completed, Archive, Revisit
>   - _and_ Date is not empty
> - _and_
>   - _where_ Repeat is empty
>   - _or_ Repeat > 0

> **sort**
>
> 1. Status ascending
> 2. DDONE_OVER_DT descending

> **properties**
>
> 1. Category
> 2. Name

page load limit: 100

## Board View

used for tasks that don't have a clear deadline. sorted in categories (see _Status_ property)

> **filter**
>
> - _where_ Status is not empty

> **sort**
>
> (no sort, does not sort events automatically)

> **properties**
>
> 1. Category
> 2. Name
> 3. END_DATE

> **group by** Status

page load limit: 100

## Calendar View

> **filter**
>
> - _where_ Status is Completed
> - _and_
>   - _where_ Category is not empty
>   - _or_ Date is empty

> **properties**
>
> 1. Category
> 2. Name

## Pages

> **properties**
>
> 1. Category
> 2. Status
> 3. Date
> 4. Repeat
> 5. URL

## Database Properties

### Name

> **type** Title

### Category

> **type** Multiselect

- Body (brown)
- Intel (purple)
- Zlich (dark gray)
- Learn (orange)
- Finance (green)
- Network (blue)
- Standard (pink)
- Optimize (yellow)
- Reproduce (red)
- Hack (dark gray)
- Write (dark gray)
- Think (dark gray)
- Other (dark gray)
- Social (dark gray)
- Design (dark gray)
- Program (dark gray)
- Research (dark gray)
- LEC &mdash; lectures
- LAB &mdash; laboratory
- DGD &mdash; discussion group
- TUT &mdash; tutorial
- HW &mdash; homework (async, not worth marks)
- AST &mdash; assignment (async, worth marks)
- QUIZ &mdash; quiz (sync, worth marks)
- TEST &mdash; test (sync, worth marks)
- MTERM &mdash; midterm (sync, worth marks)
- REPORT &mdash; papers to write (async, worth marks)
- FINAL &mdash; final exam (sync, worth marks)

### Status

> **type** Select

- Work On (blue)
- (no status)
- Next Up (blue)
- Not Started (blue)
- Backlog (light gray)
- Blocked (light gray)
- Completed (light gray)
- Archive (light gray)
- Revisit (light gray)

### Date

> **type** Date

### Repeat

> **type** Number

### URL

> **type** URL

### CREATED_DATE

> **type** Created time

### LAST_EDITED_DATE

> **type** Last edited time

### START_DATE

> **type** Formula

```jsx
if (not empty(prop("ABS_REPEAT")),
  fromTimestamp(
    (
      timestamp(start(prop("Date"))) % (1000*60*60*24*prop("ABS_REPEAT")) - timestamp(now()) % (1000*60*60*24*prop("ABS_REPEAT"))
      + 1000*60*60*24*prop("ABS_REPEAT") + (1000*60*60*24*prop("ABS_REPEAT")/7)
    ) % (1000*60*60*24*prop("ABS_REPEAT")) - 1000*60*60*24*prop("ABS_REPEAT")/7
    + timestamp(now())
  ),
  if (prop("Status") == "Revisit",
    end(prop("Date")),
    if (start(prop("Date")) != end(prop("Date")),
      start(prop("Date")),
      end(prop("Date"))
    )
  )
)
```

### END_DATE

> **type** Formula

```jsx
if (not empty(prop("ABS_REPEAT")),
  fromTimestamp(
    (
      timestamp(end(prop("Date"))) % (1000*60*60*24*prop("ABS_REPEAT")) - timestamp(now()) % (1000*60*60*24*prop("ABS_REPEAT"))
      + 1000*60*60*24*prop("ABS_REPEAT") + (1000*60*60*24*prop("ABS_REPEAT")/7)
    ) % (1000*60*60*24*prop("ABS_REPEAT")) - 1000*60*60*24*prop("ABS_REPEAT")/7
    + timestamp(now())
  ),
  if (prop("Status") == "Revisit",
    end(prop("Date")),
    if (end(prop("Date")) != end(prop("Date")),
      end(prop("Date")),
      end(prop("Date"))
    )
  )
)
```

### DDONE_OVER_DT

> **type** Formula

see [[math notation]]

the $\ : \text{duration}$ below "shifts" the event left by $\text{duration}$, which allows long-term projects to end up with higher priority at the beginning of their time allocation. this prioritizes tasks better.

$$
\begin{align*}
\text{DDONE\_OVER\_DT} & = \text{now} \cdot \text{start} : \text{duration} - \text{duration} \\\
\text{duration} & = \text{end} \cdot \text{start}
\end{align*}
$$

```jsx
(timestamp(now()) -
  2 * timestamp(prop('START_DATE')) +
  timestamp(prop('END_DATE')) +
  1000) /
  (timestamp(prop('END_DATE')) - timestamp(prop('START_DATE')) + 1000);
```

### ABS_REPEAT

> **type** Formula

```jsx
abs(prop('Repeat'));
```
