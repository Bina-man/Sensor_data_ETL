/*
Name: flow_total gt two ions
Data source: 1
Created By: mysql-dbt
Last Updated At: 2021-09-30T07:54:26.278Z
*/
select * from merged_station_summary where flow_total > 2000000;