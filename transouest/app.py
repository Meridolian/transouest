from transouest.engine import (
    format_lines,
    format_stops,
    parse_lines_file,
    parse_stops_file,
    get_stops_by_line,
    stats_stops,
    get_lines_by_stop,
)
from tkinter import *
from tkinter import ttk


lines_file = "data_files/listeLignes.xlsx"
stops_file = "data_files/nomArret.csv"


def window():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


def stops_by_line(line_input: str):
    stops_df = parse_stops_file(stops_file)
    stops_by_line_df = get_stops_by_line(line_input, stops_df)
    stops_min_df, stops_max_df = stats_stops(stops_by_line_df)
    stops = format_stops(stops_by_line_df.values.tolist())
    stops_min = format_stops(stops_min_df.values.tolist())
    stops_max = format_stops(stops_max_df.values.tolist())
    return stops, stops_min, stops_max


def lines_by_stop(stop_input: int):
    stops_df = parse_stops_file(stops_file)
    lines_df = parse_lines_file(lines_file)
    stop_label, lines_by_stop_df = get_lines_by_stop(stop_input, stops_df, lines_df)
    lines_list = format_lines(lines_by_stop_df.values.tolist())
    return stop_label, lines_list


if __name__ == "__main__":
    window()
    # line = input("Choisissez un numéro de ligne : ")
    # stops, stops_min, stops_max = stops_by_line(line)
    # print(f"Arrêts de la ligne {line} : {stops}")
    # print(f"Minimum : {stops_min}")
    # print(f"Maximum : {stops_max}")
    # print("\n")
    # stop_id = int(input("Choisissez un arrêt : "))
    # stop, lines = lines_by_stop(stop_id)
    # print(f"Lignes passant par l'arrêt {stop_id} - {stop} : {lines}")
