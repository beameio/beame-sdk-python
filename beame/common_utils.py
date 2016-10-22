import json

def parse(something):
    try:
        return json.loads(something)
    except Exception:
        return something
