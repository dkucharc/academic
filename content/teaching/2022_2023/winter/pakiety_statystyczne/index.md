---
title: Pakiety Statystyczne
summary: Laboratoria programistyczne prowadzone do wykładu [dr Andrzeja Giniewicza](http://prac.im.pwr.edu.pl/~giniew/doku.php?id=rok2223:zimowy:ps), w semestrze zimowym 2022/2023 dla studentów Wydziału Matematycznego, studiów I stopnia, kierunek Matematyka Stosowana. 

tags:
  - Winter (2022/2023)
date: '2022-10-01'

# Optional external URL for project (replaces project detail page).
external_link: ''

# image:
#  caption: Photo by rawpixel on Unsplash
#  focal_point: Smart

# links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Zajęcia będą się skupiać na przedstawieniu prawidłowego wyciągania wniosków z analiz statystycznych wykonywanych z wykorzystaniem pakietu statystycznego R.

**Zasady zaliczenia**
- Prezentacja (25 pkt).
  - [x] (2022-11-03) Metody oceny klasyfikacji w praktyce przy użyciu (`caret::confusionMatrix`) 
  - [x] (2022-11-03) Nieparametryczne metody estymacji (estymatory typu Jacknife, Bootstrap)
  - [x] (2022-11-03) Estymatory największej wiarygodności i metody optymalizacji (`stats4::mle`, `stats::nlm`) 
  - [x] (2022-11-03) Estymatory momentów centralnych (`Umoments`)
  - [ ] ...
- Aktywność (15 pkt).
- Sprawozdania w parach (60 pkt), w tym:
  - statystyka opisowa (30 pkt),
  - testowanie hipotez (30 pkt).

**Zajęcia laboratoryjne:**

0. Zajęcia wprowadzające (2022-10-06)
1. Przegląd cech statystycznych (2022-10-13)
2. Praktyczne aspekty teorii estymacji (2022-10-20) 
3. Metody estymacji i metody oceny estymatorów oraz klasyfikatorów (2022-10-27)
4. Prezentacje (2022-11-03)
5. Zajęcia odwołane (2022-11-10)
6. Wykresy (2022-11-17)
  [[Zadanie]](https://biocorecrg.github.io/CRG_RIntroduction/exercise-12-ggplot2.html)</br>
  **Referencje:**
      - [plotly](https://plotly.com/r/)
      - [ggplot2](https://ggplot2.tidyverse.org/)
7. Zajęcia odwołane (2022-11-24)
8. Testowanie hipotez - wstęp (2022-12-01)
9. Testowanie hipotez - analiza mocy testów (2022-12-08)
10. Praca zespołowa - projekt 1 (2022-12-15)
11. Testowanie normalności - analiza symulacyjna testów na podstawie [Mohd Razali, Nornadiah & Yap, Bee. (2011). Power Comparisons of Shapiro-Wilk, Kolmogorov-Smirnov, Lilliefors and Anderson-Darling Tests](https://www.researchgate.net/profile/Bee-Yap/publication/267205556_Power_Comparisons_of_Shapiro-Wilk_Kolmogorov-Smirnov_Lilliefors_and_Anderson-Darling_Tests/links/5477245b0cf29afed61446e1/Power-Comparisons-of-Shapiro-Wilk-Kolmogorov-Smirnov-Lilliefors-and-Anderson-Darling-Tests.pdf) (2022-12-22) 

12. Testowanie normalności cd. (2023-01-12)
13. Prezentacje:
  - Zarządzanie srodowiskiem `R` i jego zaleznosciami na podstawie [packrat](https://rstudio.github.io/packrat/), [renv](https://rstudio.github.io/renv/articles/renv.html) oraz [conda](https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/).
  - Modele regresji w oparciu o biblioteke[caret](https://topepo.github.io/caret/)
  - Analiza danych tabularycznych z wykorzystaniem biblioteki [dplyr](https://dplyr.tidyverse.org/)
  - Python + R = PythonR. Wykorzystanie jezyka programowania `python` w srodowisku `R` na podstawie biblioteki [reticulate](https://rstudio.github.io/reticulate/index.html)
     

14. TBA (2022-01-26)

**Materiały pomocnicze**
- [`knitr`: Elegant, flexible, and fast dynamic report generation with R](https://yihui.org/knitr/)
- [R Markdown Cookbook](https://bookdown.org/yihui/rmarkdown-cookbook/)

**Dobre praktyki programistyczne w języku R**
- [Standardy kodowania](https://style.tidyverse.org/)
- [Operator pipe `%>%` - wprowadzenie](https://www.datacamp.com/tutorial/pipe-r-tutorial)
