# Topic Modelling and Sentiment Analysis - Data Science Subreddit

#### -- Project Status - Completed

## Project Objective

[Data Science subreddit](https://www.reddit.com/r/datascience/) is the largest data science community on Reddit with over 1.6 million members. Due to the anonymous nature, a lot of discussions around career, job, as well as technical challenges are typically found in this subreddit. As a data professional myself, I often resort to this subreddit stay up to date with the job market, read the technical solutions of peers, etc. This led me to wonder what topics are trending and the sentiment around the discussions. The objective is to extract the themes among the top posts from 2023 and also to understand the sentiment by different flairs. 

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

## Exploratory Analysis

The following are the top 10 topics with highest engagement scores in 2023:

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/80a1fa41-bc95-4136-848d-342be8365417)

It appears that the discussions around job market (possibly due to the massive layoffs in tech industry) received more attention compared to other topics. 

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/3a42e7c6-c2f8-433e-b4bc-158a259f8385)

## Sentiment Analysis

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/4ee9e69c-271e-4a27-aa1a-5802d43d3ca7)



![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/34dd8506-607e-41b7-b412-186a4e4040e5)


## Topic Modelling


![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/990c8dbe-6b44-43a2-9ade-9a2a8ce32f8e)



- Practical Application and Collboration

This topic is likely about the application of data science in business and team settings, focusing on modeling, machine learning, and the integration of coding in business processes. Keywords such as "use," "model," "business," "ml" (machine learning), "code," and "engineering" reflect discussions on how data science is applied in real-world scenarios, possibly involving teamwork and collaboration.

- Job Seeking and Career Progression
  
This topic appears to center around the job market and career development in the data science field. Keywords like "job," "project," "role," "interview," "apply," "position," and "experience" suggest discussions related to finding new job opportunities, applying for positions, and discussing the experiences necessary for certain roles or career changes.

- Skills and Tools

This topic focuses on the practical skills and tools necessary in data science, such as Python, SQL, and general analytical skills. Terms like "python," "skill," "sql," and "big company" emphasize the technical competencies needed to succeed in the field and discussions about how to improve or acquire these skills.

- Learning and Career Development

Here, the emphasis seems to be on the learning journey and career advice within data science. Keywords like "learn," "start," "help," "career," "course," and "company" suggest advice threads, sharing of learning resources, or discussions about navigating career paths and workplace environments in data science.

- Problem-Solving and Research in Data Science (Projects-oriented)

This topic likely covers aspects of problem-solving, modeling, and the application of analytics and artificial intelligence in data science. The mention of "problem," "model," "analytics," "ai," and "research" points to discussions about tackling specific data science problems or projects, possibly in a team or product development environment.


#### Feature Engineering

- The data are right skewed. Hence, a log transformation was used to achieve a normal distribution.
- To reduce the dimensionality of the features, the car brands were regrouped into three groups: high-end brands (Toyota) , mid-range brands (Honda, Nissan and Mitsubishi), and Low-end brands (Suzuki and Daihatsu). Note that this grouping was determined based on the price distributions in the dataset.
- Similarly, I also regrouped the colours into two groups: black and others, as the black colour seems to be the main differentiator. I also combined the 'semi-auto' and 'manual' into one group.

#### Model Exploration

- As a baseline model, a Linear Regression model was chosen for comparison purposes. Since a non-linearity was also detected, a Random Forest model was explored to uncover complex patterns.

- As a primary metric, the goal was to achieve a low Mean Absolute Error (MAE) value of 1,000 - 2,000 USD, which was equivalent to 15 - 30 lakhs MMK at the time.

- For Linear regression, it was found that the model comformed to primary assumptions: linearity, indepedence of residuals (with Durbin Watson test score between 1.5 and 2.5), improved normality after log transformation, and homosdeasticity with randomly scattered residuals. However, some multicollinearity issues were also identified. So, Ridge and Lasso regularisation were explored. Prior to conducting regularisation, it was ensured that the training data and test data were standardised properly.

**Cross-validation Results**

| LDA Model                 | Log Likelihood    |  Perplexity|
|---------------------------|-------------------|------------|
| LDA Model (Before tuning) | = 79871           | 196        |
| LDA Model (Before tuning) | - 79794           | 195        |


The final score on test set is R2 - 0.834, MAE - 1,921

## Challenges and Further Model Improvement

- Data Availability : The dataset comprises only 500 data points, which is insufficient to cover all car models. This limitation constrains the model's ability to generalize across the full spectrum of vehicles.

- Overfitting issues: There is a model performance gap (6%) between the test set and the training set. Despite efforts in parameter tuning to reduce overfitting, this gap persisted, likely due to the small sample size and imbalanced class distribution among car models. Given that Toyota models constitute the majority of the dataset, the model may struggle to generalize effectively to less represented or unseen models.






















