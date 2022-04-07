from flask import Flask, render_template, url_for, request, jsonify
import pandas as pd 
import numpy as np 
import joblib

app = Flask(__name__)

@app.route('/test_without_db')
def test():
    return jsonify({"result": "Success", "message": "Hello World"}), 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview')
def preview():
    df = pd.read_csv('data/iris.csv')
    return render_template('preview.html', df_view=df)

@app.route('/predict', methods=["POST"])
def analyze():
    if request.method == 'POST':
        petal_length = request.form['petal_length']
        sepal_length = request.form['sepal_length']
        petal_width = request.form['petal_width']
        sepal_width = request.form['sepal_width']
        model_choice = request.form['model_choice']

        sample_data = [sepal_length, sepal_width, petal_length, petal_width]
        clean_data = [float(i) for i in sample_data]

        ex1 = np.array(clean_data).reshape(1,-1)

        model = joblib.load("model.pkl")
        ans = model.predict(ex1)

        print(ans)
    return render_template('predict.html', petal_width=petal_width, petal_length=petal_length, sepal_length=sepal_length, sepal_width=sepal_width,result_prediction=ans,model_selected=model_choice)

if __name__ == '__main__':
    app.run(debug=True)
