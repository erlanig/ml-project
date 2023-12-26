# Model clustering
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn.metrics
knn = pickle.load(open("./static/models/mammofix.pkl", "rb"))

# TES


def mammoPrediction(data):
    data = np.array(data).reshape(1, -1)
    # Get the prediction
    result = knn.predict(data)
    return result


app = Flask(__name__)

# Route untuk halaman utama


@app.route('/')
def index():
    return render_template('index.html')

# route 'form' set as 'form.html'


@app.route('/form')
def form():
    return render_template('form.html')

# Route untuk menangani submit form


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Mengambil data dari form
        birads = float(request.form['birads'])
        age = float(request.form['age'])
        shape = float(request.form['shape'])
        margin = float(request.form['margin'])
        density = float(request.form['density'])

        to_predict_list = [
            [
                birads,
                age,
                shape,
                margin,
                density,
            ]
        ]
        result = mammoPrediction(to_predict_list)

        if result == 0:
            prediction = "Benign"
        elif result == 1:
            prediction = "Malignant"
        else:
            prediction = "Error"

        # Kembalikan response atau tampilkan informasi yang diperlukan
        return render_template('output.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
