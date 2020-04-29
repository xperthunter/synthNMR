CREATE TABLE data (
	id INTEGER PRIMARY KEY NOT NULL,
	points INTEGER,
	np_plot BLOB,
	center_coords BLOB,
	plot_pixels BLOB,
	centers_pixels BLOB,
	img_specs_id INTEGER,
	plot_specs_id INTEGER,
	user_id INTEGER,
	date TEXT,
	FOREIGN KEY ([user_id]) REFERENCES "user_info" ([id]) ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY ([img_specs_id]) REFERENCES "img_specs" ([ec_id]) ON DELETE NO ACTION ON UPDATE NO ACTION,
	FOREIGN KEY ([plot_specs_id]) REFERENCES "plot_specs" ([id]) ON DELETE NO ACTION ON UPDATE NO ACTION
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

CREATE TABLE user_info (
	id INTEGER PRIMARY KEY NOT NULL,
	first_name TEXT,
	last_name TEXT,
	email TEXT
);