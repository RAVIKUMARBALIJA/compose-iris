import pickle
from sklearn.naive_bayes import GaussianNB

# define a Gaussain NB classifier
#clf = GaussianNB()
clf=None

# define the class encodings and reverse encodings
classes = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
r_classes = {y: x for x, y in classes.items()}


# function to load the model
def load_model():
    global clf
    clf = pickle.load(open("models/nb_model.pkl", "rb"))


# function to predict the flower using the model
def predict(query_data):
    clf=pickle.load(open("models/nb_model.pkl", "rb"))
    x = list(query_data.dict().values())
    prediction = clf.predict([x])[0]
    return classes[prediction]
