-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Database creation
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- DROP tables and views created previously
DROP VIEW IF EXISTS Standings;
DROP View IF EXISTS Count;
DROP VIEW IF EXISTS Wins;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS Players;

-- Create Players table
CREATE TABLE Players (
  id serial primary key,
  name text );

-- Create Matches Table
CREATE TABLE Matches (
  id serial primary key,
  player int references Players(id),
  opponent int references Players(id),
  result int );

-- Create Wins View which counts of wins of each Player
CREATE VIEW Wins AS
  SELECT Players.id, count(Matches.opponent) AS n
  FROM Players
  LEFT JOIN (SELECT * FROM Matches WHERE result > 0) AS Matches
  ON Players.id = Matches.player
  GROUP BY Players.id;

-- Create count view to count the number of matches for each player
CREATE VIEW Count AS
  SELECT Players.id, Count(Matches.opponent) AS n 
  FROM Players
  LEFT JOIN Matches
  ON Players.id = Matches.player
  GROUP BY Players.id;

-- Create Standings View which shows number of wins and matches for each player
CREATE VIEW Standings AS 
  SELECT Players.id, Players.name, Wins.n AS wins, Count.n AS matches 
  FROM Players, Wins, Count
  WHERE Players.id = Wins.id AND Wins.id = Count.id;
