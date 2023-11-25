export default function () {
    const url = 'https://exemplo.com/api/usuarios'; // Substitua pela URL real da sua API
    const headers = { 'Content-Type': 'application/json' };
    const payload = JSON.stringify({

            "tipoUsuario": "desenvolvedor",
            "email": "teste@email.com",
            "senha": "1222212121",
            "telefone": "212323224002",
            "nome": "Usuario Teste Connect",
            "genero": "Feminino",
            "data_nascimento": "30/10/2001",
            "cpf": "01234567811",
            "habilidades": ["JavaScript", "Python"],
            "experiencia": "10 anos",
            "tag_desenvolvedor": ["backend", "IA"],
            "status": True
        }
    });
  
    const response = http.post(url, payload, { headers });
  
    // Verificar o código de status da resposta
    check(response, {
      'status is 201': (r) => r.status === 201,
    });
  
    // Adicionar mais verificações conforme necessário
    // Exemplo: Verificar o conteúdo da resposta
    check(response, {
      'response contains success': (r) => r.body.includes('success'),
    });
  
    sleep(1); // Adiciona um segundo de pausa entre as solicitações
  }