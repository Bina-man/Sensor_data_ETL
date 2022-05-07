create table if not exists i80stations 
( 
    id int not null,
    fwy int not null,
    dir text not null,
    district int not null,
    county int not null,
    city text default null,
    state_pm text not null,
    abs_pm double precision not null,
    latitude double precision not null,
    longitude double precision not null,
    length double precision default null,
    type text not null,
    lanes int not null,
    name text not null,
    user_id_1 text default null,
    user_id_2 text default null,
    user_id_3 text default null,
    user_id_4 text default null,
    primary key (id)
);