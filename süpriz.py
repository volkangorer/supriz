from flask import Flask,render_template,redirect,url_for,request,flash

app = Flask(__name__)

app.secret_key = "volkan"

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/index2",methods = ["GET","POST"])
def index2():
    if request.method =="GET":
        return render_template("index.html")
    else :
      
        isim = request.form.get("isim")
        soyisim = request.form.get("soyisim")
      
        isim1 = "Ece"
        soyisim1 = "Tepeli"
      

        if isim == isim1 and soyisim == soyisim1 :

            flash("Doğru Cevap","success")
            return redirect(url_for("index3"))
            
        
        else:
            
            flash("İsim veya Soyisim Hatalı","danger")
            return render_template("index.html")

@app.route("/index3",methods = ["GET","POST"])
def index3():
    if request.method =="GET":
        return render_template("index3.html")
    else :
      
        tarih = request.form.get("tarih")
        tarih1 = "24 Mart"
        
        if tarih == tarih1 :

            flash("Doğru Cevap","success")
            return redirect(url_for("index4"))
            
        else:
            
            flash("Tarih Hatalı","danger")
            return render_template("index3.html")

@app.route("/index4",methods = ["GET","POST"])
def index4():
    if request.method =="GET":
        return render_template("index4.html")
    else :
      
        kafe = request.form.get("kafe")
        kafe1 = "Hisarönü"
        
        if kafe == kafe1 :

            flash("Doğru Cevap","success")
            return redirect(url_for("index5"))
            
        else:
            
            flash("Mekan ismi Hatalı","danger")
            return render_template("index4.html")

@app.route("/index5",methods = ["GET","POST"])
def index5():
    if request.method =="GET":
        return render_template("index5.html")
    else :
      
        hobi = request.form.get("hobi")
        hobi1 = "Stalk"
        
        if hobi == hobi1 :

            flash("Doğru Cevap","success")
            return redirect(url_for("index6"))
            
        else:
            
            flash("Hobi ismi Hatalı","danger")
            return render_template("index5.html")

@app.route("/index6",methods = ["GET","POST"])
def index6():
    if request.method =="GET":
        return render_template("index6.html")
    else :
      
        soru = request.form.get("soru")
        soru1 = "üçseçenekli"
        
        if soru == soru1 :

            flash("Doğru Cevap","success")
            return redirect(url_for("index7"))
            
        else:
            
            flash("Cevap Hatalı","danger")
            return render_template("index6.html")

@app.route("/index7",methods = ["GET","POST"])
def index7():
    if request.method =="GET":
        return render_template("index7.html")
        


if __name__ == "__main__":
    
    app.run(debug=True)