import pandas as pd
from typing import Dict, List


def parse_lines_file(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    df = df.drop(columns=["Identifiant", "Famille commerciale"])
    lines = df.values.tolist()
    return lines


def parse_stops_file(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";")
    df = df.drop(columns=["Parcours (libellé court)", "Ligne (ID)", "Ordre", "Montée autorisée", "Descente autorisée"])
    df = df.rename(columns={
        "Parcours (ID)": "route_id",
        "Ligne (nom court)": "line_id",
        "Point d'arrêt (ID)": "stop_id",
        "Point d'arrêt (nom)": "stop_label",
        "Unnamed: 9": "passenger_count"
    })
    return df


def format_lines(lines) -> List[Dict]:
    results = []
    for line in lines:
        stops = line[1].split("<>")
        results.append({
            "line_id": line[0],
            "first_stop_label": stops[0].strip(),
            "last_stop_label": stops[-1].strip()
        })
    return results


def format_stops(stops) -> List[Dict]:
    results = []
    for stop in stops:
        results.append({
            "route_id": stop[0],
            "line_id": stop[1],
            "stop_id": stop[2],
            "stop_label": stop[3],
            "passenger_count": stop[4]
        })
    return results


def stats_stops(line_id: str, stops: pd.DataFrame):
    df = stops[stops.line_id == line_id]
    stops_min = df.loc[df.passenger_count == df.passenger_count.min()]
    stops_max = df.loc[df.passenger_count == df.passenger_count.max()]
    return stops_min, stops_max
