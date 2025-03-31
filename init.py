from flask import Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)

# Load app details from JSON file
def load_apps():
    with open('apps.json', 'r') as f:
        return json.load(f)
    
apps = load_apps()


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API Gateway!"})

# Endpoint to list all applications
@app.route('/apps', methods=['GET'])
def list_apps():
    return jsonify(apps)

# Proxy the request to a specific application based on name
@app.route('/proxy/<app_name>/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_request(app_name, endpoint):
    # Find the app by name
    app_info = next((app for app in apps if app['name'] == app_name), None)

    if not app_info:
        return jsonify({"error": "App not found"}), 404

    try:
        # Forward the request to the respective application
        app_url = f"{app_info['url']}/{endpoint}"
        if request.method == 'GET':
            response = requests.get(app_url)
        elif request.method == 'POST':
            response = requests.post(app_url, json=request.json)
        elif request.method == 'PUT':
            response = requests.put(app_url, json=request.json)
        elif request.method == 'DELETE':
            response = requests.delete(app_url)
        else:
            return jsonify({"error": "Invalid HTTP method"}), 405

        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Health Check For Agent to listen the status
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get('APP_PORT', 6001))
    app.run(host='0.0.0.0', port=port)
