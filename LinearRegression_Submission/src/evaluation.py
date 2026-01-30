
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

class Evaluator:
    @staticmethod
    def calculate_metrics(y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        return {"RMSE": rmse, "MAE": mae, "R2": r2}

    @staticmethod
    def plot_regression(X_test, y_test, y_pred, title="Regression Results"):
        plt.figure(figsize=(10, 6))
        plt.scatter(X_test, y_test, color='gray', alpha=0.5, label='Actual')
        plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
        plt.title(title)
        plt.xlabel('Feature (Scaled)')
        plt.ylabel('Target')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    e = Evaluator()
    metrics = e.calculate_metrics([1, 2, 3], [1.1, 1.9, 3.2])
    print(metrics)
