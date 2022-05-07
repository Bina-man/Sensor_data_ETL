


{{ config(materialized='table') }}

SELECT ID, FWY, DIR, District, County, City, State_PM, Abs_PM, Latitude, Longitude, Length, Type, Lanes, Name
FROM analytics.I80Stations
