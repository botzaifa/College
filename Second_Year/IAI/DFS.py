def dfs_recursive(graph,source,path=[]):
    if source not in path:
        path.append(source)
        
        #Backtrack
        if source not in graph:
            return path
        
        for neighbour in graph[source]:
            path=dfs_recursive(graph,neighbour,path)
    
    return path

# Give the details of the graph
graph = {
    "A":["B","D"],
    "B":["C","F"],
    "C":["E","H","G"],
    "D":["F"],
    "E":["B","F"],
    "F":["A"],
    "G":["E","H"],
    "H":["A"]
}

dfs_element=dfs_recursive(graph,"A")
print(dfs_element)