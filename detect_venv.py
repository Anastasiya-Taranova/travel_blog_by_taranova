import os
import sys


def get_dynaconf_env():
    env_var = "ENV_FOR_DYNACONF"

    try:
        from dynaconf import settings
        env = settings.get(env_var)
    except ImportError:
        env = os.getenv(env_var)

    return env or "development"


def get_base_prefix_compat():
    """
    Get base/real prefix, or sys.prefix if there is none.
    """

    prefix = (
            getattr(sys, "base_prefix", None)
            or getattr(sys, "real_prefix", None)
            or sys.prefix
    )

    return prefix


def in_virtualenv():
    dynaconf_env = get_dynaconf_env()
    if dynaconf_env == "heroku":
        return True
    return get_base_prefix_compat() != sys.prefix


print(in_virtualenv())
