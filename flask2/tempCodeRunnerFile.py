from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil data dari form
        name = request.form.get('name')
        age = request.form.get('age')
        role = request.form.get('role')
        
        # Menampilkan data yang dikirim
        return f"""
        <h1>Data Anggota</h1>
        <p>Nama: {name}</p>
        <p>Umur: {age}</p>
        <p>Peran: {role}</p>
        <br><a href='/'>Kembali</a>
        """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)