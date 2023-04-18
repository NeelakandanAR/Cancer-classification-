import pandas as pd
from tensorflow.keras.models import model_from_json
from flask import Flask, request, jsonify

# Load the saved model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")

# Define Flask app
app = Flask(__name__)


# Define a route to accept POST requests for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json['data']

    # Create a DataFrame from the input data
    input_df = pd.DataFrame(input_data, columns=['concave points_worst',
                                                 'perimeter_worst',
                                                 'concave points_mean',
                                                 'radius_worst',
                                                 'perimeter_mean'])

    # Make predictions using the loaded model
    prediction = model.predict(input_df)
    prediction = (prediction > 0.5)

    # Return the prediction as a JSON response
    return jsonify({"prediction": int(prediction[0][0])})



if __name__ == '__main__':
    app.run()
