import logging
from variable_with_dtypes_input_function import _get_password
from  logging_setup import initialize_logging

logger = logging.getLogger(__name__)

def _output_list_unaltered_01(first_element: list, second_element: str) -> list:
    """Sorting numbers.

    Args:
        first_element (list): List of numbers.
        second_element (str): Sorting order ("asc", "desc", "None").

    Returns:
        list: Sorted list of numbers.
    """
    if second_element == "asc":
        return sorted(first_element)
    elif second_element == "desc":
        return sorted(first_element, reverse=True)
    elif second_element == "None":
        return first_element
    else:
        raise ValueError("Invalid order parameter.")

def main() -> None:
    _get_password()
    first_item = [1, 2, 5, 6, 7, 8, 69]
    second_item = ["asc", "desc", "None"]

    for order in second_item:
        sorted_list = _output_list_unaltered_01(first_item, order)
        logger.debug(f"Input: {first_item}, Order: {order}, Sorted List: {sorted_list}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()


