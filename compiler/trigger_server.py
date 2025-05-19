# trigger_server.py

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/deploy", methods=["POST"])
def deploy():
    data = request.json
    folder = data.get("folder")
    if not folder:
        return jsonify({"error": "Missing 'folder' in request"}), 400

    try:
        result = subprocess.run(
            ["python", "chat_push_deploy.py", "--folder", folder],
            capture_output=True, text=True
        )
        return jsonify({
            "output": result.stdout,
            "error": result.stderr
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
