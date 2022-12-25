# Improved Rating System

_a more intuitive way to represent "star" ratings_

> **procedure**
>
> create a graph with the following axes:
>
> - horizontal axis: rating
> - vertical axis: number of people who gave a given rating
>
> then, compute the following to show the user:
>
> - calculate the average value of the graph to get a _stability index_, where a larger number means more stability because more people submitted ratings.
> - calculate the average [[function#slope]] of the graph to get a _positivity index_, where a larger number means the reviews were more positive since there are more 5- and 4-star reviews than 1- or 2-star ones.
> - calculate the average [[function#curvature]] of the graph to get an _agreement index_, where a larger number means the reviews agree further with each other since 5-star and 1-star reviews are less common than more general 2-, 3- and 4-star ones.
