from pydantic import BaseModel, Field, ValidationError # Validates inputs


class Chat(BaseModel): # validating chats
    role: str
    content: str = Field(..., min_length=1) # must have some content


