

class XMLJSONConverter:
    """
    XML/JSON Converter
    """

    @staticmethod
    def convert_transaction_to_json(transaction):
        """
        Convert transaction array to json
        :param transaction: array - [Name, Category, Amount, Date, Account, ExpenseOrIncome]
        :return: JSON converted
        """

        output = dict({
            "name": transaction[0],
            "category": transaction[1],
            "amount": transaction[2],
            "date": transaction[3],
            "type": transaction[5],
            "comment": "",
            "account": transaction[4]
        })

        return output
