"""
## 6. Critical Connections (3.pt))

Implement the `critical_connections(n, connections)` function to identify all critical connections in a network.
"""

def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    """
    Identify all critical connections in an undirected network.

    :param n: An integer representing the number of servers/nodes in the network. 
              The servers are labeled from 0 to n-1. (int)
    :param connections: A list of lists, where each inner list [a, b] represents 
                        a bidirectional connection between server a and server b. (list[list[int]])
    :return: A list of lists, where each inner list [u, v] represents a critical connection 
             (edge) in the network. The order of the servers within an inner list does not matter 
             (i.e., [u, v] is the same as [v, u]). (list[list[int]])
    """
    # Write your code here

"""
### **Example**
# Example 1
critical_connections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]])
# Expected Output: [[1, 3]]

# Example 2
critical_connections(n=5, connections=[[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [3, 1], [3, 2]])
# Expected Output: []
"""