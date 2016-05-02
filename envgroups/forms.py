from django import forms

class CheckboxSelectMultiple(forms.SelectMultiple):
    """
    A SelectMultiple wich will use checkboxes to select individual items

    """
    class Media:
        css = {
            'all': ('checkboxselectmultiple/checkboxselectmultiple.css',)
        }
        js = (
            'checkboxselectmultiple/checkboxselectmultiple.js',
        )

    def render(self, name, value, attrs, choices=()):
        if attrs is None:
            attrs = {}
        attrs['data-checkboxselect'] = True
        return super(CheckboxSelectMultiple, self).render(name, value, attrs, choices)

class CatForm(forms.Form):
        OPTIONS = (
                ("AUT", "Austria"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
        Categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)

class SkiForm(forms.Form):
        OPTIONS = (
                ("AUT", "Austria"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
        Skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)

class ResForm(forms.Form):
        OPTIONS = (
                ("AUT", "Austria"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                )
        Resources = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)
