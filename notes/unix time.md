# Unix Time

**see** [[iso 8601]], [[math notation]]

&mdash; <https://en.wikipedia.org/wiki/Unix_time>

[[unix time]] is a date and [[time]] representation widely used in computing. simplistically, it is the [[integer]] number of seconds elapsed since `1970-01-01T00:00:00Z`, see [[iso 8601]]. in actuality, [[unix time]] experiences a discontinuity during leap seconds so the [[unix time]] number increases by exactly **`86400`** each [[coordinated universal time]] day

**properties**

[[unix time]] is not a [[function#continuous function]] with respect to [[time]] because of leap seconds

[[unix time]]stamps do not necessarily map to a unique instant in [[time]] because of positive leap seconds

> **example** `1483142400` is [[unix time]] for both `2016-12-31T23:59:60Z` (start of the leap second) and `2017-01-01T00:00:00Z` (end of the leap second, one second later)

[[unix time]]stamps do not necessarily map to a valid instant in [[time]] because of negative leap seconds

> **note** no negative leap seconds have been declared as of writing this note
