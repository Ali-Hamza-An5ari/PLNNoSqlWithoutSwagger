# Pro Mini Golf Tournament Structure DBNoSQL

This document desicropts the structure of the DBNoSQL collections: `LINES`, `MARKETS`, `VENUES`,   `TOURNAMENT_FORMAT`, and `SCORES`.
Note that each of these collections are partitioned by a sport in the SQL database 'Sports' table -- this document has collection information for the sport "Pro Mini Golf" (and when tournament dependent: for "WPL#3")


# Lines
This section describes the structure of the `LINES` collection for the Pro Mini Golf tournament, which includes the details of different betting lines. Each line represents a possible bet that can be placed within the context of this tournament.

## Structure

The `LINES` collection is an array of objects, each representing a specific line. A line object consists of the following properties:

### id
A unique identifier for each line. This will be the id of the document containing "Pro Mini Golf" lines.

### sport
The sport to which the line belongs, in this case, "Pro Mini Golf".

### lines
An array that includes information about the tournament and the venue, including:

#### tournamentID
A reference to the ID of the tournament in the SQL database.

#### venueID
A reference to the ID of the venue in SQL and NoSQL database.

#### markets
An array of markets available for betting. Each market object has the following properties:

##### market
A unique identifier for each market -- references MARKETS collection for the same sport.

##### marketLines
An array of market lines
*Note that lines associated with a given 'market' from the MARKETS collection will have differing properties based on the `market` the line belongs to. For example, for WPL#3 ToFinishTopX `market` "001", lines have the following properties:

- `lineID`: A unique identifier for each market line.
- `teamID`: A reference to the ID of the team in SQL database.
- `teamName`: The name of the team.
- `toFinishTop`: Indicates the number of positions from the top (i.e. 1 means Outright Winner) team needs to finish in for the bet to be a winner.
- `betDescription`: A text description of the bet.
- `round`: The round for which the line applies. If null, the line applies to all rounds.
- `price`: The odds offered for the line.
- `startTime`: The start time of the line or the event it refers to.
- `status`: The status of the line (e.g., 'pending', 'graded', 'cancelled', 'live').
- `result`: The result of the line if it has been graded.

When `market` is "002", the following properties are used:

- `lineID`: A unique identifier for each market line.
- `teamID`: A reference to the ID of the team in SQL database, if applicable -- if null it is for the entire team field.
- `teamName`: The name of the team or player, if applicable.
- `round`: The round for which the line applies. If null, the line applies to all rounds.
- `holes`: The specific hole or holes to which the line applies. If null, the line applies to all holes.
- `strokes`: The number of strokes for which the line applies (e.g. 1 for hole in 1, 2 for par, 3 for bogey, etc.).
- `side`: The side of the bet ('Over' or 'Under').
- `line`: The Over/Under line value.
- `price`: The odds offered for the line.
- `startTime`: The start time of the line or the event it refers to.
- `status`: The status of the line (e.g., 'pending', 'graded', 'cancelled', 'live').
- `result`: The result of the line if it has been graded (either 'over' or 'under').


## Example

