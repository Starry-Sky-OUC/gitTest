from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import numpy as np

def compute():
    matrix = np.random.rand(1000, 1000)
    result = np.dot(matrix, matrix)
    row_sums = np.sum(result, axis=1)
    return row_sums

if __name__ == '__main__':
    graphviz = GraphvizOutput()
    graphviz.output_file = 'callgraph.png'

    with PyCallGraph(output=graphviz):
        result = compute()
        print("Computation completed. Result sum:", np.sum(result))
