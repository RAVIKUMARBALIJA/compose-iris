import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
#culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'
def process_data(data):
    processed = [
        {
            "culmen_length_mm": d.culmen_length_mm,
            "culmen_depth_mm": d.culmen_depth_mm,
            "flipper_length_mm": d.flipper_length_mm,
            "body_mass_g": d.body_mass_g,
            "penguin_class": d.penguin_class,
        }
        for d in data
    ]

    return processed
