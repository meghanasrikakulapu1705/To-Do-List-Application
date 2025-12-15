from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)
        return redirect("/")
    return render_template("todo.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    if id < len(tasks):
        tasks.pop(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
