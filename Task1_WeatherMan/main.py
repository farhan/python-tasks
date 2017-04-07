from os import listdir
from os.path import isfile, join
from annual_weather_stats import AnnualWeatherStats
import weather_file_reader


def main():
    report_no = input('Please enter report no.: ')
    data_dir_path = input('Please enter weather data directory (hint: weatherdata): ')

    try:
        # Get all files present in data directory
        files_list = [file for file in listdir(data_dir_path) if isfile(join(data_dir_path, file))]
    except:
        print('No such directory exists.')
        return

    # Populate dictionary having yearly weather stats against each year
    year_files_dict = {}
    for file in files_list:
        year = file.split('_')[2]
        if year not in year_files_dict.keys():
            year_files_dict[year] = AnnualWeatherStats()
        # read_file_and_update_stats(file, year_files_dict[year])
        weather_file_reader.read_file_and_update_stats(join(data_dir_path, file), year_files_dict[year])

    print('\n\nReport  # {}'.format(report_no))

    # Print Annual Max/Min Temp results
    print('\n1. Annual Max/Min Temp')
    print('\nYear{:>20}{:>20}{:>20}{:>20}'.format('MAX Temp', 'MIN Temp', 'MAX Humidity', 'MIN Humidity'), )
    print('-' * 84)
    for year, stats in year_files_dict.items():
        print('{}{:>18}{:>20}{:>18}{:>20}'.format(year, stats.max_temp, stats.min_temp, stats.max_humidity,
                                                  stats.min_humidity))

    # Print Hot​test days of each year
    print('\n2. Hot​test days of each year')
    print('\nYear{:>20}{:>20}'.format('Date', 'Temp'))
    print('-' * 44)
    for year, stats in year_files_dict.items():
        print('{:<18}{:<16}{:>10}'.format(year, stats.hottest_day, stats.max_temp))

    print('\n\ndata_dir : {}'.format(data_dir_path))


if __name__ == "__main__": main()
