class ContactBase(BaseModel):
    name: str
    address: str
    email: str
    phone_number: str


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    owner_id: int

    # This Config class is used to provide configurations to Pydantic.
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    contacts: list[Contact] = []

    # This Config class is used to provide configurations to Pydantic.
    class Config:
        orm_mode = True