Here is an example of how to structure a line object:
***note that the "..." indicate that other lines can be added in a similar manner***
```json
{
    "id": "",
    "sport": "Pro Mini Golf",
    "lines": [
        {
            "tournamentID": "foreign reference key ID here",
            "venueID": "foreign reference key ID here",
            "markets": [
                {
                    "market": "001",
                    "marketLines": [
                        {
                            "lineID": "001",
                            "teamID": "foreign reference key ID here",
                            "teamName": "Greg Newport",
                            "toFinishTop": 1,
                            "betDescription": "Outright Winner",
                            "round": null,
                            "price": 400,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "002",
                            "teamID": "foreign reference key ID here",
                            "teamName": "Gary English",
                            "toFinishTop": 1,
                            "betDescription": "Outright Winner",
                            "round": null,
                            "price": 400,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "003",
                            "teamID": "foreign reference key ID here",
                            "teamName": "Joey Graybeal",
                            "toFinishTop": 1,
                            "betDescription": "Outright Winner",
                            "round": null,
                            "price": 550,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "004",
                            "teamID": "foreign reference key ID here",
                            "teamName": "Randy Reeves",
                            "toFinishTop": 1,
                            "betDescription": "Outright Winner",
                            "round": null,
                            "price": 600,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "005",
                            "teamID": "foreign reference key ID here",
                            "teamName": "Tony Varnadore",
                            "toFinishTop": 1,
                            "betDescription": "Outright Winner",
                            "round": null,
                            "price": 800,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "006",
                            "teamID": "foreign reference key ID here",
                            "teamName": "Field",
                            "toFinishTop": 1,
                            "betDescription": "Outright Winner",
                            "round": null,
                            "price": 120,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        }
                    ]
                    ...
                },
                {
                    "market": "002",
                    "marketLines": [
                        {
                            "lineID": "007",
                            "description": "Hole #4 Round 1 and Final Round Over 9.5",
                            "teamID": null,
                            "teamName": null,
                            "round": null,
                            "holes": "4",
                            "strokes": "9.5",
                            "side": "Over",
                            "line": 9.5,
                            "price": -150,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "008",
                            "description": "Hole #4 Round 1 and Final Round Under 9.5",
                            "teamID": null,
                            "teamName": null,
                            "round": null,
                            "holes": "4",
                            "strokes": "9.5",
                            "side": "Under",
                            "line": 9.5,
                            "price": 110,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "009",
                            "description": "Hole #8 Round 1 and Final Round Over 0.5",
                            "teamID": null,
                            "teamName": null,
                            "round": null,
                            "holes": "8",
                            "strokes": "0.5",
                            "side": "Over",
                            "line": 0.5,
                            "price": -150,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        },
                        {
                            "lineID": "010",
                            "description": "Hole #8 Round 1 and Final Round Under 0.5",
                            "teamID": null,
                            "teamName": null,
                            "round": null,
                            "holes": "8",
                            "strokes": "0.5",
                            "side": "Under",
                            "line": 0.5,
                            "price": 110,
                            "startTime": "2023-06-26T12:00:00-04:00",
                            "status": "pending",
                            "result": ""
                        }
                        ...
                    ]
                }
            ]
        }
    ]
}
```

## MARKETS Collection

The `markets` collection is an array of market types available for betting partitioned by sport. In the Pro Mini Golf sport, each object in the collection consists of the following properties:

- `marketID`: A unique identifier for each market type.
- `marketType`: A description of the type of betting market (e.g., 'Finish Top X', 'Over / Under Hole Score').

#### Example - MARKETS Collection

```json
{
    "id": "",
    "sport": "",
    "markets": [
        { 
            "marketID": "001",
            "marketType": "Finish Top X"
        },
        { 
            "marketID": "002",
            "marketType": "Over / Under Hole Score"
        },
        { 
            "marketID": "003",
            "marketType": "Over / Under Round Score"
        },
        { 
            "marketID": "004",
            "marketType": "Head to Head"
        }
    ]
}
```

## SCORES Collection
The `SCORES` collection has documents partioned by sport

For `Pro Mini Golf`
##Structure

The `SCORES` collection is an array of objects, each representing team scores for a given tournament

### id
A unique identifier for each document in the `SCORES` collection

### sport
the sport to which the line belongs to, in this case 'Pro Mini Golf' -- connects to SQL sports table

### tournament_id
the tournament that is being scored -- connects to SQL tournaments table

### tournament_name
the tournament that is being scored

### teams
An array of teams competing in the event and their scores. For 'Pro Mini Golf' each teams object has the following properties:

#### id
team id that links to SQL teams table

#### name
team name

#### rounds
an array containing

- round_number
the round number being scored

