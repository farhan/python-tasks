def read_file_and_update_stats(file_path, annual_weather_stats):
    file = open(file_path)
    try:
        lines = file.read().split('\n')
        i = -1
        for line in lines:
            i += 1
            # Skip first 2 rows
            if i < 2:
                continue
            # print('#', line)
            values = line.split(',')
            if len(values) > 15:
                try:
                    annual_weather_stats.update_weather_stat(values)
                except:
                    pass
    except:
        pass
    finally:
        file.close()
