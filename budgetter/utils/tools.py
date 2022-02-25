

def convert_amount_to_str(amount):
    """
    Convert amount to local separator

    :param amount: amount to convert
    :return: string value
    """

    result = f"{amount:,.2f}"
    result = result.replace(",", "X")
    result = result.replace(".", ",")
    result = result.replace("X", " ")

    return result
