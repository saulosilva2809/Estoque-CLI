from dataclasses import dataclass


@dataclass
class CreateCategoryDTO:
    name: str
    description: str | None = None

@dataclass
class UpdateCategoryDTO:
    name: str | None = None
    description: str | None = None
