# Research Data Impact Dashboard

A Streamlit-based interactive dashboard designed to help non-specialists understand the value and impact of research datasets. This project focuses on making complex research data accessible and meaningful to diverse stakeholders.

## Overview

The **Research Data Impact Dashboard** transforms raw research data into actionable insights through intuitive visualizations and interactive exploration. Rather than overwhelming users with variables and codebooks, it tells a data story by:

- Showing **who** is represented in the data
- Demonstrating **what** societal questions can be answered
- Revealing **which** factors matter most
- Illustrating **how** outcomes change over time
- Connecting findings to **policy and practice**

## Features

### 1. **Understand People in Context**
   - Interactive scatter plots exploring relationships between variables
   - Color-coded visualizations by demographic factors (e.g., age)
   - Real-time filtering capabilities

### 2. **Track Change Over Time**
   - Multi-wave longitudinal data visualization
   - Trajectory analysis across demographic groups
   - Time-series trend identification

### 3. **Explore What Shapes Outcomes**
   - Machine learning-based feature importance analysis
   - Random Forest models to identify key predictors
   - Interpretable rankings of factors affecting outcomes

### 4. **Inform Policy and Practice**
   - Regional and demographic comparisons
   - Actionable insights for stakeholders
   - Evidence-based decision support

## Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Fast, easy-to-use web app framework
- **Data Processing**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Visualization**: [Plotly](https://plotly.com/) - Interactive charts and graphs
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/) - Feature importance & regression models

## Installation

### Prerequisites
- Python 3.7+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/neelsoumya/chatbot_esrc.git
   cd chatbot_esrc
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run gui.py
```

The dashboard will open in your default browser at `http://localhost:8501`

### Interactive Features

- **Sidebar Controls**: 
  - Select outcome variables to analyze
  - Adjust age range sliders to filter participants
  - Real-time dashboard updates based on selections

- **Key Performance Indicators (KPIs)**:
  - Display dataset size, temporal coverage, and variable count
  - Quick overview of data scope

- **Research Questions Section**:
  - Pre-defined research questions answerable by the dataset
  - Examples: "How do financial pressures affect mental health?"

## Project Structure

```
chatbot_esrc/
├── gui.py                 # Main Streamlit application
├── requirements.txt       # Python package dependencies
├── LICENSE                # GPL-3.0 License
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Current Data

The dashboard currently uses **simulated data** for demonstration purposes:

- **Participants**: 25,000+
- **Years of Data**: 10
- **Data Waves**: 12 collection points
- **Variables**: 1,000+

**Variables include**:
- `age` - Participant age (18-80)
- `financial_strain` - Financial stress metrics
- `social_support` - Social connection measures
- `sleep_quality` - Sleep quality scores
- `exercise` - Physical activity levels
- `wellbeing` - Overall wellbeing outcome

## Example Use Cases

### For Researchers
- Demonstrate data richness and potential impact
- Show preliminary findings to funders
- Communicate research value to broader audiences

### For Policymakers
- Identify regional disparities and targeted interventions
- Understand demographic differences in wellbeing
- Make evidence-based policy decisions

### For Stakeholders
- Explore relationships between social factors and outcomes
- Understand longitudinal changes in populations
- Identify vulnerable groups needing support

## Future Enhancements

- [ ] Integration with real research datasets
- [ ] Multi-language support
- [ ] Advanced filtering and custom queries
- [ ] Export functionality for reports
- [ ] Predictive modeling features
- [ ] API integration for live data sources
- [ ] User authentication and role-based access

## Dependencies

See `requirements.txt` for exact versions:

```
streamlit
plotly
pandas
numpy
scikit-learn
```

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

## Author

**Neel Soumya** - [@neelsoumya](https://github.com/neelsoumya)

## Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Submit pull requests with improvements
- Share ideas for dataset integration

## Contact & Support

For questions, issues, or collaboration opportunities, please open an issue on [GitHub Issues](https://github.com/neelsoumya/chatbot_esrc/issues).

---

**Note**: This project is designed for research and educational purposes. When integrating with real datasets, ensure proper data privacy and ethical approvals are in place.
