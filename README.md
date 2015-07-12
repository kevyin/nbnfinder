# nbnfinder
Helps you look for properties on the market with NBN

## What this does
From a http://domain.com.au search, it goes through all the addresses and searches them through NBN's 
"Check your address" http://www.nbnco.com.au/connect-home-or-business/check-your-address.html

Features:

* Caches results in Python's Config format
* Use Domain's sort by newest to get updates on your searches

## Missing features (Todo's)
* Doesn't support off the plan buildings
* Won't work if the agent didn't type in the address properly
* Unfortunately opens up Firefox/Chrome in the foreground not background (needs to be ported to ghostdriver)
* Not a website

## How to use

    
```
    # Edit cache.cfg and add the search address as a url

    [new waterloo]
    url = http://www.domain.com.au/search/buy/state/nsw/area/eastern-suburbs/region/sydney-region/suburb/mascot/victoria-park/waterloo/zetland/?bathrooms=1&to=750000&searchterm=2017%3b2020&sort=date-asc


    # Run
    python nbnfinder.py

    # Result
    [new waterloo]
    url = http://www.domain.com.au/search/buy/state/nsw/area/eastern-suburbs/region/sydney-region/suburb/mascot/victoria-park/waterloo/zetland/?bathrooms=1&to=750000&searchterm=2017%3b2020&sort=date-asc
    135/629 gardeners road, mascot = available
    522/1 hutchinson walk, zetland = available
    3102/2 wolseley grove, zetland = no
    1015/20 gadigal ave, zetland = no
    g18/268 pitt street, waterloo = started

```

   
