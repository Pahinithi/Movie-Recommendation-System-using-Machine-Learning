# Import necessary modules
from flask import Flask, request, render_template
import pickle
import numpy as np
import difflib  # Import difflib for finding close matches

# Create a Flask application instance
app = Flask(__name__, template_folder='.')

# Load the trained movie recommendation model
with open("movie_recommendation_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html") # Render the index.html template

# Define a route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from the form
    movie_name = request.form["movie_name"].strip()

    # Find the closest match to the user input
    list_of_all_titles = model['movies_data']['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = model['movies_data'][model['movies_data'].title == close_match]['index'].values[0]

        # Get a list of similar movies
        similarity_score = list(enumerate(model['similarity'][index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        # Prepare the prediction text
        predicted_movies = [model['movies_data'].iloc[movie[0]]['title'] for movie in sorted_similar_movies[:5]]
        prediction_text = f"Movies recommended for you based on '{close_match}': " + ', '.join(predicted_movies)
    else:
        prediction_text = "Sorry, no close match found for the movie name you entered."

    # Pass the prediction value to the template
    return render_template("index.html", prediction=prediction_text)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug mode for development
