from typing import Any

import logging

from collections.abc import Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.types import TelegramObject, Update


class UpdatesDumperMiddleware(BaseMiddleware):
    async def __call__(
        self, handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]], event: Update, data: dict[str, Any]
    ) -> Any:
        json_event = event.model_dump_json(exclude_unset=True)

        logging.debug(json_event)
        res = await handler(event, data)
        if res is UNHANDLED:
            logging.warning("UNHANDLED")
        return res
