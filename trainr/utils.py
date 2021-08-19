import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
#['Adelie', 'Chinstrap', 'Gentoo']
classes = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def init_model():
    if not os.path.isfile("models/nb_model.pkl"):
        clf = GaussianNB()
        pickle.dump(clf, open("models/nb_model.pkl", "wb"))


# function to train and save the model as part of the feedback loop
def train_model(data):
    # load the model
    clf = pickle.load(open("models/nb_model.pkl", "rb"))

    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.penguin_class] for d in data]

    # fit the classifier again based on the new data obtained
    clf.fit(X, y)

    # save the model
    pickle.dump(clf, open("models/nb_model.pkl", "wb"))
