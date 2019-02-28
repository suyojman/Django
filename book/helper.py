from .models import Book


def bookAvailable(title):
		booklist = [book.title for book in Book.objects.all()]
		if title in booklist:
			return True
		else:
			return False