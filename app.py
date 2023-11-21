from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():

    pred_value = 0
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        engine = request.form['engine']
        mileage = request.form['mileage']
        fuel = request.form['fuel']
        transmission = request.form['transmission']
        owner = request.form['owner']
        seller_type = request.form['seller_type']

        feature_list = []
        
        feature_list.append(int(year))
        feature_list.append(float(mileage))
        feature_list.append(int(engine))

        name_list = ['maruti', 'hyundai', 'mahindra', 'tala', 'honda', 'toyota', 'ford', 'chevrolet', 'renault',
         'volkswagen', 'bmw', 'skoda', 'nissan', 'jaguar', 'volvo', 'datsun', 'mercedes-benz', 'fiat', 'audi', 'lexus', 
         'jeep', 'mitsubishi', 'force', 'land', 'isuzu', 'kia', 'Ambassador', 'daewoo', 'mg', 'ashok', 'opel']
        fuel_list = ['diesel', 'petrol', 'other_fuel']
        transmission_list = ['manual', 'auto']
        owner_list = ['first_owner', 'second_owner', 'third_owner', 'fourth_&_above_owner']
        seller_type_list = ['individual', 'dealer', 'trustmark_dealer']

        
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)


        traverse_list(name_list, name)
        traverse_list(fuel_list, fuel)
        traverse_list(transmission_list, transmission)
        traverse_list(owner_list, owner)
        traverse_list(seller_type_list, seller_type)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)*5

    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)