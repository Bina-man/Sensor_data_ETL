/*
Name: Name Agg
Data source: 1
Created By: mysql-dbt
Last Updated At: 2021-09-30T07:50:22.868Z
*/
select Name, count(Name), avg(flow_median) from merged_station_summary group by Name;