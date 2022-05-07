{{ config(materialized='table') }}

select `Name`, count(`Name`), avg(flow_total) from {{ref('merged_station_summary')}} group by Name
