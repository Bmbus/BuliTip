from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
games_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
@app.route("/")
def index():
    r = requests.get("https://www.openligadb.de/api/getmatchdata/bl1/2020/2").json()
    games = {}

    for i in range(0, 9):
        #print(i)
        match = str(r[i]["Team1"]["ShortName"]) + " vs. " + str(r[i]["Team2"]["ShortName"])
        try:
            result = str(r[i]["MatchResults"][0]["PointsTeam1"]) + ":" + str(r[i]["MatchResults"][0]["PointsTeam2"])
        except:
            result = "-"
        games[match] = result
    #for i in r:
    #    print(r[0]["MatchResults"][0])
    
    #return jsonify(games)
    return render_template("index.html", games=games_)


@app.route("/test")
def test():
    r = requests.get("https://www.openligadb.de/api/getmatchdata/bl1/2020/1").json()
    team_one = [0]
    team_two = ""
    result = ""
    return jsonify(r)

if __name__ == "__main__":
    app.run(port="8080", debug=True)