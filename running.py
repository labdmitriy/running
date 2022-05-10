import argparse
from pathlib import Path

import gpxpy
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
from tqdm import tqdm


def visualize_routes(data_dir, map_file):
    data_dir = Path(data_dir)
    map_file = Path(map_file)
    map_file_dir = map_file.parent
    map_file_dir.mkdir(parents=True, exist_ok=True)

    gpx_files = list(data_dir.glob("*.gpx"))
    gpx_files_count = len(gpx_files)
    points = []

    for gpx_file in tqdm(gpx_files, desc=f"{'Extract routes data': <20}"):
        with open(gpx_file, "r") as f:
            gpx_data = gpxpy.parse(f)

        data = gpx_data.tracks[0].segments[0].points

        for point in data:
            points.append(
                {
                    "file_name": gpx_file.name,
                    "lon": point.longitude,
                    "lat": point.latitude,
                    "alt": point.elevation,
                    "time": point.time,
                }
            )

    df = pd.DataFrame(points)
    routes = df.groupby("file_name")
    fig = plt.figure()

    for _, route_df in tqdm(
        routes, desc=f"{'Plot routes': <20}", total=gpx_files_count
    ):
        route_df = route_df.sort_values("time")
        plt.plot(route_df["lon"], route_df["lat"], linewidth=3)

    mplleaflet.show(fig=fig, path=map_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualizes GPX routes")
    parser.add_argument("--data", type=str, required=True, help="Folder with GPX files")
    parser.add_argument(
        "--map", type=str, required=True, help="Path to the output map file"
    )
    args = parser.parse_args()

    data_dir = args.data
    map_file = args.map

    visualize_routes(args.data, args.map)
