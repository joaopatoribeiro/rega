import os


Class Config(object):
    SECRET_KEY = os.enfiron.get('SECRET_KEY') or 'nao-vais-saber-123'
