import pickle

seed_path = "db.p"

def read_with_pickle():
    shelf = pickle.load(open(seed_path, "rb"))
    return shelf

def write_with_pickle(book_shelf):
    pickle.dump(book_shelf, open(seed_path, "wb"))
