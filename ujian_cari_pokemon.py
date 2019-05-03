from flask import Flask, render_template, request, redirect, url_for, abort
import requests

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# route untuk post pencarian pokemon
@app.route('/post', methods=['POST'])
def cari():
    nama = request.form['nama']
    return redirect(url_for('hasil', nama=nama))

# route untuk menampilkan hasil pencarian
@app.route('/hasil/<string:nama>')
def hasil(nama):
    namaPokemon = nama.lower()
    url = 'https://pokeapi.co/api/v2/pokemon/'+namaPokemon
    pokemon = requests.get(url)
    if str(pokemon) == '<Response [404]>':
        abort(404)
    else:
        return render_template('hasil.html', pokemon=pokemon)

# route untuk menampilkan halaman error
@app.errorhandler(404)
def error(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)