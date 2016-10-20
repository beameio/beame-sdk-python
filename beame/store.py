import os

credentials = {}
    
def get(fqdn):
    return credentials[fqdn]

def add(creds):
    credentials[creds.fqdn] = creds
