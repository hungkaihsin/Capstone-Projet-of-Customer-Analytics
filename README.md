# Capstone Project: Amazon Customer Sentiment Analysis

## Project Overview
This project is a capstone for a Customer Analytics course, following the CRISP-DM framework. The goal is to analyze over 37,000 customer reviews for Amazon's electronic products to identify the key drivers of customer satisfaction and dissatisfaction.

The final product is a machine learning model that can automatically classify a review as "Positive" or "Negative." This model successfully identifies 56% of all incoming negative reviews, allowing business teams to find and address customer complaints proactively.

## 1. Business Understanding
The core business problem is to understand why customers are happy or unhappy. By classifying review sentiment, we can provide actionable insights to:
* **Product Development:** Pinpoint specific features that need improvement and identify new features customers desire.
* **Marketing:** Craft more effective messaging that highlights features customers love.
* **Quality Assurance:** Identify products with recurring quality control issues.

## 2. Data Understanding
* **Dataset:** [Consumer Reviews of Amazon Products](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products) from Kaggle.
* **Content:** The dataset contains over 37,000 cleaned reviews, including review text, ratings, and product categories.
* **Key Limitation:** The dataset is limited to electronics and only includes products manufactured by Amazon.

## 3. Data Preparation & Exploratory Data Analysis (EDA)

### Preparation
* Text was cleaned by converting to lowercase, removing punctuation/numbers, and removing standard English stopwords.
* Duplicate reviews were dropped.
* Ratings were mapped to a binary sentiment class:
    * **Negative (0):** 1-star and 2-star ratings
    * **Positive (1):** 4-star and 5-star ratings
* 3-star (neutral) reviews were dropped.

### Key EDA Findings
* **Overwhelmingly Positive:** The data is highly imbalanced, with over 25,000 5-star reviews. This makes accuracy a useless metric and requires special handling (e.g., `class_weight`, SMOTE).
* **Negative Reviews are "Most Helpful":** 1-star reviews receive the most "helpful" votes from other shoppers, meaning they have a disproportionately large impact on new customers.
* **Negative Drivers Identified:** Word clouds revealed that negative reviews are dominated by words like "tablet," "battery," "screen," and "problem," while positive reviews feature "love," "easy," "use," and "kids."

## 4. Modeling
This was a binary classification task. The primary evaluation metric was the **Macro F1-Score** due to the severe class imbalance.

### Models Tested
* **Baseline Models:**
    * Multinomial Naive Bayes: Failed (Macro F1: 0.50).
    * Logistic Regression (Balanced): Macro F1: 0.65.
    * Linear SVC (Balanced): Macro F1: 0.66.
    * Baseline LSTM (Balanced): Best Baseline (Macro F1: 0.68).
* **Improved Models (Tuning):**
    * Tuned LinearSVC: CV Score: 0.7015.
    * Tuned LSTM: Failed (Test Score: 0.66, worse than baseline).
    * Tuned Logistic Regression (with SMOTE): **Winner!** (CV Score: 0.7489).

### Final Model Selection
The **Tuned Logistic Regression with SMOTE** was the clear winner. This model first uses `TfidfVectorizer` to process the text, then `SMOTE` to synthetically create more "negative" samples, and finally a `LogisticRegression` classifier.

## 5. Evaluation
The final model was evaluated on a held-out, unseen test set.

| Metric | Score | Business Interpretation |
| :--- | :--- | :--- |
| **Macro F1-Score** | 0.73 | The model is well-balanced and effective at finding both classes. |
| **Negative Recall** | 0.56 | **(Key Success)** The model finds 56% of all true negative reviews. |
| **Negative Precision** | 0.41 | When the model flags a review as negative, it is correct 41% of the time. |

The model is a high-recall tool. It intentionally makes more "false positive" mistakes (low precision) to achieve its primary goal: finding over half of all angry customers (high recall). This is a successful and valuable trade-off for the business.

## 6. Recommendations & Next Steps

### Key Recommendations
* **Product Team:** Immediately investigate the "tablet" product line for recurring issues with "battery" life and "screens."
* **Marketing Team:** Use words like "easy to use" and "great for kids" in marketing campaigns, as this language strongly resonates with 5-star reviews.
* **Support Team:** Use this model as a real-time triage tool to find and respond to negative reviews before they get traction.

### Future Work
* **Build a Frontend Dashboard:** Deploy this model as a user-friendly dashboard so the Product and Support teams can use it without running code.
* **Improve Precision:** Experiment with adjusting the model's decision threshold (e.g., from 0.5 to 0.7) or using advanced samplers like ADASYN to reduce the number of false positives.

### How to Run This Project

### Clone the repository:
```bash
git clone https://github.com/hungkaihsin/Capstone-Projet-of-Customer-Analytics.git
cd Capstone-Projet-of-Customer-Analytics

```

### Create a virtual environment (Recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Run the Jupyter Notebook:
```bash
jupyter notebook main.ipynb
```
