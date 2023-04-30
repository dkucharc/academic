---
title: 'Matrix factorization techniques for recommender systems'
# subtitle: 'Matematyczne aspekty koncepcji dryftu danych w kontekście współczesnych metod uczenia maszynowego'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

# Author notes (optional)
date: '2023-03-21T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['7']

# Publication name and optional abbreviated publication name.
# publication: In *Wowchemy Conference*
# publication_short: In *ICW*

# (abstract: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam. Quisque risus orci, mollis id ante sit amet, gravida egestas nisl. Sed ac tempus magna. Proin in dui enim. Donec condimentum, sem id dapibus fringilla, tellus enim condimentum arcu, nec volutpat est felis vel metus. Vestibulum sit amet erat at nulla eleifend gravida.)

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: ["Master", "Booked"]

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#  url: http://example.org

url_pdf: 'https://ieeexplore.ieee.org/document/5197422'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'dd'
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.

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
---


Matrix factorization is a popular technique in machine learning used for dimensionality reduction, data compression, and collaborative filtering. It involves decomposing a matrix into two or more matrices that represent latent features or factors.

The goal of matrix factorization is to extract meaningful latent factors from a matrix that can be used to make predictions or recommendations. For example, in collaborative filtering, matrix factorization can be used to predict a user's rating for an item based on their historical ratings and the ratings of similar users.

Matrix factorization techniques are widely used in recommender systems to provide personalized recommendations to users based on their historical behavior or preferences. Here are some popular matrix factorization techniques used for recommender systems:

- Singular Value Decomposition (SVD): SVD is a widely used matrix factorization technique for recommender systems. It decomposes the user-item interaction matrix into two lower-rank matrices, which represent latent factors. These factors represent the user's preferences and the item's characteristics.

- Alternating Least Squares (ALS): ALS is another popular matrix factorization technique for recommender systems. It iteratively minimizes the error between the original matrix and the reconstructed matrix using alternating optimization techniques.

- Non-negative Matrix Factorization (NMF): NMF is a matrix factorization technique that factorizes the user-item interaction matrix into two non-negative matrices, which represent the user preferences and item characteristics. It is often used for recommender systems that require non-negative values.

- Bayesian Personalized Ranking (BPR): BPR is a matrix factorization technique that learns latent factors for users and items by maximizing the likelihood of the observed interactions while minimizing the likelihood of unobserved interactions.

- Factorization Machines (FM): FM is a matrix factorization technique that can capture complex interactions between user preferences and item characteristics. It is a more powerful technique than SVD or NMF, but it requires more computational resources.

These techniques have different strengths and weaknesses and can be used depending on the specific needs of the recommender system.
