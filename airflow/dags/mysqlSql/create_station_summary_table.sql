CREATE TABLE IF NOT EXISTS `Station_Summary`
( 
  `ID` INT NOT NULL,
  `flow_99` FLOAT DEFAULT 0,
  `flow_max` FLOAT DEFAULT 0,
  `flow_median` FLOAT DEFAULT 0,
  `flow_total` FLOAT DEFAULT 0,
  `n_obs` FLOAT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;