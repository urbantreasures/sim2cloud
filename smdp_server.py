from flask import Flask, jsonify
import secrets

app = Flask(__name__)
profiles_db = {}

@app.route('/download_profile/<iccid>', methods=['GET'])
def download_profile(iccid):
    profile_token = secrets.token_hex(16)  # Simulate encrypted profile
    profiles_db[iccid] = profile_token
    return jsonify({"iccid": iccid, "token": profile_token})

if __name__ == '__main__':
    app.run(port=5000)
