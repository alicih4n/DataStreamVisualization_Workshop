
import yaml
import sys
import os
import pandas as pd
from datetime import datetime
from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.model import LinearRegressionScratch, SklearnModel
from src.evaluation import Evaluator

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    config_path = "configs/experiment_config.yaml"
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    
    cfg = load_config(config_path)
    print(f"Running experiment with config: {config_path}")

    # 1. Load Data
    loader = DataLoader(cfg['paths']['data_dir'])
    df = loader.load_csv(cfg['experiment']['dataset_name'])
    print(f"Loaded data: {df.shape}")

    # 2. Preprocess
    preprocessor = Preprocessor()
    X_train, X_test, y_train, y_test, scaler = preprocessor.preprocess(
        df, 
        feature_col=cfg['experiment']['feature_col'], 
        target_col=cfg['experiment']['target_col'],
        test_size=cfg['experiment']['test_size'],
        random_state=cfg['experiment']['random_state']
    )
    print("Data preprocessed and scaled.")

    # 3. Model Training
    model_type = cfg['model']['type']
    if model_type == 'scratch':
        model = LinearRegressionScratch(
            learning_rate=cfg['model']['learning_rate'],
            n_iterations=cfg['model']['iterations']
        )
    else:
        model = SklearnModel()
    
    print(f"Training {model_type} model...")
    model.fit(X_train, y_train)

    # 4. Evaluation
    y_pred = model.predict(X_test)
    metrics = Evaluator.calculate_metrics(y_test, y_pred)
    print("Metrics:", metrics)

    # 5. Log Experiment
    results_path = cfg['paths']['results_file']
    os.makedirs(os.path.dirname(results_path), exist_ok=True)
    
    result_entry = {
        "timestamp": datetime.now().isoformat(),
        "model": model_type,
        "feature": cfg['experiment']['feature_col'],
        "rmse": metrics['RMSE'],
        "r2": metrics['R2'],
        "params": str(cfg['model'])
    }
    
    df_res = pd.DataFrame([result_entry])
    if not os.path.exists(results_path):
        df_res.to_csv(results_path, index=False)
    else:
        df_res.to_csv(results_path, mode='a', header=False, index=False)
    
    print(f"Experiment logged to {results_path}")

if __name__ == "__main__":
    main()
