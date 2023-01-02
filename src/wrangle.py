# 1.) Plot 1 Data Wrangling
def world_electricity_data(data, pd, min, max):
    # loc method is used to selected based on criterion
    world_data = data.loc[(data["country"] == "World")]
    world_data_dict = {
        "population": world_data["population"],
        "year": world_data["year"],
        "electricity_generation": world_data["electricity_generation"],
    }
    world_population = pd.DataFrame(world_data_dict)
    world_electricity = world_population.loc[(world_population["year"] >= min)]
    world_electricity = world_electricity.loc[(world_population["year"] <= max)]
    return world_electricity


# 2.) Plot 2 Data Wrangling
def sawces_my_year_data(data, my_year):
    world_data = data.loc[(data["country"] == "World")]  # Filters only World data
    sources_my_year = world_data.loc[(world_data["year"]) >= 2000]  # Filters data from 2000 on
    sources_my_year = sources_my_year.loc[(sources_my_year["year"]) == my_year]  # Filters data to the year selected
    sources_my_year_filt = sources_my_year.iloc[:, [1, 2, 29, 30, 32, 33, 34, 35, 39, 40]]  # Filters the world energy sources
    sources_my_year_filt = sources_my_year_filt.T  # Transposes data set
    return sources_my_year_filt


# 3.) Plot 3 Data Wrangling
def regression_country_data(data, my_country, sawce, year_range):
    reg_country = data.loc[(data["country"] == my_country)]  # Filters to just the country selected
    reg_years = reg_country.loc[reg_country["year"] >= (year_range[0])]  # Filters >= Years
    reg_years = reg_years.loc[
        reg_country["year"] <= (year_range[1])
    ]  # Filters <= Years
    reg_data = reg_years.iloc[
        :, [1, 2, 29, 30, 32, 33, 34, 35, 39, 40]
    ]  # Filters to only year, country and source columns
    reg_sawce_column = reg_data.filter(
        like=sawce.lower(), axis=1
    )  # Filters out only the column of the energy source selected
    reg_year_column = reg_data.iloc[:, 1]
    reg_sawce_column["year"] = reg_year_column
    return reg_sawce_column


# 4.)


## TO-DO
"""
## PLOT 4.)
-- Wrangle for 4.) Sources World Plot
-- 


"""
