import re

def validar_email(email):
    regex = r'\S+@\S+'
    if re.match(regex, email):
        return True
    else:
        return False

def get_dados_pessoais():
    dados = {}
    dados["nome"] = input("Digite seu nome completo: ")
    dados["endereco"] = input("Digite seu endereço: ")
    dados["telefone"] = input("Digite seu telefone: ")

    email = input("Digite seu email: ")
    while not validar_email(email):
        print("Email inválido. Por favor, digite um email válido.")
        email = input("Digite seu email: ")
    dados["email"] = email

    dados["experiencias"] = []
    while True:
        experiencia = {}
        experiencia["cargo"] = input("Digite o cargo (ou digite 'sair' para finalizar): ")
        if experiencia["cargo"].lower() == "sair":
            break
        experiencia["empresa"] = input("Digite a empresa: ")
        experiencia["periodo"] = input("Digite o período (ex: 2020-2023): ")
        experiencia["descricao"] = input("Digite uma breve descrição das suas atividades: ")
        dados["experiencias"].append(experiencia)

    dados["formacoes"] = []
    while True:
        formacao = {}
        formacao["curso"] = input("Digite o curso (ou digite 'sair' para finalizar): ")
        if formacao["curso"].lower() == "sair":
            break
        formacao["instituicao"] = input("Digite a instituição: ")
        formacao["ano_conclusao"] = input("Digite o ano de conclusão: ")
        dados["formacoes"].append(formacao)

    # Coleta informações sobre habilidades
    dados["habilidades"] = input("Digite suas habilidades (separadas por vírgula): ").split(',')

    return dados

def construir_cv(info_cv):
    nome_arquivo = f"{info_cv['nome'].replace(' ', '_')}.html"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Currículo de {info_cv['nome']}</title>
           
              <link rel="stylesheet" href="style.css">
        </head>
        <body>
         <section class="infos__cv">

          <div class="resumo">
                <div class="card">
                    <h1 class="nome" >{info_cv['nome']}</h1>
                    <p><strong>Endereço:</strong> {info_cv['endereco']}</p>
                    <p><strong>Telefone:</strong> {info_cv['telefone']}</p>
                    <p><strong>Email:</strong> {info_cv['email']}</p>

                    <h2>Habilidades</h2>
                    <ul class="lista__skills">
                        {''.join(f"<li class='badge__skill'>{habilidade}</li>" for habilidade in info_cv['habilidades'])}
                    </ul>
                </div>
            </div>
                

            <div class="card">
                <h2>Experiência Profissional</h2>
                <ul>
                    {''.join(f"<li>{experiencia['cargo']} - {experiencia['empresa']} ({experiencia['periodo']})<br>{experiencia['descricao']}</li>" for experiencia in info_cv['experiencias'])}
                </ul>
            </div>

            <div class="card">

                <h2>Formação Acadêmica</h2>
                <ul>
                    {''.join(f"<li>{formacao['curso']} - {formacao['instituicao']} ({formacao['ano_conclusao']})</li>" for formacao in info_cv['formacoes'])}
                </ul>
            </div>
            
        </section>
        </body>
        </html>
        """)

if __name__ == "__main__":
    info_cv = get_dados_pessoais()
    construir_cv(info_cv)