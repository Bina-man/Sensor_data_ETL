
{{ config(materialized='table') }}

select {{ref('stations_summary')}}.flow_99,
       {{ref('stations_summary')}}.flow_max,
       {{ref('stations_summary')}}.flow_median,
       {{ref('stations_summary')}}.flow_total,
       {{ref('stations_summary')}}.n_obs,
       {{ref('stations_metadata')}}.*
from {{ref('stations_summary')}} 
inner join {{ref('stations_metadata')}} 
on {{ref('stations_summary')}}.ID = {{ref('stations_metadata')}}.ID 
