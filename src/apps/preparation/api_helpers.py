import json
import logging
import traceback
from typing import Callable
from typing import Dict
from typing import Generator
from typing import Optional
from typing import Union

import requests


class TransformationError(RuntimeError):
    def __init__(self, position, item, reason):
        msg = f"cannot transform item `{item}` @ {position}: {reason}"
        super().__init__(msg)


def call_api(
    url: str,
    /,
    headers: Optional[Dict] = None,
    params: Optional[Dict] = None,
    transform: Optional[Callable] = None,
    key: Optional[Union[int, str, Callable]] = None,
    logger: Optional[logging.Logger] = None,
) -> Generator:
    def _warn(*_wargs, **_wkwargs):
        if not logger:
            return
        logger.warning(*_wargs, **_wkwargs)

    if not transform:
        transform = lambda _pos, _item: _item

    kwargs = {}
    if headers and isinstance(headers, dict):
        kwargs["headers"] = headers
    if params and isinstance(params, dict):
        kwargs["params"] = params

    response = requests.get(url, **kwargs)
    if response.status_code != 200:
        _warn(
            f"cannot transform data from response({response.status_code}): *************\n"
            f"{response.text}\n"
            "********************************************************"
        )
        yield from []
        return

    payload = response.json()

    if isinstance(payload, dict):
        if not key:
            payload = payload.items()
        else:
            if callable(key):
                payload = key(payload)
            else:
                if key not in payload:
                    pretty = json.dumps(payload, sort_keys=True, indent=2)
                    _warn(
                        "cannot transform data from response: ******************\n"
                        f"key `{key!r}` not in payload:\n"
                        f"{pretty}\n"
                        "********************************************************"
                    )
                    payload = []
                else:
                    payload = payload[key]

    try:
        yield from (transform(position, item) for position, item in enumerate(payload))
    except TransformationError:
        _warn(
            "cannot transform data from response: ******************\n"
            f"{traceback.format_exc()}\n"
            "********************************************************"
        )
        yield from []
