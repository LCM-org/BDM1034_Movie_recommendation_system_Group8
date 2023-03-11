
Subject: 2023W-T2 BDM 1034 - Application Design for Big Data Group Number: Group 8 Group Members: Varun Sharma, Kelvin Simon, Muhammad Ibraheem, Sarathchandran Santhosh, Ankit Ambikaprasad

Project Name : Movie Recommendation System : In this project, we have used  nltk techniques and sci-kit learning to recommend similar movies based on the user input.

# Getting Started
## Pre-requisites
You will need to download and install below  packages after you install python: Sklearn (scikit-learn) - pandas - for creating the dataframes. nltk - for natural language processing.

The dataset used for this project were in csv format named tmdb_5000_credits.csv and tmdb_5000_movies.csv can be found in repo. Below is some description about the data files used for this project.we will merging several coloumns from tmdb_5000_credits.csv to tmdb_5000_movies.csv.


###Methodologies
Most of the values present in the coloumn are in the form of string of list of dictionaries. so we need to convert it into a normal list. For this purpose  we will use an inbuilt module named 'ast' which has a function called 'literal_eval' which converts a string of list into a list.
so we have functions here which will take a string of list as an argument and then we are converting that into a normal list using the literal_eval function of the ast module and looping through each item in that list(which is a dictionary) and getting the value of the name key and appending it to a empty list.

Once all the data preprocessing is done we further clean the data by removing any spaces between the two words of an element in all the column. We will explain by example why we are removing the spaces. If you the below rows of the data frame we have an actor name Sam Worthington in the first row and a director named Sam Mendes in the second row. If we do not remove the spaces between the 2 words our model can get confused and can recommend a movie of the actor Sam Worthington while it should have recommended the movie based on the director Sam Mendes.

Then by using the sklearn package and implementing feature extraction using the CountVectorizer method. This method will provide each word a numerical value according to the frequency of that word in the sentence. We are mentioning the attribute max_feature = 5000 as we will be only storing the top 5000 words from the tags column and also we removing the stop words(stop words are the words which doesnt contribute any meaning to the sentence such as i, is, the, a and many more)


Then we are using the sklearn package to get the similarity between two movies.
we will do this by using the cosine_similarity function. This function will calculate the cosine angle between the two vectors and so the smaller the angle, the more those movies are similar. Cosine_similarity of 1 will denote that the movies are same and closer the value of cosine_similarity to 1 means the 2 movies are more similar.

Lastly we create a function to get the top 5 recommended movies for a particular movie.
We will first get the index of the selected movie and then get the similarity score of the same index from the similarity matrix.
Now we will sort the similarity score of that movie and get the first 5 movie titles from it.
While sorting the list we use the enumerate function so that it keeps track of the element and its index and the we set reverse= True to sort it in descending order.
