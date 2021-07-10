from traveling_salesman import parse_csv, nearest_neighbor

if __name__ == "__main__":
    costs, col_idxs = parse_csv('instances/exercise3.csv')
    route_objects = nearest_neighbor(costs, col_idxs)
    for route_object in route_objects: print(route_object)