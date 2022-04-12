import numpy as np
from simpleai.search import SearchProblem, astar, breadth_first, depth_first

# -------------------------------------------------------------------------------------------------------------------
#                                               Solving Labyrinth
# -------------------------------------------------------------------------------------------------------------------

class SearchPath(SearchProblem):

    states = []

    HORIZONTAL = [0, 1, 0, -1, -1, 1, 1, -1]
    VERTICAL = [-1, 0, 1, 0, -1, 1, -1, 1]
    COST = [1, 1, 1, 1, 1.4, 1.4, 1.4, 1.4]

    def __init__(self, initial_state, target_state, matrix, height):
        self.height = height
        self.target_state = target_state
        self.matrix = matrix
        
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        SearchProblem.__init__(self, initial_state)

    def actions(self, state):
        act = []
        
        for i in range(8):
            idy = state[0] + self.VERTICAL[i]
            idx = state[1] + self.HORIZONTAL[i] 

            height_difference = abs(self.matrix[idy][idx]-self.matrix[state[0]][state[1]])

            if (self.matrix[idy][idx] != -1 and height_difference <= self.height):
                act.append((idy, idx, (self.COST[i]**2 + (height_difference)**2)**(1/2)))

        return act

    def result(self, state, action):
        self.states.append(action)
        return (action[0],action[1])

    def is_goal(self, state):
        return state == self.target_state

    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        x2 = self.target_state[1]
        x1 = state[1]
        
        y2 = self.target_state[0]
        y1 = state[0]

        euc_distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        #man_distance = (np.abs(x1-x2) + np.abs(y1-y2))

        return euc_distance

class MarsRover():

    distance = 0

    def __init__(self, initial_position, final_position, mars_map, height):
        self.initial_position = initial_position
        self.final_position = final_position
        self.mars_map = mars_map
        self.height = height

        print(type(self.initial_position))
        print(type(self.final_position))
        self.make_path()

    def make_path(self):
        print(self.initial_position)
        print(self.final_position)
        #self.result = astar(SearchPath(self.initial_position, self.final_position, self.mars_map, self.height), graph_search=True)
        self.result = breadth_first(SearchPath(self.initial_position, self.final_position, self.mars_map, self.height), graph_search=True)
        #self.result = depth_first(SearchPath(self.initial_position, self.final_position, self.mars_map, self.height), graph_search=True)

        self.x = []
        self.y = []
        self.z = []

        for i, (action, state) in enumerate(self.result.path()):
            if action != None:
                self.distance = self.distance + action[2]
            self.y.append(state[0])
            self.x.append(state[1])
            self.z.append(self.mars_map[state[0]][state[1]])


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z
# ------------------------------------------------------------------------------------------------------------------- EOF
