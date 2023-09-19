import logging
from logging_setup import initialize_logging

logger = logging.getLogger(__name__)

def _get_password()-> str:
    """Get user secret password

    Returns:
        Password dtype to received.
    """
    user_name = input("what is your name? ")
    user_age = input("what is your age? ")
    _create_password = input("Create your password ")
    _password_length = len(_create_password)
    secret_password = "*" *_password_length
    logger.debug(f"Your password {user_name} is a long character {secret_password} but unique, Impressive!")
    logger.info("This is cool to understand")
