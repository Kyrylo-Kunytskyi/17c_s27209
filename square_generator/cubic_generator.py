from square_generator.square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def cubics(start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 3 for i in range(start, end + 1)]