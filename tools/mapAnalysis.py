from core.nodes import Map


def best_nodes(jump_count):
    results = []
    max_count = -1

    map_data = Map()

    for location in map_data.nodes.values():
        local_count = len(map_data.find_connections(location, ["Black" for _ in range(jump_count)]))

        results.append((local_count, location))
        if local_count > max_count:
            max_count = local_count

    results.sort(reverse=True)

    return results


if __name__ == "__main__":
    jump_count = int(input("How many jumps do you want to analyse?: "))

    results = best_nodes(jump_count)

    print(f"Best Location: {results[0][1]}\t Possibilities: {results[0][0]}")

    for result in results:
        print(f"Location: {result[1].id:3}\tPossibilities: {result[0]}\tTrain station: {bool(result[1].train)!s:6}\tBus stop: {bool(result[1].bus)}")