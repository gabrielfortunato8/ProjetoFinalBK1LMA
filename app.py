from flask import (Flask, flash, redirect, render_template, request, url_for) # importa o flask
import json
import os

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages

CONTATOS_FILE = "contatos.json"
PRODUTOS_FILE = "produtos.json"

def save_contato_to_file(data):
    if os.path.exists(CONTATOS_FILE):
        with open(CONTATOS_FILE, "r") as file:
            contatos = json.load(file)
    else:
        contatos = []

    contatos.append(data)

    with open(CONTATOS_FILE, "w") as file:
        json.dump(contatos, file, indent=4)

def save_compra_to_file(data):
    if os.path.exists(PRODUTOS_FILE):
        with open(PRODUTOS_FILE, "r") as file:
            try:
                compras = json.load(file)
            except json.JSONDecodeError:
                contatos = []  # Inicializa como uma lista vazia se houver erro
    else:
        compras = []

    compras.append(data)

    with open(PRODUTOS_FILE, "w") as file:
        json.dump(compras, file, indent=4)

@app.route('/')
def paginaincial():
    return render_template('index.html')

# Rota para o formulário de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    feedback = None
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Criando o dicionário com os dados do contato
        contato_data = {
            'nome': nome,
            'email': email,
            'mensagem': mensagem
        }

        # Salvando os dados no arquivo JSON
        save_contato_to_file(contato_data)

        feedback = "Agradecemos por seu feedback. Fique de olho em seu email que logo entraremos em contato!"
    
    return render_template('contato.html', feedback=feedback)

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

