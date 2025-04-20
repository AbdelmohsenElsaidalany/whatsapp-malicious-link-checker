from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Malicious Link Checker Bot is running!"

@app.route("/analyze", methods=["POST"])
def analyze_link():
    link = request.form.get("Body", "")
    result = analyze(link)
    return result

def analyze(link):
    if not link.startswith("http"):
        return "Please send a valid URL."

    report = f"Link: {link}\n"

    # فحص الدومين
    domain = link.split("/")[2]
    report += f"- Domain: {domain}\n"

    # استخدام خدمات فحص مجانية (مثال)
    try:
        virus_total = f"https://www.virustotal.com/gui/url/search/{link}"
        report += f"- Suggested VT check: {virus_total}\n"
    except:
        report += "- Failed to analyze with VirusTotal\n"

    report += "\n(هذا تحليل مبدأي - ينصح باستخدام روابط فحص احترافية)"
    return report

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
