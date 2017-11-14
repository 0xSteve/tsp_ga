'''A python module for parsing a 2D TSP problem without file error
   detection.'''

# meta block
__author__ = "Steven Porretta"
__version__ = "0.0.1"
__maintainer__ = "Steven Porretta"
__email__ = "stevenporretta@scs.carleton.ca"
__status__ = "Development"


class Parser(object):
    '''A parser class for .tsp files.'''
    def __init__(self, filename):
        '''create an instance of the parser with a file to read.'''
        self.city_coords = {}
        self.city_tour_init = []
        self.city_tour_tuples = []
        self.filename = filename
        self.display_status = ''

        # Discard the file after parsing...
        content = self.read_filename(filename)
        self.dimension = self.get_dimension(content)
        self.edge_weight_type = self.get_edge_weight_type(content)
        self.city_coords = self.get_city_coord(content)
        self.city_tour_init = self.create_initial_tour()
        self.city_tour_tuples = self.create_initial_coord_tuples()

    def read_filename(self, filename):
        '''Line-by-line read of the .tsp file.'''

        with open(self.filename) as f:
            self.content = f.read().splitlines()
            self.display_status = 'file_loaded'
        return self.content

    def get_dimension(self, content):
        '''Find the DIMENSION line and get the dimension.'''

        for l in self.content:
            if l.startswith("DIMENSION"):
                index, space, rest = l.partition(':')
                return rest.strip()

    def get_edge_weight_type(self, content):
        """
            Check for TSP type and return it (GEO, EUC_2D)
        """
        for l in self.content:
            if l.startswith("EDGE_WEIGHT_TYPE"):
                index, space, rest = l.partition(':')
                return rest.strip()

    def get_city_coord(self, content):
        start = self.content.index("NODE_COORD_SECTION")
        end = self.content.index("EOF")
        # use line instead of l, linter complaint...
        for line in self.content[start + 1:end]:
            line = line.strip()
            city, space, coord = line.partition(" ")
            coord = coord.strip()
            x, space, y = coord.partition(" ")
            self.city_coords[int(city)] = (x.strip(), y.strip())
        return self.city_coords

    def create_initial_tour(self):
        for i in range(1, int(self.dimension) + 1):
            self.city_tour_init.append(i)
        return self.city_tour_init

    def create_initial_coord_tuples(self):
        city_tour_init = self.city_tour_init
        content = self.city_coords
        for i in city_tour_init:
            self.city_tour_tuples.append(content.get(i))
        return self.city_tour_tuples
