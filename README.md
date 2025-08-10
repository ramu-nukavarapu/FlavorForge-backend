# ⚙️ FlavorForge Backend API

A simple and efficient backend API for the FlavorForge platform. This API provides all the necessary data for the frontend dashboard, product management, and market intelligence features by processing data directly from CSV files.

---

### ✨ Endpoints

* **`GET /api/dashboard/metrics`**: Calculates and returns key dashboard metrics.
* **`GET /api/products`**: Retrieves a paginated and filterable list of products.
* **`POST /api/products`**: Creates a new product and generates a market score.
* **`GET /api/market-trends`**: Returns trend data from the `market_trends.csv` file.
* **`POST /api/analyze-product`**: Analyzes a product concept and returns AI-generated suggestions.
* **`GET /api/competitors`**: Provides a list of competitors, filterable by category.

---

### 🛠️ Tech Stack

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Dependency Management**: [uv](https://github.com/astral-sh/uv)
* **Data Processing**: [Pandas](https://pandas.pydata.org/)
* **Server**: [Uvicorn](https://www.uvicorn.org/)
* **Validation**: [Pydantic](https://docs.pydantic.dev/)

---

### 📦 Getting Started

Follow these steps to set up and run the backend API.

#### 1. Prerequisites

Make sure you have Python 3.9+ and `uv` installed on your system.

#### 2. Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ramu-nukavarapu/FlavorForge-backend.git
    cd FlavorForge-backend
    ```
2.  Install dependencies using the `pyproject.toml` file:
    ```bash
    uv sync
    ```

#### 3. Running the API

Start the Uvicorn server in the project's root directory. The API will be available at `http://127.0.0.1:8000`.
```bash
uvicorn app.main:app --reload
```