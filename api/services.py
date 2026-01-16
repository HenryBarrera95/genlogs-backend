def normalize_city(value: str) -> str:
    return (value or "").strip().lower()


ROUTES = {
    "nyc_dc": [
        {"name": "Knight-Swift Transport Services", "trucksPerDay": 10},
        {"name": "J.B. Hunt Transport Services Inc", "trucksPerDay": 7},
        {"name": "YRC Worldwide", "trucksPerDay": 5},
    ],
    "sf_la": [
        {"name": "XPO Logistics", "trucksPerDay": 9},
        {"name": "Schneider", "trucksPerDay": 6},
        {"name": "Landstar Systems", "trucksPerDay": 2},
    ],
    "other": [
        {"name": "UPS Inc.", "trucksPerDay": 11},
        {"name": "FedEx Corp", "trucksPerDay": 9},
    ],
}


def get_carriers_for_route(origin: str, destination: str):
    normalized_origin = normalize_city(origin)
    normalized_destination = normalize_city(destination)

    if "new york" in normalized_origin and "washington" in normalized_destination:
        return ROUTES["nyc_dc"]
    if "san francisco" in normalized_origin and "los angeles" in normalized_destination:
        return ROUTES["sf_la"]
    return ROUTES["other"]
