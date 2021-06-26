CREATE TABLE pokemon_data_table (
	index_column INT,
	pokedex_number INT,
	english_name VARCHAR,
	german_name VARCHAR,
	japanese_name VARCHAR,
	generation INT,
	is_sub_legendary INT,
	is_legendary INT,
	is_mythical INT,
	species VARCHAR,
	type_number INT,
	type_1 VARCHAR,
	type_2 VARCHAR,
	height_m REAL,
	weight_kg REAL,
	abilities_number INT,
	ability_1 VARCHAR,
	ability_2 VARCHAR,
	ability_hidden VARCHAR,
	total_points REAL,
	hp REAL,
	attack REAL,
	defense REAL,
	sp_attack REAL,
	sp_defense REAL,
	speed REAL,
	catch_rate REAL,
	base_friendship REAL,
	base_experience REAL,
	growth_rate VARCHAR,
	egg_type_number INT,
	egg_type_1 VARCHAR,
	egg_type_2 VARCHAR,
	percentage_male REAL,
	egg_cycles REAL,
	against_normal REAL,
	against_fire REAL,
	against_water REAL,
	against_electric REAL,
	against_grass REAL,
	against_ice REAL,
	against_fight REAL,
	against_poison REAL,
	against_ground REAL,
	against_flying REAL,
	against_psychic REAL,
	against_bug REAL,
	against_rock REAL,
	against_ghost REAL,
	against_dragon REAL,
	against_dark REAL,
	against_steel REAL,
	against_fairy REAL,
PRIMARY KEY (pokedex_number),
UNIQUE (english_name)
);