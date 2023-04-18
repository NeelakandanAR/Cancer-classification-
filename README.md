Cancer Cell Classifier
This project is an implementation of an artificial neural network (ANN) to classify cancer cells as benign or malignant based on 30 features. The data contains 570 cancer cells in total, with 357 benign and 212 malignant.

Features
The dataset has 30 features, which include mean, standard error, and worst (or largest) values for the following features:

radius
texture
perimeter
area
smoothness
compactness
concavity
concave points
symmetry
fractal dimension
Installation
To run this project, you will need the following Python packages installed:

pandas
tensorflow
flask
matplotlib
seaborn
You can install these packages using pip:

Copy code
pip install pandas tensorflow flask matplotlib seaborn
Usage
To use the cancer cell classifier, send a POST request to the Flask API with the cancer cell features in a JSON payload. For example, in Postman, you can send a request like this:

lua
Copy code
POST /predict
Content-Type: application/json

{
    "data": [[3.48797251e-01, 2.11275482e-01, 1.89910537e-01, 2.29953951e-01, 2.35951060e-01]]
}
The API will respond with a JSON payload containing the predicted class (0 for benign, 1 for malignant):

css
Copy code
HTTP/1.1 200 OK
Content-Type: application/json

{
    "prediction": 0
}
Contributing
Contributions to this project are welcome. If you find any bugs or want to suggest improvements, please open an issue or submit a pull request.

Credits
This project was created by Neelakandan AR. The cancer cell dataset was obtained from the UCI Machine Learning Repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to Kaggle for their assistance with the dataset.
