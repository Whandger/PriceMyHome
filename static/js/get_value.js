//Listas
let linha1 = document.getElementById("list_one");
let linha2 = document.getElementById("list_two");
let linha3 = document.getElementById("list_tree");
let linha4 = document.getElementById("list_four");
let linha5 = document.getElementById("list_five");
let linha6 = document.getElementById("list_six");
let linha7 = document.getElementById("list_seven");
let user_list = document.getElementById("list_user");
let text = document.getElementById("previsao")
//-------------------------------------------------------

function data() {
  // Cria uma lista com todas as linhas
  let linhas = [linha1, linha2, linha3, linha4, linha5, linha6, linha7];

  // Mapeia cada linha para um objeto
  let dados = linhas.map(linha => {
    const [quartos, metros, distancia, valor] = Array.from(
      linha.querySelectorAll("input")
    ).map(input => Number(input.value)); // Converte cada input em número

    return { quartos, metros, distancia, valor }; // Retorna um objeto por linha
  });

  // Coleta dos dados do usuário (3 inputs: quartos, metros, distancia)
  const [quartos_user, metros_user, distancia_user] = Array.from(
    user_list.querySelectorAll("input")
  ).map(input => Number(input.value));

  let dados_user = { quartos: quartos_user, metros: metros_user, distancia: distancia_user };

  console.log(dados_user);
  console.log(dados);
  post(dados, dados_user);  // enviar o array diretamente
}

async function post(dados, dados_user) {
  console.log("post Call");
  try {
    const payload = {
      imoveis: dados,
      usuario: dados_user
    };

    const response = await fetch("http://127.0.0.1:5000/api/data", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    console.log(data);
    text.innerHTML = data.previsao;
    text.style.marginLeft = "100px";

  } catch (error) {
    console.error("Erro ao buscar dados:", error);
  }
}

  let button = document.getElementById("button");
  button.addEventListener("click", data);
  
