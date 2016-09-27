# IPND_stage5_tournament
Udacity Intro to Programing Nanodegree Stage 5 Electives: Choose Your Path - Back-End Developer/ Tournament Results

### Files
* tournament.sql
* tournament.py
* tournament_test.py

### Installation
The following software is requred to run this program.
* VirtualBox: https://www.virtualbox.org/wiki/Downloads
* Vargrant: https://www.vagrantup.com/downloads.html

### Cloning the source repository
Fork the repository below to your GitHub then clone it to your local computer.

https://github.com/udacity/fullstack-nanodegree-vm

### Run Vargrant virtual machine
Commit the command below to run Vagrant VM on vagurant directory.

```
 $ vagrant up
 $ vagrant ssh
```
### Run the Swiss Tournament
First, change diretory to the tournament.
```
 $ cd /vagrant/tournament/
```
then override files with files mentioned above in this repository.

Second, initialize the tournament database.
```
$ psql
DROP DATABASE IF EXIST tournament;
CREATE DATABASE tournament;
\c tournament
\i tournament.sql
\q
```

### Run the test
Run tournament_test.py file to see the results.
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```

### References

* http://www.w3schools.com/sql/default.asp
* https://www.postgresql.org/docs/8.1/static/datatype.html
* http://bobby-tables.com


