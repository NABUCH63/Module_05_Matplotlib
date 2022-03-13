# Add Matplotlib inline magic command
#get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_file = "Input/city_data.csv"
ride_file = "Input/ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_file)
ride_data_df = pd.read_csv(ride_file)


# ### Merge the DataFrames

# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head(15)


# ## Challenge Deliverable 1. Generate a Ride-Sharing DataFrame by City Type

#  1. Get the total rides for each city type
type_chk = pyber_data_df["type"].value_counts()

# Urban = pyber_data_df.loc[pyber_data_df["type"] == "Urban"]
# Suburban = pyber_data_df.loc[pyber_data_df["type"] == "Suburban"]
# Rural = pyber_data_df.loc[pyber_data_df["type"] == "Rural"]

CityTy_Rides = pyber_data_df.groupby("type").count()["ride_id"]

# 2. Get the total drivers for each city type
CityTy_Drivers = pyber_data_df.groupby("type").sum()["driver_count"]

#  3. Get the total amount of fares for each city type
CityTy_Fares = pyber_data_df.groupby("type").sum()["fare"]

#  4. Get the average fare per ride for each city type. 
CityTy_Avg_Fare = CityTy_Fares/CityTy_Rides

# 5. Get the average fare per driver for each city type. 
CityTy_Avg_Fare_Driver = CityTy_Fares/CityTy_Drivers

#  6. Create a PyBer summary DataFrame. 
City_Type_Summary_df = pd.DataFrame({
    "Total Rides": CityTy_Rides,
    "Total Fares": CityTy_Fares,
    "Total Drivers": CityTy_Drivers,
    "Average Cost per Trip": CityTy_Avg_Fare,
    "Average Driver Intake": CityTy_Avg_Fare_Driver}, index=["Urban", "Suburban", "Rural"])
City_Type_Summary_df.head(10)

#  8. Format the columns.
City_Type_Summary_df["Total Rides"] = City_Type_Summary_df["Total Rides"].map("{:,.0f}".format)
City_Type_Summary_df["Total Drivers"] = City_Type_Summary_df["Total Drivers"].map("{:,.0f}".format)
City_Type_Summary_df["Total Fares"] = City_Type_Summary_df["Total Fares"].map("${:,.2f}".format)
City_Type_Summary_df["Average Cost per Trip"] = City_Type_Summary_df["Average Cost per Trip"].map("${:,.2f}".format)
City_Type_Summary_df["Average Driver Intake"] = City_Type_Summary_df["Average Driver Intake"].map("${:,.2f}".format)
City_Type_Summary_df.to_csv("Output/City_Summary.csv", index=True)
City_Type_Summary_df.head()


# ## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city.

# Print the merged DataFrame for reference.
print(pyber_data_df)

# 1. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
pyber_by_date = pyber_data_df.groupby(["date", "type"])["fare"].sum()

# 2. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
pyber_by_date = pyber_by_date.reset_index()

# 3. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
pyber_pivot = pyber_by_date.pivot(index=["date"], columns=["type"], values=["fare"])

# 4. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
pyber_loc_df = pyber_pivot.loc["2019-01-01":"2019-04-29"]

# 5. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
pyber_loc_df.index = pd.to_datetime(pyber_loc_df.index)

# 6. Check that the datatype for the index is datetime using df.info()
pyber_loc_df.info()

# 7. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
pyber_week_df = pyber_loc_df.fare.resample("W").sum()

# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax = plt.plot(pyber_week_df["Urban"], label="Urban")
ax = plt.plot(pyber_week_df["Suburban"], label="Suburban")
ax = plt.plot(pyber_week_df["Rural"], label="Rural")
plt.xticks(rotation=45)
plt.xlabel("Week Start")
plt.ylabel("Fare ($)")
plt.title("Fares Per City Type Over Time")
plt.legend(loc="best")
img = plt.gcf()
img.set_size_inches(12,4)
plt.tight_layout()
plt.savefig("Output/Pyber_Fares.png", dpi=200)




