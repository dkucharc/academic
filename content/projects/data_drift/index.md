---
title: 'Mathematical aspects of data drift in machine learning'
subtitle: 'Matematyczne aspekty koncepcji dryftu danych w kontekście współczesnych metod uczenia maszynowego'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

# Author notes (optional)
date: '2022-12-05T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['0']

# Publication name and optional abbreviated publication name.
# publication: In *Wowchemy Conference*
# publication_short: In *ICW*

# abstract: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam. Quisque risus orci, mollis id ante sit amet, gravida egestas nisl. Sed ac tempus magna. Proin in dui enim. Donec condimentum, sem id dapibus fringilla, tellus enim condimentum arcu, nec volutpat est felis vel metus. Vestibulum sit amet erat at nulla eleifend gravida.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**OpenAI DALL-E 2**](https://openai.com/dall-e-2/)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
# **Słowa kluczowe/Keywords:** Miary podobieństwa rozkładów, np. współczynnik stabilności populacji (*ang. population stability index*), dywergencja Kullbacka-Leiblera (*ang. Kullback-Leiblera divergence*)
---

Data drift is a common problem in machine learning where the statistical properties of the data used for model training change over time. This can lead to a drop in model performance, as the model is no longer optimized for the new distribution of data.

Data drift can occur for many reasons, such as changes in the data collection process, changes in user behavior, or changes in the underlying system being modeled. To mitigate data drift, it is important to monitor the performance of the model over time and retrain it with updated data when necessary.

There are several techniques that can be used to detect and address data drift, including:

Monitoring key performance metrics such as accuracy, precision, and recall over time to detect drops in model performance.

Using statistical tests to compare the distributions of the data used for training and testing the model.

Using data augmentation techniques such as synthetic data generation to supplement the training data and make the model more robust to changes in the data distribution.

Employing domain adaptation techniques to adapt the model to new data distributions, while minimizing the need for retraining the entire model.

By proactively monitoring and addressing data drift, machine learning models can maintain high levels of accuracy and continue to provide valuable insights even as data distribution changes over time.
