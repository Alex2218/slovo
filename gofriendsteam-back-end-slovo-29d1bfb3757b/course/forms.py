from django import forms
from .models import Package
from .widgets import DataAttributesSelect


class CourseChangeListForm(forms.ModelForm):
    packages = forms.ModelMultipleChoiceField(queryset=Package.objects.all(),
                                              required=True)

    def __init__(self, *args, **kwargs):
        print('__init____init____init____init__')
        super(CourseChangeListForm, self).__init__(*args, **kwargs)
        print(args, kwargs)
        instance = kwargs.pop('instance')
        print(instance.packages.all())
        for f in self.fields['packages'].choices:
            print(f)
        print()

        # self.fields['packages'].widget = forms.ModelMultipleChoiceField(queryset=None , use_required_attribute=False)
        data = {
            'packages': dict(Package.objects.values_list('id', 'title'))
        }
        # data['packages'][''] = ''

        # self.fields['packages'].widget = DataAttributesSelect(
        #     choices=self.fields['packages'].choices, data=data
        # )

        # super(CourseChangeListForm)


from django.forms.models import BaseInlineFormSet


class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        print('_construct_form ' , i)
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form
