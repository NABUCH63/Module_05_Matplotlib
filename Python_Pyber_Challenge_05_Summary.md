# Pyber Fare Analysis

## Background

This analysis was intended to determine the total fares over time in different city types, both for what the rider pays and the driver makes. Three city types were determined: Urban, Suburban, and Rural. The results of the analysis are summarized below.

## Results

* The city summary revealed that Urban city-types had the most rides at 1625. Suburban had the second highest value of 625, and Rural the lowest of 125 rides. Total fares and total drivers saw the same trend, with the highest activity/pricing in Urban areas and the least in Rural. The opposite was seen for average trip cost and average driver intake. Both were the least in Urban city-types and the highest in Rural. This could be directly attributed to the number of drivers in Rural city-types being 537, while the Urban areas saw that number drastically increase to 59602 drivers. The summary statistics can be seen below.

![City_summary](/Output/City_Summary.png)

* When fares were plotted over time per city-type, it was seen that each city-type maintained the initial trend; Urban city-types collected the most total fares each week and Rural the least. The plot of the fares over time can be seen below.

![Fares_Overtime_Plot](/Output/Pyber_Fares.png)

## Summary

Urban city-types show the most activity and a surplus of drivers available. This seems to decrease the average fare that each driver receives. Rural city-types display the opposite, with the least rider activity but the highest average fair received per driver. I would recommend the following:

* Decrease the number of drivers allowed to log in to the Urban areas to allow for a greater yield per driver. Maintain a ratio similar to Suburban areas, roughly 14:1 drivers to riders. Currently, Urban areas are at roughly 37:1.

* Incentivize more drivers to operate in Rural areas, increase the driver ratio to be similar to Suburban areas. Currently, Rural areas are at roughly 4:1. 

* Potentially create a fixed number of drivers able to log into certain regions based on the average number of riders over the last few months. Encourage drivers to remain with Pyber by ensuring they are able to collect a consitent and sufficient fare revenue.