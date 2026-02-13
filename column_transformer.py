import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from category_encoders import TargetEncoder, BinaryEncoder

data = pd.read_csv("cardekho_dataset.csv")



X = data.drop(['selling_price'], axis=1)  # Drop as a list
y = data[['selling_price']]  # Select target as a DataFrame

# Define numeric and categorical columns
num_features = X.select_dtypes(exclude="object").columns
onehot_columns = ['seller_type', 'fuel_type', 'transmission_type']
binary_columns = ['brand', 'model']

# Define transformers
numeric_transformer = StandardScaler()
oh_transformer = OneHotEncoder()
binary_transformer = BinaryEncoder()

# Simplify categorical columns
def simplify_categories(df, col, threshold=10):
    value_counts = df[col].value_counts()
    rare_categories = value_counts[value_counts < threshold].index
    df[col] = df[col].apply(lambda x: x if x not in rare_categories else "Other")
    return df

# Apply category simplification
for col in ['brand', 'model']:
    X = simplify_categories(X, col)

# Define the preprocessor pipeline
numeric_transformer = StandardScaler()
target_transformer = TargetEncoder(cols=onehot_columns + binary_columns)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_features),
        ("target", target_transformer, onehot_columns + binary_columns)
    ]
)

# Transform data
X_transformed = preprocessor.fit_transform(X, y)

# Ensure the shape matches the original 11 features
print("Shape of transformed data:", X_transformed.shape)
