# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hwekw@cz(2fq+fhb99$^*ecexb30*mqh1+v2yqh$w=9qw@oox@'

DATABASES = {

    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone',
        'USER': 'root',
        'PASSWORD': 'Taco1234',
        'PORT': '3306',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'autocommit' : True
        }
    }
}