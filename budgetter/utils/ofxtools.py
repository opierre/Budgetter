import os.path

from ofxtools import OFXTree

from budgetter.utils.defines import TransactionType
from budgetter.view.widgets.transaction_widgets.means_widget import MeanType


def convert_ofx_to_json(ofx_file_path: str) -> dict:
    """
    Convert OFX file to JSON to send to server

    :param ofx_file_path: OFX file path
    :return: converted data as JSON
    """

    if not os.path.exists(ofx_file_path):
        return {}

    ofx_parser = OFXTree()
    with open(ofx_file_path, "rb") as ofx_file:
        ofx_parser.parse(ofx_file)

    # Convert to OFX tree for parsing
    ofx = ofx_parser.convert()
    data = {"accounts": []}
    for statement in ofx.statements:
        data.get("accounts").append(
            {
                "account": {
                    "account_id": statement.account.acctid,
                    "amount": statement.balance.balamt,
                    "last_update": statement.balance.dtasof.strftime("%Y-%m-%d"),
                    "transactions": {
                        "count": len(statement.transactions),
                        "start_date": statement.transactions.dtstart,
                        "end_date": statement.transactions.dtend,
                        "list": [],
                    },
                }
            }
        )
        for transaction in statement.transactions:
            # TODO: fix generic term for internal transaction
            if "VIREMENT EN VOTRE FAVEUR DE OLIVIER PIERRE" in transaction.memo:
                transaction_type = TransactionType.INTERNAL
                transaction_mean = MeanType.TRANSFER
            elif float(transaction.trnamt) < 0:
                transaction_type = TransactionType.EXPENSES
                transaction_mean = MeanType.CARD
            else:
                transaction_type = TransactionType.INCOME
                transaction_mean = MeanType.CARD
            data.get("accounts")[-1].get("transactions").get("list").append(
                {
                    "name": transaction.name,
                    "amount": abs(float(transaction.trnamt)),
                    "transaction_type": transaction_type,
                    "date": transaction.dtposted.strftime('%Y-%m-%d'),
                    "comment": transaction.memo,
                    "mean": transaction_mean
                }
            )

    return data
