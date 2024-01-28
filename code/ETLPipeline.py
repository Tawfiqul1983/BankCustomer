
import sys
import os

current = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)



from zenml import pipeline
import pandas as pd
from steps import ingest, clean, encode, scale, load
import config
import logging


@pipeline(enable_cache=True, name='ETL Pipeline')
def feature_pipeline() -> None:
    """
    Pipeline to preprocess the data and make predictions.

    Args:
        None

    Returns:
        data: Preprocessed data.
    """
    try:
        logging.info('Running feature_pipeline')
        # ingest the data
        data = ingest.ingest_data(config.DATA_SOURCE)

        # clean the data
        data = clean.clean_data(data)

        # encode the data
        data = encode.encode_features(
            data, nominal_features=config.NOMINAL_FEATURES, ordinal_features=config.ORDINAL_FEATURES)
        # Scale data
        data = scale.scale_data(data)
        # load.load_features(data)
        logging.info('Feature_pipeline completed')
    except Exception as e:
        logging.error(f'Error in feature_pipeline: {e}')
        return None


if __name__ == "__main__":
    run = feature_pipeline()
