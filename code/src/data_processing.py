import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(df):
    # 1. Handle Missing Values
    df = df.dropna()  # Option to drop rows with missing values
    # Alternatively, fill missing values with column mean
    # df = df.fillna(df.mean())

    # 2. Remove Duplicates
    df = df.drop_duplicates()

    # 3. Convert Data Types
    # Example: Convert 'date' column to datetime
    # df['date'] = pd.to_datetime(df['date'])

    # 4. Encode Categorical Variables
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    # 5. Feature Scaling
    scaler = StandardScaler()
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    return df, label_encoders, scaler
