# POTENTIALLY SUPPORT MULTIPLE ENVIRONMENTS
from __future__ import absolute_import, division, print_function, unicode_literals
LOCAL = False

envs = {'dev', 'staging'}

env = 'dev'

if LOCAL:
    ENDPOINTS = {
        'asset_managers': 'http://localhost:8000',
        'assets': 'http://localhost:8000',
        'books': 'http://localhost:8000',
        'corporate_actions': 'http://localhost:8000',
        'market_data': 'http://localhost:8000',
        'monitor': 'http://localhost:8000',
        'parties': 'http://localhost:8000',
        'transactions': 'http://localhost:8000'
    }
else:
    ENDPOINTS = {
        'asset_managers': 'https://c1hes1s60m.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'assets': 'https://zc6udsq1nb.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'books': 'https://smc367plfg.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'corporate_actions': 'https://basklngdyh.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'market_data': 'https://f0rpi7vksi.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'monitor': 'https://wt50nd7j7l.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'parties': 'https://hpihgzmxoc.execute-api.ap-southeast-1.amazonaws.com/' + env,
        'transactions': 'https://1w0gb581sl.execute-api.ap-southeast-1.amazonaws.com/' + env
    }

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%z %Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

COGNITO_CLIENT_ID = '55n70ns9u5stie272e1tl7v32v'  # This is not secret - it is just an identifier

# Do not change this
COGNITO_REGION = 'us-west-2'
COGNITO_POOL = 'us-west-2_wKa82vECF'
