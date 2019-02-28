from django import forms
from .models import Book
from .helper import bookAvailable


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "price")

        # def clean_price(self):
        # 	price = self.cleaned_data.get('price')
        # 	print(price)
        # 	if len(str(price))>10:
        # 		raise forms.ValidationError("Invalid Number!! Please enter valid amount")
        # 	else:
        # 		return price

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        title = cleaned_data.get("title")
        if bookAvailable(title):
            print("HEREEE")
            msg = "You already have the same name of Book !! "
            self.add_error("title", msg)

        if len(str(price)) > 10:
            msg = "Invalid Number!! Please enter valid amount"
            self.add_error("price", msg)
