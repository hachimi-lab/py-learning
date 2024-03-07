import requests


def event_stream():
    with requests.get('http://localhost:5000/stream', stream=True) as r:
        for line in r.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                print(decoded_line)


event_stream()
