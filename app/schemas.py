from pydantic import BaseModel


# Creating a schema for the post which is going to be passed into the API
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostCreate):
    pass