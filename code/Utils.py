class Utils:

    def push(input_map, value):
        current_length = len(input_map)
        input_map[current_length+1] = value
        return value
