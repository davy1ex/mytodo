from django import forms


class AddTaskForm(forms.Form):
    input_field = forms.CharField(label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "input task and press enter to save in inbox"
            }
        )
    )