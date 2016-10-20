import json

def parse(something):
    try:
        return json.loads(something)
    except Error:
        print("X")
