from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_ng_grp_names', methods=['GET'])
def get_ng_grp_names():
    response = jsonify({
        'ng_grps': util.get_ng_grp_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_nh_names', methods=['GET'])
def get_nh_names():
    response = jsonify({
        'nh_names': util.get_nh_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_rt_names', methods=['GET'])
def get_rt_names():
    response = jsonify({
        'rt_names': util.get_rt_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_airbnb_price', methods = ['GET','POST'])
def predict_airbnb_price():
    neighbourhood_grp = request.form.get('neighbourhood_grp',False)
    neighbourhood = request.form.get('neighbourhood',False)
    room_type = request.form.get('room_type',False)
    min_nights = int(request.form.get('min_nights',False))
    no_of_reviews  = int(request.form.get('no_of_reviews',False))
    reviews_per_month = float(request.form.get('reviews_per_month',False))
    host_count = int(request.form.get('host_count',False))
    availability_365 = int(request.form.get('availability_365',False))
    name_length = int(request.form.get('name_length',False))

    response = jsonify({
        'airbnb_price': util.get_estimated_price(neighbourhood_grp, neighbourhood, room_type, min_nights,
                                                     no_of_reviews,reviews_per_month, host_count, availability_365,
                                                     name_length)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    print("Starting Python Flask Server for Airbnb NYC Price Prediction")
    util.load_saved_artifacts()
    app.run()
