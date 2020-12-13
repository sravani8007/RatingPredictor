# RatingPredictor
In this project we analyze the Board Game Geek Reviews, ratings and build a machine learning models which can predict ratings for a review. In addition to that using one of the models built a web application that can take a review and predict the rating.


Stepts to Run in a local Machine:

1. Install Python3

2. Clone the project using below command

   git clone https://github.com/sravani8007/RatingPredictor.git
   
    
3. Change the directory to RatingPredictor

   cd RatingPredictor

4. Install the following python libraries

   a. Flask
   
   b. Sklearn
   
   c. pandas
   
   d. numpy
   
   e. WTForms
   
   This can be done using a seperate environment using the environment yml file as below
   
   conda env create -f environment.yml
   conda activate rating
   
   or 
   
   Use the requiremets.txt as below
   
   pip install -r requirements.txt


5. Run the app using the below command

   python rating_predictor.py

6. Open the local host link  

7. Give a review and press the submit button

8. To test it on the hosted server try : http://sravanisuravajhula.pythonanywhere.com/
