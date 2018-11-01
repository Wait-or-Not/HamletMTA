**To wait or not to wait, that is the question HamletMTA seeks to answer.** 

## Project Aims

Waiting for the bus sucks, you can wait and wait and watch as the ETA on the MTA app pushes further and further away. Can historical data paint a better picture of when buses will actually arrive? There are also large discrepancies depending on what neighborhood you are in, the line you are riding, and the weather conditions. Wouldn’t it be nice to know with some degree of certainty whether a bus will arrive in 5, 10, or 15 minutes?

## Questions we plan to address

1. Based on a ~10 stops/lines how closely do the actual stop times reflect the posted bus schedules and what is the distribution around the scheduled time that busses actually arrive?

2. What environmental factors impact a buses schedule? What impact does time of day, temperature, and weather have?

3. What socioeconomic factors play into a buses schedule? Do we see better or worse availability in neighborhoods with different average incomes?

4. Predicting with a defined degree certainty if a bus is coming within a given time frame

## Our Data

[MTA Schedules](http://web.mta.info/nyct/service/bus/bklnsch.htm#top) (need to figure out best way to scrape or source better structured data)

[MTA Bus Statistics](https://www.kaggle.com/stoney71/new-york-city-transport-statistics)

[Weather.Gov](https://www.weather.gov/okx/CentralParkHistorical) Data from a weather monitor in central park; Each day, a 1:30 am report holds 24 hours of weather data starting at 12:00 am EST the previous day and the reports look like [this](https://forecast.weather.gov/product.php?site=NWS&issuedby=NYC&product=CLI&format=CI&version=1&glossary=1&highlight=off).

### Independent Variables

Scheduled arrival

Weather conditions

Bus line (for comparing lines)

Time of day

### Dependent Variables

Actual arrival time

## How we Use our data

The questions and data that are being explored will help gain insight into the overall punctuality of the MTA bus system. Exploring bus tardiness and modeling arrival times will help to visualize major problem points at particular stops along individual routes or issues with the bus system as a whole. What’s more, the questions we pose will yield useful heuristics for the consumers who use the buses. Given that the bus I’m waiting for has not arrived on time, how likely is it that it will not arrive at all? Knowing distribution of conditional probabilities (given weather conditions, amount of time already waited, etc.) can help provide answers; by incorporating other environmental data, like time of day or weather conditions, more context can be given to arrival times and related tardiness values. 

Ultimately, we would like to describe a methodology where late busses are recognized and the reasons for the lateness can be accounted for by the MTA. On the consumer side, the end goal is to take historical data, the rider’s location, and current environmental factors all into account to recommend whether riders ought to wait for the bus or not. 

