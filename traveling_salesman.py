from copy import deepcopy

def parse_csv(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        raw_costs_matrix = [row.strip().split(';') for row in lines]
        col_idxs = raw_costs_matrix[0][1:]

        costs_matrix = []
        for idx, string_costs_array in enumerate(raw_costs_matrix):
            if (idx != 0):
                numeric_array = [int(numeric_string) for idx, numeric_string in enumerate(string_costs_array) if idx != 0]
                costs_matrix.append(numeric_array)
        return costs_matrix, col_idxs

def nearest_neighbor_core(costs, col_idxs):
    routes = []
    for i in range(len(costs)):     
        work_costs = deepcopy(costs)
        route = []
        index = i
        route.append(index)
        for cost in work_costs: cost[index] = 0
        for i in range(len(work_costs)-1):
            index = work_costs[index].index(min([cost for cost in work_costs[index] if cost > 0]))
            route.append(index)
            for cost in work_costs: cost[index] = 0
        route.append(route[0])
        routes.append(route)
    return routes

def calc_routes_costs(routes, costs):
    routes_costs = []
    for route in routes:
        route_cost = 0
        for idx in range(len(route)-1):
            route_cost += costs[route[idx]][route[idx+1]]
        routes_costs.append(route_cost)
    return routes_costs

def nearest_neighbor(costs, col_idxs):
    routes_by_index = nearest_neighbor_core(costs, col_idxs)
    routes_costs = calc_routes_costs(routes_by_index, costs)
    routes = routes_array_index_to_point_name(col_idxs, routes_by_index)

    route_objects = []
    for i in range(len(routes)):
        route_object = {
            'route': routes[i],
            'cost': routes_costs[i]
        }
        route_objects.append(route_object)
    return route_objects

def routes_array_index_to_point_name(col_idxs, routes):  
    return [[col_idxs[index] for index in route] for route in routes]
    
