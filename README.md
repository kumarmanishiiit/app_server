# API Gateway

This is a simple API Gateway built using Flask that proxies requests to downstream applications. It supports dynamic routing using application information stored in a JSON file (`apps.json`).

## Features
- API Gateway to forward requests to downstream Flask applications
- Dynamic configuration using `apps.json`
- Supports all major HTTP methods (GET, POST, PUT, DELETE)
- Health check endpoint
- Application listing endpoint

---

## Project Structure

```
.
├── init.py          # Main application
├── apps.json        # Configuration file for downstream applications
└── README.md        # Project documentation
```

---

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)

---

## Installation

1. **Clone the Repository:**
```bash
git clone <repository_url>
cd api-gateway
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure Downstream Applications:**
- Create an `apps.json` file in the same directory. Example:
```json
[
  {
    "name": "app1",
    "url": "http://localhost:5000"
  },
  {
    "name": "app2",
    "url": "http://localhost:5001"
  }
]
```

4. **Set the Port (Optional):**
```bash
export APP_PORT=6001
```

5. **Run the Application:**
```bash
python init.py
```

---

## API Endpoints

1. **Home:**
```
GET /
Response: {"message": "Welcome to the API Gateway!"}
```

2. **List Registered Applications:**
```
GET /apps
Response: List of registered applications from apps.json
```

3. **Proxy Requests:**
```
GET, POST, PUT, DELETE /proxy/<app_name>/<path:endpoint>
Example: /proxy/app1/api/data
```
- **app_name:** The name of the application (from `apps.json`)
- **endpoint:** The downstream application endpoint

4. **Health Check:**
```
GET /health
Response: {"status": "healthy"}
```

---

## Error Handling
- **404:** App not found in `apps.json`
- **405:** Invalid HTTP method
- **500:** Proxy request failure

---

## Notes
- Ensure the downstream applications are running before proxying requests.
- The application uses `requests` library for forwarding requests.

---

## License
This project is licensed under the MIT License. See LICENSE for more details.

