# CADE - Hap Generated Files

In this folder is 3 subfolders with example data files from Hap and files generated from hap logs.

## Social Platform Files

File(s) in the `social_platform_files` folder are generated when the Hap agent sends acts that are meant to simulate posts to things like facebook and twitter.

Each line has a json object with this format:

```json
{
    "id":"16542744318510.000032",   // ID for data, can change to UUID format
    "platform":"tweeter",           // platform the data is from
    "type":"post",                  // type of data on platform
    "location":"ip_or_geo",         // Origin IP or geolocation
    "content":"Hello Followers! #newtotweeter", // what was written in the post
    "engagement":                   // audience engagement and reactions
    {
        "views":1,
        "shares":2,
        "likes":24,
        "popularity":0.1
    }
}
```

Some changes we discussed in our meeting on June 10th 2022:

```json
{
    "id":"16542744318510.000032",   // ID for data
    "platform":"tweeter",           // platform the data is from
    "type":"post",                  // type of data on platform
    "location":"ip_or_geo",         // Origin IP or geolocation
    "content":"Hello Followers! #newtotweeter", // what was written in the post
    "metadata":                     // other detail on the social media data
    {                               //  metadata fields can be specific to platform/type
        "tags": ["#newtotweeter"],  // tags on data, could also be @'s, etc.
        "views":1,
        "shares":2,
        "likes":24,
        "popularity":0.1
    }
}
```

## Hap ABT Trace Files

File(s) in the `abt_trace_logs` folder are generated when the Hap agent runs. This is a log of the behavior tree of the agent as it runs. This is used to generate the cade analysis files

Each line has a json object with this format:

```json
{
    "timestep":2,                           // time step of agent
    "time_utc":"2022-06-10T18:11:58.623Z",  // UTC time of step
    "id":"356648b6-6b1c-4a2c-9ce5-c3028e36d6fd",    // agent id
    "name":"cade_multirun_campaigns_02_1",  // agent name
    "globals":[                             // agent global variables
        {"organization_id":""},
        {"maxLoops":"15"},
        {"curLoop":""},
        {"audience":""},
        {"observed_success":""}
        ],
    "node_tree":{                           // top level node in agent behavior tree
        "uuid":"81ad7e45-9f4a-44e4-8936-6b30e8dc24c9",
        "name":"cade_multirun_campaigns_02_1",
        "type":"ABTRoot",
        "status":"active",
        "details":{
            "depth":0,
            "parent":"none",
            "state":"THOUGHT"
            },
        "subnodes":[]                       // any subnodes in tree would be nested here
        }
}
```

## CADE ABT Analysis Files

File(s) in the `cade_abt_analysis` folder are created by running a tool over a `abt_trace_logs` file. The output is something the web frontend can load in. This should match the scenario file format for the current frontend.

Each line has a json object with this format:

```json
{
    "id": "cade_multirun_campaigns_0",
    "actors": [
        {
            "id": "1f52fae9-9d80-4998-b9c4-ea030b075bb1",
            "ip_address": "000.0.0.0",
            "latitude": 0,
            "longitude": 0,
            "username": "Data_Actor"
        }
    ],
    "metadata": {           // Frontend data
        "dimensions": {
            "x": {
                "min": 0,
                "max": 1000
            },
            "y": {
                "min": 0,
                "max": 1000
        }
        }
    },
    "nodes": [
        {
            "actor": "example_actor",
            "children": [],
            "id": "2c364e03-512d-46e1-a76d-75a10180877d",
            "label": "Run_All_Campaigns_1_MentalAction",
            "parent": "a2fd8a85-8020-4f59-b415-cfc92a156ab2",
            "type": "ABTMentalAction",
            "probability": 1,
            "x": 0,             // Frontend data
            "y": 0,             // Frontend data
            "z": 12,            // Frontend data
            "opacity": 1,       // Frontend data
            "isSelected": false // Frontend data
        }
    ]
}
```

***
Charles River Analytics, Inc., Cambridge, Massachusetts </br>
Copyright (C) 2022. All Rights Reserved. </br>
See <http://www.cra.com> or email info@cra.com for more information.
