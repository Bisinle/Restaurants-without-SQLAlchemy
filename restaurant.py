class Restaurant:
    def __init__(self, name="CJ"):
        self._name = ""

        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name must be a string")

    # ----------------------------------------------------------------------------------
    # get restaurant name
    def get_name(self):
        return self._name

    # ----------------------------------------------------------------------------------
    # get restaurant review
    def get_restuarant_reveiw(self):
        from review import Review  # import list reviews from review module

        review_list = Review.print_all_reviews()

        return [
            review for review in review_list if review["restaurant_name"] == self._name
        ]

    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # get the unique customers that gave review
    def get_customer_that_gave_the_restaurant_review(self):
        listt = self.get_restuarant_reveiw()
        unique_customer = list()
        # collect the names only
        for dict in listt:
            if dict not in unique_customer:
                unique_customer.append(dict["full_name"])

            else:
                return unique_customer
        return set(unique_customer)
