// let usuario = document.querySelector('#usuario').addEventListener('input', function(event){

// })

// let senha = document.querySelector('#senha').addEventListener('input', function(event){

// })

// let buttonEnviar = document.querySelector('#buttonEnviar').addEventListener('click', function(event){
//     window.location.href = '';
// })

// let buttonCadastrar = document.querySelector('#buttonEnviar').addEventListener('click', function(event){
//     window.location.href = '';
// })

/* ------------------------------------ x ----------------------------------- */

document.addEventListener('DOMContentLoaded', function() {
    const buttonEntrar = document.querySelector('#buttonEnviar');
    const buttonCadastrar = document.querySelector('#buttonCadastrar');

    // Verifica se os botões existem no DOM
    if (!buttonEntrar || !buttonCadastrar) {
        console.error('Botões não encontrados no DOM');
        return;
    }

    buttonCadastrar.addEventListener('click', function(event) {
        event.preventDefault();
        console.log('Botão Cadastrar clicado');

        const usuario = document.querySelector('#usuario').value;
        const senha = document.querySelector('#senha').value;
        console.log(`Usuário: ${usuario}, Senha: ${senha}`);

        fetch('/cadastrar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ usuario, senha })
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '/sucesso';
            } else {
                alert('Erro ao cadastrar usuário.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });

    buttonEntrar.addEventListener('click', function(event) {
        event.preventDefault();
        console.log('Botão Entrar clicado');
        alert('Implementar a lógica de login aqui.');
    });
});