- holes
an array containing
- - `hole_number`: the hole number that related to hole in VENUE collection for VENUE of event
- - `strokes`: the number of strokes it took the team to complete the hole

- round_score
the score of the team (total strokes) for the round

- thru
the number of holes the team has played

### event_status
the status of the event (e.g., 'pending', 'cancelled', 'live', 'finished')

### event_date
the date of the event

### last_updated
datatime of last update

## Example - SCORES Collection

```json
{
    "id": "",
    "sport": "Pro Mini Golf",
    "event_id": "",
    "event_name": "WPL#3",
    "teams": [
        {
            "id": "",
            "name": "",
            "rounds": [
                {
                    "round_number": "",
                    "holes": [
                        {
                            "hole_number": "",
                            "strokes": ""
                        }
                    ],
                    "round_score": "",
                    "thru": ""
                }
            ]
        }  
    ],
    "event_status": "",
    "event_date": "",
    "last_updated": ""
}
```

## VENUE Collection
Documents are partitioned by sport and holed VENUE information

## Structure - VENUE
### id
A unique identifier for each venue partitioned by sport -- should ma

### sport
The sport that is played at the venue.

### name
The name of the venue -- should link to SQL Venue table

### city
The city where the venue is located.

### state
The state where the venue is located.

### country
The country where the venue is located.

### address
The complete address of the venue.

### description
A brief description of the venue.

### course_par
An object containing details about the course par, including total par for the entire course and 
#### holes, an array of objects each with hole_number and its respective par.

## Example - VENUE
***Note that the "..." would contain other hole data***
```json 
{
    "id": "unique identifier",
    "sport": "Pro Mini Golf",
    "name": "venue name",
    "city": "city name",
    "state": "state name",
    "country": "country name",
    "address": "complete venue address",
    "description": "description about the venue",
    "course_par": {
        "total": 36,
        "holes": [
            {
                "hole_number": 1,
                "par": 2
            },
            ...
        ]
    }
}
```

## TOURNAMENT_FORMAT Collection
The tournament_format collection stores the data related to the format of each tournament. 

## STRUCTURE - TOURNAMENT_FORMAT
Each object in the collection consists of the following properties:

### tournament_id
The unique identifier for the tournament, matching the SQL tournamentId.

### sport
the sport of the tournament, e.g., "Pro Mini Golf".

### name
The name of the tournament, e.g., "WPL#3".

###date
The date the tournament takes place.

### description
A brief description of the tournament's format.

### status
The status of the tournament.

### status_name
A descriptive name of the tournament's status.

## for the WPL#3 tournament there is also the following fields
***Note that TOURNAMENT_FORMAT is partitioned by tournament so each tournament object will have different proerties

### groups
An array of objects, each representing a group in the tournament. Each group object has:
- group_id: Identifier of the group.
- team_ids: Array of team identifiers in the group.
- winner: Identifier of the team that wins the group.

###finals: An object representing the final round of the tournament, which includes:
- team_ids: Array of team identifiers in the finals.
- winner: Identifier of the team that wins the tournament.

## Example - TOURNAMENT_FORMAT

```json
{
    "tournament_id": "matching SQL tournamedId",
    "sport": "Pro Mini Golf",
    "name": "WPL#3",
    "date": "2023-06-23",
    "description": "World Cup format, 4 groups play in round 1 with the winner of each group playng one final round",
    "status": "",
    "status_name": "",
    "groups": [
      {
        "group_id": "A",
        "team_ids": ["", "", ""],
        "winner": ""
      },
      {
        "group_id": "B",
        "team_ids": ["", "", ""],
        "winner": ""
      },
      {
        "group_id": "C",
        "team_ids": ["", "", ""],
        "winner": ""
      },
      {
        "group_id": "D",
        "team_ids": ["", "", ""],
        "winner": ""
      }
    ],
    "finals": {
      "team_ids": [],
      "winner": ""  
    }
```
