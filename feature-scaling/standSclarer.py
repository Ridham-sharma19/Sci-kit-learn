from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler (from scikit-learn) is used to scale numerical data so that:

# Mean (μ) = 0
# Standard Deviation (σ) = 1

scaler = StandardScaler()
x_scaled = scaler.fit_transform()

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform()