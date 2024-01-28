import logging
from zenml import step
import pandas as pd
from typing import Union
from joblib import dump
import config
from os import path



@step(enable_cache=True)
def scale_data(data: Union[pd.DataFrame, pd.Series]) -> Union[pd.DataFrame, None]:
    """
    Scales the input data using the standard scaler.

    Args:
        data (Union[pd.DataFrame, pd.Series]): The data to scale.

    Returns:
        Union[pd.DataFrame, pd.Series]: The scaled data.
    """

    try:
        logging.info("Scaling the data...")
        if data.empty:
            logging.info("No data to scale.")
            return None
        # scale the data using the standard scaler from scikit-learn
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
        scaler.fit(data)
        data = pd.DataFrame(scaler.transform(data), columns=data.columns)
        logging.info("Saving scaler ....")
        dump(scaler, path.join(config.ARTIFACTS_PATH, 'scalers.joblib'))
        logging.info("Scaler saved successfully.")
        logging.info("Data scaled successfully.")
        return data
    except Exception as e:
        logging.error(f"Error scaling data: {e}")
        return pd.DataFrame()
