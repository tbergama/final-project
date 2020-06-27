# Home Listing Price Prediction
Authors: Josh Lowy, Thomas Bergamaschi, Kevin Scheller

### Abstract:
The correct valuation of a home or residence can be critical to the finances of any family or business.  However, this problem is much
more complicated than counting beds and baths.  The use of machine learning enables us to model intricate relationship problems such
as home valuation with relative ease.  By using detailed home listing data, we have trained a model specific to the Sacramento area to
predict home price or rental price based on an assortment of property features.  Property price estimation is a much greater problem
than what our model and selection of features can grasp, but we aim to use this model as a starting point and reference for future
assessment.

## Deployment
**Dependencies**
- Flask
- Pandas
- Numpy
- Tensorflow (keras.models.load_model)

**Running the app**
This project is deployable via locally hosted webpage:
  After installing the necessary dependencies, open an instance of your computer's terminal and navigate to the project directory then to '/frontEnd'.  The command `python app.py` will run our application on Flask's default port which display in your terminal console.  This route can be copy-pasted into your web browser of choice and our webpage will appear.
 **Navigation**
The home route is our price generator, and the /methods route is a detailed analysis and breakdown of the project.  This route can also be accessed from the "Read more..." link on the home page.

## File Tree
- **preProcessing**
  Raw listing data, cleanup and encoding notebooks (.ipynb), and clean/encoded data (.csv)
- **machineLearning**
  Training and testing files for the model
- **frontEnd**
  Front end files for hosting the predictor tool
- **tom**
  Currently implemented keras model, authored by guess who
