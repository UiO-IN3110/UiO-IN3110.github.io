import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1, 1], [1, 0], [0.4, 0.8], [2, 5], [2, 4], [2.2, 4.6]])

target = np.array([0, 0, 0, 1, 1, 1])
colors = ["blue", "red"]


point_to_predict = np.array([1.75, 2])


def distance(p0, p1):
    d = p1 - p0
    d_2 = np.sum(d**2, axis=1)
    return np.sqrt(d_2)


distances = distance(data, point_to_predict)

for i in range(len(data)):
    p = data[i]
    t = target[i]
    c = colors[t]
    plt.plot(p[0], p[1], "o", color=c)


def KNearest(data, target, point_to_predict, n_neighbors=3):
    distances = distance(data, point_to_predict)
    sorted_args = np.argsort(distances)
    closest_labels = target[sorted_args]
    valid_labels = closest_labels[:n_neighbors]

    vote = np.bincount(valid_labels)
    plt.plot(
        point_to_predict[0],
        point_to_predict[1],
        "o",
        color=colors[vote.argmax()],
        alpha=0.5,
    )

    center = point_to_predict
    radius = (distances[sorted_args])[n_neighbors - 1]
    t = np.linspace(0, 2 * np.pi, 501)
    plt.plot(
        radius * np.cos(t) + center[0],
        radius * np.sin(t) + center[1],
        "--",
        color=colors[vote.argmax()],
    )
    return colors[vote.argmax()]


print(KNearest(data, target, point_to_predict))

plt.show()
