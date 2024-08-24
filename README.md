# Comparative Analysis of Prime Ministerial Speeches: Narendra Modi and Manmohan Singh

## Overview
This project presents a comparative analysis of speeches delivered by Prime Minister Narendra Modi (2017-2023) and former Prime Minister Dr. Manmohan Singh (2004-2014). Using natural language processing (NLP) techniques, the analysis uncovers patterns, themes, and trends in their speeches over time.

## Data Sources
The speeches were collected from the following sources:
- **Narendra Modi (NM):** 1,182 speeches extracted from official press releases (2017-2023).
- **Manmohan Singh (MS):** 1,351 speeches obtained from the PMO Archives (2004-2014).

*Note:* Speeches by Narendra Modi from 2014-2016, as well as location data for all speeches, were unavailable.

## Methodology

1. **Data Acquisition and Preprocessing**
   - Web scraping using Selenium and BeautifulSoup4 to extract speech texts.
   - Data cleaning to remove duplicates, empty speeches, and special characters.
   - Tokenization and lemmatization to standardize text for NLP analysis.

2. **Text Representation and Dimensionality Reduction**
   - **Doc2Vec** was used to generate vector representations of speeches, capturing semantic meaning at the document level.
   - **UMAP** was applied for dimensionality reduction to visualize high-dimensional vectors.

3. **Clustering and Topic Analysis**
   - **K-means clustering** grouped speeches based on similarity in their vector representations.
   - The Elbow method was used to determine the optimal number of clusters.
   - Manual annotation, supported by OpenAI's GPT model, was used to assign meaningful labels to each cluster.

## Key Findings

- **Narendra Modi's speeches** exhibited rotational diversity in topic clusters over time, suggesting adaptability and responsiveness to evolving national priorities.
- **Dr. Manmohan Singh's speeches** displayed consistency and a broader range of topics, indicating a stable and wide-ranging approach to governance.
- **Comparative analysis** highlighted distinct thematic focus patterns, reflecting different priorities and communication styles.

## Future Research Directions

- Investigate the link between speech clusters, policy decisions, and their impact on governance.
- Conduct cross-cultural comparisons with global leaders' speeches to understand the influence of context.
- Explore variations in communication strategies across different mediums, such as press conferences and online addresses.
- Perform network analysis based on speech locations to uncover patterns in political communication and regional focus.

## Repository Structure
- `data/`: Raw speech data (CSV format) for both Prime Ministers.
- `notebooks/`: Jupyter notebooks showcasing the data processing, modeling, and visualization steps.
- `models/`: Trained Doc2Vec and clustering models.
- `visualizations/`: Interactive visualizations generated using Plotly.
- `README.md`: Overview of the project.
