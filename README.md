# Codewars Ranking

A leaderboard for the upcoming Codewars competition.

This repository contains the web app for the leaderboard as well as a script to maintain the database for each candidate's score progression. The score of each candidate is meant to be set to 0 at the beginning of the competition btw, since the competing criterion is most points gained while the competition is active.

the above sentence sounds rly awkward welp i cant english IB is severely detrimental to ones language proficiency BBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

## `tools.py` Usage

Before firing up the application, run
```sh
python tools.py init
```
to initialize the database and stuff.

To add a new player to the competition, run
```sh
python tools.py add <codewars_id> <display_name>
```
to initialize the tracking of that player. Note that if `<display_name>` contains space, wrap it in quotes, or just google how to use CLI idk make it work ajksgyasjhghbfhmnbsjbfmdss

To restarts the tracking progress for one player (sets the display score to 0), do:
```sh
python tools.py reset <codewars_id>
```

To remove a player, do:
```sh
python tools.py remove <codewars_id>
```

To sync all players' starting score to their current score (effectively setting their display score to 0), do:
```sh
python tools.py resetAll
```

that should be it k thx bye gotta do my math ia
