from pydantic import BaseModel

class Message(BaseModel):
    message: str

    def __str__(self):
        return self.message