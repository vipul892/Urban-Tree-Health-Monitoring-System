from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score
import numpy as np

def regression_model_performance(actual_value,predicted_value):
    mse = mean_squared_error(actual_value, predicted_value)
    mae = mean_absolute_error(actual_value, predicted_value)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual_value, predicted_value)

    print(f"Model Performance")
    print("-" * 30)
    print(f"MSE  : {mse}")
    print(f"MAE  : {mae}")
    print(f"RMSE : {rmse}")
    print(f"R² Score : {r2}")

    return {
        "MSE": mse,
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2
    }