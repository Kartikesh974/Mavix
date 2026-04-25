from pydantic import BaseModel, EmailStr, Field

class EnquiryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=1, max_length=5000)

class EnquiryResponse(BaseModel):
    id: int
    name: str
    email: str
    message: str
    created_at: str

    class Config:
        from_attributes = True