lista_produtos = [
    {"id": 1, "nome": "Tênis Louis Vuitton Sneaker LV Skate", "preco": 199.99, "imagem": "9fb27987-0b86-467f-bc34-aa9a5b5ca81e.jfif"},
    {"id": 2, "nome": "Tênis Mizuno Beta", "preco": 199.99, "imagem": "tenis_nilke.jfif"},
    {"id": 3, "nome": "Tenis Nike Dunk Low Verniz Black", "preco": 159.99, "imagem": "tenis_adidas.jfif"},
    {"id": 4, "nome": "Tênis Adidas Campus Black and White", "preco": 219.99, "imagem": "tenis_adidas.jfif"},
    {"id": 5, "nome": "Tênis Mizuno Pro6", "preco": 199.99, "imagem": "mizuno_tenis.jfif"},
    {"id": 6, "nome": "Tênis Mizuno Pro LS Flor de Lotus", "preco": 199.99, "imagem": "mizunotenis.jfif"},
    {"id": 7, "nome": "Tênis Nike Air Max TN Plus Grey and Green", "preco": 199.99, "imagem": "tenisnike.jfif"},
    {"id": 8, "nome": "Tênis Air Force Black", "preco": 199.99, "imagem": "tenis_air_force.jfif"},
    {"id": 9, "nome": "Tênis Adidas Forum Low All White", "preco": 199.99, "imagem": "adidas_forum.jfif"},
    {"id": 10, "nome": "Tênis Nike Schox R4 Black", "preco": 199.99, "imagem": "tenis_schox.jfif"},
    {"id": 11, "nome": "Tênis Air Max 97 All White Refletivo", "preco": 199.99, "imagem": "tenis_airmax.jfif"},
    {"id": 12, "nome": "Tênis Air Jordan 4 Grey", "preco": 159.99, "imagem": "tenis_jordan.jfif"},
    {"id": 13, "nome": "Chinelo Nike Asuna", "preco": 149.99, "imagem": "chinelo_asuna.jfif"},
    {"id": 14, "nome": "Chinelo Slide Gucci", "preco": 149.99, "imagem": "chinelo_gucci.jfif"},
    {"id": 15, "nome": "Chinelo Kenner Cushy", "preco": 99.99, "imagem": "chinelo_kenner.jfif"},
    {"id": 16, "nome": "Chinelo Kenner Rakka", "preco": 99.99, "imagem": "chinelo_kenner_rakka.jfif"},
    {"id": 17, "nome": "Camiseta de Algodão Boss", "preco": 49.99, "imagem": "blusa_boss.jfif"},
    {"id": 18, "nome": "Camiseta de Algodão Anti Social Club", "preco": 49.99, "imagem": "blusa_antisocial.jfif"},
    {"id": 19, "nome": "Camiseta de Algodão Nike Vulture", "preco": 49.99, "imagem": "camisa_nikevilture.jfif"},
    {"id": 20, "nome": "Camiseta de Algodão High Company Tornado", "preco": 49.99, "imagem": "camisa_high.jfif"},
    {"id": 21, "nome": "Camiseta de Algodão Nike Sum 1972", "preco": 49.99, "imagem": "camiseta_nike.jfif"},
    {"id": 22, "nome": "Camiseta de Algodão Nike JUST DO IT", "preco": 49.99, "imagem": "camisa_nike_just.jfif"},
    {"id": 23, "nome": "Camiseta de Algodão Nike Put The Heat", "preco": 49.99, "imagem": "camisa_nikeput.jfif"},
    {"id": 24, "nome": "Camiseta de Algodão OFF WHT", "preco": 49.99, "imagem": "camiseta_offwht.jfif"},
    {"id": 25, "nome": "Camiseta de Algodão Nike Templo Japones", "preco": 49.99, "imagem": "camiseta_japones.jfif"},
    {"id": 26, "nome": "Camiseta de Algodão Nike Money Duck", "preco": 49.99, "imagem": "camiseta_money.jfif"},
    {"id": 27, "nome": "Camiseta de Algodão Nike Air", "preco": 49.99, "imagem": "blusa_nikeair.jfif"},
    {"id": 28, "nome": "Camiseta de Algodão New Era", "preco": 49.99, "imagem": "blusa_newera.jfif"},
    {"id": 29, "nome": "Camiseta de Algodão Nike Stussy", "preco": 49.99, "imagem": "blusa_stussy.jfif"},
    {"id": 30, "nome": "Camiseta de de Algodão Nike Nocta", "preco": 49.99, "imagem": "camiseta_nocta.jfif"},
    {"id": 31, "nome": "Camiseta de Algodãon The North Face", "preco": 49.99, "imagem": "blusa_the_north.jfif"},
    {"id": 32, "nome": "Camiseta Nike Athletics Dri-FIT",  "preco": 49.99, "imagem": "blusa_nike.jfif"},
    {"id": 33, "nome": "Shorts Dri-FIT Nike", "preco": 49.99, "imagem": "short_drifit.jfif"},
    {"id": 34, "nome": "Shorts Dri-FIT Nike", "preco": 49.99, "imagem": "bermuda drifit.jfif"},
    {"id": 35, "nome": "Short Jeans", "preco": 69.99, "imagem": "short_jeans.jfif"},
    {"id": 36, "nome": "Short Dri-Fit refletivo Nike", "preco": 39.99, "imagem": "bermuda_nike.jfif"},
    {"id": 37, "nome": "Short Dri-FIT Adidas", "preco": 49.99, "imagem": "short_drifitadidas.jfif"},
    {"id": 38, "nome": "Short Elastano LaVíbora", "preco": 34.99, "imagem": "short_lavibora.jfif"},
    {"id": 39, "nome": "Short Adidas de Futebol", "preco": 29.99, "imagem": "short_adidass.jfif"},
    {"id": 40, "nome": "Short Elastano Puma", "preco": 34.99, "imagem": "shortpuma.jfif"},
    {"id": 41, "nome": "Short Puma de Futebol", "preco": 29.99, "imagem": "shortumbro.jfif"},
    {"id": 42, "nome": "Short Dri-FIT BrooksField", "preco": 49.99, "imagem": "shortbrooksfield.jfif"},
    {"id": 43, "nome": "Short Elastano Gucci", "preco": 34.99, "imagem": "shortgucci.jfif"}, 
    {"id": 44, "nome": "Short Mauricinho", "preco": 34.99, "imagem": "shortmauricinho.jfif"}, 
    {"id": 45, "nome": "Perfume Ferrari Black", "preco": 150.00, "imagem": "perfume_ferrari.jfif"}, 
    {"id": 46, "nome": "Perfume Versace Eros", "preco": 150.00, "imagem": "perfume_versace.jfif"}, 
    {"id": 47, "nome": "Perfume Paco Rabanne One Million", "preco": 150.00, "imagem": "perfume_pacorabanne.jfif"}, 
    {"id": 48, "nome": " Perfume 212 Black ", "preco": 150.00, "imagem": "perfume_212_black.jfif"}, 
    {"id": 49, "nome": " Perfume Hugo Boss Bottled Night ", "preco": 150.00, "imagem": "perfume_boss.jfif"}, 
    {"id": 50, "nome": " Perfume Dior Sauvage ", "preco": 150.00, "imagem": "perfume_suavage.jfif"}, 
    {"id": 51, "nome": " Perfume Malbec Black ", "preco": 150.00, "imagem": "perfume_malbec.jfif"}, 
    {"id": 52, "nome": " Carolina Herrera Bad Boy ", "preco": 150.00, "imagem": "perfume_carolina_herrera.jfifp"}, 
    {"id": 53, "nome": " Lupa Oakley Coloridas ", "preco": 100.00, "imagem": "lupas_coloridas.jfif"}, 
    {"id": 54, "nome": " Lupa Oakley de Descanso ", "preco": 100.00, "imagem": "lupas_descanso.jfif"}, 
    {"id": 55, "nome": " Lupa Oakley Ciclismo ", "preco": 100.00, "imagem": "lupas_ciclismo.jfif"}, 
    {"id": 56, "nome": " Conjunto Emporio Armani ", "preco": 99.99, "imagem": "conjunto_emporio.jfif"}, 
    {"id": 57, "nome": " Conjunto Oakley ", "preco": 79.99, "imagem": "conjunto_oakley.jfif"}, 
    {"id": 58, "nome": " Conjunto Adidas ", "preco": 79.99, "imagem": "conjunto_aridas.jfif"}, 
    {"id": 59, "nome": " Conjunto Nike ", "preco": 79.99, "imagem": "nike_conjunto.jfif"}, 
    {"id": 60, "nome": " Conjunto Nike da França ", "preco": 79.99, "imagem": "conjunto_frança.jfif"}, 
    {"id": 61, "nome": " Conjunto Nike Básico ", "preco": 79.99, "imagem": "conjunto_basiconike.jfif"}, 
    {"id": 62, "nome": " Conjunto Adidas Esporte ", "preco": 79.99, "imagem": "conjunto_fut_adidas.jfif"}, 
    {"id": 63, "nome": " Conjunto Nike Básico Branco ", "preco": 79.99, "imagem": "conjunto_nikebranco.jfif"}, 
    {"id": 64, "nome": " Conjunto Mizuno Dri-FIT ", "preco": 79.99, "imagem": "conjunto_mizuno.jfif"},
    {"id": 65, "nome": " Conjunto Hugo Boss ", "preco": 79.99, "imagem": "conjunto boss.jfif"},
    {"id": 66, "nome": " Conjunto Lacoste ", "preco": 79.99, "imagem": "conjunto boss.jfif"}, 
    {"id": 67, "nome": " Conjunto Lacoste ", "preco": 79.99, "imagem": "conjunto_lacoste.jfif"},
    {"id": 68, "nome": " Tracksuit Roma ", "preco": 150.00, "imagem": "conjunto_roma.jfif"}, 
    {"id": 69, "nome": " Tracksuit Barcelona ", "preco": 150.00, "imagem": "conjunto_barcelon.jfif"}, 
    {"id": 70, "nome": " Tracksuit Manchester ", "preco": 150.00, "imagem": "conjunto_barcelon.jfif"}, 
    {"id": 71, "nome": " Tracksuit PSG ", "preco": 150.00, "imagem": "conjunto_psg.jfif"}, 
    {"id": 72, "nome": " Tracksuit Arsenal ", "preco": 150.00, "imagem": "conjunto_arsenal.jfif"}, 
    {"id": 73, "nome": " Tracksuit Borussia Dortmund ", "preco": 150.00, "imagem": "conjunto_borussia.jfif"}, 
    {"id": 74, "nome": " Tracksuit Real Madrid ", "preco": 150.00, "imagem": "conjunto_real.jfif"}, 
    {"id": 75, "nome": " Tracksuit Manchester City ", "preco": 150.00, "imagem": "conjunto_city.jfif"}, 
    {"id": 76, "nome": " Tracksuit Brasil ", "preco": 150.00, "imagem": "conjunto_brasil.jfif"}, 
    {"id": 77, "nome": " Tracksuit Itália ", "preco": 150.00, "imagem": "tracksuit_italia.jfif"}, 
    {"id": 78, "nome": " Tracksuit Alemanha ", "preco": 150.00, "imagem": "conjunto_alemanha.jfif"}, 
    {"id": 79, "nome": " Tracksuit Argentina ", "preco": 150.00, "imagem": "tracksuit_argentina.jfif"}, 
    {"id": 80, "nome": " Monte seu KIT por apenas R$300 ", "preco": 300.00, "imagem": "promoção_conjunto.jfif"}, 
    {"id": 81, "nome": " Monte seu KIT por apenas R$300 ", "preco": 300.00, "imagem": "promoçãoo.jfif"}, 
    {"id": 82, "nome": " Monte seu KIT por apenas R$300 ", "preco": 300.00, "imagem": "promoçãozinha.jfif"}, 
    {"id": 83, "nome": " Monte seu KIT por apenas R$300 ", "preco": 300.00, "imagem": "conjunto_comchinelo.jfif"}, 
    {"id": 84, "nome": " Monte seu KIT por apenas R$300 ", "preco": 300.00, "imagem": "promoção_quiksilver.jfi"}, 
    {"id": 85, "nome": " Monte seu KIT por apenas R$300 ", "preco": 300.00, "imagem": "promoção_chelesea.jfif"}, 
    {"id": 86, "nome": " 3 camisetas regatas de diferentes marcas por apenas R$60", "preco": 60.00, "imagem": "promoção_blusacavada.jfif"}, 
    {"id": 87, "nome": " 10 camisetas de diferentes marcas por R$300 ", "preco": 300.00, "imagem": "blusa_10 uni.jfif"},    
]