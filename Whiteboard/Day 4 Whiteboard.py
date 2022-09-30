# Day 4 Whiteboard
#
#
#
#
#
#


# Electric Company
# Create a function that takes a list that represents street lights given as a parameter called(l_street). Determine if an outage has occurred.
# A street with a total number of "F"s greater than or equal to 2 returns "Outage", anything below returns "Power"

# Example Input: [ 'T', 'F', 'F', 'F' ]
# Example Output: "Outage"

# Example Input: [ 'T', 'T', 'F', 'F' ]
# Example Output: "Outage"

# Example Input: [ 'T', 'T', 'T', 'F' ]
# Example Output: "Power"

def power_outage(l_street):
    for l in l_street:
        if l_street.count('F') >= 2:
            return "Outage"
        else:
            return "Power"


power_outage(['T', 'T', 'F', 'F'])
power_outage(['T', 'F', 'F', 'F'])
power_outage(['T', 'T', 'T', 'F'])
