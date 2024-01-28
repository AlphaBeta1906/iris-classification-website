from flask import Blueprint,render_template,request,redirect,url_for
import pickle

routes = Blueprint("routes",__name__)

@routes.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        petalLength = float(request.form.get("petalLength"))
        petalWidth = float(request.form.get("petalWidth"))
        sepalWidth = float(request.form.get("sepalWidth"))
        sepalLength = float(request.form.get("sepalLength"))
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        result = model.predict([[sepalLength,sepalWidth,petalLength,petalWidth]])
        return redirect(url_for("routes.result_page",result=result[0]))
    return render_template("index.html",title="Iris flower classification")

@routes.route("/result/<string:result>")
def result_page(result: str):
    result = result.replace("-"," ")
    data = {
        "Iris setosa": {
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Wild_iris_flower_iris_setosa.jpg/398px-Wild_iris_flower_iris_setosa.jpg?20130227162944",
            "explanation": "Setosa iris typically has smaller flowers than other species, with narrow sepals (outer petals) and petals. They usually have pale blue to violet flowers, although white specimens can also be found. Setosa iris often grows in wet, boggy habitats."
        },
        "Iris versicolor": {
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Iris_versicolor_2.jpg/800px-Iris_versicolor_2.jpg?20050731183559",
            "explanation": "Versicolor iris exhibits larger flowers than setosa, with broader sepals and petals. Their color palette ranges from blue to violet, with occasional lavender hues. Versicolor iris thrives in meadows and open woodlands."
        },
        "Iris virginica": {
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/736px-Iris_virginica.jpg",
            "explanation": "Virginica iris boasts the largest flowers among the three species, featuring wide sepals and petals. Their color spectrum encompasses blue, purple, and reddish-purple tones. Virginica iris prefers moist, forested environments."
        }
    }
    return render_template("result.html",title="Result",result=data[result],result_title=result)