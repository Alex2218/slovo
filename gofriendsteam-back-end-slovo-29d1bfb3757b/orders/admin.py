from django.contrib import admin
from .models import Order
from course.models import Course
from django import forms
from student.utils_admin_side import StudentFilterHomeTask
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        order = getattr(self, 'instance', None)
        if order.status:
            print('TRUE!!!!!!')
            self.fields['status'].widget.attrs['disabled'] = True
            print(self.fields['status'].widget.attrs)
        print('init form', order)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'package', 'status', 'get_course', 'student']
    # list_editable = ['status']
    form = OrderForm
    list_filter = [StudentFilterHomeTask]

    def get_course(self, obj):
        try:
            return Course.objects.filter(packages__in=[obj.package]).first()
        except Exception as e:
            print(type(e), e)
            print('error in admin.py OrderAdmin')

    get_course.short_description = 'Курс'

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['student'].queryset = User.objects.filter(is_active=True, role='student')
        # form = super(OrderAdmin, self).get_form(*args, **kwargs)
        # form.fields['student'].queryset = User.objects.filter(is_active=True, role='student')
        # print('get_form ', form)
        return super(OrderAdmin, self).render_change_form(request, context, *args, **kwargs)
