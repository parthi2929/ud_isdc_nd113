from sample_data import big_tickets
import random

# print("there are", len(big_tickets), "big tickets")
# random_ticket = random.choice(big_tickets)
# print(random_ticket)

def get_popular_tickets(tickets):
    """
    From a list of tickets, fetch all the tickets with 8 or 
    more "watchers". 
    """
    popular_tickets = []

    for each_ticket in tickets:
        if (len(each_ticket['people']['watchers']) >= 8):
            popular_tickets.append(each_ticket)

    return popular_tickets

popular = get_popular_tickets(big_tickets)

# TESTING CODE 
assert( len(popular) > 0 ) # must be at least one popular ticket

for ticket in popular:
    assert( len(ticket['people']['watchers']) >= 8 )
    
print("Nice job! It looks like your function is working.")