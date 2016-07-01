DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'appsco',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

DDF_FIELD_FIXTURES = {
    'django.contrib.postgres.fields.jsonb.JSONField': {
        'ddf_fixture': lambda: {}
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

SECRET_KEY = 'test'

COMPRESS_ENABLED = False

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
)

PEP8_RCFILE = 'pep8.rc'


class DisableMigrations(object):
    """
    Disable migrations when running tests
    """
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()
