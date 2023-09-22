import os.path
from datetime import datetime
from typing import Tuple

import pytz
from ofxtools import OFXTree

from budgetter.utils.defines import TransactionType
from budgetter.view.widgets.transaction_widgets.means_widget import MeanType


def convert_ofx_to_json(ofx_file_path: str) -> Tuple[dict, dict]:
    """
    Convert OFX file to JSON to send to server

    :param ofx_file_path: OFX file path
    :return: converted data as JSON, header with global info
    """

    if not os.path.exists(ofx_file_path):
        return {}, {}

    ofx_parser = OFXTree()
    with open(ofx_file_path, "rb") as ofx_file:
        ofx_parser.parse(ofx_file)

    # Convert to OFX tree for parsing
    ofx = ofx_parser.convert()
    utc_timezone = pytz.UTC
    data = {"transactions": []}
    header = {
        "count": 0,
        "accounts": [],
        "start_date": utc_timezone.localize(datetime.max),
        "end_date": utc_timezone.localize(datetime.min),
    }
    for statement in ofx.statements:
        # Get account info
        account = {
            "account_id": statement.account.acctid,
            "amount": statement.balance.balamt,
            "last_update": statement.balance.dtasof.strftime("%Y-%m-%d"),
        }

        # Update header
        header.update({"count": header.get("count") + len(statement.transactions)})
        header.get("accounts").append(account)
        if statement.transactions.dtstart < header.get("start_date"):
            header.update({"start_date": statement.transactions.dtstart})
        if statement.transactions.dtend > header.get("end_date"):
            header.update({"end_date": statement.transactions.dtend})

        # Parse transactions
        for transaction in statement.transactions:
            # TODO: fix generic term for internal transaction
            if "VIREMENT EN VOTRE FAVEUR DE OLIVIER PIERRE" in transaction.memo:
                transaction_type = TransactionType.INTERNAL.value
                transaction_mean = MeanType.TRANSFER.value
            elif float(transaction.trnamt) < 0:
                transaction_type = TransactionType.EXPENSES.value
                transaction_mean = MeanType.CARD.value
            else:
                transaction_type = TransactionType.INCOME.value
                transaction_mean = MeanType.CARD.value
            data.get("transactions").append(
                {
                    "name": transaction.name,
                    "amount": abs(float(transaction.trnamt)),
                    "transaction_type": transaction_type,
                    "date": transaction.dtposted.strftime("%Y-%m-%d"),
                    "comment": transaction.memo,
                    "mean": transaction_mean,
                    "account": account,
                }
            )

    return data, header
