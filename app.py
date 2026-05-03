from flask import Flask,render_template,request,redirect,url_for
import subprocess
import platform
app=Flask(__name__)

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')    

@app.route('/speak', methods=["GET", "POST"])
def speak():
    if request.method == "POST":
        text = request.form.get('text')
        if text:
            system = platform.system()
            if system == "Windows":
                command = [
                    "powershell", "-Command",
                    f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
                ]
            elif system == "Darwin":  # macOS
                command = ["say", text]
            else:
                command = None
            if command:
                subprocess.run(command)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
