import flask
from flask import Flask, request, render_template


app = Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['GET', 'POST'])
def predict():
    if request.method=="GET":
        return render_template("index.html")
    else:
        import joblib
        model = joblib.load('marriage_age_predict_model.ml')
        predicted_age_of_marriage = model.predict([[int(request.form['gender']),
                                int(request.form['religion']),
                                int(request.form['caste']),
                                int(request.form['mother_tongue']),
                                int(request.form['country']),
                                int(request.form['height_cms']),
                               ]])
        return render_template("index.html", result=round(predicted_age_of_marriage[0],2))


if __name__ == "__main__":
    app.run(debug=True)
