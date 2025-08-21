from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path
from functools import wraps
import inspect
import logging
import time
from datetime import datetime


logfile   = Path(__file__).parent / "inventory" / "logs" / f"{datetime.now().strftime("%Y-%m-%d")}.log"
formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

handler   = logging.FileHandler(logfile, encoding="utf-8")
handler.setFormatter(formatter)

logger    = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arguments = inspect.signature(func).bind_partial(*args, **kwargs)


        try:
            msg = f"Succesfully ran the function {func.__name__} with arguments {arguments.arguments.items()}"
            logger.info(msg)

            return func(*args, **kwargs)

        except Exception as exception:
            msg = f"Encountered {type(exception).__name__} while running the function {func.__name__} with arguments {arguments.arguments.items()} {exception}"
            console.print(msg, style="red")
            logger.error(msg)

    return wrapper

console = Console()
