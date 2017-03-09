from PIL import Image


JULIA = lambda z: z ** 2  - 0.221 - 0.713j
INTERVAL = [-1, 1]
TRESHOLD = 2


def generate_julia(pixels, julia, treshold):
    """
    Arguments:
      pixels (list (list (float))): map of complex numbers
      julia (func): Julia func to generate the fractal
      treshold (int): treshold for generated numbers
    Returns:
      pixels (list (tuple)): list of (R,G,B) tuples
    """

    def iterate(n):
        i = 0
        while abs(n) < treshold:
            n = julia(n)
            i += 1

        iterate.max_value = max(iterate.max_value, i)
        return i

    iterate.max_value = 0
    pixels = [[iterate(n) for n in row] for row in pixels]
    return [
        (r, g, 100) if n >= 200 else (0, 0, 0)
        for g, row in enumerate(pixels)
        for r, n in enumerate(row)]


def get_input(prompt, cast=None, default=None):
    """
    Arguments:
      prompt (str): text prompted for the input
      cast (func): function that cast the input in the desired type
      default (poly): default value if something goes wrong
    Returns:
      user input (poly)
    """

    if default:
        prompt = '{} [{}] '.format(prompt, default)
    uinput = raw_input(prompt)
    if cast:
        try:
            uinput = cast(uinput)
        except:
            uinput = default
    return uinput


def main():
    width = get_input(prompt='Width?: ', cast=int, default=500)
    height = get_input(prompt='Height?: ',  cast=int, default=400)

    xstep = float(INTERVAL[1] - INTERVAL[0]) / float(width-1)
    ystep = float(INTERVAL[1] - INTERVAL[0]) / float(height-1)

    complex_numbers = [[(x*xstep-1+1j*y*ystep-1j)
                        for x in range(width)]
                       for y in range(height)]

    image = Image.new('RGB', (width, height))
    image.putdata(generate_julia(complex_numbers, JULIA, TRESHOLD))
    image.show()

if __name__ == '__main__':
    main()
