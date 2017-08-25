# kaggle_SFCrime
This is the readme file for Kaggle SF crime data prediction ( April 2016)
 
<p>This repository is created for the Kaggle SF crime prediction project. In the file name <i>SF crime(1).ipynb</i>, Bernoulli Naive Bayes method was used as the predictive model, and 
in <i>SF crime(2).ipynb</i>, XGB classifier was used and yielded better results. For both methods, weekeday was extracted from Dates column, and one-hot-encoding was performed for the categorical columns. Features used for modeling were the same for both models - mainly the neighborhoods, gps coordinate (Y), and time. For the XGB classifier, a feature importance graph was generated as part of the XGB library.</p>
<p align="center"> <img scr="feature_importance.png"></p>

<p> Using Tableau, a map of the crime activity is generated as shown (for interactive map, click <a href="https://public.tableau.com/shared/9G5CTJZ4Y?:display_count=yes"> here </a>).
<p align="center">
  <img src="crime_location.png" width="450"/>
</p>
