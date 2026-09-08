import json
import urllib.parse
import subprocess

def gmaps(name, lat=None, lng=None):
    if lat and lng:
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
    q = urllib.parse.quote(name)
    return f"https://www.google.com/maps/search/?api=1&query={q}"

# Food Guide Database by City
food_db = {
    "Rovaniemi": {
        "good": {"name": "Restaurant Nili", "desc": "Gourmet Lapland reindeer & Arctic char", "cost": "~€55", "gmaps": gmaps("Restaurant Nili Rovaniemi")},
        "cheap": {"name": "Ravintola Roka Street Bistro", "desc": "Famous Finnish salmon soup & Lapland burgers", "cost": "€12-€16", "gmaps": gmaps("Ravintola Roka Street Bistro Rovaniemi")}
    },
    "Boden": {
        "good": {"name": "Bodensia Restaurant", "desc": "Nordic steak & local fish", "cost": "~320 SEK", "gmaps": gmaps("Quality Hotel Bodensia Restaurant")},
        "cheap": {"name": "Empes Gatukök Boden", "desc": "Legendary Swedish burger & sausage grill shack", "cost": "~85 SEK (€7)", "gmaps": gmaps("Empes Gatukök Boden")}
    },
    "Kiruna": {
        "good": {"name": "Spis Mat & Dryck", "desc": "Boutique Swedish Lapland bistro", "cost": "~350 SEK", "gmaps": gmaps("Spis Kiruna")},
        "cheap": {"name": "Empes Gatukök Kiruna", "desc": "Classic Swedish fast food & grilled burgers", "cost": "~85 SEK (€7)", "gmaps": gmaps("Empes Gatukök Kiruna")}
    },
    "Abisko": {
        "good": {"name": "Abisko Mountain Lodge Restaurant", "desc": "Gourmet regional venison & Arctic fish menu", "cost": "~450 SEK", "gmaps": gmaps("Abisko Mountain Lodge")},
        "cheap": {"name": "STF Abisko Restaurant Krogen", "desc": "Hearty daily lunch buffet & fika", "cost": "~145 SEK (€12)", "gmaps": gmaps("STF Abisko Mountain Station Restaurant")}
    },
    "Kemi": {
        "good": {"name": "Restaurant Lumihiutale", "desc": "Bothnian Bay seafood & sea view dining", "cost": "~€45", "gmaps": gmaps("Restaurant Lumihiutale Kemi")},
        "cheap": {"name": "Sataman Krouvi / Kauppahalli", "desc": "Local Baltic salmon soup & smoked fish", "cost": "€12-€15", "gmaps": gmaps("Sataman Krouvi Kemi")}
    },
    "Posio": {
        "good": {"name": "Naali Lodge Table", "desc": "Local wild game & Lapland berry pairings", "cost": "~€50", "gmaps": gmaps("Naali Lodge Posio")},
        "cheap": {"name": "Ansa Makasiini / S-Market Bakery", "desc": "Cozy local bistro & fresh rye pastries", "cost": "€10-€14", "gmaps": gmaps("Ansa Makasiini Posio")}
    },
    "Iso-Syöte": {
        "good": {"name": "Restaurant Hilltop Iso-Syöte", "desc": "Fell summit panoramic view dining", "cost": "~€55", "gmaps": gmaps("Restaurant Hilltop Iso-Syöte")},
        "cheap": {"name": "Romekievari Pub", "desc": "Cozy fell pub pizza & reindeer burgers", "cost": "€14-€18", "gmaps": gmaps("Romekievari Iso-Syöte")}
    },
    "Helsinki": {
        "good": {"name": "Restaurant Savotta / Version Eatery", "desc": "Traditional Finnish feast / Autograph bistro", "cost": "~€55", "gmaps": gmaps("Restaurant Savotta Helsinki")},
        "cheap": {"name": "Vanha Kauppahalli (SOUP+MORE)", "desc": "Famous Finnish creamy salmon soup (Lohikeitto)", "cost": "€12", "gmaps": gmaps("SOUP+MORE Vanha Kauppahalli Helsinki")}
    },
    "Tallinn": {
        "good": {"name": "Rataskaevu 16 / Restaurant V", "desc": "Boutique Old Town Estonian cuisine", "cost": "~€30-€40", "gmaps": gmaps("Rataskaevu 16 Tallinn")},
        "cheap": {"name": "Kompressor Pancake Pub", "desc": "LEGENDARY giant sweet & savory pancake pub", "cost": "€6-€8", "gmaps": gmaps("Kompressor Tallinn")}
    },
    "Stockholm": {
        "good": {"name": "Restaurant Pelikan / Tradition", "desc": "Classic Swedish Husmanskost meatballs", "cost": "~320 SEK", "gmaps": gmaps("Restaurant Pelikan Stockholm")},
        "cheap": {"name": "Östermalms Saluhall (Lisaköket)", "desc": "Fresh Toast Skagen & local fish soup", "cost": "~140 SEK (€12)", "gmaps": gmaps("Ostermalms Saluhall Stockholm")}
    },
    "Copenhagen": {
        "good": {"name": "Restaurant Höst / Marv & Ben", "desc": "Award-winning New Nordic dining", "cost": "~450 DKK", "gmaps": gmaps("Restaurant Host Copenhagen")},
        "cheap": {"name": "Torvehallerne (Hallernes Smørrebrød)", "desc": "Traditional Danish open-faced sandwiches & DØP Hot Dog", "cost": "€8-€12", "gmaps": gmaps("Torvehallerne Copenhagen")}
    }
}

