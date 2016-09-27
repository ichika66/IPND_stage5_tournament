#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
'''
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")
'''
def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")

def deleteMatches():
    """Remove all the match records from the database."""
#    db = connect()
#    c = db.cursor()
#    c.execute("DELETE FROM Matches")
    db, cursor = connect()
    cursor.execute("DELETE FROM Matches;")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
#    db = connect()
#    c = db.cursor()
#    c.execute("DELETE FROM Players")
    db, cursor = connect()
    cursor.execute("DELETE FROM Players;")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
#    db = connect()
#    c = db.cursor()
    db, cursor = connect()
    cursor.execute("SELECT count(id) FROM Players;")
#    c.execute("SELECT count(id) FROM Players")
#    rows = c.fetchall()
    rows = cursor.fetchone()
    db.close()
    return rows[0]
#    return rows[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()

    query = "INSERT INTO Players (name) VALUES (%s);"
    parameter = (name,)
    cursor.execute(query, parameter)
#    c = db.cursor()
#    c.execute("INSERT INTO Players (name) VALUES (%s)",(name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
 #   db = connect()
 #   c = db.cursor()
    db, cursor = connect()
 #   c.execute("SELECT id, name, wins, matches FROM Standings ORDER BY wins DESC")
    cursor.execute("SELECT id, name, wins, matches FROM Standings ORDER BY wins DESC")
    rows = cursor.fetchall()
#    rows = c.fetchall()
    db.close();
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
#    db = connect()
#    c = db.cursor()
    db, cursor = connect()
#    c.execute("INSERT INTO Matches (player, opponent, result) VALUES (%s, %s, 1)",(winner, loser,))
#    c.execute("INSERT INTO Matches (player, opponent, result) VALUES (%s, %s, 0)",(loser, winner,))
#    cursor.execute("INSERT INTO Matches (player, opponent, result) VALUES (%s, %s, 1)",(winner, loser,))
#    cursor.execute("INSERT INTO Matches (player, opponent, result) VALUES (%s, %s, 0)",(loser, winner,))
#    cursor.execute("INSERT INTO Matches (winner, loser) VALUES (%s, %s)",(loser, winner,))
    query = "INSERT INTO Matches (winner, loser) VALUES (%s, %s);"
    parameter = (winner, loser,)
    cursor.execute(query, parameter)
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
#    db = connect()
#    c = db.cursor()
#    db, cursor = connect()
#    cursor.execute("SELECT id, name, wins FROM Standings ORDER BY wins DESC")
#    c.execute("SELECT id, name, wins FROM Standings ORDER BY wins DESC")
#    rows = c.fetchall()
#    rows = cursor.fetchall()
#    db.close();
    rows = playerStandings()
    i = 0
    pairings = []
    while i < len(rows):
        player_id1 = rows[i][0]
        player_name1 = rows[i][1]
        player_id2 = rows[i + 1][0]
        player_name2 = rows[i + 1][1]
        pairings.append((player_id1, player_name1, player_id2, player_name2))
        i = i + 2
    return pairings

