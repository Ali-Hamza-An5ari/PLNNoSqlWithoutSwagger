# DBNoSQL
NoSQL DB for capturing dynamic data

# Sport Scoring desictiption 

1. **Soccer/Football:** Teams score 1 point for each goal. Matches are typically decided by the team with the most points at the end of 90 minutes plus injury time.

2. **American Football:** Six points are scored for a touchdown. Teams can then try for an extra point (1 point, kicked) or a two-point conversion (2 points). Teams also can score three points for a field goal or two points for a safety (tackling the opposing team in their own end zone).

3. **Basketball:** Points can be scored in three ways - one point for a free throw, two points for a field goal within the three-point line, and three points for a field goal outside the three-point line.

4. **Baseball** and Softball: Teams score 1 point, or "run," every time a player is able to circle the bases and return home.

5. **Tennis:** Scoring is complex. Points won go from love (0), to 15, 30, and then 40. If players are tied at 40 it's called "deuce" and they must win by two points. Games make up sets, and sets make up matches. A player usually needs to win 6 games to win a set, and best of 3 or 5 sets (depending on the competition) to win the match.

6. **Volleyball (indoor):** Points are awarded on every serve for faults by the opposing team. The first team to reach 25 points wins the set and the first team to win three sets wins the match.

7. **Golf:** Golf uses a few different scoring systems, but in stroke play, the player with the fewest strokes (hits of the ball) over the whole course wins. In match play, each hole is a separate competition, and the player winning the most holes wins.

8. **Boxing:** Boxing typically uses a 10-point must system for scoring matches. Each round, judges award the more dominant boxer 10 points and the other boxer a number of points between 7 and 9, depending on performance. The boxer with the most points at the end of the match wins. A knockout or technical knockout ends the match immediately.

9. **Hockey (including Ice Hockey):** Teams score 1 point for each goal. The team with the most points at the end of three periods wins.

10. **Rugby:** In rugby union, five points are awarded for a try (similar to a touchdown in American football), after which a conversion kick can be made for an extra 2 points. Three points can also be scored from a field goal or penalty kick.

11. **Cricket:** In cricket, runs can be scored in multiple ways, the most common of which are when the batsmen run between the wickets (1 point per run), hit the ball to the boundary (4 points), or hit the ball over the boundary without it bouncing (6 points). The team with the most runs at the end of the match wins.

12. **Mixed Martial Arts (MMA):** Matches can be won by knockout, submission, or referee stoppage. If none of these occur, the outcome is determined by the judges' scorecards. In most organizations, three judges score each round on a 10-point must system (similar to boxing), awarding 10 points to the round winner and 9 or fewer to the other fighter.

13. **Brazilian Jiu-Jitsu (BJJ):** Matches can be won by submission. If there is no submission, points are awarded for positions and maneuvers. Two points are awarded for a takedown or knee on belly, three points for a pass of the opponent's guard, and four points for a mount or back control. Advantages and penalties can also affect the score.

14. **Judo:** Matches can be won by Ippon (gaining control of your opponent and throwing them onto their back, holding them on their back for 20 seconds, or by submission). If there is no Ippon, points are awarded for lesser throws (Waza-ari) and holds (Yuko). The player with the most points at the end of the match wins.

15. **Wrestling (Freestyle and Greco-Roman):** In Olympic wrestling, points are scored for various types of success in controlling the opponent or bringing the opponent to their back. A match can be won by pinning the opponent's shoulders to the mat. If there is no pin, the wrestler with the most points at the end of the match wins.

16. **Muay Thai:** Points are awarded for strikes landed, with more points for strikes that use the "power" parts of the body (knees, elbows, kicks). Effective defense is also rewarded. If neither fighter is knocked out, the fighter with the most points wins.

17. **Kickboxing:** Similar to Muay Thai and Boxing, points are awarded for strikes landed on the opponent. The fighter with the most points at the end of the match is the winner, unless a knockout occurs.