# Baseline 22 Days Base Template
base_22_days = [
  {
    "day": 1, "date": "Dec 12 (Sat)", "title_a": "Gateway Arrival & AWD SUV Pickup", "title_b": "Ounasvaara Sunset Forest Walk & Gateway Arrival",
    "location": "Rovaniemi, Finland", "coords": [66.5039, 25.7294], "distance": "10 km (15 mins)",
    "hotel": "Arctic Light Hotel (Recommended) / Santa's Hotel Santa Claus", "hotelStatus": "pending", "bookingRef": "Unconfirmed in Folder",
    "hotelLinks": [{"name": "Arctic Light Hotel", "url": "https://www.arcticlighthotel.es/", "gmaps": gmaps("Arctic Light Hotel Rovaniemi")}],
    "food": food_db["Rovaniemi"],
    "activities_a": "Fly SIN -> MUC -> RVN (Arrive 5:15 PM); pick up AWD SUV rental; evening walk in central Rovaniemi; dinner at Nili / Gustav.",
    "activities_b": "Fly SIN -> MUC -> RVN (Arrive 5:15 PM); pick up AWD SUV rental; Ounasvaara Winter Forest Walk overlooking frozen Kemijoki river; dinner at Ravintola Roka Street Bistro.",
    "sched_a": [
      {"time": "17:15 - 18:00", "activity": "Land at RVN Airport, clear baggage claim.", "gmaps": gmaps("Rovaniemi Airport")},
      {"time": "18:00 - 18:30", "activity": "Pick up AWD SUV rental desk.", "gmaps": gmaps("Rovaniemi Airport Hertz")},
      {"time": "19:30 - 21:30", "activity": "Dinner at Restaurant Nili or Ravintola Roka.", "gmaps": gmaps("Restaurant Nili Rovaniemi")}
    ],
    "sched_b": [
      {"time": "17:15 - 18:00", "activity": "Land at RVN Airport, clear baggage claim.", "gmaps": gmaps("Rovaniemi Airport")},
      {"time": "18:00 - 18:30", "activity": "Pick up AWD SUV rental desk.", "gmaps": gmaps("Rovaniemi Airport Hertz")},
      {"time": "18:45 - 19:45", "activity": "Ounasvaara Winter Trail walk to observation tower (Kemijoki river view).", "gmaps": gmaps("Ounasvaara Lookout Tower Rovaniemi", 66.5080, 25.7600)},
      {"time": "20:00 - 21:30", "activity": "Dinner at Ravintola Roka Street Bistro.", "gmaps": gmaps("Ravintola Roka Street Bistro Rovaniemi")}
    ],
    "legs": [{"from": "RVN Airport", "to": "Rovaniemi Center", "dist": "10 km", "time": "15 mins", "route": "E75", "gmaps": gmaps("Rovaniemi Airport to Lordi Square")}],
    "tickets": [{"item": "SUV Rental Day 1", "cost": "~€75/day", "url": "https://www.hertz.fi/"}],
    "aurora": [{"name": "Arktikum Arboretum Shoreline", "desc": "Dark park along river.", "coords": [66.5078, 25.7258], "gmaps": gmaps("Arktikum Arboretum Rovaniemi", 66.5078, 25.7258)}]
  },
  {
    "day": 2, "date": "Dec 13 (Sun)", "title_a": "Sweden Border Crossing & Torne Valley", "title_b": "Gammelstad UNESCO Church Town Snow Walk & Torne Valley",
    "location": "Harads / Storklinten, Sweden", "coords": [65.8252, 21.6886], "distance": "235 km (2h 45m)",
    "hotel": "Stuga i Storklinten (Boden)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Check-in 13 Dec - Check-out 15 Dec)",
    "food": food_db["Boden"],
    "activities_a": "Drive west through Torne Valley; cross border at Tornio-Haparanda; stop at frozen Kukkolankoski rapids; check into cabin; sauna & dinner.",
    "activities_b": "Drive west through Torne Valley; cross border at Tornio-Haparanda; stop at Kukkolankoski rapids; Gammelstad Church Town UNESCO walking loop (400 medieval cottage village); Storklinten sauna & Empes Gatukök fast food.",
    "sched_a": [
      {"time": "09:00 - 10:30", "activity": "Drive Rovaniemi to Tornio border (125 km).", "gmaps": gmaps("Tornio Border Crossing")},
      {"time": "10:30 - 11:30", "activity": "Stop at Kukkolankoski frozen rapids.", "gmaps": gmaps("Kukkolankoski Rapids")},
      {"time": "14:00 - 15:30", "activity": "Check into Stuga i Storklinten.", "gmaps": gmaps("Storklinten Ski Resort")}
    ],
    "sched_b": [
      {"time": "08:30 - 10:00", "activity": "Drive Rovaniemi to Tornio border (125 km).", "gmaps": gmaps("Tornio Border Crossing")},
      {"time": "10:00 - 11:15", "activity": "Walk Kukkolankoski frozen rapids suspension bridge.", "gmaps": gmaps("Kukkolankoski Rapids")},
      {"time": "11:45 - 13:30", "activity": "Explore Gammelstad Church Town UNESCO medieval walking loop.", "gmaps": gmaps("Gammelstad Church Town Luleå", 65.6458, 22.0289)},
      {"time": "13:30 - 14:15", "activity": "Lunch at Empes Gatukök Boden.", "gmaps": gmaps("Empes Gatukök Boden")},
      {"time": "15:00 - 16:30", "activity": "Check into Stuga i Storklinten & prepare cabin.", "gmaps": gmaps("Storklinten Ski Resort")},
      {"time": "16:30 - 18:30", "activity": "Outdoor Storklinten illuminated ski slopes / toboggan hill & dusk snow walk.", "gmaps": gmaps("Storklinten Slopes", 65.8252, 21.6886)},
      {"time": "18:30 - 20:30", "activity": "Traditional Swedish wood-fired sauna & snow plunge + cabin dinner.", "gmaps": gmaps("Storklinten Sauna")},
      {"time": "21:00 - 00:00", "activity": "Self-drive Aurora Hunt at Storklinten Fell Top (3 mins drive) or Bodträsket Lake (10 mins drive).", "gmaps": gmaps("Storklinten Fell", 65.8252, 21.6886)}
    ],
    "legs": [{"from": "Rovaniemi", "to": "Storklinten", "dist": "235 km", "time": "2h 45m", "route": "E75 & Route 99", "gmaps": gmaps("Rovaniemi to Storklinten")}],
    "tickets": [{"item": "Kukkolankoski Rapids", "cost": "Free", "url": "https://www.kukkolaforsen.se/"}],
    "aurora": [{"name": "Storklinten Fell Top", "desc": "High vantage point above pine canopy (3 mins drive).", "coords": [65.8252, 21.6886], "gmaps": gmaps("Storklinten Fell", 65.8252, 21.6886)}, {"name": "Bodträsket Lake Shore", "desc": "Dark frozen lake vista (10 mins drive north).", "coords": [65.8800, 21.7200], "gmaps": gmaps("Bodtrasket Lake", 65.8800, 21.7200)}]
  },
  {
    "day": 3, "date": "Dec 14 (Mon)", "title_a": "Zero-Driving Rest & Nature Day", "title_b": "Storklinten Fell-Top Snowshoe Trek & Forest Trail",
    "location": "Harads / Storklinten, Sweden", "coords": [65.8252, 21.6886], "distance": "0 km (0h - Rest Day)",
    "hotel": "Stuga i Storklinten (Boden)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Night 2 of 2)",
    "food": food_db["Boden"],
    "activities_a": "Arctic wellness & snow day; outdoor snowshoeing / cross-country skiing; wood-fired saunas & cold plunge; night aurora watching.",
    "activities_b": "Storklinten Fell-Top Snowshoe Trek & Forest Trail; Treehotel Harads forest walk; wood-fired saunas & cold plunge; night aurora photo hunt from fell clearings.",
    "sched_a": [
      {"time": "10:30 - 13:00", "activity": "Snowshoeing through pine forests.", "gmaps": gmaps("Storklinten Trails")},
      {"time": "15:00 - 18:00", "activity": "Wood-fired sauna & cold plunge.", "gmaps": gmaps("Storklinten Sauna")},
      {"time": "21:00 - 00:00", "activity": "Night aurora watching.", "gmaps": gmaps("Storklinten Fell")}
    ],
    "sched_b": [
      {"time": "10:00 - 13:00", "activity": "Storklinten Fell-Top Snowshoe Trek / XC skiing (trails right outside cabin door).", "gmaps": gmaps("Storklinten Summit Trail", 65.8252, 21.6886)},
      {"time": "13:30 - 15:30", "activity": "Optional excursion: Harads Treehotel architectural forest walk & lunch at Brittas Pensionat (15 mins drive).", "gmaps": gmaps("Treehotel Harads Sweden", 65.8252, 20.9542)},
      {"time": "16:00 - 18:30", "activity": "Outdoor wood-fired sauna & Arctic snow plunge at Stortklinten.", "gmaps": gmaps("Storklinten Sauna")},
      {"time": "21:00 - 00:00", "activity": "Aurora photo hunt from fell summit clearings (0-500m walk from cabin).", "gmaps": gmaps("Storklinten Fell")}
    ],
    "legs": [{"from": "Cabin", "to": "Trails", "dist": "0 km", "time": "0 mins", "route": "Walk", "gmaps": gmaps("Storklinten Trails")}],
    "tickets": [{"item": "Snowshoe Rental Day", "cost": "~200 SEK", "url": "https://storklinten.se/"}],
    "aurora": [{"name": "Storklinten Fell Summit Clearings", "desc": "Right outside cabin door (0-500m walk).", "coords": [65.8252, 21.6886], "gmaps": gmaps("Storklinten Fell")}]
  },
  {
    "day": 4, "date": "Dec 15 (Tue)", "title_a": "ICEHOTEL 37 Opening Week & Sámi Reindeer", "title_b": "Luossavaara Peak Sunrise Viewpoint & ICEHOTEL 37",
    "location": "Jukkasjärvi / Kiruna, Sweden", "coords": [67.8557, 20.2253], "distance": "280 km (3h 30m)",
    "hotel": "Northernlight cabin (Kiruna)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Check-in 15 Dec)",
    "food": food_db["Kiruna"],
    "activities_a": "Drive north across Swedish Lapland tundra; tour freshly opened ICEHOTEL 37 hand-carved ice art suites; Icebar drink; Nutti Sámi Siida reindeer feeding.",
    "activities_b": "Luossavaara Peak Sunrise Viewpoint & Kiruna iron mine panorama; ICEHOTEL 37 art suites & Icebar; Nutti Sámi Siida reindeer trek; Spis Mat & Dryck / Empes Gatukök dinner.",
    "sched_a": [
      {"time": "08:30 - 12:00", "activity": "Drive Storklinten to Jukkasjärvi (280 km).", "gmaps": gmaps("Storklinten to Jukkasjarvi")},
      {"time": "12:15 - 14:30", "activity": "Tour ICEHOTEL 37 art suites & Icebar.", "gmaps": gmaps("ICEHOTEL Sweden")},
      {"time": "14:45 - 16:30", "activity": "Nutti Sámi Siida reindeer feeding.", "gmaps": gmaps("Nutti Sami Siida")}
    ],
    "sched_b": [
      {"time": "08:00 - 11:30", "activity": "Drive Storklinten to Kiruna Luossavaara peak trail (270 km).", "gmaps": gmaps("Luossavaara Kiruna", 67.8700, 20.2100)},
      {"time": "11:30 - 12:30", "activity": "Luossavaara Peak summit hike overlooking Kiruna tundra & iron mine.", "gmaps": gmaps("Luossavaara Peak Viewpoint", 67.8700, 20.2100)},
      {"time": "13:00 - 15:15", "activity": "Tour ICEHOTEL 37 art suites & Icebar in Jukkasjärvi.", "gmaps": gmaps("ICEHOTEL Sweden")},
      {"time": "15:30 - 17:00", "activity": "Nutti Sámi Siida reindeer trek & campfire fika.", "gmaps": gmaps("Nutti Sami Siida")},
      {"time": "19:00 - 21:00", "activity": "Dinner at Spis Kiruna or Empes Gatukök.", "gmaps": gmaps("Spis Kiruna")}
    ],
    "legs": [{"from": "Storklinten", "to": "Jukkasjärvi", "dist": "280 km", "time": "3h 30m", "route": "E10", "gmaps": gmaps("Storklinten to Jukkasjarvi")}],
    "tickets": [{"item": "ICEHOTEL Day Ticket", "cost": "~349 SEK", "url": "https://www.icehotel.com/"}, {"item": "Nutti Sámi Siida", "cost": "~220 SEK", "url": "https://nuttisami.se/"}],
    "aurora": [{"name": "Aptasvaara Mountain Lookout", "desc": "15 mins south of Kiruna.", "coords": [67.8100, 20.3500], "gmaps": gmaps("Aptasvaara Mountain", 67.8100, 20.3500)}]
  },
  {
    "day": 5, "date": "Dec 16 (Wed)", "title_a": "Abisko National Park & Aurora Sky Station Night 1", "title_b": "Abisko Canyon Marble Gorge & Frozen Waterfall Trek",
    "location": "Abisko / Björkliden, Sweden", "coords": [68.4064, 18.6811], "distance": "100 km (1h 15m)",
    "hotel": "Aurora View Apt – Walk to Train & Ski (Björkliden)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Ref: HM2B8KDQ4H (Host: Renberget)",
    "food": food_db["Abisko"],
    "activities_a": "Scenic mountain drive along Lake Torneträsk; explore Abisko Canyon frozen waterfalls; night chairlift ride to mountaintop Aurora Sky Station.",
    "activities_b": "Abisko Canyon Marble Gorge & Frozen Waterfall snow trek; Lake Torneträsk shoreline walk; mountaintop Aurora Sky Station night chairlift.",
    "sched_a": [
      {"time": "10:00 - 11:15", "activity": "Drive Kiruna to Abisko (100 km).", "gmaps": gmaps("Kiruna to Abisko")},
      {"time": "11:30 - 13:30", "activity": "Explore Abisko Canyon waterfalls.", "gmaps": gmaps("Abisko Canyon")},
      {"time": "20:00 - 23:30", "activity": "Aurora Sky Station chairlift ride.", "gmaps": gmaps("Aurora Sky Station Abisko")}
    ],
    "sched_b": [
      {"time": "09:30 - 10:45", "activity": "Scenic E10 mountain drive past Lake Torneträsk (100 km).", "gmaps": gmaps("Lake Tornetrask Scenic Viewpoint")},
      {"time": "11:00 - 13:30", "activity": "Abisko Canyon Marble Gorge & frozen waterfall snow trek.", "gmaps": gmaps("Abisko National Park Canyon", 68.3600, 18.7800)},
      {"time": "14:00 - 15:30", "activity": "Check into Aurora View Apt Björkliden.", "gmaps": gmaps("Bjorkliden Sweden")},
      {"time": "20:00 - 23:30", "activity": "Mountaintop Aurora Sky Station night chairlift ride.", "gmaps": gmaps("Aurora Sky Station Abisko")}
    ],
    "legs": [{"from": "Kiruna", "to": "Björkliden", "dist": "100 km", "time": "1h 15m", "route": "E10", "gmaps": gmaps("Kiruna to Bjorkliden")}],
    "tickets": [{"item": "Aurora Sky Station Chairlift", "cost": "~895 SEK", "url": "https://www.stfturist.se/en/explore/aurora-sky-station/"}],
    "aurora": [{"name": "Mount Nuolja Sky Station Summit", "desc": "World famous Blue Hole elevation view.", "coords": [68.3614, 18.7208], "gmaps": gmaps("Mount Nuolja Summit", 68.3614, 18.7208)}]
  },
  {
    "day": 6, "date": "Dec 17 (Thu)", "title_a": "Zero-Driving Alpine Tundra & Aurora Blue Hole Night 2", "title_b": "Kårsavagge Frozen Valley Snowmobile & Lapporten Alpine Trek",
    "location": "Abisko / Björkliden, Sweden", "coords": [68.4064, 18.6811], "distance": "0 km (0h - Rest Day)",
    "hotel": "Aurora View Apt – Walk to Train & Ski (Björkliden)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Ref: HM2B8KDQ4H (Night 2 of 3)",
    "food": food_db["Abisko"],
    "activities_a": "Guided alpine snowmobile safari across mountain passes toward Norwegian border (Riksgränsen); Lapporten valley views; night aurora watch.",
    "activities_b": "Guided Kårsavagge Frozen Valley Snowmobile Expedition & Silverfallet frozen waterfall trek; STF Abisko visitor center & Lake Torneträsk night aurora watch.",
    "sched_a": [
      {"time": "10:00 - 13:00", "activity": "3-hour snowmobile safari.", "gmaps": gmaps("Abisko Snowmobile Base")},
      {"time": "20:30 - 23:30", "activity": "Lake Torneträsk aurora watch.", "gmaps": gmaps("Lake Tornetrask Shore")}
    ],
    "sched_b": [
      {"time": "09:30 - 13:30", "activity": "Kårsavagge Frozen Valley snowmobile expedition toward Lapporten U-valley & Riksgränsen.", "gmaps": gmaps("Karsavagge Valley Abisko", 68.3300, 18.6000)},
      {"time": "14:00 - 15:30", "activity": "Warm lunch at Björkliden Hotel Fjället.", "gmaps": gmaps("Hotel Fjallet Bjorkliden")},
      {"time": "15:30 - 17:00", "activity": "Silverfallet (Rakkasjokk) Frozen Waterfall Walk & dawning twilight photo trek down to Lake Torneträsk ice.", "gmaps": gmaps("Silverfallet Waterfall Bjorkliden", 68.4100, 18.6700)},
      {"time": "17:15 - 18:45", "activity": "STF Abisko Turiststation Arctic climate exhibition & cozy fireside fika.", "gmaps": gmaps("STF Abisko Turiststation", 68.3600, 18.7800)},
      {"time": "19:00 - 20:30", "activity": "Panoramic dinner at Hotel Fjället / Abisko Mountain Lodge.", "gmaps": gmaps("Abisko Mountain Lodge", 68.3500, 18.7900)},
      {"time": "20:30 - 23:30", "activity": "Self-drive aurora hunt to Lake Torneträsk beach parking (E10 km 115).", "gmaps": gmaps("Lake Tornetrask Beach Parking E10", 68.3500, 18.8000)}
    ],
    "legs": [{"from": "Björkliden", "to": "Trails", "dist": "0 km", "time": "0 mins", "route": "Snowmobile", "gmaps": gmaps("Bjorkliden Base")}],
    "tickets": [{"item": "Snowmobile Safari (3h)", "cost": "~1,950 SEK", "url": "https://abiskoguesthouse.com/"}],
    "aurora": [{"name": "Lake Torneträsk Beach Layby", "desc": "Wide open vista facing north over lake.", "coords": [68.3500, 18.8000], "gmaps": gmaps("Lake Tornetrask Beach Layby", 68.3500, 18.8000)}]
  },
  {
    "day": 7, "date": "Dec 18 (Fri)", "title_a": "Zero-Driving Husky Safari & Peak Aurora Night 3", "title_b": "Trollsjön (Rissájaure) Canyon Snowshoe & Husky Safari",
    "location": "Abisko / Björkliden, Sweden", "coords": [68.4064, 18.6811], "distance": "0 km (0h - Rest Day)",
    "hotel": "Aurora View Apt – Walk to Train & Ski (Björkliden)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Ref: HM2B8KDQ4H (Night 3 of 3)",
    "food": food_db["Abisko"],
    "activities_a": "Morning 3-hour husky sledding safari through Arctic birch forest; visit Silverfallet frozen waterfall beach; dinner at Abisko Mountain Lodge; night aurora watch.",
    "activities_b": "Morning 3-hour husky sledding safari; Trollsjön (Rissájaure) Canyon Valley snowshoe hike; Silverfallet frozen waterfall beach walk; Abisko Mountain Lodge dinner.",
    "sched_a": [
      {"time": "09:00 - 12:30", "activity": "Husky sledding safari.", "gmaps": gmaps("Visit Abisko Husky Base")},
      {"time": "15:00 - 16:30", "activity": "Silverfallet waterfall beach.", "gmaps": gmaps("Silverfallet Waterfall")},
      {"time": "18:30 - 20:30", "activity": "Abisko Mountain Lodge dinner.", "gmaps": gmaps("Abisko Mountain Lodge")}
    ],
    "sched_b": [
      {"time": "09:00 - 12:00", "activity": "Morning 3-hour husky sledding safari through Arctic birch forest.", "gmaps": gmaps("Visit Abisko Husky Base")},
      {"time": "12:30 - 15:30", "activity": "Trollsjön (Rissájaure) canyon valley snowshoe trek & Silverfallet frozen waterfall beach.", "gmaps": gmaps("Silverfallet Rakkasjokk", 68.4000, 18.6300)},
      {"time": "18:30 - 20:30", "activity": "Gourmet dinner at Abisko Mountain Lodge.", "gmaps": gmaps("Abisko Mountain Lodge")}
    ],
    "legs": [{"from": "Björkliden", "to": "Silverfallet", "dist": "5 km", "time": "8 mins", "route": "E10", "gmaps": gmaps("Bjorkliden to Silverfallet")}],
    "tickets": [{"item": "Husky Safari (3h)", "cost": "~2,500 SEK", "url": "https://visitabisko.com/"}],
    "aurora": [{"name": "Björkliden Overlook Layby", "desc": "Elevated panorama over lake & Lapporten.", "coords": [68.4064, 18.6811], "gmaps": gmaps("Bjorkliden Overlook", 68.4064, 18.6811)}]
  },
  {
    "day": 8, "date": "Dec 19 (Sat)", "title_a": "Finland Re-entry & SnowCastle of Kemi", "title_b": "Bothnian Bay Sea-Ice Trail & SnowCastle of Kemi",
    "location": "Kemi, Finland", "coords": [65.7363, 24.5637], "distance": "340 km (4h 00m)",
    "hotel": "Cozy Apartment by the Sea 2 Rooms (Kemi)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Check-in 19 Dec - Check-out 21 Dec)",
    "food": food_db["Kemi"],
    "activities_a": "Cross-border drive south to Finnish Bothnian coast; cross border at Tornio; check in; explore SnowExperience365 indoor ice castle and ice bar.",
    "activities_b": "Cross-border drive south; Bothnian Bay Sea-Ice Trail walk onto thick frozen sea ice (Free public access); SnowExperience365 ice castle; Sataman Krouvi salmon soup dinner.",
    "sched_a": [
      {"time": "08:30 - 12:30", "activity": "Drive Björkliden to Kemi (340 km).", "gmaps": gmaps("Bjorkliden to Kemi")},
      {"time": "15:30 - 18:00", "activity": "SnowExperience365 ice castle.", "gmaps": gmaps("SnowExperience365 Kemi")}
    ],
    "sched_b": [
      {"time": "08:30 - 12:30", "activity": "Drive Björkliden to Kemi (340 km).", "gmaps": gmaps("Bjorkliden to Kemi")},
      {"time": "14:00 - 15:30", "activity": "Bothnian Bay Sea-Ice Trail walk onto thick frozen gulf sea ice (Free access, no ticket needed).", "gmaps": gmaps("Kemi Inner Harbour Ice Trail", 65.7363, 24.5637)},
      {"time": "16:00 - 18:00", "activity": "Explore SnowExperience365 indoor ice castle & ice bar.", "gmaps": gmaps("SnowExperience365 Kemi")},
      {"time": "18:30 - 20:30", "activity": "Dinner at Sataman Krouvi or Restaurant Lumihiutale.", "gmaps": gmaps("Sataman Krouvi Kemi")}
    ],
    "legs": [{"from": "Björkliden", "to": "Kemi", "dist": "340 km", "time": "4h 00m", "route": "E10 & E4", "gmaps": gmaps("Bjorkliden to Kemi")}],
    "tickets": [{"item": "Sea-Ice Shoreline Trail", "cost": "Free (No Ticket Needed)", "url": "https://experience365.fi/"}, {"item": "SnowExperience365 Ticket", "cost": "€18/pax", "url": "https://experience365.fi/"}],
    "aurora": [{"name": "Inner Harbour Coastal Promenade", "desc": "Dark shoreline facing north over frozen bay.", "coords": [65.7363, 24.5637], "gmaps": gmaps("Kemi Harbour Promenade", 65.7363, 24.5637)}]
  },
  {
    "day": 9, "date": "Dec 20 (Sun)", "title_a": "Sampo Icebreaker Cruise & Sea Ice Floating", "title_b": "Sampo Icebreaker & Ajos Peninsula Ice Ridge Trail",
    "location": "Kemi, Finland", "coords": [65.7363, 24.5637], "distance": "20 km (20m local)",
    "hotel": "Cozy Apartment by the Sea 2 Rooms (Kemi)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Night 2 of 2)",
    "food": food_db["Kemi"],
    "activities_a": "Official Sampo Icebreaker Cruise: crush sea ice, engine room tour, survival drysuit floating in open sea-ice pool; coastal sauna.",
    "activities_b": "Official Sampo Icebreaker Cruise & drysuit ice float; Ajos Peninsula sunset ice ridge trail walk; coastal sauna & Lumihiutale seafood dinner.",
    "sched_a": [
      {"time": "09:30 - 13:00", "activity": "Sampo Icebreaker Cruise & ice float.", "gmaps": gmaps("Sampo Icebreaker Kemi")},
      {"time": "15:30 - 18:00", "activity": "Coastal sauna session.", "gmaps": gmaps("Kemi Sauna")}
    ],
    "sched_b": [
      {"time": "08:30 - 12:00 / 13:00 - 16:30", "activity": "Official Sampo Icebreaker Cruise: 3.5h sea-ice crush & survival drysuit ocean ice float (Slot 1: 08:30-12:00 or Slot 2: 13:00-16:30).", "gmaps": gmaps("Sampo Icebreaker Kemi")},
      {"time": "13:15 - 14:30", "activity": "Lunch at SnowCastle Lumihiutale Restaurant.", "gmaps": gmaps("Restaurant Lumihiutale Kemi")},
      {"time": "15:00 - 16:30", "activity": "Ajos Peninsula sunset ice ridge trail walk along coastal ice pack.", "gmaps": gmaps("Ajos Harbour Kemi", 65.6700, 24.5500)},
      {"time": "17:00 - 19:00", "activity": "Coastal sauna session.", "gmaps": gmaps("Kemi Sauna")}
    ],
    "legs": [{"from": "Kemi Center", "to": "Ajos Harbour", "dist": "15 km", "time": "20 mins", "route": "Ajos Road", "gmaps": gmaps("Kemi to Ajos Harbour")}],
    "tickets": [{"item": "Sampo Icebreaker Cruise (3.5h)", "cost": "€340/pax", "url": "https://experience365.fi/icebreaker-sampo/"}],
    "aurora": [{"name": "Ajos Harbour Breakwater", "desc": "Unobstructed dark horizon over gulf ice.", "coords": [65.6700, 24.5500], "gmaps": gmaps("Ajos Harbour Kemi", 65.6700, 24.5500)}]
  },
  {
    "day": 10, "date": "Dec 21 (Mon)", "title_a": "Check-in Rantapolku 1 Posio", "title_b": "Korouoma Frozen Waterfalls Canyon 5 km Loop Hike",
    "location": "Posio, Finland", "coords": [66.1089, 28.1633], "distance": "170 km (2h 15m)",
    "hotel": "Idyllic sauna cottage by the lake (Rantapolku 1, Posio)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Ref: HMYPAMHXW9 (Host: Leena)",
    "food": food_db["Posio"],
    "activities_a": "Scenic drive east to Posio; stop at S-Market Posio for groceries; check into Airbnb (Rantapolku 1); evening lakeside sauna & quiet aurora watch.",
    "activities_b": "Drive Kemi to Posio; Korouoma Frozen Waterfalls Canyon 5 km loop hike (Koronjää trail past 60m giant blue icefalls & Mammoth Falls); check in at Rantapolku 1 cottage; lakeside sauna.",
    "sched_a": [
      {"time": "10:00 - 12:15", "activity": "Drive Kemi to Posio (170 km).", "gmaps": gmaps("Kemi to Posio")},
      {"time": "14:00 - 15:30", "activity": "Check into Rantapolku 1 Posio.", "gmaps": gmaps("Rantapolku 1 Posio")},
      {"time": "16:00 - 19:00", "activity": "Lakeside wood sauna.", "gmaps": gmaps("Lake Kitkajarvi Posio")}
    ],
    "sched_b": [
      {"time": "08:30 - 10:30", "activity": "Drive Kemi to Korouoma Nature Reserve (140 km).", "gmaps": gmaps("Kemi to Korouoma Canyon")},
      {"time": "10:45 - 13:45", "activity": "Hike Koronjää 5 km loop trail in Korouoma Canyon past 60m frozen icefalls & Mammoth Falls.", "gmaps": gmaps("Koronjää Trailhead Korouoma", 66.1550, 28.1440)},
      {"time": "14:00 - 14:30", "activity": "Campfire sausage lunch at Korouoma lean-to shelter.", "gmaps": gmaps("Korouoma Lean-to Shelter")},
      {"time": "15:00 - 15:30", "activity": "Drive 30 mins to Posio cottage at Rantapolku 1.", "gmaps": gmaps("Rantapolku 1 Posio")},
      {"time": "16:30 - 19:30", "activity": "Lakeside wood sauna & ice hole plunge.", "gmaps": gmaps("Lake Kitkajarvi Posio")}
    ],
    "legs": [{"from": "Kemi", "to": "Korouoma Trailhead", "dist": "140 km", "time": "1h 50m", "route": "Road 81", "gmaps": gmaps("Kemi to Korouoma Canyon Parking")}],
    "tickets": [{"item": "Ice Cleats / Crampons", "cost": "€12/pair", "url": "https://posiolapland.com/"}],
    "aurora": [{"name": "Rantapolku Private Lake Dock", "desc": "Dark horizon over frozen Lake Kitkajärvi.", "coords": [66.1089, 28.1633], "gmaps": gmaps("Rantapolku Posio", 66.1089, 28.1633)}]
  },
  {
    "day": 11, "date": "Dec 22 (Tue)", "title_a": "Riisitunturi National Park World-Class Tykky Trees", "title_b": "Riisitunturi Summit Crown-Snow Tree Circuit + Campfire Feast",
    "location": "Posio, Finland", "coords": [66.1089, 28.1633], "distance": "60 km (50m roundtrip)",
    "hotel": "Idyllic sauna cottage by the lake (Rantapolku 1, Posio)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Ref: HMYPAMHXW9 (Night 2 of 2)",
    "food": food_db["Posio"],
    "activities_a": "Drive to Riisitunturi National Park; 10:30 AM golden twilight snowshoe hike (Riisin rääpäsy 4.3 km trail) among Tykky snow-sculpture trees; campfire lunch.",
    "activities_b": "Riisitunturi Summit Crown Snow-Tree Circuit snowshoe hike; campfire sausage & hot berry tea lunch in open wilderness hut; night aurora photo hunt at summit.",
    "sched_a": [
      {"time": "10:30 - 13:30", "activity": "Snowshoe hike in Riisitunturi.", "gmaps": gmaps("Riisitunturi National Park")},
      {"time": "17:00 - 19:30", "activity": "Lakeside sauna session.", "gmaps": gmaps("Posio Cottage Sauna")}
    ],
    "sched_b": [
      {"time": "09:45 - 10:15", "activity": "Drive 25 mins to Riisitunturi trailhead (30 km).", "gmaps": gmaps("Riisitunturi Trailhead", 66.2167, 28.5667)},
      {"time": "10:30 - 13:30", "activity": "Riisitunturi Summit Crown Snow-Tree Circuit snowshoe trek.", "gmaps": gmaps("Riisitunturi Summit", 66.2167, 28.5667)},
      {"time": "13:30 - 14:30", "activity": "Campfire sausage & hot tea lunch at wilderness hut.", "gmaps": gmaps("Riisitunturi Wilderness Hut")},
      {"time": "17:00 - 19:30", "activity": "Lakeside sauna session.", "gmaps": gmaps("Posio Cottage Sauna")}
    ],
    "legs": [{"from": "Posio Cottage", "to": "Riisitunturi Trailhead", "dist": "30 km", "time": "25 mins", "route": "Road 3470", "gmaps": gmaps("Posio to Riisitunturi")}],
    "tickets": [{"item": "Snowshoe Rental", "cost": "€20/day", "url": "https://posiolapland.com/"}],
    "aurora": [{"name": "Riisitunturi Park Base Parking", "desc": "Pristine fell skies framed by snow trees.", "coords": [66.2167, 28.5667], "gmaps": gmaps("Riisitunturi Parking", 66.2167, 28.5667)}]
  },
  {
    "day": 12, "date": "Dec 23 (Wed)", "title_a": "Easy 1h Hop to Iso-Syöte Fell", "title_b": "Syöte National Park Crown-Snow Forest Snowshoe Trail",
    "location": "Iso-Syöte, Finland", "coords": [65.6265, 27.6083], "distance": "75 km (55 mins)",
    "hotel": "Apartment with a view at the top of Iso-Syöte (Host Arto)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Confirmed (Host: Arto)",
    "food": food_db["Iso-Syöte"],
    "activities_a": "Short 55-minute drive to Iso-Syöte fell summit; check in; afternoon downhill skiing or panoramic fell-top spa; dinner at Restaurant Hilltop.",
    "activities_b": "Drive to Iso-Syöte; Syöte National Park Crown-Snow Forest snowshoe trail trek through ancient spruce canopy; fell summit downhill skiing or spa; Restaurant Hilltop dinner.",
    "sched_a": [
      {"time": "10:30 - 11:30", "activity": "Drive Posio to Iso-Syöte (75 km).", "gmaps": gmaps("Posio to Iso-Syote")},
      {"time": "13:30 - 16:30", "activity": "Downhill skiing or fell-top spa.", "gmaps": gmaps("Iso-Syote Ski Resort")}
    ],
    "sched_b": [
      {"time": "10:00 - 11:00", "activity": "Drive Posio to Iso-Syöte fell summit (75 km).", "gmaps": gmaps("Posio to Iso-Syote")},
      {"time": "11:30 - 13:30", "activity": "Syöte National Park Crown-Snow Forest snowshoe trail trek.", "gmaps": gmaps("Syote National Park Visitor Centre", 65.6265, 27.6083)},
      {"time": "14:00 - 17:00", "activity": "Downhill skiing on Iso-Syöte slopes or panoramic fell-top spa.", "gmaps": gmaps("Iso-Syote Ski Resort")},
      {"time": "19:30 - 21:30", "activity": "Dinner at Restaurant Hilltop Iso-Syöte.", "gmaps": gmaps("Restaurant Hilltop Iso-Syote")}
    ],
    "legs": [{"from": "Posio", "to": "Iso-Syöte Fell Top", "dist": "75 km", "time": "55 mins", "route": "Road 863", "gmaps": gmaps("Posio to Iso-Syote")}],
    "tickets": [{"item": "Iso-Syöte Ski Pass 3h", "cost": "€42/pax", "url": "https://syote.fi/en/"}],
    "aurora": [{"name": "Iso-Syöte Fell Summit Deck", "desc": "Highest elevation in southern Lapland.", "coords": [65.6265, 27.6083], "gmaps": gmaps("Iso-Syote Fell Summit", 65.6265, 27.6083)}]
  },
  {
    "day": 13, "date": "Dec 24 (Thu)", "title_a": "Confirmed Booking: Iso-Syöte Treehouse / Igloo (Christmas Eve)", "title_b": "Pyhitys Fell Panoramic Winter Ridge Hike & Glass Igloo Feast",
    "location": "Iso-Syöte, Finland", "coords": [65.6265, 27.6083], "distance": "0 km (0h - Rest Day)",
    "hotel": "Syöte Igloos / Iso-Syöte Treehouse", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Check-in 24 Dec)",
    "food": food_db["Iso-Syöte"],
    "activities_a": "Check into confirmed Syöte Treehouse / Igloo; Christmas Eve feast, private fell-top sauna, panoramic glass view of snow-covered spruce canopy.",
    "activities_b": "Pyhitys Fell Panoramic Winter Ridge Hike (360-degree views of southern Lapland); check into Syöte Glass Igloo / Treehouse; Christmas Eve gala feast.",
    "sched_a": [
      {"time": "11:00 - 12:00", "activity": "Move to Syöte Glass Igloo.", "gmaps": gmaps("Syote Igloos")},
      {"time": "18:00 - 21:00", "activity": "Christmas Eve Gala Feast.", "gmaps": gmaps("Hotel Iso-Syote Restaurant")}
    ],
    "sched_b": [
      {"time": "09:30 - 12:00", "activity": "Pyhitys Fell Panoramic Winter Ridge Hike (360-degree winter landscape view).", "gmaps": gmaps("Pyhitys Fell Syote", 65.6500, 27.8000)},
      {"time": "12:30 - 14:00", "activity": "Check into confirmed Syöte Glass Igloo / Treehouse & champagne toast.", "gmaps": gmaps("Syote Igloos")},
      {"time": "14:30 - 17:00", "activity": "Private glass sauna session overlooking fell summit.", "gmaps": gmaps("Syote Igloos Sauna")},
      {"time": "18:00 - 21:00", "activity": "Traditional Finnish Christmas Eve Buffet Feast at Hotel Iso-Syöte.", "gmaps": gmaps("Hotel Iso-Syote Restaurant")}
    ],
    "legs": [{"from": "Iso-Syöte Top", "to": "Syöte Igloos", "dist": "0.5 km", "time": "2 mins", "route": "Fell Road", "gmaps": gmaps("Iso-Syote Top to Igloos")}],
    "tickets": [{"item": "Christmas Eve Gala Buffet", "cost": "€75/pax", "url": "https://hotellisyoete.fi/en/"}],
    "aurora": [{"name": "Glass Roof Igloo Bedroom", "desc": "Watch aurora from bed inside heated glass dome.", "coords": [65.6265, 27.6083], "gmaps": gmaps("Syote Igloos", 65.6265, 27.6083)}]
  },
  {
    "day": 14, "date": "Dec 25 (Fri)", "title_a": "Santa Claus Village & VR Express Sleeper Train", "title_b": "Arctic Circle Hiking Area Suspension Bridge Walk & Sleeper Train",
    "location": "En-Route VR Night Train", "coords": [66.5039, 25.7294], "distance": "160 km (2h 00m)",
    "hotel": "VR Santa Claus Express Sleeper Train (9:00 PM)", "hotelStatus": "confirmed", "bookingRef": "VR Train Booking (Rovaniemi -> Helsinki)",
    "food": food_db["Rovaniemi"],
    "activities_a": "Drive to Rovaniemi; explore Santa Claus Village & post office; return AWD SUV at station ($0 drop-off fee); board 9:00 PM VR Sleeper Train.",
    "activities_b": "Drive to Rovaniemi; Arctic Circle Hiking Area (Vikaköngäs suspension bridge walk over roaring frozen rapids); Santa Claus Village; 9:00 PM VR Sleeper Train.",
    "sched_a": [
      {"time": "10:00 - 12:00", "activity": "Drive to Rovaniemi (160 km).", "gmaps": gmaps("Iso-Syote to Rovaniemi")},
      {"time": "12:15 - 16:30", "activity": "Explore Santa Claus Village.", "gmaps": gmaps("Santa Claus Village Rovaniemi")},
      {"time": "21:00", "activity": "Board VR Sleeper Train to Helsinki.", "gmaps": gmaps("Rovaniemi Railway Station")}
    ],
    "sched_b": [
      {"time": "09:30 - 11:30", "activity": "Drive north from Iso-Syöte to Arctic Circle Hiking Area (150 km).", "gmaps": gmaps("Vikakongas Arctic Circle Hiking Area", 66.6500, 26.0500)},
      {"time": "11:30 - 13:30", "activity": "Vikaköngäs suspension bridge walk over roaring frozen rapids & pine forest trail.", "gmaps": gmaps("Vikakongas Suspension Bridge", 66.6500, 26.0500)},
      {"time": "14:00 - 17:00", "activity": "Explore Santa Claus Village: cross Arctic Circle line & main post office.", "gmaps": gmaps("Santa Claus Village Rovaniemi")},
      {"time": "19:00 - 20:00", "activity": "Return AWD SUV rental at Rovaniemi Railway Station.", "gmaps": gmaps("Rovaniemi Railway Station")},
      {"time": "21:00", "activity": "Overnight VR Santa Claus Express Sleeper Train departs for Helsinki.", "gmaps": gmaps("Rovaniemi Railway Station")}
    ],
    "legs": [{"from": "Iso-Syöte", "to": "Vikaköngäs", "dist": "150 km", "time": "1h 50m", "route": "Road 81", "gmaps": gmaps("Iso-Syote to Vikakongas")}],
    "tickets": [{"item": "VR Sleeper Cabin", "cost": "~€210", "url": "https://www.vr.fi/en"}],
    "aurora": [{"name": "Train Cabin Window", "desc": "Night sky passing outside sleeper train window.", "coords": [65.0121, 25.4651], "gmaps": gmaps("Oulu Railway Station", 65.0121, 25.4651)}]
  },
  {
    "day": 15, "date": "Dec 26 (Sat)", "title_a": "Helsinki Boxing Day & Löyly Smoke Sauna", "title_b": "Suomenlinna Sea Fortress Island Walk & Löyly Sauna",
    "location": "Helsinki, Finland", "coords": [60.1699, 24.9384], "distance": "0 km (Transit)",
    "hotel": "Hotel U14 Autograph Collection", "hotelStatus": "confirmed", "bookingRef": "Confirmed Hotel U14 Autograph Collection",
    "food": food_db["Helsinki"],
    "activities_a": "Arrive Helsinki 9:00 AM; explore Oodi Library & Senate Square; afternoon seaside smoke sauna & Baltic ice dip at Löyly.",
    "activities_b": "Arrive Helsinki 9:00 AM; ferry to Suomenlinna UNESCO Sea Fortress for 4 km coastal sea-wall walking loop; lunch at SOUP+MORE (Vanha Kauppahalli Lohikeitto); Löyly smoke sauna & Baltic ice dip.",
    "sched_a": [
      {"time": "09:00", "activity": "Arrive Helsinki Central Station.", "gmaps": gmaps("Helsinki Central Station")},
      {"time": "10:45 - 13:00", "activity": "Explore Oodi Library & Senate Square.", "gmaps": gmaps("Oodi Library Helsinki")},
      {"time": "14:00 - 16:30", "activity": "Löyly seaside smoke sauna & ice dip.", "gmaps": gmaps("Löyly Helsinki Sauna")}
    ],
    "sched_b": [
      {"time": "09:00", "activity": "Arrive Helsinki Central Railway Station.", "gmaps": gmaps("Helsinki Central Station")},
      {"time": "09:45 - 10:00", "activity": "15-minute ferry ride from Market Square to Suomenlinna Island.", "gmaps": gmaps("Market Square Helsinki Ferry Terminal")},
      {"time": "10:00 - 12:30", "activity": "4 km coastal sea-wall walking loop around Suomenlinna fortress tunnels & cannons.", "gmaps": gmaps("Suomenlinna Fortress Walk", 60.1472, 24.9872)},
      {"time": "13:00 - 14:00", "activity": "Lunch at Vanha Kauppahalli SOUP+MORE (Famous creamy Finnish salmon soup Lohikeitto for €12).", "gmaps": gmaps("SOUP+MORE Vanha Kauppahalli Helsinki")},
      {"time": "15:00 - 17:30", "activity": "Seaside smoke sauna & Baltic sea ice dip at Löyly Helsinki.", "gmaps": gmaps("Löyly Helsinki Sauna")}
    ],
    "legs": [{"from": "Market Square", "to": "Suomenlinna", "dist": "3 km", "time": "15 mins", "route": "HSL Ferry", "gmaps": gmaps("Helsinki to Suomenlinna Ferry")}],
    "tickets": [{"item": "Suomenlinna Ferry", "cost": "€3.10", "url": "https://www.hsl.fi/en"}, {"item": "Löyly Sauna 2h", "cost": "€24", "url": "https://www.loylyhelsinki.fi/en/"}]
  },
  {
    "day": 16, "date": "Dec 27 (Sun)", "title_a": "Baltic Sea Ferry Transit & Medieval Tallinn", "title_b": "Lahemaa Viru Bog Snowshoe Hike & Medieval Tallinn",
    "location": "Tallinn, Estonia", "coords": [59.4370, 24.7536], "distance": "90 km (1h 15m)",
    "hotel": "Hotel Telegraaf, Autograph Collection (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Autograph Collection in Tallinn Old Town",
    "hotelLinks": [{"name": "Hotel Telegraaf (Marriott)", "url": "https://www.marriott.com/en-us/hotels/tllak-hotel-telegraaf-autograph-collection/overview/", "gmaps": gmaps("Hotel Telegraaf Tallinn")}],
    "food": food_db["Tallinn"],
    "activities_a": "Morning 2h Megastar ferry across Baltic Sea; explore UNESCO medieval Old Town, Town Hall Christmas Market & Toompea Hill vista.",
    "activities_b": "Morning 2h Megastar ferry to Tallinn; 45-min drive east to Lahemaa National Park for Viru Bog 3.5 km snowshoe boardwalk hike; check in at Hotel Telegraaf; cheap pancake feast at Kompressor Pancake Pub.",
    "sched_a": [
      {"time": "10:30 - 12:30", "activity": "Megastar Ferry to Tallinn.", "gmaps": gmaps("Tallinn Passenger Port")},
      {"time": "14:30 - 17:30", "activity": "Explore Old Town & Christmas Market.", "gmaps": gmaps("Tallinn Old Town")}
    ],
    "sched_b": [
      {"time": "10:30 - 12:30", "activity": "Megastar Ferry transit across Baltic Sea to Tallinn.", "gmaps": gmaps("Tallinn Passenger Port")},
      {"time": "13:00 - 13:45", "activity": "Drive 45 mins east to Lahemaa National Park Viru Bog trailhead (55 km).", "gmaps": gmaps("Viru Bog Parking Lahemaa", 59.4714, 25.6600)},
      {"time": "13:45 - 15:45", "activity": "3.5 km snow-covered peat bog boardwalk hike to Viru Bog observation tower.", "gmaps": gmaps("Viru Bog Watchtower", 59.4714, 25.6600)},
      {"time": "16:30 - 17:00", "activity": "Return drive & check in at Hotel Telegraaf Old Town.", "gmaps": gmaps("Hotel Telegraaf Tallinn")},
      {"time": "18:00 - 19:30", "activity": "Pancake feast at Kompressor Pancake Pub (Giant sweet & savory pancakes for €6-€8!).", "gmaps": gmaps("Kompressor Tallinn")}
    ],
    "legs": [{"from": "Tallinn Port", "to": "Viru Bog", "dist": "55 km", "time": "45 mins", "route": "Route 1", "gmaps": gmaps("Tallinn Port to Viru Bog Parking")}],
    "tickets": [{"item": "Megastar Ferry Ticket", "cost": "~€32", "url": "https://www.tallinksilja.com/en"}]
  },
  {
    "day": 17, "date": "Dec 28 (Mon)", "title_a": "Flight TLL -> ARN to Stockholm", "title_b": "Monteliusvägen Cliffside Skyline Walk & Flight to Stockholm",
    "location": "Stockholm, Sweden", "coords": [59.3293, 18.0686], "distance": "0 km (Flight)",
    "hotel": "Sheraton Stockholm Hotel (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Waterfront Hotel near Central Station",
    "hotelLinks": [{"name": "Sheraton Stockholm (Marriott)", "url": "https://www.marriott.com/en-us/hotels/stosi-sheraton-stockholm-hotel/overview/", "gmaps": gmaps("Sheraton Stockholm Hotel")}],
    "food": food_db["Stockholm"],
    "activities_a": "Morning visit Kadriorg Palace; late afternoon flight to Stockholm (TLL -> ARN); evening walk through illuminated Norrmalm & Nybroplan.",
    "activities_b": "Visit Kadriorg Palace & Telliskivi Creative City; flight to Stockholm; Monteliusvägen cliffside skyline walk overlooking Lake Mälaren & Gamla Stan; Sheraton Stockholm Hotel.",
    "sched_a": [
      {"time": "15:30 - 16:30", "activity": "Flight TLL -> ARN.", "gmaps": gmaps("Stockholm Arlanda Airport")},
      {"time": "18:00", "activity": "Check into Sheraton Stockholm Hotel.", "gmaps": gmaps("Sheraton Stockholm Hotel")}
    ],
    "sched_b": [
      {"time": "09:30 - 11:30", "activity": "Visit Kadriorg Art Museum Palace grounds & Telliskivi Creative City.", "gmaps": gmaps("Kadriorg Palace Tallinn")},
      {"time": "15:30 - 16:30", "activity": "Flight TLL -> ARN (SAS / Ryanair, 1h).", "gmaps": gmaps("Stockholm Arlanda Airport")},
      {"time": "17:00 - 17:30", "activity": "Arlanda Express train to Stockholm Central (18 mins).", "gmaps": gmaps("Stockholm Central Station")},
      {"time": "18:00 - 18:30", "activity": "Check into Sheraton Stockholm Hotel.", "gmaps": gmaps("Sheraton Stockholm Hotel")},
      {"time": "19:00 - 20:30", "activity": "Monteliusvägen cliffside skyline walk overlooking Lake Mälaren & illuminated Gamla Stan.", "gmaps": gmaps("Monteliusvagen Stockholm", 59.3190, 18.0620)}
    ],
    "legs": [{"from": "Arlanda Airport", "to": "Stockholm Central", "dist": "40 km", "time": "18 mins", "route": "Arlanda Express Train", "gmaps": gmaps("Arlanda to Stockholm Central")}],
    "tickets": [{"item": "Arlanda Express Train", "cost": "~320 SEK", "url": "https://www.arlandaexpress.com/"}]
  },
  {
    "day": 18, "date": "Dec 29 (Tue)", "title_a": "Stockholm Core Day 1", "title_b": "Royal Djurgården Waterfront 6 km Nature Loop & Gamla Stan",
    "location": "Stockholm, Sweden", "coords": [59.3293, 18.0686], "distance": "0 km (Metro/Walk)",
    "hotel": "Sheraton Stockholm Hotel (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Waterfront Hotel",
    "hotelLinks": [{"name": "Sheraton Stockholm (Marriott)", "url": "https://www.marriott.com/en-us/hotels/stosi-sheraton-stockholm-hotel/overview/", "gmaps": gmaps("Sheraton Stockholm Hotel")}],
    "food": food_db["Stockholm"],
    "activities_a": "Full day of historic Stockholm: cobblestone alleys of Gamla Stan (Old Town), Royal Palace, Stortorget, and Nobel Prize Museum.",
    "activities_b": "Royal Djurgården waterfront 6 km nature walking loop; Gamla Stan medieval alleys & Royal Palace; lunch at Östermalms Saluhall (Lisaköket Toast Skagen).",
    "sched_a": [
      {"time": "09:30 - 12:00", "activity": "Gamla Stan walking tour.", "gmaps": gmaps("Gamla Stan Stockholm")},
      {"time": "15:00 - 17:00", "activity": "Nobel Prize Museum.", "gmaps": gmaps("Nobel Prize Museum Stockholm")}
    ],
    "sched_b": [
      {"time": "09:30 - 12:00", "activity": "Royal Djurgården waterfront 6 km nature walking loop along Djurgårdsbrunnskanalen.", "gmaps": gmaps("Royal Djurgarden Stockholm", 59.3250, 18.1000)},
      {"time": "12:30 - 13:30", "activity": "Lunch at Östermalms Saluhall (Lisaköket Toast Skagen & seafood soup).", "gmaps": gmaps("Ostermalms Saluhall Stockholm")},
      {"time": "14:00 - 16:30", "activity": "Gamla Stan medieval alleys, Stortorget & Royal Palace.", "gmaps": gmaps("Royal Palace Stockholm")},
      {"time": "18:30 - 21:00", "activity": "Dinner at Meatballs for the People / Pelikan.", "gmaps": gmaps("Meatballs for the People Stockholm")}
    ],
    "legs": [{"from": "Sheraton", "to": "Djurgården", "dist": "3 km", "time": "15 mins", "route": "Tram 7", "gmaps": gmaps("Sheraton to Djurgarden")}],
    "tickets": [{"item": "Royal Palace Ticket", "cost": "~190 SEK", "url": "https://www.kungligaslotten.se/english.html"}]
  },
  {
    "day": 19, "date": "Dec 30 (Wed)", "title_a": "Stockholm Core Day 2", "title_b": "Tyresta National Park Primeval Forest Trail & Vasa Museum",
    "location": "Stockholm, Sweden", "coords": [59.3293, 18.0686], "distance": "0 km (Ferry/Tram)",
    "hotel": "Sheraton Stockholm Hotel (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Waterfront Hotel",
    "hotelLinks": [{"name": "Sheraton Stockholm (Marriott)", "url": "https://www.marriott.com/en-us/hotels/stosi-sheraton-stockholm-hotel/overview/", "gmaps": gmaps("Sheraton Stockholm Hotel")}],
    "food": food_db["Stockholm"],
    "activities_a": "Maritime & culture day: tour 17th-century Vasa Museum, explore Djurgården island & Skansen, or visit ABBA The Museum; traditional Swedish dinner.",
    "activities_b": "30-min drive to Tyresta National Park for primeval pine forest trail hike (500-year-old virgin trees); 17th-century Vasa Museum warship tour; ABBA Museum.",
    "sched_a": [
      {"time": "09:30 - 12:00", "activity": "Tour Vasa Museum.", "gmaps": gmaps("Vasa Museum Stockholm")},
      {"time": "13:30 - 16:30", "activity": "Visit ABBA The Museum.", "gmaps": gmaps("ABBA The Museum")}
    ],
    "sched_b": [
      {"time": "08:45 - 09:30", "activity": "Drive 30 mins south to Tyresta National Park village (25 km).", "gmaps": gmaps("Tyresta National Park Village", 59.1833, 18.2333)},
      {"time": "09:30 - 12:00", "activity": "Tyresta National Park primeval forest trail hike through 500-year-old pine trees & lakes.", "gmaps": gmaps("Tyresta National Park Trailhead", 59.1833, 18.2333)},
      {"time": "13:00 - 15:30", "activity": "Tour 17th-century Vasa Museum (preserved 1628 warship).", "gmaps": gmaps("Vasa Museum Stockholm")},
      {"time": "16:00 - 18:00", "activity": "Visit ABBA The Museum.", "gmaps": gmaps("ABBA The Museum")},
      {"time": "19:00 - 21:30", "activity": "Dinner at Restaurant Tradition (Husmanskost).", "gmaps": gmaps("Restaurant Tradition Stockholm")}
    ],
    "legs": [{"from": "Sheraton", "to": "Tyresta National Park", "dist": "25 km", "time": "30 mins", "route": "Route 73", "gmaps": gmaps("Sheraton to Tyresta National Park")}],
    "tickets": [{"item": "Vasa Museum Ticket", "cost": "~190 SEK", "url": "https://www.vasamuseet.se/en"}, {"item": "ABBA Museum Ticket", "cost": "~290 SEK", "url": "https://abbathemuseum.com/en/"}]
  },
  {
    "day": 20, "date": "Dec 31 (Thu)", "title_a": "High-Speed Train & NYE Tivoli Celebration", "title_b": "Copenhagen Lakes & Kastellet Star-Fortress Walk + Tivoli NYE",
    "location": "Copenhagen, Denmark", "coords": [55.6761, 12.5683], "distance": "0 km (Train)",
    "hotel": "Copenhagen Marriott Hotel (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Harborfront Hotel near Tivoli",
    "hotelLinks": [{"name": "Copenhagen Marriott Hotel", "url": "https://www.marriott.com/en-us/hotels/cphdk-copenhagen-marriott-hotel/overview/", "gmaps": gmaps("Copenhagen Marriott Hotel")}],
    "food": food_db["Copenhagen"],
    "activities_a": "Morning SJ High-Speed Train from Stockholm Central to Copenhagen Central (5h 10m via Öresund Bridge); check in; New Year's Eve gala dinner & midnight fireworks at Tivoli Gardens.",
    "activities_b": "SJ High-Speed Train to Copenhagen; Kastellet 17th-century star-fortress & Little Mermaid coastal walk; Copenhagen Lakes (Søerne); Tivoli Gardens NYE gala dinner & midnight fireworks.",
    "sched_a": [
      {"time": "08:20 - 13:30", "activity": "SJ High-Speed Train to Copenhagen.", "gmaps": gmaps("Copenhagen Central Station")},
      {"time": "19:00 - 01:00", "activity": "Tivoli Gardens NYE Gala & Fireworks.", "gmaps": gmaps("Tivoli Gardens Copenhagen")}
    ],
    "sched_b": [
      {"time": "08:20 - 13:30", "activity": "SJ High-Speed Train from Stockholm Central to Copenhagen Central (5h 10m via Öresund Bridge).", "gmaps": gmaps("Copenhagen Central Station")},
      {"time": "14:00 - 14:45", "activity": "Check into Copenhagen Marriott Hotel.", "gmaps": gmaps("Copenhagen Marriott Hotel")},
      {"time": "15:00 - 17:00", "activity": "Kastellet 17th-century star-fortress ramparts walk & Little Mermaid coastal path.", "gmaps": gmaps("Kastellet Copenhagen", 55.6914, 12.5950)},
      {"time": "19:00 - 23:30", "activity": "New Year's Eve Gala Dinner at Tivoli Gardens Restaurant.", "gmaps": gmaps("Tivoli Gardens Copenhagen")},
      {"time": "00:00 - 01:00", "activity": "Spectacular Midnight Fireworks over Tivoli Gardens.", "gmaps": gmaps("Tivoli Gardens Copenhagen")}
    ],
    "legs": [{"from": "Stockholm", "to": "Copenhagen", "dist": "650 km", "time": "5h 10m", "route": "SJ High Speed Train", "gmaps": gmaps("Stockholm to Copenhagen Train")}],
    "tickets": [{"item": "SJ High-Speed Train", "cost": "~€65", "url": "https://www.sj.se/en"}, {"item": "Tivoli NYE Admission & Gala", "cost": "~1,170 DKK", "url": "https://www.tivoli.dk/en"}]
  },
  {
    "day": 21, "date": "Jan 01 (Fri)", "title_a": "New Year's Day in Copenhagen", "title_b": "Amager Strandpark Coastal Dune Walk & CopenHill Roof Trek",
    "location": "Copenhagen, Denmark", "coords": [55.6761, 12.5683], "distance": "0 km (Metro/Walk)",
    "hotel": "Copenhagen Marriott Hotel (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Harborfront Hotel",
    "hotelLinks": [{"name": "Copenhagen Marriott Hotel", "url": "https://www.marriott.com/en-us/hotels/cphdk-copenhagen-marriott-hotel/overview/", "gmaps": gmaps("Copenhagen Marriott Hotel")}],
    "food": food_db["Copenhagen"],
    "activities_a": "Relaxed New Year's Day stroll; view CopenHill rooftop architecture, Amalienborg Palace royal guard change, and Nyhavn / Strøget cafe culture.",
    "activities_b": "Amager Strandpark coastal dune sea walk; CopenHill rooftop mountain urban trek & panorama; Amalienborg Palace royal guard change; Torvehallerne Hallernes Smørrebrød.",
    "sched_a": [
      {"time": "12:00 - 12:45", "activity": "Amalienborg Palace Royal Guard Change.", "gmaps": gmaps("Amalienborg Palace")},
      {"time": "13:00 - 15:00", "activity": "Visit CopenHill rooftop view.", "gmaps": gmaps("CopenHill Copenhagen")}
    ],
    "sched_b": [
      {"time": "09:30 - 11:30", "activity": "Amager Strandpark coastal dune sea walk along Öresund strait.", "gmaps": gmaps("Amager Strandpark Copenhagen", 55.6550, 12.6350)},
      {"time": "12:00 - 12:45", "activity": "Amalienborg Palace Royal Guard Changing Ceremony.", "gmaps": gmaps("Amalienborg Palace Copenhagen")},
      {"time": "13:00 - 15:00", "activity": "CopenHill rooftop urban mountain trek & panoramic city viewpoint.", "gmaps": gmaps("CopenHill Copenhagen", 55.6810, 12.6200)},
      {"time": "15:30 - 17:00", "activity": "Open-faced sandwich feast at Torvehallerne Hallernes Smørrebrød & DØP Hot Dog.", "gmaps": gmaps("Torvehallerne Copenhagen")}
    ],
    "legs": [{"from": "Marriott", "to": "Amager Strandpark", "dist": "5 km", "time": "12 mins", "route": "Metro M2", "gmaps": gmaps("Copenhagen Marriott to Amager Strandpark")}],
    "tickets": [{"item": "CopenHill Viewpoint", "cost": "Free", "url": "https://www.copenhill.dk/en"}]
  },
  {
    "day": 22, "date": "Jan 02 (Sat)", "title_a": "SQ352 Non-stop to Singapore", "title_b": "King's Garden (Kongens Have) Morning Stroll & Flight Home",
    "location": "Flight Home (In Flight)", "coords": [55.6180, 12.6508], "distance": "0 km (Metro)",
    "hotel": "In Flight (Singapore Airlines SQ352)", "hotelStatus": "confirmed", "bookingRef": "SQ352 Non-stop (Dep CPH 12:00 PM, Arr SIN Jan 03 7:30 AM)",
    "food": food_db["Copenhagen"],
    "activities_a": "Morning 13-minute Metro to CPH Airport; depart on Singapore Airlines SQ352 non-stop to Singapore at 12:00 PM (Arrive SIN Jan 03, 7:30 AM).",
    "activities_b": "King's Garden (Kongens Have) morning castle stroll; 13-minute Metro to CPH Airport; depart on Singapore Airlines SQ352 non-stop to Singapore at 12:00 PM.",
    "sched_a": [
      {"time": "09:15 - 09:30", "activity": "Metro to CPH Airport.", "gmaps": gmaps("Copenhagen Airport")},
      {"time": "12:00", "activity": "Flight SQ352 departs CPH to SIN.", "gmaps": gmaps("Copenhagen Airport")}
    ],
    "sched_b": [
      {"time": "08:30 - 09:30", "activity": "King's Garden (Kongens Have) morning stroll around Rosenborg Castle.", "gmaps": gmaps("Kings Garden Copenhagen", 55.6850, 12.5780)},
      {"time": "09:45 - 10:00", "activity": "13-minute Metro M2 ride to Copenhagen Airport (CPH).", "gmaps": gmaps("Copenhagen Airport Metro Station")},
      {"time": "10:15 - 11:30", "activity": "Check in at Singapore Airlines desk & tax refund.", "gmaps": gmaps("Copenhagen Airport Terminal 3")},
      {"time": "12:00", "activity": "Flight SQ352 departs CPH non-stop to Singapore (Arrives SIN Jan 03 at 07:30 AM).", "gmaps": gmaps("Copenhagen Airport")}
    ],
    "legs": [{"from": "King's Garden", "to": "CPH Airport", "dist": "9 km", "time": "13 mins", "route": "Metro M2", "gmaps": gmaps("Kings Garden to CPH Airport")}],
    "tickets": [{"item": "CPH Metro Ticket", "cost": "36 DKK", "url": "https://intl.m.dk/"}]
  }
]

