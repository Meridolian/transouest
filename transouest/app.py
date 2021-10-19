import pandas as pd


lines_file = "data_files/listeLignes.xlsx"
stops_file = "data_files/nomArret.csv"


def explore_data():
    lines = pd.read_excel(lines_file)
    print(lines)
    c4 = lines.loc[lines["Nom court"] == "C4"]
    print(c4)

    stops = pd.read_csv(stops_file, sep=";")


if __name__ == "__main__":
    explore_data()
