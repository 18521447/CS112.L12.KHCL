class Accumulator:
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        pass


if __name__ == '__main__':
    metric = [0.0, 0.0]
    for X, y in data_iter:
        metric[0] += accuracy(net(X), y)
        metric[1] += tf.size(y).numpy()
        print(metric.data)
        print("**")
    print(metric.data)
    return metric[0] / metric[1]

