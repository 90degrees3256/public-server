from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')  
    if not target_url:
        return "Missing 'url' parameter", 400

    try:
        response = requests.get(target_url)
        return Response(response.content, status=response.status_code, headers=dict(response.headers))
    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
