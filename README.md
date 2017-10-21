# kaggle_SFCrime
### UPDATE: the trained model is deployed into a Flask web app hosted by pythonanywhere.com (http://jypucca.pythonanywhere.com/). 

<p>This repository is created for the Kaggle SF crime prediction project. In the file name <i>SF crime(1).ipynb</i>, Bernoulli Naive Bayes method was used - it assumes independence between the features (columns in the dataframe) and that each feature is treated as a binary variable. Therefore, one-hot-encoding is required to format the data. In <i>SF crime(2).ipynb</i>, Xtreme Gradient Boosting (XGB) classifier was used and yielded better results (top 29% LB ranking). XGB is a regularized boosting algorithm in which the weak classifier learns its parameters based on the performance of the previous classifier, giving more weight to previously misclassified samples (or large error in case of regression). 
 
For the XGB classifier, a feature importance graph was generated as part of the XGB library. Feature importance score (F score on x-axis) is a measure of how useful a feature is when it comes to improving decision tree performance within the Ensemble model. Based on this graph, the GPS location, hours, and certain months (June, October) yielded strong predictive powers in determining the probability of a crime category.</p>

![alt text](https://github.com/yinniyu/kaggle_SFCrime/blob/master/feature_importance(2).png)

<p> Using Tableau, a map of the crime activity is generated as shown (for interactive map, click <a href="https://public.tableau.com/shared/F3RWWW3FS?:display_count=yes"> here </a>).
<p align="center">
  <img src="crime_location.png" width="650"/>
</p></p>
