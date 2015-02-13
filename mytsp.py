import math
import sys

sys.setrecursionlimit(16000)
visited = []

def read_input(r):
    #Set up to read the text file line by line storing the city id, x coord., and y coord. in separate arrays.
    #It sets up the arrays and notable variables before calling calculations and passing in those variables.
    
    city_id = []
    x = []
    y = []

    with open(r) as f:
        for line in f:
            data = line.split()
            city_id.append(int(data[0]))
            x.append(int(data[1]))
            y.append(int(data[2]))

    shortest_edges = []
    start = 0
    first_x = x[0]
    first_y = y[0]
    visited.append(start)
    d = calculations(city_id, x, y, shortest_edges, start, first_x, first_y, visited)
    return(d)

def calculations(city_id, x, y, shortest_edges, start, first_x, first_y, visited):
    #Recursively finds the nearest neighbor from the starting point.
    #Base case occurs when the length of city_id reaches 2 and we manually find the last points.

    if len(city_id) == 2:
        test = round(math.sqrt(((x[0] - x[1])**2) + ((y[0] - y[1])**2)))
        shortest_edges.append(int(test))

        if start == 0:
            visited.append(city_id[1])
            test = round(math.sqrt(((x[1] - first_x)**2) + ((y[1] - first_y)**2)))
            shortest_edges.append(int(test))
            return shortest_edges
        else:
            visited.append(city_id[0])
            test = round(math.sqrt(((x[0] - first_x)**2) + ((y[0] - first_y)**2)))
            shortest_edges.append(int(test))
            return shortest_edges
        
    least = "inf"
    fin = 0
    newCity = city_id[:start] + city_id[start + 1:]
    newX = x[:start] + x[start + 1:]
    newY = y[:start] + y[start + 1:]

    for j in range(0, (len(newCity))):
        test = round(math.sqrt(((x[start] - newX[j])**2) + ((y[start] - newY[j])**2)))
        if (test < least):
            least = test
            fin = j
    shortest_edges.append(int(least))
    visited.append(newCity[fin])

    calculations(newCity, newX, newY, shortest_edges, fin, first_x, first_y, visited)

    return shortest_edges

def write_output(d, r):
    #Prints the contents of visited and the sum of shortest_edges to our .tour file line by line.
    
    file = open(r + '.tour', 'w')

    file.write(str(sum(d))+"\n")

    for i in range(0, (len(visited))):
        file.write(str(visited[i])+"\n")

def main():
    #The main function that calls the rest of the functions to read, calculate and write.

    import time
    start_time = time.time()
    
    r = str(sys.argv[1])
    d_array = read_input(r)
    write_output(d_array, r)

    elapsed = time.time() - start_time
    print (elapsed)

main()
            
