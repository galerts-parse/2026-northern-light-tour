import json
import subprocess

full_data = {
  "days": [
    {
      "day": 1,
      "date": "Dec 12 (Sat)",
      "title": "Gateway Arrival & AWD SUV Pickup",
      "location": "Rovaniemi, Finland",
      "coords": [66.5039, 25.7294],
      "distance": "10 km (15 mins)",
      "hotel": "Arctic Light Hotel (Recommended) / Santa's Hotel Santa Claus",
      "hotelStatus": "pending",
      "bookingRef": "Unconfirmed in Folder - Marriott Homes & Villas available nearby",
      "hotelLinks": [
        {"name": "Arctic Light Hotel", "url": "https://www.arcticlighthotel.es/"},
        {"name": "Santa's Hotel Santa Claus", "url": "https://santashotels.fi/en/hotels/hotel-santa-claus-rovaniemi/"}
      ],
      "activities": "Fly SIN -> MUC -> RVN (Arrive 5:15 PM); pick up AWD SUV rental; evening walk in central Rovaniemi; dinner at Nili / Gustav.",
      "scheduleNotes": "Gateway Arrival & AWD SUV Pickup",
      "tags": ["Flight Arrival", "SUV Rental Pickup", "Rovaniemi Dinner"],
      "hourlySchedule": [
        {"time": "17:15 - 18:00", "activity": "Land at Rovaniemi Airport (RVN), clear passport control & baggage claim."},
        {"time": "18:00 - 18:30", "activity": "Pick up AWD SUV rental at airport desk; verify winter tires, ice scraper & safety kit."},
        {"time": "18:30 - 18:50", "activity": "Short 10 km drive south on E75 to central Rovaniemi hotel."},
        {"time": "19:30 - 21:30", "activity": "Dinner at Restaurant Nili (traditional Lapland game/reindeer) or Gustav Grill & Bar."},
        {"time": "21:30 - 22:30", "activity": "Evening stroll around Lordi Square & Lumberjack's Candle Bridge."}
      ],
      "drivingLegs": [
        {"from": "RVN Airport", "to": "Rovaniemi Center", "dist": "10 km", "time": "15 mins", "route": "Highway E75"}
      ],
      "ticketCosts": [
        {"item": "AWD SUV Rental Day 1", "cost": "~€75/day", "url": "https://www.hertz.fi/"},
        {"item": "Lapland Dinner at Nili", "cost": "~€55/pax", "url": "https://nili.fi/en/"}
      ],
      "auroraSpots": [
        {"name": "Arktikum Arboretum Shoreline", "desc": "Dark park along Ounasjoki river, 15-min walk from Lordi Square.", "coords": [66.5078, 25.7258]}
      ]
    },
    {
      "day": 2,
      "date": "Dec 13 (Sun)",
      "title": "Sweden Border Crossing & Torne Valley",
      "location": "Harads / Storklinten, Sweden",
      "coords": [65.8252, 21.6886],
      "distance": "235 km (2h 45m)",
      "hotel": "Stuga i Storklinten (Boden)",
      "hotelStatus": "confirmed",
      "bookingRef": "Booking.com (Check-in 13 Dec - Check-out 15 Dec)",
      "activities": "Drive west through Torne Valley; cross border at Tornio-Haparanda; stop at frozen Kukkolankoski river rapids; check into cabin/lodge; evening sauna & Nordic dinner.",
      "scheduleNotes": "Sweden Border Crossing & Torne Valley",
      "tags": ["Cross Border", "Torne Valley", "Storklinten Sauna"],
      "hourlySchedule": [
        {"time": "09:00 - 10:30", "activity": "Depart Rovaniemi west on E75/Road 29 toward Tornio border (125 km, 1h 20m)."},
        {"time": "10:30 - 11:30", "activity": "Cross Finnish-Swedish border at Tornio-Haparanda; stop at Kukkolankoski frozen rapids."},
        {"time": "11:30 - 13:30", "activity": "Drive scenic Route 99 / Highway 94 toward Boden & Storklinten (110 km, 1h 25m)."},
        {"time": "14:00 - 15:30", "activity": "Check in at Stuga i Storklinten; unpack & prepare wood-fired sauna."},
        {"time": "17:00 - 19:30", "activity": "Nordic dinner at Storklinten Restaurant; evening relaxation."},
        {"time": "20:30 - 23:00", "activity": "First night self-drive aurora scan over Storklinten ski slopes."}
      ],
      "drivingLegs": [
        {"from": "Rovaniemi", "to": "Kukkolankoski", "dist": "125 km", "time": "1h 20m", "route": "E75 & Road 29"},
        {"from": "Kukkolankoski", "to": "Storklinten", "dist": "110 km", "time": "1h 25m", "route": "Route 99 & Highway 94"}
      ],
      "ticketCosts": [
        {"item": "Kukkolankoski Rapids Access", "cost": "Free", "url": "https://www.kukkolaforsen.se/"}
      ],
      "auroraSpots": [
        {"name": "Storklinten Fell Top Parking", "desc": "High vantage point above pine canopy away from town lights.", "coords": [65.8252, 21.6886]}
      ]
    },
    {
      "day": 3,
      "date": "Dec 14 (Mon)",
      "title": "Zero-Driving Rest & Nature Day",
      "location": "Harads / Storklinten, Sweden",
      "coords": [65.8252, 21.6886],
      "distance": "0 km (0h - Rest Day)",
      "hotel": "Stuga i Storklinten (Boden)",
      "hotelStatus": "confirmed",
      "bookingRef": "Booking.com (Night 2 of 2)",
      "activities": "Arctic wellness & snow day; outdoor snowshoeing / cross-country skiing through pine forests; wood-fired saunas & cold plunge; night aurora watching.",
      "scheduleNotes": "Zero-Driving Rest & Nature Day",
      "tags": ["Rest Day", "Snowshoeing", "Wood-fired Sauna", "Aurora Spotting"],
      "hourlySchedule": [
        {"time": "09:00 - 10:30", "activity": "Leisurely breakfast in cabin; prepare thermal layers."},
        {"time": "10:30 - 13:00", "activity": "Guided snowshoeing or cross-country ski trek through pine forest."},
        {"time": "13:00 - 14:30", "activity": "Lunch at Storklinten Lodge."},
        {"time": "15:00 - 18:00", "activity": "Traditional Swedish wood-fired sauna & optional snow plunge."},
        {"time": "19:00 - 21:00", "activity": "Cabin dinner & hot berry tea."},
        {"time": "21:00 - 00:00", "activity": "Night aurora watching from cabin deck & clearings."}
      ],
      "drivingLegs": [
        {"from": "Local Cabin Stay", "to": "Local Trails", "dist": "0 km", "time": "0 mins", "route": "None"}
      ],
      "ticketCosts": [
        {"item": "Snowshoe Rental Day", "cost": "~200 SEK (~€18)", "url": "https://storklinten.se/"}
      ],
      "auroraSpots": [
        {"name": "Storklinten Lake Shore", "desc": "Dark open frozen lake clearing right by cabin area.", "coords": [65.8252, 21.6886]}
      ]
    },
    {
      "day": 4,
      "date": "Dec 15 (Tue)",
      "title": "ICEHOTEL 37 Opening Week & Sámi Reindeer",
      "location": "Jukkasjärvi / Kiruna, Sweden",
      "coords": [67.8557, 20.2253],
      "distance": "280 km (3h 30m)",
      "hotel": "Northernlight cabin (Kiruna)",
      "hotelStatus": "confirmed",
      "bookingRef": "Booking.com (Check-in 15 Dec - Check-out 16 Dec)",
      "activities": "Drive north across Swedish Lapland tundra; tour freshly opened ICEHOTEL 37 hand-carved ice art suites & ice chapel (opens Dec 11); drink at original Icebar; reindeer feeding at Nutti Sámi Siida.",
      "scheduleNotes": "ICEHOTEL 37 Opening Week & Sámi Reindeer",
      "tags": ["ICEHOTEL 37", "Icebar", "Sámi Culture", "Reindeer Feeding"],
      "hourlySchedule": [
        {"time": "08:30 - 12:00", "activity": "Scenic morning drive north on Highway 97 & E10 to Jukkasjärvi (280 km, 3h 30m)."},
        {"time": "12:15 - 14:30", "activity": "Tour freshly opened ICEHOTEL 37 hand-carved art suites, ice chapel & drink at Icebar."},
        {"time": "14:45 - 16:30", "activity": "Visit Nutti Sámi Siida; feed reindeer & enjoy traditional Sámi fika around campfire."},
        {"time": "17:00 - 18:00", "activity": "Check into Northernlight cabin in Kiruna."},
        {"time": "19:00 - 21:00", "activity": "Dinner at Steakis / Spis in Kiruna city center."},
        {"time": "21:30 - 23:30", "activity": "Self-drive aurora hunt to Aptasvaara Mountain lookout."}
      ],
      "drivingLegs": [
        {"from": "Storklinten", "to": "Jukkasjärvi", "dist": "280 km", "time": "3h 30m", "route": "E10 North"}
      ],
      "ticketCosts": [
        {"item": "ICEHOTEL Day Entry Ticket", "cost": "~349 SEK (~€30)", "url": "https://www.icehotel.com/"},
        {"item": "Nutti Sámi Siida Reindeer Ticket", "cost": "~220 SEK (~€19)", "url": "https://nuttisami.se/"}
      ],
      "operatorComparisons": [
        {"activity": "Sámi Reindeer Tour", "op1": "Nutti Sámi Siida (220 SEK, Authentic culture)", "op2": "Kiruna Sled Dog Tour (350 SEK)", "rec": "Nutti Sámi Siida"}
      ],
      "auroraSpots": [
        {"name": "Aptasvaara Mountain Lookout", "desc": "15 mins south of Kiruna, high altitude dark sky panorama.", "coords": [67.8100, 20.3500]}
      ]
    },
    {
      "day": 5,
      "date": "Dec 16 (Wed)",
      "title": "Abisko National Park & Aurora Sky Station Night 1",
      "location": "Abisko / Björkliden, Sweden",
      "coords": [68.4064, 18.6811],
      "distance": "100 km (1h 15m)",
      "hotel": "Aurora View Apt – Walk to Train & Ski (Björkliden)",
      "hotelStatus": "confirmed",
      "bookingRef": "Airbnb Ref: HM2B8KDQ4H (Host: Renberget, Check-in 16 Dec - Check-out 19 Dec)",
      "activities": "Scenic mountain drive along Lake Torneträsk; explore Abisko Canyon frozen waterfalls; night open-chairlift ride to mountaintop Aurora Sky Station on Mount Nuolja.",
      "scheduleNotes": "Abisko National Park & Aurora Sky Station Night 1",
      "tags": ["Lake Torneträsk", "Abisko Canyon", "Aurora Sky Station", "Mt Nuolja"],
      "hourlySchedule": [
        {"time": "10:00 - 11:15", "activity": "Scenic mountain drive along E10 past Lake Torneträsk to Abisko/Björkliden (100 km, 1h 15m)."},
        {"time": "11:30 - 13:30", "activity": "Hike snow trails into Abisko Canyon frozen waterfalls & limestone gorge."},
        {"time": "14:00 - 15:30", "activity": "Check into Aurora View Apt in Björkliden."},
        {"time": "17:30 - 19:30", "activity": "Dinner at Abisko Tourist Station Restaurant."},
        {"time": "20:00 - 23:30", "activity": "Open-chairlift ride to mountaintop Aurora Sky Station on Mt Nuolja."}
      ],
      "drivingLegs": [
        {"from": "Kiruna", "to": "Björkliden", "dist": "100 km", "time": "1h 15m", "route": "E10 Scenic Route"}
      ],
      "ticketCosts": [
        {"item": "Aurora Sky Station Chairlift Ticket", "cost": "~895 SEK (~€78)", "url": "https://www.stfturist.se/en/explore/aurora-sky-station/"}
      ],
      "auroraSpots": [
        {"name": "Mount Nuolja Sky Station Summit", "desc": "World famous microclimate Blue Hole elevation view.", "coords": [68.3614, 18.7208]}
      ]
    },
    {
      "day": 6,
      "date": "Dec 17 (Thu)",
      "title": "Zero-Driving Alpine Tundra & Aurora Blue Hole Night 2",
      "location": "Abisko / Björkliden, Sweden",
      "coords": [68.4064, 18.6811],
      "distance": "0 km (0h - Rest Day)",
      "hotel": "Aurora View Apt – Walk to Train & Ski (Björkliden)",
      "hotelStatus": "confirmed",
      "bookingRef": "Airbnb Ref: HM2B8KDQ4H (Night 2 of 3)",
      "activities": "Guided alpine snowmobile safari across mountain passes toward the Norwegian border (Riksgränsen); marvel at Lapporten U-shaped valley; night aurora watch at Lake Torneträsk shores.",
      "scheduleNotes": "Zero-Driving Alpine Tundra & Aurora Blue Hole Night 2",
      "tags": ["Snowmobile Safari", "Riksgränsen", "Lapporten Valley", "Aurora Blue Hole"],
      "hourlySchedule": [
        {"time": "09:30 - 10:00", "activity": "Meet snowmobile guide at Björkliden / Abisko Guesthouse base; gear fitting."},
        {"time": "10:00 - 13:00", "activity": "3-hour guided snowmobile safari up alpine passes toward Norwegian border & Lapporten."},
        {"time": "13:30 - 15:00", "activity": "Warm lunch at Björkliden Hotel Fjället."},
        {"time": "15:30 - 18:00", "activity": "Rest & warm sauna in apartment."},
        {"time": "20:30 - 23:30", "activity": "Self-drive aurora hunt to Lake Torneträsk beach parking (E10 km 115)."}
      ],
      "drivingLegs": [
        {"from": "Björkliden Base", "to": "Abisko Trails", "dist": "0 km", "time": "0 mins", "route": "Local Snowmobile"}
      ],
      "ticketCosts": [
        {"item": "Guided Snowmobile Safari (3h)", "cost": "~1,950 SEK (~€170)", "url": "https://abiskoguesthouse.com/"}
      ],
      "operatorComparisons": [
        {"activity": "Snowmobile Safari", "op1": "Abisko Guesthouse (1,950 SEK, small groups)", "op2": "Visit Abisko (2,100 SEK)", "rec": "Abisko Guesthouse"}
      ],
      "auroraSpots": [
        {"name": "Lake Torneträsk Beach Layby (E10 km 115)", "desc": "Wide open vista facing north over frozen lake.", "coords": [68.3500, 18.8000]}
      ]
    },
    {
      "day": 7,
      "date": "Dec 18 (Fri)",
      "title": "Zero-Driving Husky Safari & Peak Aurora Night 3",
      "location": "Abisko / Björkliden, Sweden",
      "coords": [68.4064, 18.6811],
      "distance": "0 km (0h - Rest Day)",
      "hotel": "Aurora View Apt – Walk to Train & Ski (Björkliden)",
      "hotelStatus": "confirmed",
      "bookingRef": "Airbnb Ref: HM2B8KDQ4H (Night 3 of 3)",
      "activities": "Morning 3-hour husky sledding safari through Arctic birch forest; visit Silverfallet frozen waterfall beach; dinner at Abisko Mountain Lodge; night aurora watch.",
      "scheduleNotes": "Zero-Driving Husky Safari & Peak Aurora Night 3",
      "tags": ["Husky Safari", "Silverfallet Waterfall", "Abisko Mountain Lodge"],
      "hourlySchedule": [
        {"time": "09:00 - 12:30", "activity": "Morning 3-hour husky sledding safari through Arctic birch forest & frozen rivers."},
        {"time": "13:00 - 14:30", "activity": "Lunch & warm soup."},
        {"time": "15:00 - 16:30", "activity": "Short drive to Silverfallet (Rakkasjokk) frozen waterfall beach."},
        {"time": "18:30 - 20:30", "activity": "Gourmet dinner at Abisko Mountain Lodge."},
        {"time": "21:00 - 00:00", "activity": "Final night aurora watch at Björkliden Overlook."}
      ],
      "drivingLegs": [
        {"from": "Björkliden", "to": "Silverfallet", "dist": "5 km", "time": "8 mins", "route": "E10"}
      ],
      "ticketCosts": [
        {"item": "3-Hour Husky Sledding Safari", "cost": "~2,500 SEK (~€218)", "url": "https://visitabisko.com/"}
      ],
      "operatorComparisons": [
        {"activity": "Husky Safari", "op1": "Visit Abisko (2,500 SEK, thermal gear included)", "op2": "Kiruna Dog Sled (2,200 SEK + transport)", "rec": "Visit Abisko"}
      ],
      "auroraSpots": [
        {"name": "Björkliden Overlook Layby", "desc": "Elevated panorama overlooking Lake Torneträsk & Lapporten.", "coords": [68.4064, 18.6811]}
      ]
    },
    {
      "day": 8,
      "date": "Dec 19 (Sat)",
      "title": "Finland Re-entry & SnowCastle of Kemi",
      "location": "Kemi, Finland",
      "coords": [65.7363, 24.5637],
      "distance": "340 km (4h 00m)",
      "hotel": "Cozy Apartment by the Sea 2 Rooms (Kemi)",
      "hotelStatus": "confirmed",
      "bookingRef": "Booking.com (Check-in 19 Dec - Check-out 21 Dec)",
      "activities": "Scenic cross-border drive south from Swedish mountains to Finnish Bothnian coast; cross border at Tornio; check in; explore SnowExperience365 indoor ice castle and ice bar.",
      "scheduleNotes": "Finland Re-entry & SnowCastle of Kemi",
      "tags": ["Cross Border", "Bothnian Coast", "SnowExperience365", "Ice Castle"],
      "hourlySchedule": [
        {"time": "08:30 - 12:30", "activity": "Cross-border drive south from Björkliden via Kiruna & Gällivare on E10 (340 km, 4h)."},
        {"time": "12:30 - 13:30", "activity": "Cross Swedish-Finnish border at Haparanda/Tornio."},
        {"time": "14:00 - 15:00", "activity": "Check into Cozy Apartment by the Sea in Kemi."},
        {"time": "15:30 - 18:00", "activity": "Explore SnowExperience365 indoor ice castle, ice bar & ice sculptures."},
        {"time": "18:30 - 20:30", "activity": "Seafood dinner at Restaurant Lumihiutale overlooking Bothnian Bay."}
      ],
      "drivingLegs": [
        {"from": "Björkliden", "to": "Kemi", "dist": "340 km", "time": "4h 00m", "route": "E10 & E4"}
      ],
      "ticketCosts": [
        {"item": "SnowExperience365 Ticket", "cost": "€18/pax", "url": "https://experience365.fi/"}
      ],
      "auroraSpots": [
        {"name": "Inner Harbour Coastal Promenade", "desc": "Dark shoreline facing north over frozen Bothnian Bay.", "coords": [65.7363, 24.5637]}
      ]
    },
    {
      "day": 9,
      "date": "Dec 20 (Sun)",
      "title": "Sampo Icebreaker Cruise & Sea Ice Floating",
      "location": "Kemi, Finland",
      "coords": [65.7363, 24.5637],
      "distance": "20 km (20m local)",
      "hotel": "Cozy Apartment by the Sea 2 Rooms (Kemi)",
      "hotelStatus": "confirmed",
      "bookingRef": "Booking.com (Night 2 of 2)",
      "activities": "Official Sampo Icebreaker Cruise (operational season starts Dec 18!): crush through solid sea ice, engine room tour, survival drysuit floating in open sea-ice pool; coastal sauna.",
      "scheduleNotes": "Sampo Icebreaker Cruise & Sea Ice Floating",
      "tags": ["Sampo Icebreaker", "Drysuit Floating", "Frozen Sea Ice", "Coastal Sauna"],
      "hourlySchedule": [
        {"time": "08:30 - 09:15", "activity": "Breakfast; 15 km drive south to Ajos Harbour (20 mins)."},
        {"time": "09:30 - 13:00", "activity": "Official Sampo Icebreaker Cruise: crush sea ice, engine room tour, survival drysuit ice float."},
        {"time": "13:15 - 14:30", "activity": "Hot lunch buffet at SnowCastle Lumihiutale Restaurant."},
        {"time": "15:30 - 18:00", "activity": "Relaxing coastal sauna session."},
        {"time": "19:00 - 21:00", "activity": "Dinner in Kemi town center."}
      ],
      "drivingLegs": [
        {"from": "Kemi Center", "to": "Ajos Harbour", "dist": "15 km", "time": "20 mins", "route": "Ajos Road"}
      ],
      "ticketCosts": [
        {"item": "Sampo Icebreaker Cruise Ticket", "cost": "€340/pax", "url": "https://experience365.fi/icebreaker-sampo/"}
      ],
      "operatorComparisons": [
        {"activity": "Icebreaker Cruise", "op1": "Sampo Icebreaker (Kemi, €340, Includes drysuit float & meal)", "op2": "Polar Explorer (Sweden border, €320)", "rec": "Sampo Icebreaker"}
      ],
      "auroraSpots": [
        {"name": "Ajos Harbour Breakwater", "desc": "Unobstructed dark horizon over frozen gulf ice.", "coords": [65.6700, 24.5500]}
      ]
    },
    {
      "day": 10,
      "date": "Dec 21 (Mon)",
      "title": "Check-in Rantapolku 1 Posio",
      "location": "Posio, Finland",
      "coords": [66.1089, 28.1633],
      "distance": "170 km (2h 15m)",
      "hotel": "Idyllic sauna cottage by the lake (Rantapolku 1, Posio)",
      "hotelStatus": "confirmed",
      "bookingRef": "Airbnb Ref: HMYPAMHXW9 (Host: Leena, Check-in 21 Dec - Check-out 23 Dec)",
      "activities": "Scenic drive east to Posio; stop at S-Market Posio for groceries; check into Airbnb (Rantapolku 1); evening lakeside sauna & quiet aurora watch.",
      "scheduleNotes": "Check-in Rantapolku 1 Posio (Airbnb Booked)",
      "tags": ["Posio Cottage", "Lakeside Sauna", "Local Groceries", "Quiet Aurora"],
      "hourlySchedule": [
        {"time": "10:00 - 12:15", "activity": "Scenic drive east from Kemi via Ranua to Posio (170 km, 2h 15m)."},
        {"time": "12:30 - 13:30", "activity": "Stop at S-Market Posio for grocery stocking (sausage, firewood snacks, drinks)."},
        {"time": "14:00 - 15:30", "activity": "Check into lakeside cottage at Rantapolku 1, Posio."},
        {"time": "16:00 - 19:00", "activity": "Fire up private lakeside wood sauna & ice hole plunge."},
        {"time": "19:30 - 21:00", "activity": "Home-cooked cabin dinner."},
        {"time": "21:00 - 00:00", "activity": "Aurora watch directly from private frozen lake dock."}
      ],
      "drivingLegs": [
        {"from": "Kemi", "to": "Posio", "dist": "170 km", "time": "2h 15m", "route": "Road 81 & Road 863"}
      ],
      "ticketCosts": [
        {"item": "Grocery Stocking S-Market", "cost": "~€60", "url": "https://www.s-kaupat.fi/"}
      ],
      "auroraSpots": [
        {"name": "Rantapolku Lake Kitkajärvi Private Dock", "desc": "Zero light pollution, direct northern view over frozen lake.", "coords": [66.1089, 28.1633]}
      ]
    },
    {
      "day": 11,
      "date": "Dec 22 (Tue)",
      "title": "Riisitunturi National Park World-Class Tykky Trees",
      "location": "Posio, Finland",
      "coords": [66.1089, 28.1633],
      "distance": "60 km (50m roundtrip)",
      "hotel": "Idyllic sauna cottage by the lake (Rantapolku 1, Posio)",
      "hotelStatus": "confirmed",
      "bookingRef": "Airbnb Ref: HMYPAMHXW9 (Night 2 of 2)",
      "activities": "25-minute drive to Riisitunturi National Park; 10:30 AM golden twilight snowshoe hike (Riisin rääpäsy 4.3 km trail) among Europe's heaviest Tykky snow-sculpture trees; campfire lunch at wilderness hut.",
      "scheduleNotes": "Riisitunturi National Park World-Class Tykky Trees",
      "tags": ["Riisitunturi", "Tykky Snow Trees", "Golden Twilight Hike", "Campfire Lunch"],
      "hourlySchedule": [
        {"time": "09:45 - 10:15", "activity": "25-minute drive from cottage to Riisitunturi National Park trailhead (30 km)."},
        {"time": "10:30 - 13:30", "activity": "Golden twilight snowshoe hike on Riisin rääpäsy 4.3 km trail through Tykky snow trees."},
        {"time": "13:30 - 14:30", "activity": "Campfire sausage & hot berry tea lunch at open wilderness hut."},
        {"time": "15:00 - 15:30", "activity": "Return drive to Posio cottage."},
        {"time": "17:00 - 19:30", "activity": "Lakeside sauna session."},
        {"time": "20:00 - 23:30", "activity": "Night aurora photo hunt at Riisitunturi trailhead."}
      ],
      "drivingLegs": [
        {"from": "Posio Cottage", "to": "Riisitunturi Trailhead", "dist": "30 km", "time": "25 mins", "route": "Road 3470"}
      ],
      "ticketCosts": [
        {"item": "Snowshoe Rental per Pair", "cost": "€20/day", "url": "https://posiolapland.com/"},
        {"item": "Guided Tykky Hike (Optional)", "cost": "€85/pax", "url": "https://posiolapland.com/"}
      ],
      "operatorComparisons": [
        {"activity": "Tykky Snowshoe Hike", "op1": "Self-guided with map (€20 rental)", "op2": "Naali Lodge Guided (€85/pax)", "rec": "Self-Guided (Well marked trail)"}
      ],
      "auroraSpots": [
        {"name": "Riisitunturi Park Base Parking", "desc": "Pristine Arctic fell skies framed by heavy snow trees.", "coords": [66.2167, 28.5667]}
      ]
    },
    {
      "day": 12,
      "date": "Dec 23 (Wed)",
      "title": "Easy 1h Hop to Iso-Syöte Fell",
      "location": "Iso-Syöte, Finland",
      "coords": [65.6265, 27.6083],
      "distance": "75 km (55 mins)",
      "hotel": "Apartment with a view at the top of Iso-Syöte (Host Arto)",
      "hotelStatus": "confirmed",
      "bookingRef": "Airbnb Confirmed (Host: Arto)",
      "activities": "Relaxed morning in Posio; short 55-minute drive to Iso-Syöte fell summit; check in; afternoon downhill skiing or panoramic fell-top spa; dinner at Restaurant Hilltop.",
      "scheduleNotes": "Easy 1h Hop to Iso-Syöte Fell",
      "tags": ["Fell Summit", "Downhill Skiing", "Fell-top Spa", "Restaurant Hilltop"],
      "hourlySchedule": [
        {"time": "10:30 - 11:30", "activity": "Short 55-minute drive south from Posio to Iso-Syöte fell summit (75 km)."},
        {"time": "12:00 - 13:30", "activity": "Check into Arto's view apartment at top of Iso-Syöte."},
        {"time": "13:30 - 16:30", "activity": "Afternoon downhill skiing on Iso-Syöte slopes or Arctic fell-top spa session."},
        {"time": "17:00 - 19:00", "activity": "Private in-apartment sauna."},
        {"time": "19:30 - 21:30", "activity": "Dinner at Restaurant Hilltop Iso-Syöte."}
      ],
      "drivingLegs": [
        {"from": "Posio", "to": "Iso-Syöte Fell Top", "dist": "75 km", "time": "55 mins", "route": "Road 863"}
      ],
      "ticketCosts": [
        {"item": "Iso-Syöte Ski Pass 3h", "cost": "€42/pax", "url": "https://syote.fi/en/"},
        {"item": "Fell-top Spa Entry", "cost": "€25/pax", "url": "https://hotellisyoete.fi/en/"}
      ],
      "auroraSpots": [
        {"name": "Iso-Syöte Fell Summit Deck", "desc": "Highest elevation in southern Lapland, 360-degree horizon.", "coords": [65.6265, 27.6083]}
      ]
    },
    {
      "day": 13,
      "date": "Dec 24 (Thu)",
      "title": "Confirmed Booking: Iso-Syöte Treehouse / Igloo (Christmas Eve)",
      "location": "Iso-Syöte, Finland",
      "coords": [65.6265, 27.6083],
      "distance": "0 km (0h - Rest Day)",
      "hotel": "Syöte Igloos / Iso-Syöte Treehouse",
      "hotelStatus": "confirmed",
      "bookingRef": "Booking.com (Check-in 24 Dec - Check-out 25 Dec)",
      "activities": "Check into your confirmed Iso-Syöte Treehouse / Igloo (luggage transferred across path); Christmas Eve feast, private fell-top sauna, panoramic glass view of snow-covered spruce canopy.",
      "scheduleNotes": "Confirmed Booking: Iso-Syöte Treehouse / Igloos (Christmas Eve)",
      "tags": ["Christmas Eve", "Glass Igloo / Treehouse", "Private Sauna", "Holiday Feast"],
      "hourlySchedule": [
        {"time": "11:00 - 12:00", "activity": "Luggage transfer across path into confirmed Syöte Glass Igloo / Treehouse."},
        {"time": "12:00 - 14:00", "activity": "Christmas Eve champagne toast with panoramic view of snow-draped spruce canopy."},
        {"time": "14:30 - 17:00", "activity": "Private glass sauna session overlooking fell summit."},
        {"time": "18:00 - 21:00", "activity": "Traditional Finnish Christmas Eve Buffet Feast at Hotel Iso-Syöte."},
        {"time": "21:00 - 02:00", "activity": "Night aurora watch directly from glass roof bed."}
      ],
      "drivingLegs": [
        {"from": "Iso-Syöte Top", "to": "Syöte Igloos", "dist": "0.5 km", "time": "2 mins", "route": "Fell Road"}
      ],
      "ticketCosts": [
        {"item": "Christmas Eve Gala Buffet", "cost": "€75/pax", "url": "https://hotellisyoete.fi/en/"}
      ],
      "auroraSpots": [
        {"name": "Glass Roof Igloo Bedroom", "desc": "Watch northern lights while lying in bed inside heated glass dome.", "coords": [65.6265, 27.6083]}
      ]
    },
    {
      "day": 14,
      "date": "Dec 25 (Fri)",
      "title": "Santa Claus Village & VR Express Sleeper Train",
      "location": "En-Route VR Night Train",
      "coords": [66.5039, 25.7294],
      "distance": "160 km (2h 00m)",
      "hotel": "VR Santa Claus Express Sleeper Train (9:00 PM)",
      "hotelStatus": "confirmed",
      "bookingRef": "VR Train Booking (Rovaniemi -> Helsinki Central)",
      "activities": "Christmas Day morning at Iso-Syöte; drive to Rovaniemi; explore Santa Claus Village & post office; return AWD SUV at station ($0 drop-off fee); board 9:00 PM VR Santa Claus Express Sleeper Train.",
      "scheduleNotes": "Confirmed Booking: VR Sleeper Train 9:00 PM",
      "tags": ["Santa Claus Village", "Post Office", "SUV Return", "VR Sleeper Train"],
      "hourlySchedule": [
        {"time": "10:00 - 12:00", "activity": "Christmas morning drive north from Iso-Syöte to Rovaniemi (160 km, 2h)."},
        {"time": "12:15 - 16:30", "activity": "Explore Santa Claus Village: cross Arctic Circle line, visit Main Post Office & meet Santa."},
        {"time": "17:00 - 18:30", "activity": "Christmas Day dinner in Rovaniemi."},
        {"time": "19:00 - 20:00", "activity": "Return AWD SUV rental at Rovaniemi Railway Station."},
        {"time": "20:15 - 20:45", "activity": "Board VR Santa Claus Express Sleeper Train (Private en-suite cabin)."},
        {"time": "21:00", "activity": "Overnight sleeper train departs Rovaniemi for Helsinki."}
      ],
      "drivingLegs": [
        {"from": "Iso-Syöte", "to": "Rovaniemi Station", "dist": "160 km", "time": "2h 00m", "route": "Road 81"}
      ],
      "ticketCosts": [
        {"item": "VR Sleeper Cabin (2-person)", "cost": "~€210", "url": "https://www.vr.fi/en"}
      ],
      "auroraSpots": [
        {"name": "Train Cabin Window", "desc": "Scenery and night sky passing outside sleeper train window.", "coords": [65.0121, 25.4651]}
      ]
    },
    {
      "day": 15,
      "date": "Dec 26 (Sat)",
      "title": "Helsinki Boxing Day & Löyly Smoke Sauna",
      "location": "Helsinki, Finland",
      "coords": [60.1699, 24.9384],
      "distance": "0 km (Transit)",
      "hotel": "Hotel U14 Autograph Collection",
      "hotelStatus": "confirmed",
      "bookingRef": "Confirmed Hotel U14 Autograph Collection",
      "activities": "Arrive Helsinki Central 9:00 AM (Boxing Day); explore Oodi Central Library & Senate Square; afternoon seaside smoke sauna & Baltic ice dip at Löyly.",
      "scheduleNotes": "Confirmed Booking: Hotel U14 Autograph Collection",
      "tags": ["Oodi Library", "Senate Square", "Löyly Sauna", "Baltic Ice Dip"],
      "hourlySchedule": [
        {"time": "09:00", "activity": "Arrive Helsinki Central Railway Station on VR Sleeper Train."},
        {"time": "09:30 - 10:30", "activity": "Drop luggage at Hotel U14 Autograph Collection."},
        {"time": "10:45 - 13:00", "activity": "Explore Oodi Central Library, Senate Square & Helsinki Cathedral."},
        {"time": "14:00 - 16:30", "activity": "Seaside smoke sauna & Baltic sea ice dip at Löyly Helsinki."},
        {"time": "17:00 - 18:30", "activity": "Check in & refresh at Hotel U14."},
        {"time": "19:00 - 21:30", "activity": "Boxing Day dinner at Version Eatery & Garden (Hotel U14)."}
      ],
      "drivingLegs": [
        {"from": "Helsinki Central", "to": "Löyly Sauna", "dist": "3 km", "time": "10 mins", "route": "Tram / Taxi"}
      ],
      "ticketCosts": [
        {"item": "Löyly Sauna 2h Ticket", "cost": "€24/pax", "url": "https://www.loylyhelsinki.fi/en/"}
      ],
      "operatorComparisons": [
        {"activity": "Helsinki Public Sauna", "op1": "Löyly (Modern, Baltic ice dip, €24)", "op2": "Kotiharjun (Traditional 1928 wood sauna, €18)", "rec": "Löyly"}
      ]
    },
    {
      "day": 16,
      "date": "Dec 27 (Sun)",
      "title": "Baltic Sea Ferry Transit & Medieval Tallinn",
      "location": "Tallinn, Estonia",
      "coords": [59.4370, 24.7536],
      "distance": "0 km (Ferry)",
      "hotel": "Hotel Telegraaf, Autograph Collection (Recommended Marriott)",
      "hotelStatus": "pending",
      "bookingRef": "Marriott Autograph Collection in Tallinn Old Town",
      "hotelLinks": [
        {"name": "Hotel Telegraaf (Marriott)", "url": "https://www.marriott.com/en-us/hotels/tllak-hotel-telegraaf-autograph-collection/overview/"}
      ],
      "activities": "Morning 2-hour Megastar express ferry across Baltic Sea; explore UNESCO medieval Old Town, Town Hall Christmas Market, and Toompea Hill vista.",
      "scheduleNotes": "Baltic Sea Ferry Transit & Medieval Tallinn",
      "tags": ["Megastar Ferry", "UNESCO Old Town", "Christmas Market", "Toompea Hill"],
      "hourlySchedule": [
        {"time": "09:00 - 09:45", "activity": "Tram to West Harbour Terminal 2 (Helsinki)."},
        {"time": "10:30 - 12:30", "activity": "Board Tallink Megastar Express Ferry across Baltic Sea to Tallinn (2h)."},
        {"time": "13:00 - 14:00", "activity": "Check into Hotel Telegraaf, Autograph Collection in Old Town."},
        {"time": "14:30 - 17:30", "activity": "Explore UNESCO Old Town, Town Hall Christmas Market & St. Olaf Church."},
        {"time": "18:00 - 19:30", "activity": "Sunset panorama from Toompea Hill (Kohtuotsa viewing platform)."},
        {"time": "20:00 - 22:00", "activity": "Medieval feast dinner at Olde Hansa."}
      ],
      "drivingLegs": [
        {"from": "Tallinn Port", "to": "Hotel Telegraaf", "dist": "2 km", "time": "7 mins", "route": "Taxi / Walk"}
      ],
      "ticketCosts": [
        {"item": "Megastar Ferry Deck Ticket", "cost": "~€32/pax", "url": "https://www.tallinksilja.com/en"}
      ]
    },
    {
      "day": 17,
      "date": "Dec 28 (Mon)",
      "title": "Flight TLL -> ARN to Stockholm",
      "location": "Stockholm, Sweden",
      "coords": [59.3293, 18.0686],
      "distance": "0 km (Flight)",
      "hotel": "Sheraton Stockholm Hotel (Recommended Marriott)",
      "hotelStatus": "pending",
      "bookingRef": "Marriott Waterfront Hotel near Central Station",
      "hotelLinks": [
        {"name": "Sheraton Stockholm (Marriott)", "url": "https://www.marriott.com/en-us/hotels/stosi-sheraton-stockholm-hotel/overview/"}
      ],
      "activities": "Morning visit to Kadriorg Palace or Seaplane Harbour; late afternoon flight to Stockholm (TLL -> ARN); evening walk through illuminated Norrmalm & Nybroplan.",
      "scheduleNotes": "Flight TLL -> ARN to Stockholm",
      "tags": ["Kadriorg Palace", "Flight TLL-ARN", "Norrmalm", "Nybroplan Illuminations"],
      "hourlySchedule": [
        {"time": "09:30 - 11:30", "activity": "Visit Kadriorg Art Museum Palace grounds & Seaplane Harbour."},
        {"time": "12:00 - 13:00", "activity": "Lunch in Tallinn Creative City (Telliskivi)."},
        {"time": "13:30 - 14:00", "activity": "Taxi to Tallinn Airport (TLL)."},
        {"time": "15:30 - 16:30", "activity": "Flight TLL -> ARN (SAS / Ryanair, 1h)."},
        {"time": "17:00 - 17:30", "activity": "Arlanda Express train to Stockholm Central (18 mins)."},
        {"time": "18:00 - 18:30", "activity": "Check into Sheraton Stockholm Hotel."},
        {"time": "19:00 - 21:30", "activity": "Evening walk through winter light illuminations at Norrmalm & Nybroplan."}
      ],
      "drivingLegs": [
        {"from": "Stockholm Arlanda Airport", "to": "Stockholm Central", "dist": "40 km", "time": "18 mins", "route": "Arlanda Express Train"}
      ],
      "ticketCosts": [
        {"item": "Arlanda Express Train Ticket", "cost": "~320 SEK (~€28)", "url": "https://www.arlandaexpress.com/"}
      ]
    },
    {
      "day": 18,
      "date": "Dec 29 (Tue)",
      "title": "Stockholm Core Day 1",
      "location": "Stockholm, Sweden",
      "coords": [59.3293, 18.0686],
      "distance": "0 km (Metro/Walk)",
      "hotel": "Sheraton Stockholm Hotel (Recommended Marriott)",
      "hotelStatus": "pending",
      "bookingRef": "Marriott Waterfront Hotel",
      "hotelLinks": [
        {"name": "Sheraton Stockholm (Marriott)", "url": "https://www.marriott.com/en-us/hotels/stosi-sheraton-stockholm-hotel/overview/"}
      ],
      "activities": "Full day of historic Stockholm: cobblestone alleys of Gamla Stan (Old Town), Royal Palace, Stortorget, and Nobel Prize Museum.",
      "scheduleNotes": "Stockholm Core Day 1",
      "tags": ["Gamla Stan", "Royal Palace", "Stortorget", "Nobel Prize Museum"],
      "hourlySchedule": [
        {"time": "09:30 - 12:00", "activity": "Guided walking tour of Gamla Stan (Old Town) & Stortorget square."},
        {"time": "12:15 - 13:30", "activity": "Royal Palace of Stockholm interior tour & Changing of the Guard."},
        {"time": "13:30 - 14:30", "activity": "Traditional Swedish meatball lunch at Bakfickan / Den Gyldene Freden."},
        {"time": "15:00 - 17:00", "activity": "Tour Nobel Prize Museum."},
        {"time": "18:30 - 21:00", "activity": "Dinner in Gamla Stan."}
      ],
      "drivingLegs": [
        {"from": "Sheraton Stockholm", "to": "Gamla Stan", "dist": "1 km", "time": "10 mins", "route": "Walk"}
      ],
      "ticketCosts": [
        {"item": "Royal Palace Ticket", "cost": "~190 SEK (~€16)", "url": "https://www.kungligaslotten.se/english.html"},
        {"item": "Nobel Prize Museum Ticket", "cost": "~140 SEK (~€12)", "url": "https://nobelprizemuseum.se/en/"}
      ]
    },
    {
      "day": 19,
      "date": "Dec 30 (Wed)",
      "title": "Stockholm Core Day 2",
      "location": "Stockholm, Sweden",
      "coords": [59.3293, 18.0686],
      "distance": "0 km (Ferry/Tram)",
      "hotel": "Sheraton Stockholm Hotel (Recommended Marriott)",
      "hotelStatus": "pending",
      "bookingRef": "Marriott Waterfront Hotel",
      "hotelLinks": [
        {"name": "Sheraton Stockholm (Marriott)", "url": "https://www.marriott.com/en-us/hotels/stosi-sheraton-stockholm-hotel/overview/"}
      ],
      "activities": "Maritime & culture day: tour 17th-century Vasa Museum, explore Djurgården island & Skansen, or visit ABBA The Museum; traditional Swedish dinner.",
      "scheduleNotes": "Stockholm Core Day 2",
      "tags": ["Vasa Museum", "Djurgården", "Skansen", "ABBA Museum"],
      "hourlySchedule": [
        {"time": "09:30 - 12:00", "activity": "Tour 17th-century Vasa Museum (preserved 1628 warship)."},
        {"time": "12:15 - 13:30", "activity": "Lunch on Djurgården island."},
        {"time": "13:30 - 16:30", "activity": "Visit ABBA The Museum or Skansen Open Air Museum."},
        {"time": "17:00 - 18:30", "activity": "Ferry ride back across Stockholm harbour."},
        {"time": "19:30 - 22:00", "activity": "Dinner at Oaxen Krog / Pelikan."}
      ],
      "drivingLegs": [
        {"from": "Sheraton Stockholm", "to": "Vasa Museum", "dist": "3 km", "time": "15 mins", "route": "Tram 7"}
      ],
      "ticketCosts": [
        {"item": "Vasa Museum Ticket", "cost": "~190 SEK (~€16)", "url": "https://www.vasamuseet.se/en"},
        {"item": "ABBA The Museum Ticket", "cost": "~290 SEK (~€25)", "url": "https://abbathemuseum.com/en/"}
      ]
    },
    {
      "day": 20,
      "date": "Dec 31 (Thu)",
      "title": "High-Speed Train & NYE Tivoli Celebration",
      "location": "Copenhagen, Denmark",
      "coords": [55.6761, 12.5683],
      "distance": "0 km (Train)",
      "hotel": "Copenhagen Marriott Hotel (Recommended Marriott)",
      "hotelStatus": "pending",
      "bookingRef": "Marriott Harborfront Hotel near Tivoli",
      "hotelLinks": [
        {"name": "Copenhagen Marriott Hotel", "url": "https://www.marriott.com/en-us/hotels/cphdk-copenhagen-marriott-hotel/overview/"}
      ],
      "activities": "Morning SJ High-Speed Train from Stockholm Central to Copenhagen Central (5h 10m via Öresund Bridge); check in; New Year's Eve gala dinner & midnight fireworks at Tivoli Gardens.",
      "scheduleNotes": "High-Speed Train & NYE Tivoli Celebration",
      "tags": ["SJ High-Speed Train", "Öresund Bridge", "NYE Gala", "Tivoli Fireworks"],
      "hourlySchedule": [
        {"time": "08:20 - 13:30", "activity": "SJ High-Speed Train from Stockholm Central to Copenhagen Central (5h 10m via Öresund Bridge)."},
        {"time": "14:00 - 15:00", "activity": "Check into Copenhagen Marriott Hotel."},
        {"time": "15:30 - 18:00", "activity": "Pre-NYE stroll around Nyhavn harbour."},
        {"time": "19:00 - 23:30", "activity": "New Year's Eve Gala Dinner at Tivoli Gardens Restaurant."},
        {"time": "00:00 - 01:00", "activity": "Spectacular Midnight Fireworks over Tivoli Gardens."}
      ],
      "drivingLegs": [
        {"from": "Stockholm Central", "to": "Copenhagen Central", "dist": "650 km", "time": "5h 10m", "route": "SJ High Speed Train"}
      ],
      "ticketCosts": [
        {"item": "SJ High-Speed Train Ticket", "cost": "~€65/pax", "url": "https://www.sj.se/en"},
        {"item": "Tivoli NYE Admission & Gala", "cost": "~1,170 DKK (~€157)", "url": "https://www.tivoli.dk/en"}
      ]
    },
    {
      "day": 21,
      "date": "Jan 01 (Fri)",
      "title": "New Year's Day in Copenhagen",
      "location": "Copenhagen, Denmark",
      "coords": [55.6761, 12.5683],
      "distance": "0 km (Metro/Walk)",
      "hotel": "Copenhagen Marriott Hotel (Recommended Marriott)",
      "hotelStatus": "pending",
      "bookingRef": "Marriott Harborfront Hotel",
      "hotelLinks": [
        {"name": "Copenhagen Marriott Hotel", "url": "https://www.marriott.com/en-us/hotels/cphdk-copenhagen-marriott-hotel/overview/"}
      ],
      "activities": "Relaxed New Year's Day stroll; view CopenHill rooftop architecture, Amalienborg Palace royal guard change, and Nyhavn / Strøget cafe culture.",
      "scheduleNotes": "New Year's Day in Copenhagen",
      "tags": ["CopenHill", "Amalienborg Palace", "Nyhavn", "Strøget Cafe Culture"],
      "hourlySchedule": [
        {"time": "10:30 - 12:00", "activity": "Relaxed New Year's Day morning; walk along Strøget & Nyhavn."},
        {"time": "12:00 - 12:45", "activity": "Amalienborg Palace Royal Guard Changing Ceremony."},
        {"time": "13:00 - 15:00", "activity": "Visit CopenHill rooftop artificial ski slope & panoramic vista."},
        {"time": "15:30 - 17:30", "activity": "Danish hygge cafe session."},
        {"time": "18:30 - 21:00", "activity": "New Year's Day dinner in Copenhagen."}
      ],
      "drivingLegs": [
        {"from": "Copenhagen Marriott", "to": "Nyhavn / Amalienborg", "dist": "2 km", "time": "15 mins", "route": "Walk / Metro"}
      ],
      "ticketCosts": [
        {"item": "CopenHill Viewpoint Access", "cost": "Free / ~150 DKK ski", "url": "https://www.copenhill.dk/en"}
      ]
    },
    {
      "day": 22,
      "date": "Jan 02 (Sat)",
      "title": "SQ352 Non-stop to Singapore",
      "location": "Flight Home (In Flight)",
      "coords": [55.6180, 12.6508],
      "distance": "0 km (Metro)",
      "hotel": "In Flight (Singapore Airlines SQ352)",
      "hotelStatus": "confirmed",
      "bookingRef": "SQ352 Non-stop (Dep CPH 12:00 PM, Arr SIN Jan 03 7:30 AM)",
      "activities": "Morning 13-minute Metro to CPH Airport; depart on Singapore Airlines SQ352 non-stop to Singapore at 12:00 PM (Arrive SIN Jan 03, 7:30 AM).",
      "scheduleNotes": "SQ352 Non-stop to Singapore",
      "tags": ["Metro to CPH", "SQ352 Non-stop", "Singapore Flight"],
      "hourlySchedule": [
        {"time": "08:30 - 09:00", "activity": "Check out of Copenhagen Marriott Hotel."},
        {"time": "09:15 - 09:30", "activity": "13-minute Metro M3/M2 ride to Copenhagen Airport (CPH)."},
        {"time": "09:45 - 11:30", "activity": "Check in at Singapore Airlines desk, bag drop & tax refund."},
        {"time": "12:00", "activity": "Flight SQ352 departs CPH non-stop to Singapore (Arrives SIN Jan 03 at 07:30 AM)."}
      ],
      "drivingLegs": [
        {"from": "Copenhagen Marriott", "to": "CPH Airport", "dist": "8 km", "time": "13 mins", "route": "Metro M2"}
      ],
      "ticketCosts": [
        {"item": "CPH Metro Ticket", "cost": "36 DKK (~€5)", "url": "https://intl.m.dk/"}
      ]
    }
  ],
  "emergencyGuide": {
    "contacts": [
      {"country": "Unified Europe", "number": "112", "desc": "Emergency services (Police, Ambulance, Fire) - Works without SIM"},
      {"country": "Finland", "number": "+358 200 8080", "desc": "Autoliitto (Automobile and Touring Club of Finland Road Service)"},
      {"country": "Sweden", "number": "+46 20 912 912", "desc": "Assistanskåren (Swedish Road & Towing Assistance)"}
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

# Convert to JSON string
full_json = json.dumps(full_data)

# Encrypt using OpenSSL AES-256-CBC md5 (CryptoJS compatible)
proc = subprocess.Popen(['openssl', 'enc', '-aes-256-cbc', '-md', 'md5', '-pass', 'pass:8520', '-base64', '-A'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate(input=full_json.encode('utf-8'))
enc_b64 = out.decode('utf-8').strip()

# Save into data.js
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(f'const encryptedItineraryData = "{enc_b64}";\n')

print('✅ Complete dataset generated and encrypted into data.js! Length:', len(enc_b64))
