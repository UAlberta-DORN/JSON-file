import os
import json
import requests


def test_api():
    data = json.dumps({'value': 10})
    r1 = requests.get("http://localhost:105/dorn/all")
    print(r1.json())
    r2 = requests.put("http://localhost:105/dorn/0", json=data)
    print(r2.json())
    r3 = requests.get("http://localhost:105/dorn/0")
    print(r3.json())


if __name__ == '__main__':
    os.system("start /b python flask_Test.py")
    test_api()