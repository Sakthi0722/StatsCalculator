#***Cochran’s Sample Size Formula***

The Cochran formula allows you to calculate an ideal sample size given a desired level of precision, desired confidence level, and the estimated proportion of the attribute present in the population.

Cochran’s formula is considered especially appropriate in situations with large populations. A sample of any given size provides more information about a smaller population than a larger one, so there’s a ‘correction’ through which the number given by Cochran’s formula can be reduced if the whole population is relatively small.

The Cochran formula is:

![cochran](https://www.statisticshowto.com/wp-content/uploads/2018/01/cochran-1.jpeg)

Where:

*e is the desired level of precision (i.e. the margin of error),*

*p is the (estimated) proportion of the population which has the attribute in question, and*

*q is 1 – p.*

The z-value is found in a Z table.

Suppose we are doing a study on the inhabitants of a large town, and want to find out how many households serve breakfast in the mornings. We don’t have much information on the subject to begin with, so we’re going to assume that half of the families serve breakfast: this gives us maximum variability. So p = 0.5. Now let’s say we want 95% confidence, and at least 5 percent—plus or minus—precision. A 95 % confidence level gives us Z values of 1.96, per the normal tables, so we get

>((1.96)^2 (0.5) (0.5)) / (0.05)^2 = 385.

So a random sample of 385 households in our target population should be enough to give us the confidence levels we need.

