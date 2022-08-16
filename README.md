# Introduction

This project is focus on classifying and extracting skills from the resume dataset provided by [Marti Palan](https://www.kaggle.com/datasets/maitrip/resumes) and [Hend Labib](https://www.kaggle.com/code/hendlabib12/resume-extraction/data)from kaggle.

## JUPYTER NOTEBOOK

### 1. [RESUME CLEAN & ADD SKILLS](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/RESUME_CLEAN_%26_ADD_SKILLS_XilinTian.ipynb)

This notebook Focused on clean the resume dataset by using pandas. Droped the NaN rows and columns, then reseted the index. After finishing the cleaning, added the 'skills' columns to that dataset and filled in the score for each resume, which is if the resume contains the skill in that column, it result one in the table, otherwise is zero. Saved the dataset as a [csv](https://github.com/xilin-tian/Resume_Classification/blob/main/original%20data%20and%20result%20csv/resume_add_skills.csv).

### 2. [SIMPLE MATCH & MACHINE LEARNING](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/SIMPLE_MATCH_%26_MACHINE_LEARNING.ipynb)

By imported the csv file that I got in the first notebook, used the [Sørensen–Dice coefficient (Dice similarity coefficient)](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) to calculate the similarity score by setting the TP(True Positive) as the original resume and compared resume both got 1 for the same skill, FP(False Positive) as the original resume and compared resume both got 0 for the same skill, FN(False Negative) as the score of the original resume are not equal to the score of the compared resume. Then listed the ten highest scoring resumes

Secondly, extracted the Category as the label and apply K-means clustering and KNN (for k = 30) on the dataset, however, the accuracy for both algorithms are not good, 1.45% and 13.41% correspodingly. Thus, the resume dataset need more deeper cleaning and remove the noise to increase the accuracy.

### 3. [NLP AND SPACY](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/NLP_AND_SPACY.ipynb)

Deleted the \x and \n in the resume by using re.sub to accomplish my goal, then used the first resume as the sample resume and pick 30 other resumes from different Categories, apply spacy.similarity to get the 'score_Version_1' column and repeat these step on the resumes after removing the stopwords to get 'score_Version_2' column.

> Used spacy and [regex](https://en.wikipedia.org/wiki/Regular_expression) to clean the Resume dataset further（Remove stopwords and \\n）then find the similarity score.

### 4. [Extract SKILLS](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/EXTRACT_SKILLS.ipynb)
Used a jsonl file from [jobzilla](https://github.com/kingabzpro/jobzilla_ai/blob/main/jz_skill_patterns.jsonl), added the 'skills' in to the spacy entity ruler and prase the skills out with a sorted sequence.


### 5.[Similarity of Skills](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/SIMILARITY_OF_SKILLS.ipynb)
Choosed a random resume as the sample, then used Sørensen–Dice coefficient and spacy.similarity to get the table that contained the similarity score with a descending list so that it is clear to see which resume in the dataset has the best match to the sample resume.

### 6.[Classification Through Skills](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/CLASSIFICATION_THROUGH_SKILLS.ipynb)
Used [Elbow Method with Within-Cluster-Sum of Squared Error (WCSS))](https://en.wikipedia.org/wiki/Elbow_method_(clustering) and [Silhouette (clustering))](https://en.wikipedia.org/wiki/Silhouette_(clustering) to testify the appropriate k value for k-mean clustering, both of the methods showed that 30 is the suitable value which is matched the origional numbers of category in the resume dataset.

### 7.[Functions](https://github.com/xilin-tian/Resume_Classification/blob/main/jupyter%20notebook/Functions.ipynb)
Combined the code that I wrote before and created as a list of functions: parse skills, find match resume, and parse the University. Parsed the code to VS code.

## VS CODE

</ol>
