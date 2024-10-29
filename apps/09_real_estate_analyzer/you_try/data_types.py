class Purchase:
    def __init__(self, street, city, zip_code, state, beds, baths, sq__ft,
                 house_type, sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.state = state
        self.beds = int(beds)
        self.baths = int(baths)
        self.sq__ft = sq__ft
        self.house_type = house_type
        self.sale_date = sale_date
        self.price = int(price)
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def create_purchase_from_dict(data_dict):

        street = data_dict["street"]
        city = data_dict["city"]
        zip_code = data_dict["zip"]
        state = data_dict["state"]
        beds = data_dict["beds"]
        baths = data_dict["baths"]
        sq__ft = data_dict["sq__ft"]
        house_type = data_dict["type"]
        sale_date = data_dict["sale_date"]
        price = data_dict["price"]
        latitude = data_dict["latitude"]
        longitude = data_dict["longitude"]

        return Purchase(street, city, zip_code, state, beds, baths, sq__ft,
                        house_type, sale_date, price, latitude, longitude)

    def __repr__(self):
        return f"{self.street}, {self.city}, {self.zip_code}, {self.state}, {self.beds}, {self.baths}, {self.sq__ft}, {self.house_type}, {self.sale_date}, {self.price}, {self.latitude}, {self.longitude}"


