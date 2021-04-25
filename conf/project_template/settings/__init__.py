from split_settings.tools import optional, include

include(
    'project.py',  # root project settings (not recommended to make any changes here.)
    
    # include project level settings..
    'default.py', # contains actual/final config/switches.
    'production/*.py', # contains production-stage configurations.
    'development/*.py',  # contains testing-stage configurations.

    # include app level settings.
    optional('../apps/*/settings/default.py'),
    optional('../apps/*/settings/production.py'),
    optional('../apps/*/settings/development.py'),
    optional('../apps/*/settings/others/*.py'),
    
    optional('third_party.py'),
    
    optional('override.py'), # contains configurations to override switches.
)
