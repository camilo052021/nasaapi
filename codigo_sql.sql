
DROP TABLE IF EXISTS results;
CREATE TABLE results(
    activityID TEXT ,
    catalog TEXT ,
    startTime TEXT ,
    sourceLocation TEXT,
    activeRegionNum INT,
    Date DATE ,
    id_x TEXT PRIMARY KEY NOT NULL,
    id_y INT ,
    uid TEXT ,
    brand TEXT ,
    name TEXT ,
    style TEXT ,
    hop TEXT ,
    yeast TEXT ,
    malts TEXT ,
    ibu TEXT,
    alcohol DECIMAL,
    blg TEXT ,
    Country TEXT ,
    FundationYear INT
);

CREATE VIEW relex as
SELECT * FROM public.results
WHERE id_y is not null;