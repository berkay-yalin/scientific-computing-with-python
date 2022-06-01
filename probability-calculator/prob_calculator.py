import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        contents = [[k for i in range(int(v))] for k, v in kwargs.items()]
        self.contents = [j for i in contents for j in i]

    def draw(self, draws):
        if draws >= len(self.contents):
            return self.contents
        else:
            drawn = []
            for _ in range(draws):
                index = random.randrange(len(self.contents))
                drawn.append(self.contents[index])
                self.contents.pop(index)
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(num_experiments):
        balls = list(set(hat.contents))
        events = copy.deepcopy(hat).draw(num_balls_drawn)

        observed = {i: events.count(i) for i in balls if i in expected_balls}
        expected = expected_balls

        if all(observed[i] >= expected[i] for i in observed):
            successes += 1

    return successes/num_experiments
