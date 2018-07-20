"""
Facility location model

Replica/edge server placement

Goal:
Minimize the total cost of operation
"""
if __name__ == '__main__':

    # index : set of potential locations of replica server
    # value : cost of placing replica server at location i
    F = [2, 5, 3, 1]

    # selector : place or not to place replica in location i
    y = [0, 1, 0, 1]

    # set of end users
    # index : end user
    # value : units of demand of end user j
    D = [10, 30, 15, 10]

    # selector : deliver or not deliver content to user j from location i
    # Note: yi must be equal or greater than xij, no content can be delivered if replica was not deployed
    xi = [0, 0, 0, 1]

    # delivery cost from replica server location i to an end-user j
    ci = [5, 10, 15, 20]

    placing_cost = 0

    # cost of placing replicas in the selected locations
    for i in range(len(F)):
        placing_cost += F[i] * y[i]

    # cost of deliver dj units of demand from replica server location i to an end-user j

    network_cost = 0
    for i in range(len(F)):
        for j in range(len(D)):
            # units of demand * delivery cost * selector
            network_cost +=  D[j] * ci[j] * xi[j]

    total_cost = placing_cost + network_cost
    print(total_cost)

