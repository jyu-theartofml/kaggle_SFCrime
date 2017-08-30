from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators, FloatField
import pickle
#import sqlite3
from sklearn.externals import joblib
import os
import numpy as np
import pandas as pd

# import word vector from local dir


app2 = Flask(__name__)

######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
clf = joblib.load('xgb_model.pkl')
col_names=joblib.load('col_names.pkl')

def classify(document):
    pkl_file = open('crime_categories.pkl', 'rb')
    crime = pickle.load(pkl_file)
    feat_array=np.zeros(len(col_names))
    for f in document:
        arr_index = np.where(col_names == f)
        feat_array[arr_index[0]]=1
    feat_array[-3]=document[2]
    feat_array[-2]=document[3]
    feat_array[-1]=document[4]
    h=feat_array.reshape(len(feat_array), 1)
    X=pd.DataFrame(h.T, columns=col_names)
    y = clf.predict(X)
    result=clf.predict_proba(X)
    proba = np.max(result)
    return crime[y[0]], proba


month_list=['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep',
   'Oct', 'Nov', 'Dec']
neighborhood_list=['BAYVIEW', 'CENTRAL', 'INGLESIDE', 'MISSION',
   'NORTHERN', 'PARK', 'RICHMOND', 'SOUTHERN', 'TARAVAL', 'TENDERLOIN']
hour_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

######## Flask
class ReviewForm(Form):
    Y_coord = FloatField('latitude(i.e., 37.733)', validators= [validators.InputRequired()])
    X_coord = FloatField('longitude(i.e., -122.394)',validators= [validators.InputRequired()])


@app2.route('/')
def index():

    form = ReviewForm(request.form)
    return render_template('index.html', form=form, month_list=month_list, hour_list=hour_list, neighborhood_list=neighborhood_list)

@app2.route("/test" , methods=['GET', 'POST'])
def test():
    form = ReviewForm(request.form)
    latitude = form.Y_coord.data
    longitude = form.X_coord.data
    month=request.form.get('month')
    neighborhood=request.form.get('neighborhood')
    hour=request.form.get('hour')
    data=[month, neighborhood, longitude, latitude, int(hour)]
    return render_template('test.html',
                            data=data)


@app2.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST':
        latitude = form.Y_coord.data
        longitude = form.X_coord.data
        month=request.form.get('month')
        neighborhood=request.form.get('neighborhood')
        hour=request.form.get('hour')
        data=[month, neighborhood, longitude, latitude, int(hour)]
        y, proba = classify(data)
        return render_template('results.html',
                                data=data,
                                prediction=y,
                                probability=round(proba*100, 2))
    return render_template('index.html', form=form, month_list=month_list, hour_list=hour_list, neighborhood_list=neighborhood_list)


if __name__ == '__main__':
    app2.run(debug=True)
