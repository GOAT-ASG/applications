import requests
import streamlit as st
import smtplib
import email.message

st.title('CEP-CRUD')
st.markdown('author: Adrian')
pwd = 00

def validation():
    name = str(st.text_input(label=('Nome: '))).title()
    tel = str(st.text_input(label=('Telefone: '))).replace(' ','')
    email = str(st.text_input(label=('E-mail: '))).strip()
    cpf = str(st.text_input(label=('CPF: '))).strip()
    cep = str(st.text_input(label=('CEP: '))).strip()
    if not name or not tel or not email or not cep or not cpf:
        return False
    else:
        return name, tel, email, cpf, cep
    
def error_check(info):
    endereco = ''
    errorlist = []
    if info == False:
        error = "Digite as todas as credênciais"
        errorlist.append(error)
    if str(info[0]).replace(' ','').isalpha() == False:
        error = "Nome inválido"
        errorlist.append(error)
    if (len(info[1]) != 10 and len(info[1]) != 11) or str(info[1]).isnumeric() == False:
        error = "Número de telefone inválido"
        errorlist.append(error)
    if '@' in info[2] and '@' not in str(info[2])[0]:
        dot = str(info[2]).find('@')
        if '.' not in info[2][dot:] or str(info[2])[-1] == '.':
            error = 'E-mail sem domínio'
            errorlist.append(error)
    else:
        error = 'E-mail inválido'
        errorlist.append(error)
    if len(info[3]) != 11 or str(info[3]).isnumeric() == False:
        error = "Número de CPF incorreto"
        errorlist.append(error)
    try:
        response = requests.get(f'https://viacep.com.br/ws/{info[4]}/json')
        endereco = response.json()
        if 'erro' in endereco and response.status_code == 200:
            error = 'CEP inexistente'
            errorlist.append(error)
        else:
            response.status_code = response.status_code
    except:
        error = f"CEP incorreto, erro: {response.status_code}"
        errorlist.append(error)
    return endereco, errorlist

def mail(receiver, name, password):
    mail_text = f'''
    <p>Boa Tarde, <i>{name}</i>!</p>
    <p>Seu cadastro foi feito com sucesso</p>
    <p>Atenciosamente,</p>
    <p>-ASG</p>
    '''

    message = email.message.Message()

    message['Subject'] = 'assunto aqui'
    message['From'] = 'ASGteste2024@outlook.com'
    message['To'] = str(receiver)
    message.add_header('Content-Type', 'text/html')

    message.set_payload(mail_text)
    
    server = smtplib.SMTP('smtp-mail.outlook.com: 587')
    server.starttls()
    server.login(message['From'], password)
    server.sendmail(message['From'], [message['To']], message.as_string().encode('latin1'))

try:
    info = validation()
    error_check(info)
    st.write('')
    if len(error_check(info)[1]) != 0:
        for i in range(len(error_check(info)[1])):
            st.error(error_check(info)[1][i])
    else:
        text_contents = (f'Nome: {info[0]}\nTelefone: {info[1]}\nE-mail: {info[2]}\nCPF: {info[3]}\nEstado: {error_check(info)[0]["uf"]} | Cidade: {error_check(info)[0]["localidade"]} | Bairro: {error_check(info)[0]["bairro"]} | Rua: {error_check(info)[0]["logradouro"]}\n \n')
        if st.button("CADASTRAR"):
            mail(info[2], info[0], pwd)
        st.download_button("SALVAR INFORMAÇÕES",text_contents,"Informações.txt")       
except:
    st.write('')