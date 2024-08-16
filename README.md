# Movie Recommendation System

## Overview

This project is a Movie Recommendation System that uses machine learning techniques to recommend movies based on a given input movie name. The system is built with Python using libraries such as Pandas, Scikit-Learn, and Flask for the web application.

## Features

- **Movie Recommendations**: Suggests movies similar to a user-provided movie.
- **Web Interface**: Allows users to input a movie name and get recommendations.
- **Machine Learning Model**: Utilizes TF-IDF Vectorizer and Cosine Similarity for recommendations.

## Technologies Used

- **Python**: Main programming language.
- **Flask**: Web framework for creating the web application.
- **Pandas**: Data manipulation and analysis.
- **Scikit-Learn**: For machine learning features such as TF-IDF and Cosine Similarity.
- **Pickle**: To serialize and deserialize the model.
- **HTML/CSS**: For frontend design.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Scikit-Learn
- Pickle

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Pahinithi/Movie-Recommendation-System-using-Machine-Learning/tree/main
    cd Movie-Recommendation-System
    ```

2. **Install the required Python packages:**

    ```bash
    pip install flask pandas scikit-learn
    ```

3. **Download the dataset** and place it in the `/kaggle/input/movie-recommendation-system/` directory.

4. **Run the recommendation model script** to generate and save the model:

    ```bash
    python generate_model.py
    ```

5. **Run the Flask application:**

    ```bash
    python app.py
    ```

6. **Open a web browser** and go to `http://127.0.0.1:5000` to access the Movie Recommendation System.

## How It Works

1. **Data Loading**: The dataset is loaded into a Pandas DataFrame.
2. **Feature Selection**: Selected features are combined into a single text feature.
3. **Text Vectorization**: The combined text data is transformed into TF-IDF vectors.
4. **Similarity Calculation**: Cosine Similarity is used to find similar movies.
5. **Recommendation**: Based on the input movie name, similar movies are suggested.

## Usage

- Enter the name of a movie into the input field on the web page.
- Click the "Get Recommendations" button.
- The system will display a list of recommended movies based on the input.

## Model

The recommendation model is serialized and saved using Pickle. It includes:

- **Vectorizer**: TF-IDF Vectorizer used for text transformation.
- **Similarity**: Precomputed cosine similarity matrix.
- **Movies Data**: The dataset used for recommendations.
- **Selected Features**: Features used for creating the recommendation model.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Suggestions and contributions are welcome!

## License

This project is licensed under the MIT License 

## Contact

For any questions or inquiries, please reach out to nithilan32@gmail.com.

