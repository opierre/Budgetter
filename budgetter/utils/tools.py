from PySide6.QtWidgets import QWidget


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


def update_style(widget: QWidget, style_sheet: str):
    """
    Update style dynamically

    :param widget: widget
    :param style_sheet: style sheet to apply
    :return: None
    """

    widget.setStyleSheet(style_sheet)
    widget.style().unpolish(widget)
    widget.style().polish(widget)
