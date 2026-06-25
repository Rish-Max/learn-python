import matplotlib.pyplot as plt

X_AXIS = [1,2,3,4,5]
Y_AXIS = [1,4,9,16,25]

def plot_linear_graph(x_axis, y_axis):
    plt.figure(figsize=(10, 5))
    plt.plot(x_axis, y_axis)
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Graph Plot")
    plt.show()

def plot_bar_graph(x_axis, y_axis):
    plt.figure(figsize=(10, 5))
    plt.bar(x_axis, y_axis)
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Bar Graph")
    plt.show()



plot_linear_graph(X_AXIS, Y_AXIS)
plot_bar_graph(X_AXIS, Y_AXIS)