# Topic Modelling and Sentiment Analysis - Data Science Subreddit

#### -- Project Status - Completed

## Project Objective

[Data Science subreddit](https://www.reddit.com/r/datascience/) is the largest data science community on Reddit with over 1.6 million members. Due to its anonymous nature, it is a rich source of discussions about careers, job market conditions, and technical challenges that are not normally discussed on formal platforms. As a data professional, I often visit this subreddit to stay updated on the job market and to read about both technical and workplace challenges faced by peers. This piqued my curiosity about the trending topics and the sentiment surrounding these discussions. The objective of this project is to extract and analyse the main themes from the top posts of 2023 and to understand the sentiment associated with different flairs.

### Skills Used
* Data Crawling using Reddit API
* Text Mining
* Topic Modelling
* Sentiment Analysis

### Technologies
* Python
* NLTK
* Tfidf Vectorizer (sklearn)
* LDA (sklearn) 

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is available [here](https://github.com/khinydnlin/car_auction_price_predictions/blob/main/dataset.csv) within this repo.   
3. Data processing and modelling scripts are documented in a [Jupyter notebook](https://github.com/khinydnlin/car_auction_price_predictions/blob/main/Car%20Auction%20Price%20Predictions.ipynb).
4. The project findings and other details can be found below:

## Project Description

### Data Sources

The following information were retrieved from the subreddit using Reddit API Wrapper (PRAW):

Top Posts (2023)
- date and time
- flair
- engagement score (upvotes minus downvotes)
- titles
- contents
- top 5 comments

### Key Insights

#### Exploratory Analysis

The following are the top 10 topics with highest engagement scores in 2023:

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/80a1fa41-bc95-4136-848d-342be8365417)

It appears that the discussions around job market (possibly due to the massive layoffs in tech industry) received more attention compared to other topics. 

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/2c0d8a7f-914c-4adb-b025-aa135d785a97)


#### Sentiment Analysis

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/67ca1d7f-3993-4c82-9aa9-5b8605579b81)




![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/c881f882-5499-48a1-9da9-90ec0dc36bed)



#### Topic Modelling


![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/990c8dbe-6b44-43a2-9ade-9a2a8ce32f8e)

- Practical Application and Collboration

Top words: **use work people model business code ml know mean test engineering need write**

This topic is likely about the application of data science in business and team settings, focusing on modeling, machine learning, and the integration of coding in business processes. Keywords such as "use," "model," "business," "ml" (machine learning), "code," and "engineering" reflect discussions on how data science is applied in real-world scenarios, possibly involving teamwork and collaboration.

- Job Seeking and Career Progression

Top words: **job project role interview great question apply ask year position experience change try**

This topic appears to center around the job market and career development in the data science field. Keywords like "job," "project," "role," "interview," "apply," "position," and "experience" suggest discussions related to finding new job opportunities, applying for positions, and discussing the experiences necessary for certain roles or career changes.

- Skills and Tools

Top words: **look good make python skill need think know big job level field sql**

This topic focuses on the practical skills and tools necessary in data science, such as Python, SQL, and general analytical skills. Terms like "python," "skill," "sql," and "big company" emphasize the technical competencies needed to succeed in the field and discussions about how to improve or acquire these skills.

- Learning and Career Development

Top words: **time learn start give help pay company work day best career point course**

Here, the emphasis seems to be on the learning journey and career advice within data science. Keywords like "learn," "start," "help," "career," "course," and "company" suggest advice threads, sharing of learning resources, or discussions about navigating career paths and workplace environments in data science.

- Problem-Solving and Research in Data Science (Projects-oriented)

Top words: **problem model first analytics come ai hard new team product tell example research**

This topic likely covers aspects of problem-solving, modeling, and the application of analytics and artificial intelligence in data science. The mention of "problem," "model," "analytics," "ai," and "research" points to discussions about tackling specific data science problems or projects, possibly in a team or product development environment.

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/014bb0ed-5542-40d6-a843-b9f0a1336534)

### Modelling

#### Text Preprocessing

As for text preprocessing, the urls, line breaks, and digits were removed. For sentiment analysis, Vader lexicon-based sentiment analyser was used due to its capability to detect emjois and informal language which is common in social media lanaguage. The compound polarity scores obtained from the analysis were then regrouped into three sentiment classes: positive ( > 0.05 ) , negative ( < 0.05 ), and neutral. 

To prepare for topic modelling, the stopwords list from nltk was updated by adding custom stopwords that are domain-specific and reddit-specific slangs/words. For example, words like data science is likely to occur in majority of posts. Similarly, words like 'op' (Original poster) is quite common on Reddit.

**Custom Stopwords Removal**:

'back','go','like','get','take','feel','see','also','will','would','lot','stuff','maybe','even',
'actually','probably','may','sure','post','around','one','still','someone','thing','analyst','might','want',
'well','two','pretty','anything','something','already','never','able','ago','bit','cause','cuz','basically',
'yes','no','never','almost','anyone','science','scientist','scientists','data','op','ds','really','will','many',
'much','something','everything','always','etc',

**Experimenting with different parameters for vectorization/tokenization**

**Hyperparameter tuning for LDA model using random-search**


| LDA Model                 | Log Likelihood    |  Perplexity|
|---------------------------|-------------------|------------|
| LDA Model (Before tuning) | = 79871           | 196        |
| LDA Model (Before tuning) | - 79794           | 195        |


#### Challenges and Further Model Improvement

- Text mining is an iterative process and involved a lot of subjective judgement. During this process, I learned the shortcomings of some algorithm. For example, Vader fails to detect certain slangs and sarcasms such as incorrectly identifying "bullshit" as a positive statement.























