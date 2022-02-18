# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 'ASD_toddler_model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('quiz.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Age_Mons = int(request.form['age'])
        Sex = request.form.get('sex')
        A1 = request.form.get('A1')
        A2 = request.form.get('A2')
        A3 = request.form.get('A3')
        A4 = request.form.get('A4')
        A5 = request.form.get('A5')
        A6 = request.form.get('A6')
        A7 = request.form.get('A7')
        A8 = request.form.get('A8')
        A9 = request.form.get('A9')
        A10 = request.form.get('A10')
        Ethnicity = request.form.get('Ethnicity')
        Jaundice = request.form.get('Jaundice')
        Family_mem_with_ASD = request.form.get('Family_mem_with_ASD')
        data = np.array([[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10,
                        Age_Mons, Sex, Ethnicity, Jaundice, Family_mem_with_ASD]])
        my_prediction = model.predict(data)
        return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)
