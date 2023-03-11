### Deepika is a girl who loves writing comments. She posted a comment on website one day and she was wondering whether she would get upvotes or downvotes. There were a persons who would upvote, b persons who would downvote, and there were also another c persons who would vote, but she don't know whether they would upvote or downvote. Each of the a+b+c people would vote exactly one time. If there are more people upvote than downvote, the result will be "+"; if there are more people downvote than upvote, the result will be "-"; otherwise the result will be "0". Because of the c unknown persons, the result may be uncertain if there are more than one possible results. The result is uncertain if and only if there exist two different situations of how the c persons vote that means the results are different in the two situations. Help Deepika to tell the result or report that the result is uncertain.

## Input Format

The only line contains three integers a , b, c (0?a,b,c?100), corresponding to the number of persons who would upvote, downvote or unknown.

## Constraints

- (0<=a,b,c<=100)

## Output Format

If there is only one possible result, print the result : "+", "-" or "0". Otherwise, print "?" to report that the result is uncertain.
````
Sample Input 0

0 0 1

Sample Output 0

?
````

````
Sample Input 1

1 1 0

Sample Output 1

0
````