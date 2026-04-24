from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


# ── Request Schemas ──────────────────────────────────────────────────────────

class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UpdateTargetsRequest(BaseModel):
    daily_calorie_target: int | None = Field(None, ge=500, le=10000)
    daily_protein_target: int | None = Field(None, ge=10, le=500)
    daily_carbs_target: int | None = Field(None, ge=10, le=1000)
    daily_fat_target: int | None = Field(None, ge=10, le=500)


# ── Response Schemas ─────────────────────────────────────────────────────────

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    daily_calorie_target: int
    daily_protein_target: int
    daily_carbs_target: int
    daily_fat_target: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AuthResponse(BaseModel):
    user: UserResponse
    token: TokenResponse


class MessageResponse(BaseModel):
    message: str
