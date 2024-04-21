# Car Auction Price Predictions (Myanmar)

#### -- Project: Freelance Project

## Project Objective
This project was carried out as part of freelance contract for one of the automotive players in Myanmar back in 2019. Until recently, due to import restrictions, Myanmar's automotive market was primarily dominated by the second-hand cars. As a result, the market lacked transparency and a proper pricing mechanism as the transactions were mainly handled by unofficial car brokers. The objective of the project was to understand the factors influencing the second-hand car prices and to estimate the car prices based on their attribtues. The end goal was to develop a data-driven fair pricing mechanism for an automotive platform.

### Skills Used
* Data Collection
* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest

### Technologies
* Python 

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is available [here](https://github.com/khinydnlin/car_auction_price_predictions/blob/main/dataset.csv) within this repo.   
3. Data processing and modelling scripts are documented in a [Jupyter notebook](https://github.com/khinydnlin/car_auction_price_predictions/blob/main/Car%20Auction%20Price%20Predictions.ipynb).
4. The project findings and other details can be found below:

## Project Description

### Data Sources

The data was manually collected from the major car brokers in the market because of the lack of public data on resale prices. The following featuers were collected:

| Data                  |
| ----------------------|
| car brand             |
| car make              |
| engine power          | 
| mileage in km         |  
| colour                |
| steering position     |
| transimission type    |
| fuel type             |
| car body type         |
| price in MMK          |
| price in USD          |
*Note: 1 USD - 1,400 Myanmar Kyats (MMK) exchange rate was used

### Machine Learning Model Development 

#### Insights

![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/3a42e7c6-c2f8-433e-b4bc-158a259f8385)


![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/408469db-e0fe-40fc-9182-8c5d7722712d)


![image](https://github.com/khinydnlin/topic_modelling_ds_subreddit/assets/145341635/34dd8506-607e-41b7-b412-186a4e4040e5)


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

| ML Models        | R2    | MAE (USD) |
|------------------|-------|-----------|
| Linear Regression| 0.829 | 2,520     | 
| Ridge Regression | 0.834 | 2,363     |
| Lasso Regression | 0.749 | 2,714     |
| Random Forest    | 0.892 | 1,624     |

Due to the lowest MAE scores of Random Forest, the Random Forest model was selected as final model to fit on the test data.

The final score on test set is R2 - 0.834, MAE - 1,921

## Challenges and Further Model Improvement

- Data Availability : The dataset comprises only 500 data points, which is insufficient to cover all car models. This limitation constrains the model's ability to generalize across the full spectrum of vehicles.

- Overfitting issues: There is a model performance gap (6%) between the test set and the training set. Despite efforts in parameter tuning to reduce overfitting, this gap persisted, likely due to the small sample size and imbalanced class distribution among car models. Given that Toyota models constitute the majority of the dataset, the model may struggle to generalize effectively to less represented or unseen models.






















