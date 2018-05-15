import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
#if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
DEBUG = False
# else:
# DEBUG = True


# don't share this with anybody.
SECRET_KEY = '+2ie+=9*vj3zo@c)n5w75ap3ouyw#rcw@r-dt3uf&rvr&j4hbg'

SENTRY_DSN = 'http://bb8e7c0737264a5dbb46a83d5ae4edff:0dcd498260c443bcaf70df542f969ae2@sentry.otree.org/285'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY, USD
REAL_WORLD_CURRENCY_CODE = 'RUB'
USE_POINTS = True



# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'ru'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_HTML = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}


## THIS IS NEEDED FOR TZHUR EXPERIMENT

# CHANNEL_ROUTING = 'bribery_effort_base.routing.channel_routing'
# CHANNEL_ROUTING = 'bribery_effort_withinfo.routing.channel_routing'
# CHANNEL_ROUTING = 'bribery_effort_thirdparty.routing.channel_routing'
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#CHANNEL_ROUTING = 'bribery_effort_base.routing.channel_routing'
#CHANNEL_ROUTING = 'bribery_effort_base_IT.routing.channel_routing'
# CHANNEL_ROUTING = 'bribery_effort_base_RU.routing.channel_routing'
CHANNEL_ROUTING = 'bribery_effort_info_RU.routing.channel_routing'
#CHANNEL_ROUTING = 'bribery_effort_info_IT.routing.channel_routing'
#CHANNEL_ROUTING = 'bribery_effort_withinfo.routing.channel_routing'
#CHANNEL_ROUTING = 'bribery_effort_thirdparty.routing.channel_routing'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

ROOM_DEFAULTS = {}

ROOMS = [
    {
        'name': 'lab2',
        'display_name': 'p2',
        'participant_label_file': 'PlayerList2.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab3',
        'display_name': 'p3',
        'participant_label_file': 'PlayerList3.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab4',
        'display_name': 'p4',
        'participant_label_file': 'PlayerList4.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab5',
        'display_name': 'p5',
        'participant_label_file': 'PlayerList5.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab6',
        'display_name': 'p6',
        'participant_label_file': 'PlayerList6.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab8',
        'display_name': 'p8',
        'participant_label_file': 'PlayerList8.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab9',
        'display_name': 'p9',
        'participant_label_file': 'PlayerList9.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab10',
        'display_name': 'p10',
        'participant_label_file': 'PlayerList10.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab12',
        'display_name': 'p12',
        'participant_label_file': 'PlayerList12.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab15',
        'display_name': 'p15',
        'participant_label_file': 'PlayerList15.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab16',
        'display_name': 'p16',
        'participant_label_file': 'PlayerList16.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab18',
        'display_name': 'p18',
        'participant_label_file': 'PlayerList18.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab20',
        'display_name': 'p20',
        'participant_label_file': 'PlayerList20.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab24',
        'display_name': 'p24',
        'participant_label_file': 'PlayerList24.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab25',
        'display_name': 'p25',
        'participant_label_file': 'PlayerList25.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab28',
        'display_name': 'p28',
        'participant_label_file': 'PlayerList28.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab30',
        'display_name': 'p30',
        'participant_label_file': 'PlayerList30.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab32',
        'display_name': 'p32',
        'participant_label_file': 'PlayerList32.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab35',
        'display_name': 'p35',
        'participant_label_file': 'PlayerList35.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab36',
        'display_name': 'p36',
        'participant_label_file': 'PlayerList36.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab40',
        'display_name': 'p40',
        'participant_label_file': 'PlayerList40.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab42',
        'display_name': 'p42',
        'participant_label_file': 'PlayerList42.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab45',
        'display_name': 'p48',
        'participant_label_file': 'PlayerList45.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab48',
        'display_name': 'p48',
        'participant_label_file': 'PlayerList48.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab50',
        'display_name': 'p50',
        'participant_label_file': 'PlayerList50.txt',
        'use_secure_urls': False,
    },
    {
        'name': 'lab52',
        'display_name': 'p52',
        'participant_label_file': 'PlayerList52.txt',
        'use_secure_urls': False,
    },
]

