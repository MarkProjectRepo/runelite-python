from enum import Enum

class GrandExchangeOfferState(Enum):
    """
    Describes the state of a Grand Exchange offer.
    """
    EMPTY = 0
    CANCELLED_BUY = 1
    CANCELLED_SELL = 2
    BUYING = 3
    BOUGHT = 4

class GrandExchangeOffer:
    """
    Represents an offer in a grand exchange slot.
    """

    def __init__(self, offer_instance, gateway):
        self.offer_instance = offer_instance

    def get_quantity_sold(self) -> int:
        """
        Gets the quantity of bought or sold items.

        Returns:
            int: The quantity bought or sold.
        """
        return self.offer_instance.getQuantitySold()

    def get_item_id(self) -> int:
        """
        Gets the ID of the item being bought or sold.

        Returns:
            int: The item ID.
        """
        return self.offer_instance.getItemId()

    def get_total_quantity(self) -> int:
        """
        Gets the total quantity being bought or sold.

        Returns:
            int: The total quantity.
        """
        return self.offer_instance.getTotalQuantity()

    def get_price(self) -> int:
        """
        Gets the offer or sell price per item.

        Returns:
            int: The offer price.
        """
        return self.offer_instance.getPrice()

    def get_spent(self) -> int:
        """
        Gets the total amount of money spent so far.

        Returns:
            int: The amount spent.
        """
        return self.offer_instance.getSpent()

    def get_state(self) -> GrandExchangeOfferState:
        """
        Gets the current state of the offer.

        Returns:
            GrandExchangeOfferState: The offer's state.
        """
        
        return GrandExchangeOfferState(self.offer_instance.getState()).value