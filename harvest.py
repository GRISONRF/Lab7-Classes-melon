############
# Part 1   #
############

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType(
    "musk",
    "Muskmelon",
    1998,
    "green",
    True,
    True
    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casa = MelonType(
    "cas",
    "Casaba",
    2003,
    "orange",
    True,
    False
    )
    casa.add_pairing("strawberries")
    casa.add_pairing("mint")
    all_melon_types.append(casa)

    crenshaw = MelonType(
    "cren",
    "Crenshaw",
    1996,
    "green",
    True,
    False
    )
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow = MelonType(
    "yw",
    "Yellow Watermelon",
    2013,
    "yellow",
    True,
    True
    )
    yellow.add_pairing("ice cream")
    all_melon_types.append(yellow)

    print(all_melon_types)
    return all_melon_types

melon_obj_lst=make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pair in melon.pairings:
            print(f'- {pair}')

print_pairing_info(melon_obj_lst)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        if melon.code not in melon_dict:
            melon_dict[melon.code] = melon
    
    print(melon_dict)
    return melon_dict

make_melon_type_lookup(melon_obj_lst)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self, type, shape_rating, color_rating, field, harvested_by):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by
    
    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5) and self.field != 3
    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    
    melon_lst=[melon_1, melon_2, melon_3,melon_4, melon_5, melon_6,melon_7, melon_8, melon_9]
    print(melon_lst)
    return melon_lst

make_melons(melon_obj_lst)


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
