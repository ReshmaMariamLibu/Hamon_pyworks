# importing json file
import json
# Import the sqrt function from the math module to compute the square root in the phi coefficient calculation
from math import sqrt

# Load the journal file and return the parsed data as a list of dictionaries
def load_journal(filename):
    with open(filename, 'r') as file: # opens the file in read mode
        data = json.load(file)
    return data


# Computes the correlation between the given event and 'squirrel'
def compute_phi(filename, event):
    journal = load_journal(filename) # Load the journal data
    n00 = n01 = n10 = n11 = 0 # initializes counters the 0
    
# Iterate through each entry in the journal
    for entry in journal:
        event_occurred = event in entry['events'] # Check if the event occurred
        squirrel_occurred = entry['squirrel'] # checks if the squirrel transformation occured

 # Update counters based on the occurrence of the event and squirrel transformation
        if event_occurred and squirrel_occurred:
            n11 += 1
        elif event_occurred and not squirrel_occurred:
            n10 += 1
        elif not event_occurred and squirrel_occurred:
            n01 += 1
        elif not event_occurred and not squirrel_occurred:
            n00 += 1
    
    phi = (n11 * n00 - n10 * n01) / sqrt((n10 + n11) * (n00 + n01) * (n01 + n11) * (n00 + n10)) # calculates the phi coffecient using the assigned formula
    
    return phi # returns the value of phi
    
# Compute correlations for all events and return a dictionary with event correlations."""
def compute_correlations(filename):
    journal = load_journal(filename)  # Load the journal data
    event_correlations = {} # Initialize a dictionary to hold the correlations
    all_events = set(event for entry in journal for event in entry['events'])  # Create a set of all unique events set method is used to avoid duplication of events.
    
# Compute the phi coefficient for each event and store it in the dictionary
    for event in all_events: 
        event_correlations[event] = compute_phi(filename, event)
    return event_correlations

# Find the events with highest positive and negative correlation with 'squirrel'
def diagnose(filename):
    correlations = compute_correlations(filename) # Compute the correlations for all the events
    
    highest_event = max(correlations, key=correlations.get) # finds the event that has the highest correlation with the transformation into a squirrel and .get method is used to retrieve the value associated with a given key. 
    highest_value=correlations[highest_event]
    lowest_event = min(correlations, key=correlations.get) # To retrieve the minimum correlation value for the  previous event
    lowest_value=correlations[lowest_event]
    return highest_event,lowest_event,highest_value,lowest_value


if __name__ == "__main__":
    filename = "journal.json"
# Diagnose to find the most positively and negatively correlated events
    highest_event, lowest_event,highest_value,lowest_value = diagnose(filename)
    print(f"Event most positively correlated with becoming a squirrel: {highest_event},highest correlation value is: {highest_value}")
    print(f"Event most negatively correlated with becoming a squirrel: {lowest_event},lowest correlation value is: {lowest_value}")
