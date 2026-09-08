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

def build_days_route_a():
    return [
        {
          "day": 1, "date": "Dec 12 (Sat)", "title": "Gateway Arrival & AWD SUV Pickup", "location": "Rovaniemi, Finland", "coords": [66.5039, 25.7294], "gmaps": gmaps("Rovaniemi Central", 66.5039, 25.7294),
          "distance": "10 km (15 mins)", "hotel": "Arctic Light Hotel (Recommended) / Santa's Hotel Santa Claus", "hotelStatus": "pending", "bookingRef": "Unconfirmed in Folder",
          "hotelLinks": [{"name": "Arctic Light Hotel", "url": "https://www.arcticlighthotel.es/", "gmaps": gmaps("Arctic Light Hotel Rovaniemi")}],
          "activities": "Fly SIN -> MUC -> RVN (Arrive 5:15 PM); pick up AWD SUV rental; evening walk in central Rovaniemi; dinner at Nili / Gustav.",
          "scheduleNotes": "Gateway Arrival & AWD SUV Pickup", "tags": ["Flight Arrival", "SUV Rental Pickup", "Rovaniemi Dinner"],
          "foodGuide": food_db["Rovaniemi"],
          "hourlySchedule": [
            {"time": "17:15 - 18:00", "activity": "Land at RVN Airport, clear baggage claim.", "gmaps": gmaps("Rovaniemi Airport")},
            {"time": "18:00 - 18:30", "activity": "Pick up AWD SUV rental desk.", "gmaps": gmaps("Rovaniemi Airport Hertz")},
            {"time": "19:30 - 21:30", "activity": "Dinner at Restaurant Nili or Ravintola Roka.", "gmaps": gmaps("Restaurant Nili Rovaniemi")}
          ],
          "drivingLegs": [{"from": "RVN Airport", "to": "Rovaniemi Center", "dist": "10 km", "time": "15 mins", "route": "E75", "gmaps": gmaps("Rovaniemi Airport to Lordi Square")}],
          "ticketCosts": [{"item": "SUV Rental Day 1", "cost": "~€75/day", "url": "https://www.hertz.fi/"}],
          "auroraSpots": [{"name": "Arktikum Arboretum Shoreline", "desc": "Dark park along river.", "coords": [66.5078, 25.7258], "gmaps": gmaps("Arktikum Arboretum Rovaniemi", 66.5078, 25.7258)}]
        },
        {
          "day": 2, "date": "Dec 13 (Sun)", "title": "Sweden Border Crossing & Torne Valley", "location": "Harads / Storklinten, Sweden", "coords": [65.8252, 21.6886], "gmaps": gmaps("Storklinten Sweden", 65.8252, 21.6886),
          "distance": "235 km (2h 45m)", "hotel": "Stuga i Storklinten (Boden)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Check-in 13 Dec)",
          "activities": "Drive west through Torne Valley; cross border at Tornio-Haparanda; stop at frozen Kukkolankoski rapids; check into cabin; sauna & dinner.",
          "scheduleNotes": "Sweden Border Crossing & Torne Valley", "tags": ["Cross Border", "Torne Valley", "Storklinten Sauna"],
          "foodGuide": food_db["Boden"],
          "hourlySchedule": [
            {"time": "09:00 - 10:30", "activity": "Drive Rovaniemi to Tornio border (125 km).", "gmaps": gmaps("Tornio Border Crossing")},
            {"time": "10:30 - 11:30", "activity": "Stop at Kukkolankoski frozen rapids.", "gmaps": gmaps("Kukkolankoski Rapids")},
            {"time": "14:00 - 15:30", "activity": "Check into Stuga i Storklinten.", "gmaps": gmaps("Storklinten Ski Resort")}
          ],
          "drivingLegs": [{"from": "Rovaniemi", "to": "Storklinten", "dist": "235 km", "time": "2h 45m", "route": "E75 & Route 99", "gmaps": gmaps("Rovaniemi to Storklinten")}],
          "ticketCosts": [{"item": "Rapids Access", "cost": "Free", "url": "https://www.kukkolaforsen.se/"}],
          "auroraSpots": [{"name": "Storklinten Fell Top", "desc": "High vantage point above pine canopy.", "coords": [65.8252, 21.6886], "gmaps": gmaps("Storklinten Fell", 65.8252, 21.6886)}]
        }
    ]

