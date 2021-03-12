
import pandas as pd
import matplotlib.pyplot as plt

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Willkommenseite
@app.route("/")
@app.route("/Welcome.html")
def welcome():
    return render_template('Welcome.html')

# Navigationsseite
@app.route("/index.html")
def home():
    return render_template('index.html')


#Data Source
file = 'Data/WHO.xlsx'
# Load spreadsheet: xl
xl = pd.ExcelFile(file)


#Child Growth Documentation
@app.route("/Growth.html")
def growth():

    # load a sheet into a DataFrame by name
    df1 = xl.parse('Größe Mädchen (cm)')
    # create copy to avoid data manipulation
    girl_length = df1.copy()

    # diagram data
    plt.figure(0)
    plt.plot(girl_length.Woche, girl_length['M'], color='green', label='Mittelwert')

    # customization of plot
    plt.title('Größe Mädchen (cm)')
    plt.xlabel('Zeit (Woche)')
    plt.ylabel('Länge (cm)')
    plt.axis((0, 14, 42, 68))

    # legend
    plt.legend(loc='lower right')


    return render_template('Growth.html')


#Child Weight Documentation
@app.route("/Weight.html")
def weight():

    df2 = xl.parse('Gewicht Mädchen (gramm)')
    girl_weight = df2.copy()

    plt.figure(1)
    plt.plot(girl_weight.Woche, girl_weight['M'], color='green', label='Mittelwert')

    plt.title('Gewicht Mädchen (gramm)')
    plt.xlabel('Zeit (Woche)')
    plt.ylabel('Masse (Gramm)')
    plt.axis((0, 14, 3000, 6000))

    # legend
    plt.legend(loc='lower right')
    plt.savefig('static/images/girl_weight.png')

    return render_template('Weight.html')


#Mental Health Quizz
@app.route("/Mental_Health.html")
def quizz():
    return render_template('Mental_Health.html')


#Future Goal if user has no permission to enter admin
#user gets redirected
@app.route("/admin")
def admin():
    return redirect(url_for("index.html"))


if __name__ == "__main__":
    app.run(debug=True)
