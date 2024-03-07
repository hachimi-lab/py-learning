from typing import TypeVar, Generic, Optional

import requests
from pydantic import BaseModel, ValidationError

DataT = TypeVar('DataT', bound=BaseModel)


class ResponseBody(Generic[DataT], BaseModel):
    code: int
    msg: str
    data: Optional[DataT]


class LoginReqBody(BaseModel):
    username: str
    password: str


class LoginRespBody(ResponseBody[str]):
    pass


req_body = LoginReqBody(username='my_username', password='my_password')
headers = {'Content-Type': 'application/json'}

try:
    resp = requests.post('https://example.com/login', data=req_body.json(), headers=headers)
    resp.raise_for_status()  # 如果状态码不是200，抛出异常
    resp_body = LoginRespBody.parse_raw(resp.text)
    print(resp_body.data)
except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except ValidationError as val_err:
    print(f'Validation error occurred: {val_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
