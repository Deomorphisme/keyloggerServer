from typing import TypedDict

class Log(TypedDict):
    time_agent: str
    time_server: str
    method: str
    host: str
    ip: str
    layout: str
    input: str
