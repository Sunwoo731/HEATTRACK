# HEATTRACK: Satellite-Based Thermal Leak Detection System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**HEATTRACK** is a **Physics-Aware AI System** for detecting district heating pipe leaks using **Arirang-3A (KOMPSAT-3A)** satellite imagery. By combining thermal diffusion physics with deep learning (TS²uRF), it identifies micro-leaks in underground infrastructure with high precision.

## 🚀 Key Features

*   **TS²uRF Super-Resolution**: Fuses KOMPSAT-3A (Thermal) and Sentinel-2 (Optical) to achieve **10m resolution** (R²=0.76).
*   **Physics-Aware AutoEncoder**: Incorporates thermal diffusion equations into the loss function to minimize false alarms.
*   **High-Precision Detection**: Achieved **AUC 0.9371** (vs. 0.9047 for statistical models), validating effectiveness in Anyang downtown test sites.

---

## 📊 Detection Results & Analysis

### 1. TS²uRF Super-Resolution (Before vs After)
Demonstrates the restoration of 10m-level thermal details from blurred Arirang satellite imagery.
![Super Resolution Result](docs/assets/new_arirang_consolidated.png)
> **Result**: Average R² Score **0.7608** (Successful structural restoration)

### 2. Anomaly Detection Performance (ROC Curve)
Comparison between the proposed Physics-Aware model (Red) and traditional statistical monitoring (Blue).
![ROC Curve](docs/assets/roc_curve_analysis.png)
> **Result**: **AUC 0.937** (approx. 3.2%p improvement over baseline)

### 3. Applied Case: Anyang Downtown Heatmap
Visualized "Linear Anomalies" along the major district heating pipelines in Pyeongchon, Anyang.
![Anyang Heatmap](docs/assets/anyang_zoom_report.png)
> **Result**: Successfully pinpointed high-risk segments matching underground facility maps.

---

## 🏗 System Architecture

The pipeline consists of four main stages:

1.  **Data Acquisition**: KOMPSAT-3A (Arirang) Thermal Infrared + Sentinel-2 MSI.
2.  **Super-Resolution (TS²uRF)**: Restoring spatial details of thermal imagery using logic-based texture transfer from optical data.
3.  **Physics-Informed Modeling**:
    *   *Hybrid Loss*: MSE + Thermal Diffusion Constraint.
    *   *Normal Learning*: Learning thermodynamic patterns of safe buried pipes.
4.  **Reporting**: Visualizing "Linear Anomalies" along the transmission network.

## 📂 Project Structure

```bash
HEATTRACK/
├── configs/           # Configuration files
├── src/               # Core source code
│   ├── data/          # Data loaders & Synthetic generators
│   ├── models/        # AutoEncoder & Isolation Forest models
│   ├── processing/    # Downscaling & Preprocessing logic
│   └── visualization/ # Dashboard & Map generation
├── scripts/           # Utility scripts (training, evaluation)
├── docs/              # Documentation
└── notebooks/         # Jupyter Notebooks for experiments
```

## 💻 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/HEATTRACK.git
    cd HEATTRACK
    ```

2.  **Set up Environment**
    ```bash
    # using conda
    conda create -n heattrack python=3.9
    conda activate heattrack
    
    # install dependencies
    pip install -r requirements.txt
    ```

3.  **Configuration**
    Copy the example config and edit it with your settings (e.g., Google Cloud Project ID).
    ```bash
    cp configs/config.example.yaml configs/config.yaml
    ```

## ⚡ Quick Start

**1. Generate Synthetic Pipe Network (Demo)**
Create a simulated pipe network for testing without restricted GIS data.
```bash
python -m src.main simulate
```

**2. Download Satellite Data**
Fetch the latest available satellite imagery for the target regions.
```bash
python -m src.main download
```

**3. Run Analysis Pipeline**
Propagate data through the downscaling and detection models.
```bash
python -m src.main pipeline
```

## 📊 Data & Reproducibility

*   **Satellite Data**: Sources from KARI (KOMPSAT) and Copernicus (Sentinel-2).
*   **Pipe Data**: Due to security regulations, real underground facility maps cannot be shared. A **synthetic generator** (`src.data.synthetic`) is provided to create realistic mock data for reproduction.

## 🛡 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Credits

Developed for the [Project Name/Course] by [Your Name/Team].
Special thanks to Korea District Heating Corp (KDHC) for domain insights.
