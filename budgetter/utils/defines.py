from enum import Enum
from typing import List


class TransactionMean(Enum):
    """
    Transactions Mean
    """

    CASH = "CASH"
    CARD = "CARD"
    TRANSFER = "TRANSFER"


class TransactionType(Enum):
    """
    Transactions Mean
    """

    INCOME = "INCOME"
    EXPENSES = "EXPENSES"
    INTERNAL = "INTERNAL"


class Categories(Enum):
    MORTGAGE = ":/categories/categories/real_estate_agent_FILL0_wght400_GRAD0_opsz48.svg"
    RENT = ":/categories/categories/apartment_FILL0_wght400_GRAD0_opsz48.svg"
    TAXES = ":/categories/categories/receipt_long_FILL0_wght400_GRAD0_opsz48.svg"
    GAS = ":/categories/categories/local_gas_station_FILL0_wght400_GRAD0_opsz48.svg"
    CAR = ":/categories/categories/directions_car_FILL0_wght400_GRAD0_opsz48.svg"
    TRANSPORTATION = ":/categories/categories/train_FILL0_wght400_GRAD0_opsz48.svg"
    PARKING = ":/categories/categories/local_parking_FILL0_wght400_GRAD0_opsz48.svg"
    GROCERIES = ":/categories/categories/shopping_cart_FILL0_wght400_GRAD0_opsz48.svg"
    RESTAURANT = ":/categories/categories/restaurant_FILL0_wght400_GRAD0_opsz48.svg"
    ELECTRICITY = ":/categories/categories/outlet_FILL0_wght400_GRAD0_opsz48.svg"
    WATER = ":/categories/categories/water_drop_FILL0_wght400_GRAD0_opsz48.svg"
    ELECTRONICS = ":/categories/categories/devices_FILL0_wght400_GRAD0_opsz48.svg"
    INTERNET = ":/categories/categories/wifi_FILL0_wght400_GRAD0_opsz48.svg"
    SUBSCRIPTIONS = ":/categories/categories/subscriptions_FILL0_wght400_GRAD0_opsz48.svg"
    CLOTHING = ":/categories/categories/checkroom_FILL0_wght400_GRAD0_opsz48.svg"
    MEDICAL = ":/categories/categories/medical_services_FILL0_wght400_GRAD0_opsz48.svg"
    INSURANCE = ":/categories/categories/personal_injury_FILL0_wght400_GRAD0_opsz48.svg"
    CHILD = ":/categories/categories/child_care_FILL0_wght400_GRAD0_opsz48.svg"
    SPORT_MEMBERSHIP = ":/categories/categories/fitness_center_FILL0_wght400_GRAD0_opsz48.svg"
    HAIRCUT = ":/categories/categories/cut_FILL0_wght400_GRAD0_opsz48.svg"
    BANK_FEES = ":/categories/categories/account_balance_FILL0_wght400_GRAD0_opsz48.svg"
    PERSONAL_LOANS = ":/categories/categories/request_quote_FILL0_wght400_GRAD0_opsz48.svg"
    INVESTING = ":/categories/categories/waterfall_chart_FILL0_wght400_GRAD0_opsz48.svg"
    EDUCATION = ":/categories/categories/school_FILL0_wght400_GRAD0_opsz48.svg"
    GIFTS = ":/categories/categories/redeem_FILL0_wght400_GRAD0_opsz48.svg"
    MOVIES = ":/categories/categories/movie_FILL0_wght400_GRAD0_opsz48.svg"
    MUSIC = ":/categories/categories/music_note_FILL0_wght400_GRAD0_opsz48.svg"
    VACATIONS = ":/categories/categories/holiday_village_FILL0_wght400_GRAD0_opsz48.svg"
    SALARY = ":/categories/categories/payments_FILL0_wght400_GRAD0_opsz48.svg"

    @classmethod
    def has_key_in(cls, key: str) -> bool:
        """
        Return key presence in categories

        :param key: key to look for
        :return: True/False
        """
        return key.upper() in cls.__members__

    @classmethod
    def get_members(cls) -> List:
        """
        Return categories list

        :return: categories as a list
        """
        return [member.capitalize().replace('_', ' ') for member in list(cls.__members__)]