18. **Boxing:** As previously mentioned, boxing uses a 10-point must system. Each round, judges award the more dominant boxer 10 points and the other boxer a number of points between 7 and 9, depending on performance. The boxer with the most points at the end of the match wins. A knockout or technical knockout ends the match immediately.

Remember, each organization may have specific rules and regulations, so it is always best to refer to the rules set by the official governing body for a detailed understanding.

One common approach would be to use a NoSQL database like MongoDB, which uses a document-oriented model. This model is flexible and can easily accommodate a wide variety of different sport structures.

Here's an example of how you might design your database:
```
{
    "_id": ObjectId(),
    "match_id": "123456", // a unique identifier for each match
    "sport": "Football", // sport type
    "teams": [ // details of the teams or players involved
        {
            "name": "Team A",
            "score": 3 // in football, the score would simply be the number of goals
        },
        {
            "name": "Team B",
            "score": 2
        }
    ],
    "details": { // an optional field for additional scoring details, could be useful for sports like boxing, mma, etc.
        "rounds": [
            {
                "round_number": 1,
                "Team A_points": 10,
                "Team B_points": 9
            },
            // more rounds data...
        ]
    },
    "date": ISODate("2023-06-09T00:00:00Z") // the date of the match
}


```

This design is simple and can cover a wide variety of sports, but it might need to be extended depending on the specifics of each sport. The "details" field could hold additional data, such as player stats or individual round scores. For instance, in tennis you could include details for sets and games within each set.

To insert data into the database, you could use code like the following:

```
db.SCORES.insert({
    "match_id": "123456",
    "sport": "Football",
    "teams": [
        {
            "name": "Team A",
            "score": 3
        },
        {
            "name": "Team B",
            "score": 2
        }
    ],
    "date": new Date()
})

```

This JavaScript code uses MongoDB's insert function to create a new document in the "SCORES" collection.

Please note that you'll need a running MongoDB server and the MongoDB Node.js driver installed to run these commands. Also, remember to replace the example values with the actual data you want to store.

Remember, this is a basic example and may not fully represent all the complexities of each sport's scoring system. It's a starting point from which you can adapt and expand to better suit your needs.

Given the variability in scoring systems for each sport, a key feature of the NoSQL design is the flexibility to adapt to these different systems. Here's an extended example for the 18 sports mentioned, showcasing the kind of data you might include in each:

```
[
    {
        "_id": ObjectId(),
        "match_id": "001",
        "sport": "Soccer",
        "teams": [
            {"name": "Team A", "score": 1},
            {"name": "Team B", "score": 3}
        ],
        "date": ISODate("2023-06-09T00:00:00Z")
    },
    {
        "_id": ObjectId(),
        "match_id": "002",
        "sport": "American Football",
        "teams": [
            {"name": "Team A", "touchdowns": 3, "field_goals": 2, "safeties": 0, "two_point_conversions": 1, "extra_points": 2},
            {"name": "Team B", "touchdowns": 2, "field_goals": 1, "safeties": 1, "two_point_conversions": 0, "extra_points": 2}
        ],
        "date": ISODate("2023-06-10T00:00:00Z")
    },
    //... similar documents for other sports
    {
        "_id": ObjectId(),
        "match_id": "018",
        "sport": "Kickboxing",
        "fighters": [
            {"name": "Fighter A", "knockouts": 0, "points": 30},
            {"name": "Fighter B", "knockouts": 0, "points": 28}
        ],
        "date": ISODate("2023-06-26T00:00:00Z")
    }
]

```
In this model, each match has its own document. The teams or fighters array contains an object for each participant, with fields for their name and scores. Each scoring method (e.g., goals in soccer, touchdowns and field goals in American football, knockouts and points in kickboxing) gets its own field. This design provides the flexibility to adapt to different scoring systems, but also maintains a level of consistency that makes the data easier to work with.

As previously mentioned, this is a basic design and you might want to add more fields depending on your needs. For example, you could include details of each round in combat sports, or details of each set in tennis.

To insert these documents into your collection, you'd use the insertMany method in MongoDB:
```
db.SCORES.insertMany([/*... your documents here ...*/])

```
Remember to replace the placeholders with your actual data. You can also adjust this basic design as necessary to fit your specific use case.

