import configparser

config = configparser.ConfigParser()
config.read('config.ini')


DATA_SOURCE = 'data/bank.csv'
ARTIFACTS_PATH = 'model'
NOMINAL_FEATURES = [
    'job', 'marital', 'default', 'housing', 'loan', 'contact', 'poutcome', 'deposit'
]
ORDINAL_FEATURES = ['education',]
NUMERICAL_FEATURES = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
TARGET_FEATURE = 'target'
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
API_KEY_HOPSWORKS = config['hopsworks']['API_KEY']
FEATURE_GROUP_NAME = config['hopsworks']['FEATURE_GROUP_NAME']
FEATURE_DESCRIPTIONS = [
    {"name": "age", "description": "Customer's age"},
    {"name": "job", "description": "Customer's occupation or job type"},
    {"name": "marital",
        "description": "Customer's marital status (e.g., married, single, divorced)"},
    {"name": "education", "description": "Customer's level of education"},
    {"name": "default",
        "description": "Whether the customer has credit in default (yes/no)"},
    {"name": "balance", "description": "Current account balance"},
    {"name": "yearly_income", "description": "Annual income of the customer"},
    {"name": "num_children", "description": "Number of children the customer has"},
    {"name": "housing",
        "description": "Whether the customer has housing loan (yes/no)"},
    {"name": "loan",
        "description": "Whether the customer has a personal loan (yes/no)"},
    {"name": "contact",
        "description": "Type of communication contact with the customer (e.g., cellular, telephone)"},
    {"name": "day", "description": "Day of the month when the contact was made"},
    {"name": "month", "description": "Month of the year when the contact was made"},
    {"name": "duration", "description": "Duration of the last contact in seconds"},
    {"name": "campaign", "description": "Number of contacts performed during this campaign for this client"},
    {"name": "pdays", "description": "Number of days since the customer was last contacted"},
    {"name": "previous", "description": "Number of contacts performed before this campaign"},
    {"name": "poutcome", "description": "Outcome of the previous marketing campaign"},
    {"name": "deposit",
        "description": "Whether the customer subscribed to a term deposit (yes/no)"},
]
