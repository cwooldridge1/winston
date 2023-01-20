from pydantic import BaseModel, Field
import time

class SocketResponse(BaseModel):
    type: str
    status: int
    data: dict
    time: float = Field(default_factory=lambda: time.time() *1000) #time in milliseconds
    route: str #the route to emit the response to 


class ContentResponse(SocketResponse):
    status: int = 200 
    route: str = 'content'
