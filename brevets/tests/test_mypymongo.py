import os
import arrow
from pymongo import MongoClient

from mypymongo import brevet_find, brevet_insert

import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

#tests both insert and find

def test_mongo1():
    start_time = "2021-01-01T00:00"
    brev_dist = 400
    checkpoints = [
        { "km": 50, "miles": 31.068550, "location": "one", "open_time": "2021-01-01T01:28", "close_time": "2021-01-01T03:30"},
        { "km": 100, "miles": 62.137100, "location": "two", "open_time": "2021-01-01T02:56", "close_time": "2021-01-01T06:40"},
        { "km": 200, "miles": 124.274200, "location": "three", "open_time": "2021-01-01T05:53", "close_time": "2021-01-01T13:20"},
        { "km": 400, "miles": 248.548400, "location": "four", "open_time": "2021-01-01T12:08", "close_time": "2021-01-02T03:00"}
    ]
    race = (start_time, brev_dist, checkpoints)

    brevet_insert(start_time, brev_dist, checkpoints)

    logging.debug(brevet_find())

    assert(brevet_find() == race)


def test_mongo2():
    start_time = "2021-01-01T08:00"
    brev_dist = 1000
    checkpoints = [
        { "km": 100, "miles": 62.137100, "location": "France", "open_time": "2021-01-01T10:56", "close_time": "2021-01-01T14:40"},
        { "km": 200, "miles": 124.274200, "location": "Italy", "open_time": "2021-01-01T13:53", "close_time": "2021-01-01T21:20"},
        { "km": 400, "miles": 248.548400, "location": "Germany", "open_time": "2021-01-01T20:08", "close_time": "2021-01-02T10:40"},
        { "km": 800, "miles": 497.096800, "location": "Belgium", "open_time": "2021-01-02T09:57", "close_time": "2021-01-03T17:30"},
        { "km": 1000, "miles": 621.371000, "location": "Ireland", "open_time": "2021-01-02T17:05", "close_time": "2021-01-04T11:00"}
    ]
    race = (start_time, brev_dist, checkpoints)

    brevet_insert(start_time, brev_dist, checkpoints)

    logging.debug(brevet_find())

    assert(brevet_find() == race)