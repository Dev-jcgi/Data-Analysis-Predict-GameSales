from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Cargar el modelo
model = pickle.load(open('model/model_regresion.pkl', 'rb'))

# Cargar el dataframe
df_juegos = pd.read_csv('data/df_juegos.csv')

# Cargar las columnas del modelo de entrenamiento
with open('model/X_train.pkl', 'rb') as f:
    model_columns = pickle.load(f)

@app.route('/')
def home():
    generos = df_juegos['Genero'].unique().tolist()
    plataformas = df_juegos['Plataforma'].unique().tolist()
    companias = df_juegos['Compañia_Desarrollo'].unique().tolist()
    
    return render_template('index.html', generos=generos, plataformas=plataformas, companias=companias)

@app.route('/predict', methods=['POST'])
def predict():
    # Recibir los datos del formulario
    genero = request.form['genero']
    plataforma = request.form['plataforma']
    compania = request.form['compania']
    
    # Crear un dataframe con los datos recibidos
    nuevo_juego = pd.DataFrame({
        'Genero': [genero],
        'Plataforma': [plataforma],
        'Compañia_Desarrollo': [compania]
    })

    # Convertir las características categóricas a numéricas
    nuevo_juego = pd.get_dummies(nuevo_juego)
    nuevo_juego = nuevo_juego.reindex(columns=model_columns, fill_value=0)

    # Hacer la predicción
    ventas_predichas = model.predict(nuevo_juego)
# Generar el mensaje
    if ventas_predichas[0] >= 0.548394:
        mensaje = "La predicción sugiere que el juego será exitoso"
    else:
        mensaje = "Alguna de las características seleccionadas no cumplen con los requisitos para que el juego sea exitoso"

    return render_template('result.html', prediction=ventas_predichas[0], mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
