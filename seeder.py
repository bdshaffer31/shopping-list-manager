from book import Book
import pickle
from master_db import MasterDB

class Seeder:

    def __init__(self):
        self.seed_path = "db.p"

    def read_with_pickle(self):
        shelf = pickle.load( open( self.seed_path, "rb" ) )
        return shelf

    def write_with_pickle(self, book_shelf):
        pickle.dump( book_shelf, open( self.seed_path, "wb" ) )

    