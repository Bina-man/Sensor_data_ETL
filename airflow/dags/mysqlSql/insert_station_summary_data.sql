LOAD DATA 
INFILE '/var/lib/mysql-files/station_summary.csv' 
INTO TABLE Station_Summary 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';