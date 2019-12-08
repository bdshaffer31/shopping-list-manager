import pickle

class Seeder:

    def __init__(self):
        self.seed_path = "db.p"

    def read_with_pickle(self):
        shelf = pickle.load(open(self.seed_path, "rb"))
        return shelf

    def write_with_pickle(self, book_shelf):
        pickle.dump(book_shelf, open(self.seed_path, "wb"))

    def write_for_humans(self, book_shelf):
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx", 'w')
        self.write_master_for_humans(book_shelf.master_list, seed_file)
        for book in book_shelf.books:
            seed_file.writelines('**** ' + book.name + ' **** \n')
            self.write_book_for_humans(book, seed_file)
        seed_file.writelines('******** \n')
        seed_file.close()

    def write_master_for_humans(self, book, seed_file):
        seed_file.writelines("===== Ingredients =====\n")
        for item in book.ingredients:
            seed_file.writelines(item.name + ' | ' + item.cost + ' | ' + item.location + ' | \n')
        seed_file.writelines("===== Recipes =====\n")
        for item in book.recipes:
            seed_file.writelines(item.name + ' | ' + item.meal + ' | ')
            for ingr in item.ingredients:
                seed_file.writelines(ingr.name + ', ')
            seed_file.writelines(' | \n')

    def write_book_for_humans(self, book, seed_file):
        seed_file.writelines("===== Recipes =====\n")
        for item in book.recipes:
            seed_file.writelines(item + '\n')
