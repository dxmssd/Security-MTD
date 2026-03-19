from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

#modelo y escalador
MODEL_PATH = "model_ghost_node.pkl"
SCALER_PATH = "scaler_ghost_node.pkl"
                                    

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Modelo y escalador cargados correctamente.")
    
except Exception as e:
    print(f"Error al cargar el modelo o el escalador: {e}")
    model = None

#rute for kubernetes
@app.route('/health')
def health():
    return "OK", 200



@app.route('/predict', methods=['POST'])
def predict():
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    try:
        #converitr json a dataframe
        df = pd.DataFrame[(data)]
        
        #escalar los datos
        df_scaled = scaler.transform(df)
        
        #predecir con el modelo 0 = Normal, 1 = Ataque
        prediction = model.predict(df_scaled)[0]
        
        return jsonify({
            "status": "success",
            "prediction": int(prediction),
            "action" : "mutate" if prediction == 1 else "no action"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)