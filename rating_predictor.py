
import pickle
import numpy as np
from flask import Flask, render_template, flash, request,redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    review = TextField('Review:', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

        #print form.errors
        if request.method == 'POST':
            review=request.form['review']
        #print name

        if form.validate():
            with open('log_reg.pkl','rb') as f_log_reg:
                log_reg=pickle.load(f_log_reg)

            with open('vocabulary.pkl','rb') as f_vocabulary:
                vocabulary=pickle.load(f_vocabulary)

            vector=TfidfVectorizer(vocabulary=vocabulary)
            #sample_review=['The movie is super','The movie is not worst','The movie is  excellent','The movie is  worst','I like this movie','i like this movie']
            sample_review=[review]
            sample_review_vector_x=vector.fit_transform(sample_review)
            print(sample_review)


            results=log_reg.predict(sample_review_vector_x)
            dict_result={ sample_review[i]:results[i] for i in range(len(sample_review)) }
            print(results)
            flash(str(int(results[0])))

        else:
            flash('Error: Game Review is required ')

        return render_template('rating_predictor.html', form=form)

if __name__ == "__main__":
    app.run()