Here's an example of how you could add scoring for Golf, CARJITSU, Major League Paintball, Pro Mini Golf, and Slap Fight Championships. As these sports all have very different scoring methods, the document structure will vary significantly between them:

```
[
    // ... other sports ...

    // Golf
    {
        "_id": ObjectId(),
        "match_id": "019",
        "sport": "Golf",
        "tournament": "The Masters",
        "players": [
            {"name": "Player A", "rounds": [72, 70, 69, 68], "total_score": 279},
            {"name": "Player B", "rounds": [70, 70, 71, 72], "total_score": 283},
            // ... other players ...
        ],
        "date": ISODate("2023-06-28T00:00:00Z")
    },

    // CARJITSU
    {
        "_id": ObjectId(),
        "match_id": "020",
        "sport": "CARJITSU",
        "drivers": [
            {"name": "Driver A", "points": 25},
            {"name": "Driver B", "points": 18},
            // ... other drivers ...
        ],
        "date": ISODate("2023-06-29T00:00:00Z")
    },

    // Major League Paintball
    {
        "_id": ObjectId(),
        "match_id": "021",
        "sport": "Major League Paintball",
        "teams": [
            {"name": "Team A", "flags_captured": 3, "players_eliminated": 5},
            {"name": "Team B", "flags_captured": 2, "players_eliminated": 6},
            // ... other teams ...
        ],
        "date": ISODate("2023-06-30T00:00:00Z")
    },

    // Pro Mini Golf
    {
        "_id": ObjectId(),
        "match_id": "022",
        "sport": "Pro Mini Golf",
        "players": [
            {"name": "Player A", "rounds": [40, 39, 41], "total_score": 120},
            {"name": "Player B", "rounds": [42, 42, 40], "total_score": 124},
            // ... other players ...
        ],
        "date": ISODate("2023-07-01T00:00:00Z")
    },

    // Slap Fight Championships
    {
        "_id": ObjectId(),
        "match_id": "023",
        "sport": "Slap Fight Championships",
        "fighters": [
            {"name": "Fighter A", "knockouts": 1, "points": 20},
            {"name": "Fighter B", "knockouts": 0, "points": 10},
            // ... other fighters ...
        ],
        "date": ISODate("2023-07-02T00:00:00Z")
    }
]
```
Each sport's scoring details are included in an array of players, drivers, teams, or fighters. For example, in Golf, each player's score is represented as an array of their scores for each round and their total score. In Major League Paintball, each team's score includes the number of flags they captured and the number of opposing players they eliminated.

Remember to adapt these examples based on the actual data you want to store. For example, you might want to store more detailed information, such as the details of each round in a fight, or each hole in a golf tournament.

You can add these documents to your MongoDB collection using the insertMany method:

```
db.SCORES.insertMany([/*... your documents here ...*/])
```

If you wish to keep a record of the scores for each individual hole, storing an array of hole objects within the rounds array would be a great approach. Here's how you could modify the Pro Mini Golf document to reflect this:

```
// Pro Mini Golf
{
    "_id": ObjectId(),
    "match_id": "022",
    "sport": "Pro Mini Golf",
    "players": [
        {
            "name": "Player A",
            "rounds": [
                {
                    "round_number": 1,
                    "holes": [
                        {"hole_number": 1, "strokes": 2},
                        {"hole_number": 2, "strokes": 3},
                        // ... other holes ...
                    ],
                    "round_score": 30
                },
                // ... other rounds ...
            ],
            "total_score": 120
        },
        // ... other players ...
    ],
    "date": ISODate("2023-07-01T00:00:00Z")
}
```
This way, you not only record the total score for each round and the whole game but also keep a detailed scorecard for each round. This allows for more in-depth analysis of the game if required. Remember to adjust the strokes field based on the player's actual score for each hole.

Remember to add these documents to your MongoDB collection using the insert or insertMany method:

```
db.SCORES.insert(/*... your document here ...*/)
```
