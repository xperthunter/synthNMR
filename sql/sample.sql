CREATE TABLE data (
	id INTEGER PRIMARY KEY NOT NULL,
	points INTEGER,
	np_plot BLOB,
	center_coords BLOB,
	plot_pixels BLOB,
	centers_pixels BLOB,
	todays_date TEXT,
	img_specs_id INTEGER,
	FOREIGN KEY ([img_specs_id]) REFERENCES "img_specs" ([id]) ON DELETE NO
	ACTION ON UPDATE NO ACTION
);

CREATE TABLE img_specs (
    id INTEGER PRIMARY KEY NOT NULL,
    figsize TEXT,
    dpi TEXT
);

CREATE TABLE plot_specs (
    id INTEGER PRIMARY KEY NOT NULL,
    density FLOAT,
    lower_limit FLOAT,
    upper_limit FLOAT,
    mode TEXT,
    variance FLOAT
);
