# Sports Celebrity Image Classifier

https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/5163bf7d-6dce-4a22-9171-1d4a7a3e44d5

## In this data science and machine learning project, I have classified sports personalities. I have restricted classification to only 5 people,

1. Maria Sharapova
2. Serena Williams
3. Virat Kohli
4. Roger Federer
5. Lionel Messi
## Technologies used in this project,
1. Python 3.8
2. Numpy and OpenCV for data cleaning
3. Matplotlib & Seaborn for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI
## Model Selection and Methodology


![Screenshot (98)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/18500676-2694-4a72-878e-b288c7c5a7ff)

In this project, OpenCV haarcascade was used to detect face and two eyes. Wavelet transform was used to extract these features from the images. Finally after processing and cleaning the data, it was given as input to models. Various models were tried using GridSearchCV and Support Vector Machine (SVM) Algorithm was found to give the best resutls with a score of 74.42%.

![Screenshot (97)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/fb73604c-8df4-4f9b-a04d-b94820550021)

Above is the heatmap showing the results of Support Vector Machine (SVM) Algorithm on test data. For test images, SVM was found to give a score of 95%. The model accuracy could be improved by using a bigger dataset. Also deep learning may give better results for image classificaion

# Frontend Snapshot

![Screenshot (90)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/b856a7a3-b8c7-4ba0-9667-b9eb1ab43791)
 
# Result Snapshot
 # 1. Maria Sharapova

![Screenshot (91)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/be482411-1338-4781-aaf1-134f2ebf73ab)
# 2. Lionel Messi
![Screenshot (92)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/a3a22e99-6fc5-41dd-9130-19257cdfe88d)
# 3. Serena Williams
![Screenshot (93)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/302bf23b-d509-4a5a-89f6-90d2d1e74201)
# 4. Roger Federer
![Screenshot (94)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/d612eeb8-7a77-4d6b-9a97-186d7b5504ca)
# 5. Virat Kohli
![Screenshot (96)](https://github.com/ayushi825/SportsPersonClassifier/assets/90374474/abafb56b-e545-47fe-b4d9-b28821b6f7a3)
