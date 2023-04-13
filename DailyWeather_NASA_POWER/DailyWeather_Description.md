### Project description:
This Python project aims to fetch daily weather data from the NASA Power API and convert it into a data frame for further analysis. The project utilizes popular libraries such as Pandas, Python Requests, JSON, Typing, and Seaborn.

### Steps to fetch the data, eg- API key required or not, steps to retrieve it, order of script run
By entering the location data in the form of Latitude and Longitude and Using Python Requests, the project fetches daily weather data from the NASA Power API and converts the data into a JSON format. The JSON data is then loaded into a Pandas data frame using the Pandas library. The Typing library is used to ensure that the data is correctly typed, and Seaborn is used to visualize the data for easy analysis.

### Parameter details
Temperature at 2 Meters, Frequency- Daily, Unit- deg C
- T2M: Temperature at 2 Meters
- T2M_MAX: Temperature at 2 Meters Maximum
- T2M_MIN: Temperature at 2 Meters Minimum
- PRECTOTCORR: Precipitation Corrected mm/day

### API reference link

https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/

### Keep the repository clean
- Avoid committing the downloaded .json or .csv file into the repository

### Citations
- Parameter Metadata: https://power.larc.nasa.gov/#resources