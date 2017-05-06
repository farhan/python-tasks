class AnnualWeatherStats:
    # Data file column ids
    ID_DAY = 0
    ID_MAX_TEMP = 1
    ID_MIN_TEMP = 3
    ID_MAX_HUMIDITY = 7
    ID_MIN_HUMIDITY = 9

    def __init__(self, max_temp=-1000, min_temp=1000, max_humidity=-1000,
                 min_humidity=1000, hottest_day=None):
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.max_humidity = max_humidity
        self.min_humidity = min_humidity
        self.hottest_day = hottest_day

    def update_weather_stat(self, new_values):
        """
        Updates the annual weather stats by catering a new
        day record read from data file

        :param new_values: List of values of a row read from data file
        """
        # Max temp & hottest day
        if float(new_values[self.ID_MAX_TEMP]) > self.max_temp:
            self.max_temp = float(new_values[self.ID_MAX_TEMP])
            self.hottest_day = new_values[self.ID_DAY]
        # Min temp
        if float(new_values[self.ID_MIN_TEMP]) < self.min_temp:
            self.min_temp = float(new_values[self.ID_MIN_TEMP])
        # Max humidity
        if float(new_values[self.ID_MAX_HUMIDITY]) > self.max_humidity:
            self.max_humidity = float(new_values[self.ID_MAX_HUMIDITY])
        # Min humidity
        if float(new_values[self.ID_MIN_HUMIDITY]) < self.min_humidity:
            self.min_humidity = float(new_values[self.ID_MIN_HUMIDITY])
