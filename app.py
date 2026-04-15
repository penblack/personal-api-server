from flask import Flask, request, jsonify
import boto3
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

s3 = boto3.client(
    "s3",
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    region_name=config.AWS_REGION,
)

@app.route("/health")
def health():
    return jsonify(ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("file")
    if not f:
        return jsonify(error="no file"), 400
    s3.upload_fileobj(f, config.AWS_BUCKET, f.filename)
    return jsonify(url=f"https://{config.AWS_BUCKET}.s3.amazonaws.com/{f.filename}")

if __name__ == "__main__":
    app.run(debug=config.DEBUG)
