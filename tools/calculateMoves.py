from core.nodes import Map


def pretty_connections(node, move_list):
    map_data = Map()
    result = map_data.find_connections_by_id(node, move_list)
    if result:
        list_result = list(result)
        list_result.sort()
        return f"Mr X could be in any of these locations: {list_result}"
    else:
        return "No options found"


if __name__ == "__main__":
    start_node = int(input("Which node are we starting at: "))
    moves = []

    previous = None
    while previous not in ("End", ""):
        previous = input("Input move: ")
        moves.append(previous)
    moves = moves[:-1]

    print(pretty_connections(start_node, moves))
