# import time

import requests
from fastapi import FastAPI
from starlette.responses import StreamingResponse

app = FastAPI()


# 模拟处理流式数据
def process_data(data: str) -> str:
    return data


def third_party_sse():
    with requests.get('http://third-party-service/stream', stream=True) as r:
        for line in r.iter_lines():
            if line:
                line = line.decode('utf-8')
                data = process_data(line)
                yield data


@app.get("/stream")
async def stream():
    # def event_stream():
    #     while True:
    #         yield f"data: {time.time()}\n\n"
    #         time.sleep(1)

    # return StreamingResponse(event_stream(), media_type="text/event-stream")
    return StreamingResponse(third_party_sse(), media_type="text/event-stream")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
