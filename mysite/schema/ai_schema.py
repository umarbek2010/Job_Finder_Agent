from pydantic import BaseModel, Field


class TicketInputSchema(BaseModel):
    text: str = Field(min_length=1, max_length=2222)


class JobItem(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    company: str = Field(min_length=1, max_length=150)
    location: str = Field(min_length=1, max_length=100)
    salary: str | None = Field(default=None)
    description: str = Field(min_length=1, max_length=500)


class TicketOutputSchema(BaseModel):
    answer: str = Field(min_length=1, max_length=600)
    jobs: list[JobItem] = Field(default_factory=list)
    recommendations: str | None = Field(default=None)



class AnswerInputSchema(BaseModel):
    text: str = Field(min_length=1, max_length=2222)
    facts: str | None = Field(default=None, min_length=1, max_length=1111)


class AnswerOutputSchema(BaseModel):
    text_draft: str
    review: bool = True
    preferred_city: str | None = Field(default=None)



