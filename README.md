
# This is the Submission for Project for TCS HumAIn.
> Colab:https://colab.research.google.com/github/Mohit-Patil/Taxonomy-Creation/blob/master/Taxonomy.ipynb



# **-----TAXONOMY CREATION-----**

## 1. Importing Libraries.
>import pandas as pd</br>
>import collections</br>
>import random</br>
>from bs4 import BeautifulSoup</br>
>from nltk.corpus import stopwords</br>
>import re</br>
>from sklearn.preprocessing import MultiLabelBinarizer</br>
>from sklearn.utils import shuffle</br>
>import tensorflow as tf</br>
>import nltk</br>
>nltk.download('stopwords')</br>
>nltk.download('punkt')</br>

  

## 2. Connecting Google Drive to Save Processed Data sets.
* Used to Store Data and Model on the Google Drive.

* Data can be recovered if the Run time crashes.
## 3. Downloading Dataset from Kaggle.

  

* Instead of Downloading the dataset locally, we download it to Colab Runtime utilizing the network speed and storage constraints.

1. Install Kaggle API.

2. Download the Dataset from the Competition list.

3. Unzip the Train and Test Data.
  

## 4. Preproceesing and Cleaning the Data

  

### Dataset Description

- **Id** - Unique identifier for each question.

- **Title** - The question's title.

- **Body** - The body of the question.

- **Tags** - The tags associated with the question.

  

- *Size(Compressed)*: 2.19GB

- *Size(Actual)*: 6.76GB

- *No. of Rows*: 6034195

- *No. of Columns*: 4

  
  

### Dataset Link

Dataset: [Facebook Recruiting III - Keyword Extraction](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data) competition on Kaggle.

  

### Loading Datasets into Dataframe

  

- Using Pandas Library
  

### 4.1 Deleting Missing data from the Rows

  

- Using Inbuilt Functions of Pandas library.
  

### 4.2: Deleting Unnecessary Columns.

  

- The Columns "Id" and "Index" are of no use

- Removing them using drop(...) function of Pandas Library
  

### 4.3: Removing Duplicates.

  

- Dataset contains duplicates in it.

- We only remove duplicates from only the "Body" column because the "Title" may be same for many data points but they may have different "Body"

- Also "Tags" may be same for 2 Questions so we do not remove duplicates from "Tags" column

- After Removing Duplicates we reset the index values.
### 4.4: Calculating Total Tags Present 
  >Total Tags Present 12030708</br>
>Average Number of Tags Present per Row 2.8959135600213175


### 4.5: Frequently Occurring Tags

  - List of tags which occur the most number of times.

- Freq_Tags : *size* = 100.

- We take 100 frequent tags to limit the data size.
-   

### 4.6: Storing Indices of the Rows which Contain Frequent Tags

  

- We store the Indices of the data points which contain the most frequent tags.

- We do this by comparing Tags of each data point and storing the data point's index into Sample_Index.
  

### Randomly Choosing Indices with Frequent Tags

  

- Sample_Index now contains indices of *674746* data points.

- So we choose *600000* random data points out of those.
  

### 4.7: Choosing Data with the above Randomly Chosen Indices

  

- Now we select the data points which match the indices in the above randomly fetched indices which have frequent tags.

- Using iloc(..) function present in pandas Library.

- Then, we reset the indices and drop the unwanted "index" column.
  

### 4.8: Separating Tags in a row

  

- We separate space separated tags in each data point to comma spearated.

> Example: [c++ clion array] now becomes [c++, clion, array]
  

### 4.9: Removing Html Tags From the Body Column

  

- Html Tags are removed as they add too much noise to the data and can make model to perform abruptly

- Removed using 're' function.
  

### 4.10: Concatenating Title And Body Into One Column

  

- Joining both "Title" and "Body" Columns of every data point to form a single Column.

- Also converting them to lowercase to maintain uniformity.
  

### 4.11: Removing Stop Words and Frequent Tags from The Body Column

  

- Removing words such as I, am, he, was, .... from the "Body" of each data point as it adds noise and can cause model to overfit.

- We also remove the frequent tags so that the model does not closely train on the frequent occurring words.

- Also the reason is some Questions have the tags in their question itself but some do not have any tag mentioned in the Question. So to avoid this, we remove stopwords and frequent tags also.

- Using NLTK Library and its Tokenizer and StopWords.
  

# 5. Data Preparation

- Now that our data is cleaned we now divide the dependent and independent columns from each other.
  

### 5.1 Encoding Tags</br>

  

- We now Encode top tags to multi-hot array.</br>

- We first split the tag values of each dataset and the multi-hot encode them using MultiLabelBinarizer() from sklearn library.</br>
### 5.2: Splitting Prepared Data into Train and Cross Validation Set

  

- We now Split the data into Train and Test Set using 80/20 split.</br>
### 5.3: Tokenizing and Transforming.</br>

  

- First "Body" of each Data Point is Tokenized and then transformed to matrices of 0's and 1's depending if the word is in Bag of Words.</br>
# 6. Building and Training the Model
  

### Model</br>

  

- The Model is a sequential model comprising of different Layers:

  - Input Layer(shape = 50)

  - Dense/ Fully Connected Layer(shape = 80)

  - Dense/ Fully Connected Layer(shape = 140)

  - Output Layer(shape = 100)

 - The First Three Layers use Relu Activation function whereas the last layer uses Sigmoid Activation function to output if a tag is related or not.</br>

- Sigmoid outputs values between [0,1], so this tells of strong or how weak is a tag related.</br>

- Extensively uses Tensorflow and keras.</br>![enter image description here](https://lh3.googleusercontent.com/K1gFReK7KodUs1UDbmt_GkVfisFwUFbQGSnZL17iGzeC4Sp7kuV6pwcc5L0D8_StTdoYOowr9-bu)
  

### Performance on Validation Set

  

- The Model performs well on the cross validation set while training as well as on test set.

- Accuracy = 98%
- # Hardware and Software Used:

  
  

* GPU: Tesla T4

  

* RAM: 25.81 GB

* Softwares: Pandas, Keras, Tensorflow, Sklearn, nltk, pickle
