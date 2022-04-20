from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("full_name", "email", "phone_number",
                  "address_line_1", "address_line_2", "town_city",
                  "county_state", "zip_code", "country")

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "address_line_1": "Address Line 1",
            "address_line_2": "Address Line 2",
            "town_city": "Town/City",
            "county_state": "County/State",
            "zip_code": "Zip Code",
            }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False


class CheckOrderForm(forms.Form):
    order_number = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields["order_number"].widget.attrs["autofocus"] = True
        self.fields["order_number"].widget.attrs[
                "placeholder"] = "Order Number *"
        self.fields["order_number"].widget.attrs["class"] = "border-black \
                                                        rounded-0"
        self.fields["order_number"].label = False
