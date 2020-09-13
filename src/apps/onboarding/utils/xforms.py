from typing import Iterable
from typing import Optional

from apps.onboarding.utils.xmodels import a
from django import forms
from django.db import models


def gen_textinput_admin_form(
    model_cls: type,
    model_fields: Iterable[models.Field],
    text_input_size: Optional[int] = 100,
) -> type:
    """
    Give me these:
    :param model_cls - a model you want to be displayed in Django Admin
    :param model_fields: model fields to be displayed as <input type="text">
    :param text_input_size: size attribute of <input type="text">
    And I will generate and
    :return a ModelForm class
    """

    size = text_input_size or 100
    fields = (a(_field) for _field in model_fields)
    widgets = {
        _field: forms.TextInput(attrs={"text_input_size": str(size)})
        for _field in fields
    }

    cls_meta_dict = {
        "model": model_cls,
        "fields": "__all__",
        "widgets": widgets,
    }
    cls_meta = type("Meta", (), cls_meta_dict)

    cls_form_dict = {"Meta": cls_meta}
    cls_form = type(
        f"{model_cls.__name__}AdminFormWithTextInputs",
        (forms.ModelForm,),
        cls_form_dict,
    )

    return cls_form
