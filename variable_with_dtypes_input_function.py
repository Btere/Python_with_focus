def _get_password()-> str:
    """Get user secret password

    Returns:
        Password dtype to received.
    """
    user_name = input("what is your name? ")
    user_age = input("what is your age? ")
    _create_password = input("Create your password")
    _password_length = len(_create_password)
    secret_password = "*" *_password_length
    print(f" Your password {user_name} is long character but unique, Impressive!")
_get_password()

