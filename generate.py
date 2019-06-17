import pandas as pd

def generate_dom(row):
    dom = ""
    dom += "<h2>" + row["title"] + "</h2>\n"
    dom += "<p>" + row["authors"] + "</p>\n"
    return dom

if __name__ == "__main__":
    data = pd.read_csv("data.csv")

    dom = ""
    for index, row in data.iterrows():
        dom += generate_dom(row)

    print(dom)
