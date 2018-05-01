--This script creates the staging schema and all of the staging tables where the csvs will be loaded
IF NOT EXISTS ( SELECT  *
                FROM    sys.schemas
                WHERE   name = N'stg' ) 
    EXEC('CREATE SCHEMA [stg] AUTHORIZATION [dbo]');
GO

--Create the game staging table
IF OBJECT_ID(N'stg.game', 'U') IS NOT NULL
BEGIN
	DROP TABLE stg.game
END

CREATE TABLE stg.game
	(
		game_player_key bigint NOT NULL
		,game_key bigint NOT NULL
		, player_key bigint NOT NULL
		, team_key bigint NOT NULL
		, [fg2ptatt] INT NOT NULL
        , [fg2ptmade] INT NOT NULL
        , [fg3ptatt] INT NOT NULL
        , [fg3ptmade] INT NOT NULL
        , [fgatt] INT NOT NULL
        , [fgmade] INT NOT NULL
        , [ftatt] INT NOT NULL
        , [ftmade] INT NOT NULL
        , [offreb] INT NOT NULL
        , [defreb] INT NOT NULL
        , [reb] INT NOT NULL
        , [ast] INT NOT NULL
        , [pts] INT NOT NULL
        , [tov] INT NOT NULL
        , [stl] INT NOT NULL
        , [blk] INT NOT NULL
        , [blkagainst] INT NOT NULL
        , [foulpers] INT NOT NULL
        , [plusminus] INT NOT NULL
        , [minseconds] INT NOT NULL
		,CONSTRAINT pk_game_player_key PRIMARY KEY CLUSTERED
			(
				game_player_key ASC
			)
	)

--Create the schedule staging table
IF OBJECT_ID(N'stg.schedule', 'U') IS NOT NULL
BEGIN
	DROP TABLE stg.schedule
END

CREATE TABLE stg.schedule
	(
		game_key bigint NOT NULL
		, date_key int NOT NULL
		, away_team_key bigint NOT NULL
		, home_team_key bigint NOT NULL
		,CONSTRAINT pk_game_key PRIMARY KEY CLUSTERED
			(
				game_key ASC
			)
	)

--Create the team staging table
IF OBJECT_ID(N'stg.team', 'U') IS NOT NULL
BEGIN
	DROP TABLE stg.team
END

CREATE TABLE stg.team
	(
		team_key bigint NOT NULL
		, team_city nvarchar(20) NOT NULL
		, team_name nvarchar(20) NOT NULL
		, team_abbrev nvarchar(5) NOT NULL
		, active_flag bit NOT NULL
	)

--Create the player staging table
IF OBJECT_ID(N'stg.player', 'U') IS NOT NULL
BEGIN
	DROP TABLE stg.player
END

CREATE TABLE stg.player
	(
		player_team_key bigint NOT NULL
		, player_key bigint NOT NULL
		, team_key bigint NOT NULL
		, start_date_key int NOT NULL
		, end_date_key int NULL
		, last_name nvarchar(20) NOT NULL
		, first_name nvarchar(20) NOT NULL
		, position nvarchar(3) NOT NULL
		, height nvarchar(5) NOT NULL
		, weight int NOT NULL
		, age int NOT NULL
		, active_flag bit NOT NULL
	)

--Create the season staging table
IF OBJECT_ID(N'stg.season', 'U') IS NOT NULL
BEGIN
	DROP TABLE stg.season
END

CREATE TABLE stg.season
	(
		season_key int IDENTITY(1,1) NOT NULL
		, season_name nvarchar(25) NOT NULL
		, season_start_date_key int NOT NULL
	)

--Create the season staging table
IF OBJECT_ID(N'stg.injury', 'U') IS NOT NULL
BEGIN
	DROP TABLE stg.injury
END

CREATE TABLE stg.injury
	(
		injury_key bigint IDENTITY(1,1) NOT NULL
		, player_key bigint NOT NULL
		, team_key bigint NOT NULL
		, injury_start_date_key int NOT NULL
		, injury_end_date_key int NULL
		, injury_description nvarchar(100) NULL
		, severity int NULL
	)