from flask import Flask, render_template

app = Flask("学生成绩管理")
print(app.config)


@app.route("/")
def index():
    return render_template("index.html")


app.run(debug=True)
