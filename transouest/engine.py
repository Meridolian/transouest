import pandas as pd
from typing import Dict, List


def parse_lines_file(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    df = df.drop(columns=["Identifiant", "Famille commerciale"])
    df = df.rename(columns={
        "Nom court": "line_id",
        "Nom long": "line_label",
    })
    return df


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
        print(line)
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


def get_stops_by_line(line_id: str, stops: pd.DataFrame) -> pd.DataFrame:
    return stops[stops.line_id == line_id]


def get_lines_by_stop(stop_id: int, stops_df: pd.DataFrame, lines_df: pd.DataFrame):
    stops = stops_df.loc[stops_df.stop_id == stop_id]
    stop_label = stops.head(1).stop_label.values[0]
    lines = stops.line_id.values.tolist()
    lines_by_stop_df = lines_df.loc[lines_df.line_id.isin(lines)]
    return stop_label, lines_by_stop_df


def stats_stops(stops: pd.DataFrame):
    stops_min = stops.loc[stops.passenger_count == stops.passenger_count.min()]
    stops_max = stops.loc[stops.passenger_count == stops.passenger_count.max()]
    return stops_min, stops_max
