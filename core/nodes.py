import os

from config import ROOT_DIR


class Node:
    def __init__(self, id):
        self.id = id
        self.taxi = set()
        self.bus = set()
        self.train = set()
        self.boat = set()

    def __repr__(self):
        return f"Node {self.id}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def get_connections(self, move_type=None):
        if move_type == "Taxi":
            return self.taxi
        if move_type == "Bus":
            return self.bus
        if move_type == "Train":
            return self.train
        if move_type == "Boat":
            return self.boat
        if move_type == "Black" or move_type is None:
            return self.taxi | self.bus | self.train | self.boat


class Map:
    def __init__(self):
        nodes = {}
        for i in range(1, 201):
            nodes[i] = Node(i)

        del nodes[108]  # Fun fact, there is no node 108 in the scotland yard map.

        with open(os.path.join(ROOT_DIR, "core/data/taxiConnections.txt"), 'r') as taxis:
            connections = taxis.read().split()
            for connection in connections:
                connection = connection.split(',')
                connection = [int(x) for x in connection]
                nodes[connection[0]].taxi.add(connection[1])
                nodes[connection[1]].taxi.add(connection[0])

        with open(os.path.join(ROOT_DIR, "core/data/busConnections.txt"), 'r') as buses:
            connections = buses.read().split()
            for connection in connections:
                connection = connection.split(',')
                connection = [int(x) for x in connection]
                nodes[connection[0]].bus.add(connection[1])
                nodes[connection[1]].bus.add(connection[0])

        with open(os.path.join(ROOT_DIR, "core/data/trainConnections.txt"), 'r') as trains:
            connections = trains.read().split()
            for connection in connections:
                connection = connection.split(',')
                connection = [int(x) for x in connection]
                nodes[connection[0]].train.add(connection[1])
                nodes[connection[1]].train.add(connection[0])

        with open(os.path.join(ROOT_DIR, "core/data/boatConnections.txt"), 'r') as boats:
            connections = boats.read().split()
            for connection in connections:
                connection = connection.split(',')
                connection = [int(x) for x in connection]
                nodes[connection[0]].boat.add(connection[1])
                nodes[connection[1]].boat.add(connection[0])

        self.nodes = nodes

    def find_connections(self, node, move_list=list):
        if not move_list:
            return set()

        if isinstance(move_list, str):
            move_list = [move_list]

        options = node.get_connections(move_list[0])

        result = set()
        if len(move_list[1:]) >= 1:
            for option in options:
                result = result.union(self.find_connections(self.nodes[option], move_list[1:]))
            return result

        else:
            return options

    def find_connections_by_id(self, node_id, move_list=list):
        return self.find_connections(self.nodes[node_id], move_list)
