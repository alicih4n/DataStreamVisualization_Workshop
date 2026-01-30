
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, df, feature_col, target_col, test_size=0.2, random_state=42):
        """
        Selects features/target, splits data, and scales features.
        """
        if feature_col not in df.columns:
            raise ValueError(f"Feature {feature_col} not found in dataframe")
        
        X = df[[feature_col]].values
        y = df[target_col].values

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test, self.scaler

if __name__ == "__main__":
    # Test
    df = pd.DataFrame({'income': [1, 2, 3, 4, 5], 'price': [10, 20, 30, 40, 50]})
    p = Preprocessor()
    Xt, Xte, yt, yte, s = p.preprocess(df, 'income', 'price')
    print("Preprocessing test passed")
