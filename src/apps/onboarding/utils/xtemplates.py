from typing import Dict
from typing import Optional

import jinja2
from delorean import Delorean
from django.conf import settings
from django.http import HttpRequest
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

from apps.onboarding.utils import consts
from apps.onboarding.utils.xdatetime import get_user_hour


def user_hour(request: HttpRequest) -> Dict[str, int]:
    hour = get_user_hour(request)
    ctx = {
        "user_hour": hour,
        "daylight_hours": consts.DAYLIGHT,
    }

    return ctx


def big_brother(_request: Optional[HttpRequest] = None) -> Dict[str, str]:
    if settings.DEBUG:  # pragma: nocover
        return {}

    return {
        "google_analytics": consts.SCRIPT_GOOGLE_ANALYTICS,
        "google_tag_manager": consts.SCRIPT_GOOGLE_TAG_MANAGER,
        "yandex_metrika": consts.SCRIPT_YANDEX_METRIKA,
    }


def build_jinja2_environment(**options) -> Environment:
    undefined_cls = (jinja2.ChainableUndefined, jinja2.DebugUndefined)[settings.DEBUG]

    opts = options.copy()
    opts.update(
        {"auto_reload": True, "undefined": undefined_cls,}
    )

    env = Environment(**opts)

    global_names = {
        "debug": settings.DEBUG,
        "Delorean": Delorean,
        "project_name": consts.PROJECT_NAME.lower(),
        "repr": repr,
        "static": static,
        "url": reverse,
        "user_hour": user_hour,
    }

    global_names.update(big_brother())

    env.globals.update(**global_names)

    return env
