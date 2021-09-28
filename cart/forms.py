from django import forms

# i+1 is to provide cart button 1 in display but 0 as value.
PRODUCT_QUANTITY_CHOICES = [(i, str(i + 1)) for i in range(0, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        coerce=int, choices=PRODUCT_QUANTITY_CHOICES)
    override = forms.BooleanField(
        required=False, widget=forms.HiddenInput, initial=False)
