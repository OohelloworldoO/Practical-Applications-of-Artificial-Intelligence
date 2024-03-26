from sklearn.preprocessing import MinMaxScaler

# 把數據按比例縮小至0~1範圍
scalar=MinMaxScaler(feature_range=(0, 1))
scaled_prices=scaler.fit_transform(df.values)