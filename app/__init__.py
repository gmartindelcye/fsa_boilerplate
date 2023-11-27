import os
from app.core.config import Settings
from dotenv import dotenv_values

environment = os.environ.get('APP_ENV', 'local')

if environment == 'local':
    config = dotenv_values('.env-local')
elif environment == 'dev':
    config = dotenv_values('.env-dev')
elif environment == 'prod':
    config = dotenv_values('.env')
else:
    raise ValueError('Environment not found')

# load_dotenv(getenv("ENV_FILE"))
settings = Settings(**config)

