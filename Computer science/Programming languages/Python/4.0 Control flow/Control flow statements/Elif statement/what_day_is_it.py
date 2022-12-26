# Today the whole word uses the Coordinated Universal Time
# (UTC) to disctinguish between the time zones. The UTC is
# considered to be the 0, and the rest of the time zones are
# expressed using positive or negative offsets from the UTC. For,
# instance, London is in the zone UTC+00:00 (or GMT) and
# Moscow is in the zone UTC+3:00.

# There are 14 positive offsets (from UTC+1:00 to UTC+14:00) and
# 12 negative offsets (from-12:00 to UTC-1:00). This also
# means that at a particular hour, three calendar days are
# observed on the planet. For example, if now it's Sunday, 11:30 in
# the morning in Londo, then in the time zone with +14:00 offset
# people are already living in the "next day", Monday, because
# their time is 14 hours ahead of London.

# Your task is stated as follows:

# - the reference time point is Tuesday, 10:30 in the morning
#    in London (UTC+00:00)
# - read the input string containing the number and the sign
#   of this number (for example, +4, -10) . Note, however, that
#   there will be no sign if the number is 0. The number is 
#   always an integer.
# - this number is the offset for some time zone.
# - your program should calculate the day of the week in the
#   time zone for which you were given the offset. The 
#   reference time point for your calculations is mentioned
#   above. 
# - output the day of the week in the given time zone.

# For example, if the input is -11, then, relatively to London, it's
# "the day before" in this time zone, that is, it's still Monday, but if
# the input is +3, then it's Tuesday, the same as in London.

# The input format:
# The value of offset with the sign (e.g. +3 or -9)

# The output format:
# The day of the week in that timezone.

time = input()
if time[0] == '0':
    print("Tuesday")
else:
    if time[0] == '-':    
        if int(time.strip('-')) > 10:
            print("Monday")
        else:
            print("Tuesday")
    elif time[0] == '+':
        if int(time.strip('+')) > 13:       
            print("Wednesday")
        else:
            print("Tuesday")