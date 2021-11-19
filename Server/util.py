import json
import pickle
import numpy as np
__ng_grp_names= None
__nh_names=None
__rt_names=None

__data_columns=None
__rf2_random =None


def get_estimated_price(neighbourhood_grp, neighbourhood, room_type, min_nights, no_of_reviews,
                  reviews_per_month, host_count, availability_365, name_length):
    try:
        ng_index = __data_columns.index(neighbourhood_grp.lower())
        nh_index = __data_columns.index(neighbourhood.lower())
        rt_index = __data_columns.index(room_type.lower())
    except:
        ng_index = nh_index = rt_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = min_nights
    x[1] = no_of_reviews
    x[2] = reviews_per_month
    x[3] = host_count
    x[4] = availability_365
    x[5] = name_length

    if ng_index >= 0:
        x[ng_index] = 1
    if nh_index >= 0:
        x[nh_index] = 1
    if rt_index >= 0:
        x[rt_index] = 1

    return round(float(__rf2_random.predict([x])[0]),2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __ng_grp_names
    global __nh_names
    global __rt_names
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __ng_grp_names = __data_columns[6:11]
        __nh_names = __data_columns[11:230]
        __rt_names = __data_columns[230:]
    global __rf2_random
    if __rf2_random is None:
        with open("./artifacts/Airbnb_NYC_Price_Prediction.pickle", 'rb') as f:
            __rf2_random = pickle.load(f)
    print("loading saved artifacts...done")


def get_ng_grp_names():
    return __ng_grp_names

def get_data_columns():
    return __data_columns

def get_nh_names():
    return __nh_names

def get_rt_names():
    return __rt_names


if __name__ =='__main__':
    load_saved_artifacts()
