create table if not exists station_summary
( 
  id int not null,
  flow_99 float default 0,
  flow_max float default 0,
  flow_median float default 0,
  flow_total float default 0,
  n_obs float default 0
);