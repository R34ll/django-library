from typing import Optional

from ninja import NinjaAPI, Schema, ModelSchema
from django.shortcuts import get_object_or_404
from books.models import Book, Author

api = NinjaAPI()

class AuthorSchema(ModelSchema):
	class Meta:
		model = Author
		fields = "__all__"



class BookSchema(ModelSchema):
	author: AuthorSchema
	class Meta:
		model = Book
		fields = "__all__"

class BookInSchema(Schema):
	title:str
	description:str
	author_id:int
	isbn: str



class BookPatchSchema(Schema):
	title: Optional[str] = None
	description: Optional[str] = None
	author_id: Optional[int] = None
	isbn: Optional[str] = None



@api.get("/books/{book_id}",response=BookSchema)
def book_detail(request, book_id: int):
	book = get_object_or_404(Book, id=book_id)
	return book


@api.get("/books", response=list[BookSchema])
def book_list(request):
	"This method list all the books"
	return Book.objects.all()



@api.post("/books", response=BookSchema)
def create_book(request, payload:BookInSchema):
	book = Book.objects.create(**payload.dict())
	return book


@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
	book = get_object_or_404(Book, id=book_id)
	book.delete()
	return {"success":True}


@api.patch("/books/{book_id}", response=BookSchema)
def edit_book(request, book_id: int, payload: BookPatchSchema):
	book = get_object_or_404(Book, id=book_id)
	for attr, value in payload.dict(exclude_unset=True).items():
		setattr(book, attr, value)

	book.save()
	return book











