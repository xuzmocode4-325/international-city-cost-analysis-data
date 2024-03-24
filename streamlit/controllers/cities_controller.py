from utils.loaders.data_loader import DataLoader

class CitiesController:
    """
    Model for managing city data.
    """

    def __init__(self, country):
        """
        Initialize the CitiesController with the given country.

        Args:
            country (str): The name of the country.
        """
        self.data_loader = DataLoader() 
        self.cities = self.get_cities(country)

    def get_cities(self, country):
        """
        Get cities for the given country.

        Args:
            country (str): The name of the country.

        Returns:
            list: A list of cities in the specified country.
        """
        df = self.data_loader.load_data()
        if df is not None:
            cities_df = df[df["Country"] == country]
            cities_list = cities_df['City'].tolist()  # Assuming column name is 'City'
            return cities_list
        else:
            return []