# Generate 22 full days for Route A and Route B
days_route_a = []
days_route_b = []

for item in base_22_days:
    # Route A day object
    da = {
        "day": item["day"], "date": item["date"], "title": item["title_a"], "location": item["location"],
        "coords": item["coords"], "gmaps": gmaps(item["title_a"] + " " + item["location"], item["coords"][0], item["coords"][1]),
        "distance": item["distance"], "hotel": item["hotel"], "hotelStatus": item["hotelStatus"], "bookingRef": item["bookingRef"],
        "hotelLinks": item.get("hotelLinks", []), "foodGuide": item["food"], "activities": item["activities_a"],
        "scheduleNotes": item["title_a"], "tags": ["Route A Baseline"], "hourlySchedule": item["sched_a"],
        "drivingLegs": item["legs"], "ticketCosts": item.get("tickets", []), "auroraSpots": item.get("aurora", [])
    }
    days_route_a.append(da)

    # Route B day object
    db = {
        "day": item["day"], "date": item["date"], "title": item["title_b"], "location": item["location"],
        "coords": item["coords"], "gmaps": gmaps(item["title_b"] + " " + item["location"], item["coords"][0], item["coords"][1]),
        "distance": item["distance"], "hotel": item["hotel"], "hotelStatus": item["hotelStatus"], "bookingRef": item["bookingRef"],
        "hotelLinks": item.get("hotelLinks", []), "foodGuide": item["food"], "activities": item["activities_b"],
        "scheduleNotes": "Route B High-Action Upgrade: " + item["title_b"], "tags": ["Route B High-Action", "Nature Walk", "Local Food"],
        "hourlySchedule": item["sched_b"], "drivingLegs": item["legs"], "ticketCosts": item.get("tickets", []), "auroraSpots": item.get("aurora", [])
    }
    days_route_b.append(db)

