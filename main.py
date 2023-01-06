import requests as req
import matplotlib.pyplot as plt

servers = [
    ["Example Server 1", "127.0.0.1"],
    ["Example Server 2", "127.0.0.1"],
    ["Example Server 3", "127.0.0.1"],
]

plt.figure(num="FiveM Player Count Tracker")
plt.title("FiveM Player Count Tracker")

for i in servers:
    xAxis = []
    yAxis = []
    try:
        server = i[0]
        res = req.get(f"http://{i[1]}:40120/chartData/svMain").json()
        xAxis = (list(range(1, len(res)+1)))
        for i in res:
            yAxis.append(i["clients"])
        plt.plot(xAxis, yAxis, label=server)
    except Exception as e:
        print(e)

plt.legend()
plt.show()