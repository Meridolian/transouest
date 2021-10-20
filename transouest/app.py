from engine import format_lines, format_stops, parse_lines_file, parse_stops_file, stats_stops


lines_file = "data_files/listeLignes.xlsx"
stops_file = "data_files/nomArret.csv"


def window():
    pass


def app(line_input: str):
    # lines_df = parse_lines_file(lines_file)
    # lines = lines_df.values.tolist()
    # format_lines(lines)
    stops_df = parse_stops_file(stops_file)
    stops_min_df, stops_max_df = stats_stops(line_input, stops_df)
    stops_min, stops_max = stops_min_df.values.tolist(), stops_max_df.values.tolist()
    print(f"Minimum : {format_stops(stops_min)}")
    print(f"Maximum : {format_stops(stops_max)}")
    # stops = stops_df.values.tolist()
    # format_stops(stops)


if __name__ == "__main__":
    line = input("Choisissez un numéro de ligne")
    app(line)
