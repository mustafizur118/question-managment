from decouple import config


SERVICE_NAME = 'question-management'
DEBUG = config('DEBUG', default=True, cast=bool)
SYSTEM_USER = ''

POSTGRES_HOST = config('POSTGRES_HOST', default='localhost')
POSTGRES_PORT = config('POSTGRES_PORT', default=5432, cast=int)
POSTGRES_USER = config('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD', default='1234')
POSTGRES_DB_NAME = config('POSTGRES_DB_NAME', default='question-management')

SECRET_KEY = config('SECRET_KEY', default='03t$j&_+4fb^s2d9g55+=eird(mpe3z=g5ud^+z97ia(8933g6')





