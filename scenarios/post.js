import http from 'k6/http';
import { check, fail } from 'k6';
import { sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

export let getCustomerDuration = new Trend('get_customer_duration');
export let getCustomerFailRate = new Rate('get_customer_fail_rate');
export let getCustomerSuccessRate = new Rate('get_customer_success_rate');
export let getCustomerReqs = new Rate('get_customer_reqs');

export default function () {
    const url = 'http://127.0.0.1:5000/signup_developer'; // Substitua pela URL real da sua API
    const headers = { 'Content-Type': 'application/json' };
    const payload = JSON.stringify({
            tipoUsuario: "desenvolvedor",
            email: "teste@email.com",
            senha: "1222212121",
            telefone: "212323224002",
            nome: "Usuario Teste Connect",
            genero: "Feminino",
            data_nascimento: "30/10/2001",
            cpf: "01234567811",
            habilidades: ["JavaScript", "Python"],
            experiencia: "10 anos",
            tag_desenvolvedor: ["backend", "IA"]
    });
  
    const response = http.post(url, payload, { headers });
  
    // Verificar o código de status da resposta
    check(response, {
      'status is 201': (r) => r.status === 201,
    });
  
}