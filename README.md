## Buttercup Home Automation

This project automates lights, thermostats, door locks and other devices in Buttercup.

===
Lights 

Send email notification when lights are on between 2am - 6am [people are sleeping]

Allow people to choose their own room light settings. 
	CASE WHEN DATE = weekday/weekends
	AND TIME is >= 1am
	THEN turn lights off/on IF light IS NOT off 

Enforce default light settings for common areas (all non rooms)
	CASE WHEN DATE = weekday
	AND time is >= 2am
	THEN turn lights off IF light IS NOT off 

===
Thermostat 

Send email notification when thermostat is active between 10am-5pm on weekday [people are at work]

Upstairs
	CASE WHEN DATE = ANY
	AND TIME is >= 8am
	AND TIME is <= 9am
	THEN thermostat to 75 

===


## Kahmanda room

## GC room 


## TJ room 

## Diana room


## Living room 


## Smartswitch1


## Kitchen front


## Kitchen back