def build_days_route_b():
    return [
        {
          "day": 1, "date": "Dec 12 (Sat)", "title": "Ounasvaara Sunset Forest Walk & Gateway Arrival", "location": "Rovaniemi, Finland", "coords": [66.5039, 25.7294], "gmaps": gmaps("Ounasvaara Winter Trail Rovaniemi", 66.5080, 25.7600),
          "distance": "10 km (15 mins)", "hotel": "Arctic Light Hotel (Recommended) / Santa's Hotel Santa Claus", "hotelStatus": "pending", "bookingRef": "Unconfirmed in Folder",
          "hotelLinks": [{"name": "Arctic Light Hotel", "url": "https://www.arcticlighthotel.es/", "gmaps": gmaps("Arctic Light Hotel Rovaniemi")}],
          "activities": "Fly SIN -> MUC -> RVN (Arrive 5:15 PM); pick up AWD SUV rental; Ounasvaara Winter Forest Walk overlooking frozen Kemijoki river; dinner at Ravintola Roka Street Bistro.",
          "scheduleNotes": "Route B Upgrade: Adds Ounasvaara Winter Sunset Forest Walk", "tags": ["Nature Walk", "Ounasvaara Ridge", "Lapland Street Food"],
          "foodGuide": food_db["Rovaniemi"],
          "hourlySchedule": [
            {"time": "17:15 - 18:00", "activity": "Land at RVN Airport, clear baggage claim.", "gmaps": gmaps("Rovaniemi Airport")},
            {"time": "18:00 - 18:30", "activity": "Pick up AWD SUV rental desk.", "gmaps": gmaps("Rovaniemi Airport Hertz")},
            {"time": "18:45 - 19:45", "activity": "Ounasvaara Winter Trail walk to observation tower (Kemijoki river view).", "gmaps": gmaps("Ounasvaara Lookout Tower Rovaniemi", 66.5080, 25.7600)},
            {"time": "20:00 - 21:30", "activity": "Dinner at Ravintola Roka Street Bistro (Famous Lohikeitto salmon soup & Lapland burgers).", "gmaps": gmaps("Ravintola Roka Street Bistro Rovaniemi")}
          ],
          "drivingLegs": [{"from": "RVN Airport", "to": "Ounasvaara Tower", "dist": "12 km", "time": "15 mins", "route": "E75 & Ounasvaarantie", "gmaps": gmaps("Rovaniemi Airport to Ounasvaara Lookout Tower")}],
          "ticketCosts": [{"item": "Ounasvaara Trail Access", "cost": "Free", "url": "https://www.visitrovaniemi.fi/"}],
          "auroraSpots": [{"name": "Arktikum Arboretum Shoreline", "desc": "Dark park along river.", "coords": [66.5078, 25.7258], "gmaps": gmaps("Arktikum Arboretum Rovaniemi", 66.5078, 25.7258)}]
        },
        {
          "day": 2, "date": "Dec 13 (Sun)", "title": "Gammelstad UNESCO Church Town Snow Walk & Torne Valley", "location": "Harads / Storklinten, Sweden", "coords": [65.8252, 21.6886], "gmaps": gmaps("Gammelstad Church Town Sweden", 65.6458, 22.0289),
          "distance": "250 km (3h 00m)", "hotel": "Stuga i Storklinten (Boden)", "hotelStatus": "confirmed", "bookingRef": "Booking.com (Check-in 13 Dec)",
          "activities": "Drive west through Torne Valley; cross border at Tornio-Haparanda; stop at Kukkolankoski rapids; Gammelstad Church Town UNESCO walking loop (400 medieval cottage village); Storklinten sauna & Empes Gatukök fast food.",
          "scheduleNotes": "Route B Upgrade: Adds Gammelstad UNESCO Village Walk", "tags": ["UNESCO Village", "Gammelstad", "Torne Valley", "Local Cheap Eats"],
          "foodGuide": food_db["Boden"],
          "hourlySchedule": [
            {"time": "08:30 - 10:00", "activity": "Drive Rovaniemi to Tornio border (125 km).", "gmaps": gmaps("Tornio Border Crossing")},
            {"time": "10:00 - 11:15", "activity": "Walk Kukkolankoski frozen rapids suspension bridge.", "gmaps": gmaps("Kukkolankoski Rapids")},
            {"time": "11:45 - 13:30", "activity": "Explore Gammelstad Church Town UNESCO medieval walking loop.", "gmaps": gmaps("Gammelstad Church Town Luleå", 65.6458, 22.0289)},
            {"time": "13:30 - 14:15", "activity": "Lunch at Empes Gatukök Boden (Iconic Swedish burger & sausage grill shack).", "gmaps": gmaps("Empes Gatukök Boden")},
            {"time": "15:00 - 16:30", "activity": "Check into Stuga i Storklinten & prepare wood sauna.", "gmaps": gmaps("Storklinten Ski Resort")}
          ],
          "drivingLegs": [
            {"from": "Tornio", "to": "Gammelstad", "dist": "125 km", "time": "1h 20m", "route": "E4", "gmaps": gmaps("Tornio to Gammelstad Church Town")},
            {"from": "Gammelstad", "to": "Storklinten", "dist": "65 km", "time": "50 mins", "route": "Highway 97", "gmaps": gmaps("Gammelstad to Storklinten")}
          ],
          "ticketCosts": [{"item": "Gammelstad UNESCO Visitor Center", "cost": "Free", "url": "https://www.gammelstad.se/"}],
          "auroraSpots": [{"name": "Storklinten Fell Top", "desc": "High vantage point above pine canopy.", "coords": [65.8252, 21.6886], "gmaps": gmaps("Storklinten Fell", 65.8252, 21.6886)}]
        },
        {
          "day": 10, "date": "Dec 21 (Mon)", "title": "Korouoma Frozen Waterfalls Canyon 5 km Loop Hike", "location": "Posio, Finland", "coords": [66.1089, 28.1633], "gmaps": gmaps("Korouoma Canyon Reserve", 66.1550, 28.1440),
          "distance": "170 km (2h 15m)", "hotel": "Idyllic sauna cottage by the lake (Rantapolku 1, Posio)", "hotelStatus": "confirmed", "bookingRef": "Airbnb Ref: HMYPAMHXW9 (Host: Leena)",
          "activities": "Drive Kemi to Posio; Korouoma Frozen Waterfalls Canyon 5 km loop hike (Koronjää trail past 60m giant blue icefalls & Mammoth Falls); check in at Rantapolku 1 cottage; lakeside sauna.",
          "scheduleNotes": "Route B Major Upgrade: Korouoma Canyon Frozen Icefalls Hike!", "tags": ["Korouoma Canyon", "Frozen Icefalls", "Mammoth Falls", "Canyon Hike"],
          "foodGuide": food_db["Posio"],
          "hourlySchedule": [
            {"time": "08:30 - 10:30", "activity": "Drive east from Kemi to Korouoma Nature Reserve (140 km).", "gmaps": gmaps("Kemi to Korouoma Canyon")},
            {"time": "10:45 - 13:45", "activity": "Hike Koronjää 5 km loop trail in Korouoma Canyon past 60m frozen icefalls & Mammoth Falls.", "gmaps": gmaps("Koronjää Trailhead Korouoma", 66.1550, 28.1440)},
            {"time": "14:00 - 14:30", "activity": "Campfire sausage lunch at Korouoma canyon open lean-to shelter.", "gmaps": gmaps("Korouoma Lean-to Shelter")},
            {"time": "15:00 - 15:30", "activity": "Drive 30 mins to Posio cottage at Rantapolku 1.", "gmaps": gmaps("Rantapolku 1 Posio")},
            {"time": "16:30 - 19:30", "activity": "Lakeside wood sauna & ice hole plunge.", "gmaps": gmaps("Lake Kitkajärvi Posio")}
          ],
          "drivingLegs": [{"from": "Kemi", "to": "Korouoma Trailhead", "dist": "140 km", "time": "1h 50m", "route": "Road 81", "gmaps": gmaps("Kemi to Korouoma Canyon Parking")}],
          "ticketCosts": [{"item": "Crampons / Ice Cleats Rental", "cost": "€12/pair", "url": "https://posiolapland.com/"}],
          "auroraSpots": [{"name": "Rantapolku Private Lake Dock", "desc": "Dark horizon over frozen Lake Kitkajärvi.", "coords": [66.1089, 28.1633], "gmaps": gmaps("Rantapolku Posio", 66.1089, 28.1633)}]
        },
        {
          "day": 15, "date": "Dec 26 (Sat)", "title": "Suomenlinna Sea Fortress Island Walk & Löyly Sauna", "location": "Helsinki, Finland", "coords": [60.1699, 24.9384], "gmaps": gmaps("Suomenlinna Sea Fortress Helsinki", 60.1472, 24.9872),
          "distance": "0 km (Transit)", "hotel": "Hotel U14 Autograph Collection", "hotelStatus": "confirmed", "bookingRef": "Confirmed Hotel U14 Autograph Collection",
          "activities": "Arrive Helsinki Central 9:00 AM; ferry to Suomenlinna UNESCO Sea Fortress for 4 km coastal sea-wall walking loop; lunch at SOUP+MORE (Vanha Kauppahalli Lohikeitto); Löyly seaside smoke sauna & Baltic ice dip.",
          "scheduleNotes": "Route B Upgrade: Adds Suomenlinna Sea Fortress Island Walk & Vanha Kauppahalli Salmon Soup", "tags": ["Suomenlinna", "UNESCO Island Walk", "Vanha Kauppahalli", "Löyly Sauna"],
          "foodGuide": food_db["Helsinki"],
          "hourlySchedule": [
            {"time": "09:00", "activity": "Arrive Helsinki Central Railway Station.", "gmaps": gmaps("Helsinki Central Station")},
            {"time": "09:45 - 10:00", "activity": "15-minute ferry ride from Market Square to Suomenlinna Island.", "gmaps": gmaps("Market Square Helsinki Ferry Terminal")},
            {"time": "10:00 - 12:30", "activity": "4 km coastal sea-wall walking loop around Suomenlinna fortress tunnels & cannons.", "gmaps": gmaps("Suomenlinna Fortress Walk", 60.1472, 24.9872)},
            {"time": "13:00 - 14:00", "activity": "Lunch at Vanha Kauppahalli SOUP+MORE (Famous creamy Finnish salmon soup Lohikeitto for €12).", "gmaps": gmaps("SOUP+MORE Vanha Kauppahalli Helsinki")},
            {"time": "15:00 - 17:30", "activity": "Seaside smoke sauna & Baltic sea ice dip at Löyly Helsinki.", "gmaps": gmaps("Löyly Helsinki Sauna")}
          ],
          "drivingLegs": [{"from": "Market Square", "to": "Suomenlinna", "dist": "3 km (Ferry)", "time": "15 mins", "route": "HSL Ferry", "gmaps": gmaps("Helsinki to Suomenlinna Ferry")}],
          "ticketCosts": [{"item": "Suomenlinna Ferry Ticket", "cost": "€3.10/pax", "url": "https://www.hsl.fi/en"}, {"item": "Löyly Sauna 2h", "cost": "€24/pax", "url": "https://www.loylyhelsinki.fi/en/"}]
        },
        {
          "day": 16, "date": "Dec 27 (Sun)", "title": "Lahemaa Viru Bog Snowshoe Hike & Medieval Tallinn", "location": "Tallinn, Estonia", "coords": [59.4370, 24.7536], "gmaps": gmaps("Viru Bog Study Trail Lahemaa Estonia", 59.4714, 25.6600),
          "distance": "90 km (1h 15m)", "hotel": "Hotel Telegraaf, Autograph Collection (Recommended Marriott)", "hotelStatus": "pending", "bookingRef": "Marriott Autograph Collection in Tallinn Old Town",
          "hotelLinks": [{"name": "Hotel Telegraaf (Marriott)", "url": "https://www.marriott.com/en-us/hotels/tllak-hotel-telegraaf-autograph-collection/overview/", "gmaps": gmaps("Hotel Telegraaf Tallinn")}],
          "activities": "Morning 2h Megastar ferry to Tallinn; 45-min drive east to Lahemaa National Park for Viru Bog 3.5 km snowshoe boardwalk hike; check in at Hotel Telegraaf; cheap pancake feast at Kompressor Pancake Pub.",
          "scheduleNotes": "Route B Major Upgrade: Adds Lahemaa Viru Bog Snowshoe Walk & Kompressor Pancake Pub", "tags": ["Viru Bog", "Lahemaa National Park", "Kompressor Pancakes", "Old Town"],
          "foodGuide": food_db["Tallinn"],
          "hourlySchedule": [
            {"time": "10:30 - 12:30", "activity": "Megastar Ferry transit across Baltic Sea to Tallinn.", "gmaps": gmaps("Tallinn Passenger Port")},
            {"time": "13:00 - 13:45", "activity": "Drive 45 mins east to Lahemaa National Park Viru Bog trailhead (55 km).", "gmaps": gmaps("Viru Bog Parking Lahemaa", 59.4714, 25.6600)},
            {"time": "13:45 - 15:45", "activity": "3.5 km snow-covered peat bog boardwalk hike to Viru Bog observation tower.", "gmaps": gmaps("Viru Bog Watchtower", 59.4714, 25.6600)},
            {"time": "16:30 - 17:00", "activity": "Return drive & check in at Hotel Telegraaf Old Town.", "gmaps": gmaps("Hotel Telegraaf Tallinn")},
            {"time": "18:00 - 19:30", "activity": "Pancake feast at Kompressor Pancake Pub (Giant sweet & savory pancakes for €6-€8!).", "gmaps": gmaps("Kompressor Tallinn")}
          ],
          "drivingLegs": [{"from": "Tallinn Port", "to": "Viru Bog", "dist": "55 km", "time": "45 mins", "route": "Route 1", "gmaps": gmaps("Tallinn Port to Viru Bog Parking")}],
          "ticketCosts": [{"item": "Megastar Ferry Ticket", "cost": "~€32/pax", "url": "https://www.tallinksilja.com/en"}, {"item": "Lahemaa Park Entry", "cost": "Free", "url": "https://loodusegakoos.ee/"}]
        }
    ]

# Construct full multi-route JSON payload
payload = {
    "routes": {
        "routeA": {"name": "Route A: Baseline Itinerary (Classic)", "days": build_days_route_a()},
        "routeB": {"name": "Route B: High-Action Nature & Foodie Explorer", "days": build_days_route_b()}
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

print('✅ Multi-route dataset with Google Maps links generated and encrypted into data.js! Length:', len(enc_b64))
