class Node:

    def get_parent(self):
        return self.parent

    def get_f(self):
        return self.f

    def get_g(self):
        return self.g
    
    def get_h(self):
        return self.h

    def get_matrix(self):
        return self.matrix

    def get_next_nodes(self):

        next_nodes = []

        for i, x in enumerate(self.matrix):
            if x == 0:
                empty_pos = (i // self.size, i % self.size)

        if empty_pos[0] > 0:
            matrix = self.matrix[:]
            matrix[empty_pos[0] * self.size + empty_pos[1]] = matrix[(empty_pos[0] - 1) * self.size + empty_pos[1]]
            matrix[(empty_pos[0] - 1)* self.size + empty_pos[1]] = 0
            next_nodes.append(matrix)
        if empty_pos[0] < self.size - 1:
            matrix = self.matrix[:]
            matrix[empty_pos[0] * self.size + empty_pos[1]] = matrix[(empty_pos[0] + 1) * self.size + empty_pos[1]]
            matrix[(empty_pos[0] + 1)* self.size + empty_pos[1]] = 0
            next_nodes.append(matrix)
        if empty_pos[1] > 0:
            matrix = self.matrix[:]
            matrix[empty_pos[0] * self.size + empty_pos[1]] = matrix[empty_pos[0] * self.size + empty_pos[1] - 1]
            matrix[empty_pos[0] * self.size + empty_pos[1] - 1] = 0
            next_nodes.append(matrix)
        if empty_pos[1] < self.size - 1:
            matrix = self.matrix[:]
            matrix[empty_pos[0] * self.size + empty_pos[1]] = matrix[empty_pos[0] * self.size + empty_pos[1] + 1]
            matrix[empty_pos[0] * self.size + empty_pos[1] + 1] = 0
            next_nodes.append(matrix)

        return next_nodes


    def compute_g(self):
        
        tmp_parent = self.get_parent()
        self.g = 0

        while tmp_parent is not None:
            self.g += 1
            tmp_parent = tmp_parent.get_parent()

    def get_path(self):

        path = []

        tmp_matrix = self.matrix[:]
        path.append(tmp_matrix)

        tmp_parent = self.get_parent()

        while tmp_parent is not None:
            
            tmp_matrix = tmp_parent.get_matrix()[:]
            path.append(tmp_matrix)
            tmp_parent = tmp_parent.get_parent()
        
        return path

    def compute_h(self):

        self.h = 0
        
        for i, x in enumerate(self.matrix):
            current_pos = (i // self.size, i % self.size)
            target_pos = (self.target[x])
            self.h += abs(current_pos[0] - target_pos[0]) + abs(current_pos[1] - target_pos[1])


    
    def compute_f(self):
        self.f = self.g + self.h

    def set_g(self, g):
        self.g = g
    
    def set_parent(self, parent):
        self.parent = parent
    
    def check(self):

        state = True
        for i, x in enumerate(self.matrix):
            if (i // self.size, i % self.size) != self.target[x]:
                state = False

        return state


    def __init__(self, matrix, target, size, parent=None):

        self.matrix = matrix
        self.parent = parent
        self.target = target
        self.size = size
        self.compute_g()
        self.compute_h()
        self.compute_f()
