from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cubes():

    numbers = [1,2,3,4,5,6,7,8]

    results = []

    for n in numbers:

        results.append({

            "number": n,

            "cube": n**3

        })

    return render_template(
        "index.html",
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
