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
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    tmp_i, tmp_j = i, j
                    break

        if tmp_i > 0:
            matrix = [x[:] for x in self.matrix]
            matrix[tmp_i][tmp_j] = matrix[tmp_i - 1][tmp_j]
            matrix[tmp_i - 1][tmp_j] = 0
            next_nodes.append(matrix)

        if tmp_j > 0:
            matrix = [x[:] for x in self.matrix]
            matrix[tmp_i][tmp_j] = matrix[tmp_i][tmp_j - 1]
            matrix[tmp_i][tmp_j - 1] = 0
            next_nodes.append(matrix)

        if tmp_i < len(self.matrix) - 1:
            matrix = [x[:] for x in self.matrix]
            matrix[tmp_i][tmp_j] = matrix[tmp_i + 1][tmp_j]
            matrix[tmp_i + 1][tmp_j] = 0
            next_nodes.append(matrix)
        
        if tmp_j < len(self.matrix) - 1:
            matrix = [x[:] for x in self.matrix]
            matrix[tmp_i][tmp_j] = matrix[tmp_i][tmp_j + 1]
            matrix[tmp_i][tmp_j + 1] = 0
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

        tmp_matrix = [x[:] for x in self.matrix]
        path.append(tmp_matrix)

        tmp_parent = self.get_parent()

        while tmp_parent is not None:
            
            tmp_matrix = [x[:] for x in tmp_parent.get_matrix()]
            path.append(tmp_matrix)
            tmp_parent = tmp_parent.get_parent()
        
        return path

    def compute_h(self):

        self.h = 0
        for i in range(len(self.target)):
            for j in range(len(self.target)):
                if self.matrix[i][j] != self.target[i][j] and self.matrix[i][j] != 0:
                    self.h += 1
    
    def compute_f(self):
        self.f = self.g + self.h

    def set_g(self, g):
        self.g = g
    
    def set_parent(self, parent):
        self.parent = parent

    def __init__(self, matrix, target, parent=None):

        self.matrix = matrix
        self.parent = parent
        self.target = target
        self.compute_g()
        self.compute_h()
        self.compute_f()
