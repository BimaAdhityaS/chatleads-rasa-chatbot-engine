# 🤖 Rasa Chatbot API

This project uses **Rasa Open Source** to provide a chatbot that can be interacted with through HTTP API endpoints.

## 📦 Requirements

- Python 3.8 or higher
- Rasa Open Source
- (Optional) Ngrok for public URL testing
- cURL or Postman for API testing

## 🔧 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-project.git
    cd your-project
    ```

2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install rasa
    ```

4. Train the model:
    ```bash
    rasa train
    ```

## 🚀 Running the Rasa API Server

Run the Rasa server with API access enabled:

```bash
rasa run --enable-api --cors "*" --debug