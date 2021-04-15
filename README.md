# MinuteRepeaterHW
A minute repeater that chime the time of day implemented in Python on a Raspberry Pi 4 and 2 servo motors

A minute repeater is a complication in horology. More information about it can be found here: https://en.wikipedia.org/wiki/Minute_repeater

The minute repeater chimes the time in this pattern:
X number of low pitch chime, with X = the hours of the day in the 12-hour clock system (X = hours of the day % 12)
Y number of high pitch chime quickly followed by a low pitch chime, with Y = the number of 15 minutes intervals by the time the minute repeater is ran (Y = minutes of the day / 15)
Z number of high pitch chime, with Z = the number of minutes remaining after the number of 15 minutes intervals have been accounted for (Z = minutes of the day % 15)

For example, at 23:37 or 11:37 PM, X = 11, Y = 2, Z = 7
At 03:13 or 3:13 PM, X = 3, Y = 0, Z = 13
