from django.contrib.auth.models import User
from django.shortcuts import render

#pg inicial
def index(request):
    return render(request, 'index.html')

#Forms de cadastro usuário
def create(request):
    return render(request, 'create.html')

#Inserção de dados dos usuários no banco
def store(request):
    data = {}

    if 'password' in request.POST and 'password-conf' in request.POST:
        password = request.POST['password']
        password_conf = request.POST['password-conf']

        if password != password_conf:
            data['msg'] = 'Senha e confirmação de senha diferentes'
            data['class'] = 'alert-danger'
            return render(request, 'create.html', data)
    else:
        data['msg'] = 'Campos de senha ausentes no formulário'
        data['class'] = 'alert-danger'
        return render(request, 'create.html', data)

    # Restante do código para o caso em que a validação é bem-sucedida
    user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
    user.last_name = request.POST['lastName']
    user.first_name = request.POST['name']
    user.save()
    data['msg'] = 'Dados armazenados com sucesso'
    data['class'] = 'alert-success'
    return render(request, 'create.html', data)