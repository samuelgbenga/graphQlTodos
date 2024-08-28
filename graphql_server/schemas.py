
from typing import Optional
import strawberry


@strawberry.type
class Task:
	id: int
	content: str
	is_done: bool = False


@strawberry.input
class PaginationInput:
	offset: int
	limit: int

@strawberry.input
class UpdateTaskInput:
	content: Optional[str] = None
	is_done: Optional[bool] = None
	