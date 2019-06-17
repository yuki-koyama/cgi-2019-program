import pandas as pd

def generate_paper_dom(row):
    dom = ""
    dom += "<h5>" + row["title"] + "</h5>\n"
    dom += "<p>" + row["authors"] + "</p>\n"
    return dom

def generate_session_dom(data, session_name, session_data):
    dom = ""
    dom += "<hr />\n"
    dom += "<h3>[" + session_name + "] " + session_data["name"] + " <small>" + session_data["datetime"] + "</small></h3>\n"
    dom += "<hr />\n"
    for index, row in data.iterrows():
        if row["session"] == session_name:
            dom += generate_paper_dom(row)
    return dom

if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    template = open('template.html').read()

    sessions = {
        "VC1": { "name": "3D Reconstruction and VR/AR", "datetime": "June 18th, 09:00-10:45" },
        "VC2": { "name": "Rendering and VR/AR", "datetime": "June 18th, 13:15-15:00" },
        "VC3": { "name": "Geometric Modelling, Geometric Computing, Shape and Surface Modelling", "datetime": "June 18th, 15:15-17:00" },
        "VC4": { "name": "Machine Learning for Graphics", "datetime": "June 19th, 09:00-10:45" },
        "VC5": { "name": "Visual Analytics, Image Processing and Pattern Recognition", "datetime": "June 19th, 13:15-15:00" },
        "VC6": { "name": "Visual Analytics and Image Processing", "datetime": "June 20th, 09:15-11:00" },
        "VC7": { "name": "Computer Animation", "datetime": "June 20th, 09:15-11:00" },
    }

    dom = ""
    for key, item in sessions.items():
        dom += generate_session_dom(data, key, item)

    page = template.replace("<!--list-->", dom)

    print(page)
