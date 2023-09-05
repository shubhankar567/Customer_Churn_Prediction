from flask import Flask, request, render_template, jsonify
from src.pipelines.predict_pipeline import CustomData, ModelPrediction
from flask_cors import cross_origin

application = Flask(__name__)


@cross_origin
@application.route('/')
def home_page():
    return render_template('index.html')

@cross_origin
@application.route('/predict', methods = ['GET', 'POST'])  # type: ignore
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')

    else: 
        data = CustomData(
            CustomerID = int(request.form.get('CustomerID')), # type: ignore 
            Name = request.form.get('Name'), # type: ignore
            Age = int(request.form.get('Age')), # type: ignore
            Gender = request.form.get('Gender'), # type: ignore
            Location = request.form.get('Location'), # type: ignore
            Subscription_Length_Months = int(request.form.get('Subscription_Length_Months')), # type: ignore
            Monthly_Bill = float(request.form.get('Monthly_Bill')), # type: ignore
            Total_Usage_GB = float(request.form.get('Total_Usage_GB')) # type: ignore
        )
        
        # Cnverting the random input data into a dataframe
        input_dataset = data.data_to_dataframe() # type: ignore

        # Predicting
        predict_obj = ModelPrediction()
        output = predict_obj.prediction(input_dataset)

        # Rounding off the result 
        results = round(output[0],2)

        return render_template('form.html', final_result = results)
    
if __name__ == '__main__':
    application.run(host = '0.0.0.0', port = 5000)