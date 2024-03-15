class SquareGenerator:
    def squares(start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 2 for i in range(start, end + 1)]