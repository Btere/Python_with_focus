import logging
from typing import Union

def initialize_logging(level: Union[int, str] = logging.DEBUG) -> None:
    """Initilazing logger

    Args:
        filename: "save_log_info".
        level: Defaults to log.DEBUG.
    """
    if type(level) == str:
        level = logging.getLevelName(level.upper())


    # shorter log level name for better alignment
    logging.addLevelName(logging.CRITICAL, "CRT")
    logging.addLevelName(logging.ERROR, "ERR")
    logging.addLevelName(logging.WARNING, "WRN")
    logging.addLevelName(logging.INFO, "INF")
    logging.addLevelName(logging.DEBUG, "DBG")

    # create logger
    logging.basicConfig(level=level, format="[%(asctime)s] [%(levelname)-3s] [%(filename)s:%(lineno)s] %(message)s")


