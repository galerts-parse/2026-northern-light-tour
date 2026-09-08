import json
import subprocess
import urllib.parse

def make_gmaps_url(name, coords=None):
    if coords and len(coords) == 2:
        return f"https://www.google.com/maps/search/?api=1&query={coords[0]},{coords[1]}"
    query = urllib.parse.quote(name)
    return f"https://www.google.com/maps/search/?api=1&query={query}"

# 1. Route A (Baseline)
# 2. Route B (High-Action Nature & Foodie Explorer)

route_a_days = [
    {
      "day": 1,
      "date": "Dec 12 (Sat)",
      "title": "Gateway Arrival & AWD SUV Pickup",
      "location": "Rovaniemi, Finland",
      "coords": [66.5039, 25.7294],
      "gmaps": make_gmaps_url("Rovaniemi Central", [66.5039, 25.7294]),
      "distance": "10 km (15 mins)",
      "hotel": "Arctic Light Hotel (Recommended) / Santa's Hotel Santa Claus",
      "hotelStatus": "pending",
      "bookingRef": "Unconfirmed in Folder - Marriott Homes & Villas available nearby",
      "hotelLinks": [
        {"name": "Arctic Light Hotel", "url": "https://www.arcticlighthotel.es/", "gmaps": make_gmaps_url("Arctic Light Hotel Rovaniemi")},
        {"name": "Santa's Hotel Santa Claus", "url": "https://santashotels.fi/en/hotels/hotel-santa-claus-rovaniemi/", "gmaps": make_gmaps_url("Santa's Hotel Santa Claus Rovaniemi")}
      ],
      "activities": "Fly SIN -> MUC -> RVN (Arrive 5:15 PM); pick up AWD SUV rental; evening walk in central Rovaniemi; dinner at Nili / Gustav.",
      "scheduleNotes": "Gateway Arrival & AWD SUV Pickup",
      "tags": ["Flight Arrival", "SUV Rental Pickup", "Rovaniemi Dinner"],
      "foodGuide": {
        "good": {"name": "Restaurant Nili", "desc": "Gourmet Lapland reindeer & Arctic char", "cost": "~€55", "gmaps": make_gmaps_url("Restaurant Nili Rovaniemi")},
        "cheap": {"name": "Ravintola Roka Street Bistro", "desc": "Famous Finnish salmon soup & Lapland burgers", "cost": "€12-€16", "gmaps": make_gmaps_url("Ravintola Roka Street Bistro Rovaniemi")}
      },
      "hourlySchedule": [
        {"time": "17:15 - 18:00", "activity": "Land at Rovaniemi Airport (RVN), clear passport control & baggage claim.", "gmaps": make_gmaps_url("Rovaniemi Airport")},
        {"time": "18:00 - 18:30", "activity": "Pick up AWD SUV rental at airport desk; verify winter tires & safety kit.", "gmaps": make_gmaps_url("Rovaniemi Airport Hertz")},
        {"time": "18:30 - 18:50", "activity": "Drive 10 km south on E75 to central Rovaniemi hotel.", "gmaps": make_gmaps_url("Lordi's Square Rovaniemi")},
        {"time": "19:30 - 21:30", "activity": "Dinner at Restaurant Nili or Ravintola Roka Street Bistro.", "gmaps": make_gmaps_url("Restaurant Nili Rovaniemi")},
        {"time": "21:30 - 22:30", "activity": "Stroll around Lordi Square & Lumberjack's Candle Bridge.", "gmaps": make_gmaps_url("Lumberjack's Candle Bridge Rovaniemi")}
      ],
      "drivingLegs": [
        {"from": "RVN Airport", "to": "Rovaniemi Center", "dist": "10 km", "time": "15 mins", "route": "Highway E75", "gmaps": make_gmaps_url("Rovaniemi Airport to Lordi Square")}
      ],
      "ticketCosts": [
        {"item": "AWD SUV Rental Day 1", "cost": "~€75/day", "url": "https://www.hertz.fi/"},
        {"item": "Lapland Dinner at Nili", "cost": "~€55/pax", "url": "https://nili.fi/en/"}
      ],
      "auroraSpots": [
        {"name": "Arktikum Arboretum Shoreline", "desc": "Dark park along Ounasjoki river, 15-min walk from Lordi Square.", "coords": [66.5078, 25.7258], "gmaps": make_gmaps_url("Arktikum Arboretum Rovaniemi", [66.5078, 25.7258])}
      ]
    }
]

# Let's write a python generator to populate all 22 days for both Route A and Route B with Google Maps links!
print("Preparing full dataset build script...")
