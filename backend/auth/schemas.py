from pydantic import BaseModel, EmailStr


class UserCreateBase(BaseModel):
    email: EmailStr
    password: str
    name: str
    second_name: str
    last_name: str


class UserBase(BaseModel):
    id: int
    email: EmailStr
    name: str
    second_name: str
    last_name: str

    class Config:
        from_attributes = True


class TokenInfo(BaseModel):
    access_token: bytes
    refresh_token: bytes
    type: str = 'Bearer'
