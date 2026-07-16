from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_serializer
from datetime import datetime
from pydantic import StringConstraints
from typing import Annotated

QuestionForm = Annotated[
    str,
    StringConstraints(max_length=5000)
]

class Metrics(BaseModel):
    left_score: int = Field(
        ge=0,
        le=100,
        description="Score of the left philosophical position."
    )

    right_score: int = Field(
        ge=0,
        le=100,
        description="Score of the right philosophical position."
    )

    label: str = Field(
        description="Overall classification label."
    )

    evidence: str = Field(
        description="Direct quotes or strong reasoning from the essay."
    )
    
class Compass(BaseModel):
    individualism_collectivism: Metrics
    rationalism_irrationalism: Metrics
    universalism_relativism: Metrics
    determinism_free_will: Metrics
    overall_summary: str = Field(description="Provide an overall analysis, key themes, closest philosophical traditions and an AI disclaimer")

class CompassResponse(BaseModel):
    philosophical_compass: Compass

