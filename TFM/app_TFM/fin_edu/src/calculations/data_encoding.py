import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def encode_data(data):
    encoder = OneHotEncoder(drop='first')
    gender_encoded = encoder.fit_transform(data[['gender']]).toarray()
    gender_df = pd.DataFrame(gender_encoded, columns=encoder.get_feature_names_out(['gender']))
    data_encoded = pd.concat([data.drop(['gender'], axis=1), gender_df], axis=1)
    return data_encoded
