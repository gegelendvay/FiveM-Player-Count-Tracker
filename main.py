import matplotlib.pyplot as plt
import requests as req

servers = [
    ["Example Server 1", "127.0.0.1", "b"],
    ["Example Server 2", "127.0.0.1", "green"],
    ["Example Server 3", "127.0.0.1", "#9128f6"],
]

plt.figure(num="FiveM Player Count Tracker")
plt.title("FiveM Player Count Tracker")

for i in servers:
    xAxis, yAxis = [], []
    try:
        server, color = i[0], i[2]
        res = req.get(f"http://{i[1]}:40120/chartData/svMain").json()
        xAxis = list(range(0, 360))
        for i in res:
            yAxis.append(i["clients"])
        while len(yAxis) != 360:
            yAxis.insert(0, 0)
        average = round(sum(yAxis)/len(yAxis), 2)
        plt.plot(xAxis, yAxis, label=f'{server} - {average}', color=color)
    except Exception as e:
        print(e)

plt.xlabel("Time ~ 30h")
plt.ylabel("Player Count")
plt.legend()
plt.show()