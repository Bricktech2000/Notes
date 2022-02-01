# Notion Time Management

## Board View

- used for tasks that don't have a clear deadline
- sorted in categories (see *Status* property)

### filter

displays any task that has a status set

### sort

doesn't sort events automatically

## Day View

- used for events that generally happen within a single day (friend meetups, classes, etc.)

### filter

end date is within next week or end date is on or before today

and

status is not completed and date is not empty

> displays any event that isn't completed and that is within one day of today
> 

### sort

> sorts events by ascending end date
> 

## Month View

- used for long-term events (assignments, reports, deadlines, etc.)
- allows me to have a global view of everything going on at a glance

### filter

displays any event that has a date, that isn't completed and that isn't a class to attend

### sort

sorts events by status, or

sorts events by priority based on the current progress on the timeline (ddone over dt)

## Database Properties

### Name (visible)

the name of the page

### Date (visible)

the start and end date for a page

### EMPTY_DATE

an empty date, used below

### CREATED_DATE

the date a page was created, used below

### START_DATE

```jsx
if(contains(prop("Category"), "DAY"), fromTimestamp(timestamp(start(prop("Date"))) % 86400000 + floor(timestamp(now()) / 86400000) * 86400000), if(contains(prop("Category"), "WK") or contains(prop("Category"), "LEC") or contains(prop("Category"), "DGD") or contains(prop("Category"), "LAB") or contains(prop("Category"), "TUT"), fromTimestamp((timestamp(start(prop("Date"))) - timestamp(now()) % 604800000 + 86400000) % 604800000 + timestamp(now()) % 604800000 - 86400000 + floor(timestamp(now()) / 604800000) * 604800000), if(prop("Status") == "Not Completed", end(prop("Date")), if(start(prop("Date")) != end(prop("Date")), start(prop("Date")), if(not empty(prop("Date")), prop("CREATED_DATE"), prop("EMPTY_DATE"))))))
```

### END_DATE

```jsx
if(contains(prop("Category"), "DAY"), fromTimestamp(timestamp(end(prop("Date"))) % 86400000 + floor(timestamp(now()) / 86400000) * 86400000), if(contains(prop("Category"), "WK") or contains(prop("Category"), "LEC") or contains(prop("Category"), "DGD") or contains(prop("Category"), "LAB") or contains(prop("Category"), "TUT"), fromTimestamp((timestamp(end(prop("Date"))) - timestamp(now()) % 604800000 + 86400000) % 604800000 + timestamp(now()) % 604800000 - 86400000 + floor(timestamp(now()) / 604800000) * 604800000), if(start(prop("Date")) != end(prop("Date")), end(prop("Date")), if(not empty(prop("Date")), end(prop("Date")), prop("EMPTY_DATE")))))
```

### DDONE_OVER_DT

```jsx
(timestamp(now()) - timestamp(prop("START_DATE"))) / (timestamp(prop("END_DATE")) - timestamp(prop("START_DATE")) + 1000)
```

### Status (visible)

one of the following values:

- Back Burner
- Not Started
- Next Up
- Work On
- No Status
- Worked On
- Blocked
- Not Completed (hidden)
- Completed (hidden)
- Archive (hidden)

### Category (visible)

multiple of the following values:

- WK — repeats every week
- DAY — repeats every day
- OPT — optional event
- Personal (blue)
- Learning (blue)
- Hobbies (orange)
- Social (orange)
- Work (green)
- uOttawa (green)
- **all classes**
- LEC — lectures
- LAB — laboratory
- DGD — discussion group
- TUT — tutorial
- HW — homework (async, not worth marks)
- AST — assignment (async, worth marks)
- QUIZ — quiz (sync, worth marks)
- TEST — test (sync, worth marks)
- MTERM — midterm (sync, worth marks)
- REPORT — papers to write (async, worth marks)
- FINAL — final exam (sync, worth marks)

### URL (visible)

a quick way to add a link to a page