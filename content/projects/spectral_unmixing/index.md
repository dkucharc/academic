---
title: 'Linear unmixing models on hyperspectral data'
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
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.)

tags: ["Bachelor", "Free", "ML", "Remote Sensing"]

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
#  - name: Custom Link
#    url: http://example.org

url_pdf: 'https://downloads.hindawi.com/journals/mpe/2020/3735403.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
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

Linear unmixing is a popular technique used for analyzing hyperspectral data. Hyperspectral imaging is a remote sensing technique that captures the electromagnetic radiation reflected from the Earth's surface across hundreds of narrow spectral bands. Linear unmixing is used to extract information about the different materials present in the scene based on their spectral signatures.

The linear unmixing model assumes that each pixel in the hyperspectral image can be represented as a linear combination of the spectral signatures of the materials present in that pixel. In other words, the pixel's spectrum is a weighted sum of the spectra of the constituent materials. This model is expressed mathematically as:

𝐼(λ) = 𝑆(λ)𝐴

where 𝐼(λ) is the observed spectrum at wavelength λ, 𝑆(λ) is the matrix of spectral signatures for the materials of interest, and 𝐴 is the abundance matrix that represents the proportion of each material present in the pixel.

The linear unmixing process involves estimating the abundance matrix 𝐴 for each pixel in the image. This is typically done using optimization techniques such as least squares, non-negative least squares, or constrained least squares. Once the abundance matrix is estimated, the abundance maps can be generated for each material, providing information about the spatial distribution of the different materials in the scene.

Linear unmixing is widely used in applications such as mineral mapping, vegetation analysis, and urban land-use classification, among others. It is a powerful tool for extracting information from hyperspectral data and can provide valuable insights into the Earth's surface and its composition.
