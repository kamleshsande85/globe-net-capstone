import os

# Simple one-liner to create the structure


def create_simple():
    folders = ["diagrams", "configs", "evidence", "video"]
    files = {
        "": ["GLOBE-NET.pkt", "REPORT.md", "README.md"],
        "diagrams": ["world-map.drawio", "as-path-bgp.png"],
        "configs": ["R1-home.txt", "PE1-mumbai.txt"],
        "evidence": ["traceroute.txt", "dig-trace.txt", "undersea-ping-80ms.png"],
        "video": ["5-min-walkthrough.mp4"]
    }

    for folder in folders:
        os.makedirs(f"globe-net/{folder}", exist_ok=True)

    for folder, file_list in files.items():
        path = f"globe-net/{folder}" if folder else "globe-net"
        for file in file_list:
            open(f"{path}/{file}", 'w').close()

    print("Structure created!")


create_simple()
