def create_counter():
    count = [0]

    def counter():
        count[0] += 1

        return count[0]

    return counter
