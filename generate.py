import pandas as pd

def generate_dom(row):
    dom = ""
    dom += "<h5>" + row["title"] + "</h5>\n"
    dom += "<p>" + row["authors"] + "</p>\n"
    return dom

if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    template = open('template.html').read()

    dom = ""
    for index, row in data.iterrows():
        dom += generate_dom(row)

    page = template.replace("<!--list-->", dom)

    print(page)