ALLOWED_HOSTS=['*']

# CHANNEL_ROUTING = 'bribery_effort_base.routing.channel_routing'
# CHANNEL_ROUTING = 'bribery_effort_thirdparty.routing.channel_routing'


SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 50.00,
    'participation_fee': 150.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'bribery_effort_base_RU',
        'display_name': "bribery_effort_base_RU",
        'num_demo_participants': 3,
        'app_sequence': ['bribery_effort_base_RU', 'payment_info', 'my_survey'],
    },
    {
        'name': 'bribery_effort_info_RU',
        'display_name': "bribery_effort_info_RU",
        'num_demo_participants': 3,
        'app_sequence': ['bribery_effort_info_RU', 'payment_info', 'my_survey'],
    },
    {
        'name': 'public_goods',
        'display_name': "Public Goods",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods', 'payment_info'],
    },
    {
        'name': 'guess_two_thirds',
        'display_name': "Guess 2/3 of the Average",
        'num_demo_participants': 3,
        'app_sequence': ['guess_two_thirds', 'payment_info'],
    },
    {
        'name': 'my_survey',
        'display_name': "Survey large",
        'num_demo_participants': 1,
        'app_sequence': ['my_survey', 'payment_info'],
    },
    {
        'name': 'quiz',
        'display_name': "Quiz",
        'num_demo_participants': 1,
        'app_sequence': ['quiz'],
    },
    {
        'name': 'BRET',
        'display_name': "BRET",
        'num_demo_participants': 1,
        'app_sequence': ['bret'],
    },
    {
        'name': 'PG_standard',
        'display_name': "Базовая игра КУСБ",
        'num_demo_participants': 5,
        'app_sequence': ['PG_standard', 'PG_threshold', 'my_survey'],         #'use_browser_bots': False
    },
    {
        'name': 'PG_threshold',
        'display_name': "Threshold game - admin",
        'num_demo_participants': 5,
        'app_sequence': ['PG_threshold'],         #'use_browser_bots': False
    },
    {
        'name': 'Russian_games',
        'display_name': "Dict-Ultim-Trust Games in Russian",
        'num_demo_participants': 4,
        'app_sequence': ['dictator_rus', 'ultimatum_simple_rus', 'trust_rus'],
    },
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
    # {
    #     'name': 'ultimatum_strategy',
    #     'display_name': "Ultimatum (strategy method treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': True,
    # },
    {
        'name': 'simple_games_rus',
        'display_name': "Simple Games Russia",
        'num_demo_participants': 4,
        'app_sequence': ['dictator_rus', 'ultimatum_simple_rus', 'trust_rus']
    },
    {
        'name': 'roshambo_single',
        'display_name': "RSP",
        'num_demo_participants': 1,
        'app_sequence': ['roshambo_single', 'survey_rps']
    },
    {
        'name': 'dictator_rus_no_reg',
        'display_name': "Dictator Game no Regions",
        'num_demo_participants': 2,
        'app_sequence': ['dictator_rus_no_reg', 'my_survey']
    },
    {
        'name': 'ultimatum_simple_rus_no_reg',
        'display_name': "Ultimatum Game no Regions",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_simple_rus_no_reg', 'my_survey']
    },
    {
        'name': 'trust_rus_no_reg',
        'display_name': "Trust Game no Regions",
        'num_demo_participants': 2,
        'app_sequence': ['trust_rus_no_reg','my_survey']
    }
]
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'stackelberg',
###     'display_name': "Stackelberg Competition",
###     'real_world_currency_per_point': 0.01,
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'stackelberg', 'payment_info'
###     ],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
    # {
    #     'name': 'real_effort',
    #     'display_name': "Real-effort transcription task",
    #     'num_demo_participants': 1,
    #     'app_sequence': [
    #         'real_effort',
    #     ],
    # },
    # ]
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },

otree.settings.augment_settings(globals())
