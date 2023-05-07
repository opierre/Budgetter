import re
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def parse_file(path_to_file: str, sep: str = ";") -> List:
    """
    Check file is conform to expected format
    Training dataset CSV file with ; as sep: date;<x columns describing transaction>;amount;category
    Data to compute CSV file with ; as sep: date;<x columns describing transaction>;amount

    :param path_to_file: path to file
    :param sep: separator for CSV file
    :return: lines read as a list
    """

    lines = []
    date_regexp = [
        "^\d{4}/\d{2}/\d{2}" + f"{sep}",
        "^\d{2}/\d{2}/\d{2}" + f"{sep}",
        "^\d{2}/\d{2}/\d{4}" + f"{sep}",
    ]
    with open(path_to_file) as fd:
        line = fd.readline()

        # Parse all lines and check format for each line starting with a valid date
        while line != "":
            for regexp in date_regexp:
                if re.match(regexp, line):
                    lines.append(line.strip())
                    break
            line = fd.readline()
    return lines


class CategoryPredictor:
    """
    Predict categories according to training dataset
    """

    # Removing words that aren't relevant for classification, therefore
    # introducing classification noise.
    # These words may need to be adapted.
    STOP_WORDS = ["carte", "cb", "du", "facture", "paiement"]

    def __init__(self, training_dataset: List[str], data_to_test: List[str]):
        # Store training set data frames
        self.training_dataset = training_dataset
        self.training_dataset_transaction = []
        self.training_dataset_category = []

        # Store data to parse
        self._data_to_set = data_to_test

        # Process training data: transaction fields & category
        self.__build_dataset_frames(training_dataset)

        # Store vector
        self.vector = TfidfVectorizer(
            stop_words="english",
            token_pattern="(?u)\\b\\w[a-zA-Z0-9_\\-\\.]+\\b",
            ngram_range=(1, 3),
        )

        # Store pipeline with different steps
        self.pipeline = Pipeline(
            [("vector", self.vector), ("regression", LogisticRegression())]
        )

    def __build_dataset_frames(self, training_dataset: List[str]):
        """
        Buidl training dataset frames with X the transaction and Y the category

        :param training_dataset: training dataset ["dd/mm/yyyy;field_1;field_n;price;category"]
        :return:
        """
        for dataset in training_dataset:
            # Remove date and price from transaction because it is not necessary for predicting category
            # First and last column
            transaction_useful_columns = ";".join(dataset.split(";")[1:-1])
            category = dataset.split(";")[-1]
            self.training_dataset_transaction.append(f"{transaction_useful_columns}")
            self.training_dataset_category.append(category)

    def predict(self) -> List[str]:
        """
        Predict categories for list of items

        :return: prediction as list of strings
        """

        self.pipeline.fit(
            self.training_dataset_transaction, self.training_dataset_category
        )
        return self.pipeline.predict(self._data_to_set)