# Construct full payload
payload = {
    "routes": {
        "routeB": {"name": "Route B: High-Action Nature & Foodie Explorer (22 Days)", "days": days_route_b},
        "routeA": {"name": "Route A: Baseline Itinerary (Classic 22 Days)", "days": days_route_a}
    },
    "emergencyGuide": {
        "contacts": [
            {"country": "Unified Europe", "number": "112", "desc": "Emergency services (Police, Ambulance, Fire) - Works without SIM", "gmaps": gmaps("Nearest Police Station")},
            {"country": "Finland", "number": "+358 200 8080", "desc": "Autoliitto (Automobile and Touring Club of Finland Road Service)", "gmaps": gmaps("Autoliitto Helsinki")},
            {"country": "Sweden", "number": "+46 20 912 912", "desc": "Assistanskåren (Swedish Road & Towing Assistance)", "gmaps": gmaps("Assistanskaren Sweden")}
        ],
        "dosAndDonts": [
            "DO keep headlight lenses clean of slush and ice at every fuel stop.",
            "DO maintain 4-to-6 second follow distance behind snowplows & lorries to avoid gravel windshield chips.",
            "DO keep fuel tank above 50% capacity at all times in case of blizzard delays.",
            "DON'T slam on brakes or jerk steering wheel on black ice; pump brakes smoothly or let ABS work.",
            "DON'T leave wet gloves, boots, or water bottles in the car overnight (they will freeze solid)."
        ],
        "unstuckSteps": [
            "1. DIG OUT: Clear snow away from around all 4 tires and underneath the chassis frame with emergency shovel.",
            "2. ALIGN: Straighten steering wheel to minimize rolling resistance.",
            "3. DISABLE TCS: Temporarily turn off Traction Control (TCS / ESP button) so AWD can spin slightly and bite into grip.",
            "4. TRACTION MATS: Place car floor mats or tree branches directly under the drive wheels.",
            "5. ROCK VEHICLE: Shift smoothly between Drive (D) and Reverse (R), tapping gas gently to build momentum.",
            "6. TOW EYE: If pulled by another car, screw in the emergency tow eye from the trunk spare kit into front/rear bumper."
        ]
    },
    "packingChecklist": [
        {"cat": "Layering System", "items": ["2-3x Merino Wool Thermal Tops & Bottoms (200-260g)", "Fleece Jacket / Wool Sweater", "Packable Down Insulator Jacket", "Windproof & Waterproof Heavy Arctic Parka (-20°C)", "Insulated Snow Pants"]},
        {"cat": "Footwear & Accessories", "items": ["3-4x Thick Merino Wool Ski Socks", "Waterproof Arctic Winter Boots (Sorel/Baffin -30°C)", "Fleece-lined Windproof Beanie", "Balaclava & Wool Neck Gaiter", "Thermal Glove Liners + Waterproof Down Mittens"]},
        {"cat": "Car & Winter Safety", "items": ["Emergency Snow Shovel & Ice Scraper", "12V Car USB Charger & Heating Vent Phone Mount", "Thermal Water Flask & High-Calorie Trail Snacks", "10+ Pairs Hand & Toe Chemical Warmers"]},
        {"cat": "Photography & Aurora", "items": ["Camera with Manual Exposure + Wide Lens (f/1.4 - f/2.8)", "Sturdy Aluminum/Carbon Fiber Tripod", "Extra Camera Batteries (Keep in inner pocket!)", "Headlamp with RED Light Mode"]}
    ]
}

full_json = json.dumps(payload)

proc = subprocess.Popen(['openssl', 'enc', '-aes-256-cbc', '-md', 'md5', '-pass', 'pass:8520', '-base64', '-A'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate(input=full_json.encode('utf-8'))
enc_b64 = out.decode('utf-8').strip()

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(f'const encryptedItineraryData = "{enc_b64}";\n')

print(f"✅ SUCCESSFULLY BUILT & ENCRYPTED ALL 22 DAYS FOR ROUTE A & ROUTE B!")
print(f"Route A Days: {len(days_route_a)} | Route B Days: {len(days_route_b)}")
print(f"Ciphertext length: {len(enc_b64)} bytes")
