from django import forms

PRODUCT_OTHER_CHOICE = 'other'
PRODUCT_CATEGORY_CHOICES = (
    (PRODUCT_OTHER_CHOICE, 'Другое'),
    ('food', 'Еда'),
    ('drink', 'Вода'),
    ('cloth', 'Одежда'),
    ('electronics', 'Электроника')
)




class ProductForm(forms.Form):
    name = forms.CharField(label='name', required=True)
    description = forms.CharField(max_length=100, label='description', required=True)
    category = forms.ChoiceField(label='category', required=True, choices=PRODUCT_CATEGORY_CHOICES)
    amount = forms.IntegerField(label='amount', required=True)
    price = forms.DecimalField(label='price',required=True)

