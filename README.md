# Customer-churn-analysis-and-profiling
Final year project

Dataset description
==========================

original datasets        -> ds1.pkl          | ds2.pkl 

transformed & cleaned    -> ds1_trans.pkl    | ds2_trans.pkl 

training sets            -> df1_train.pkl    | df2_train.pkl 

test sets                -> df1_test.pkl     | df2_test.pkl 

======================================================================

original datasets               -> ds1.pkl           | ds2.pkl 

where only churn entries        -> df1_churn.pkl     | df2_churn.pkl 

where only non churn entiries   -> df1_not_churn.pkl | df2_not_churn.pkl 



For customer profiles :-

1. Segment Customers [Unsupervised ML] using whole (excluding the churn column) as well as parts of dataset

2. Identify set of attributes for which we can obtain distinctive scatter plots

3. Eliminate outliers if any (clusters with very low member count)

4. Cross reference actual dataset [Index is needed for each entry] (since the data used for the clustering is the transformed data)

5. And calculate statistics on those selected set of attributes which makes up out profile

6. Tabulate range/mean/variance/attribute values for each cluster (consumer segment) for each of the selected attributes

7. Compare the profiles obtained on the datasets using various algorithms however each result is separate and we can only selected the best out of them and not combine them to arrive at a middle ground!


 

 


 

 

 


 

 
