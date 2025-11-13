# dataroutes.py
from flask import Blueprint, request, jsonify
from server.utils.housesPrice import machine
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define o blueprint
get_databp = Blueprint('data', __name__)
post_databp = Blueprint('postData', __name__)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@get_databp.route('/api/data', methods=["POST"])
def Data():
    try:
        data = request.get_json()
        logger.debug(f"JSON recebido: {data}")
        
        data_imoveis = data["imoveis"]
        data_user = data["usuario"]
        logger.debug(f"Dados usuário: {data_user}")
        logger.debug(f"Dados imóveis: {data_imoveis}")
        
        X = [[item["quartos"], item["metros"], item["distancia"]] for item in data_imoveis]
        Y = [item["valor"] for item in data_imoveis]
        Z = [[data_user["quartos"], data_user["metros"], data_user["distancia"]]]

        logger.debug(f"Shape X: {np.array(X).shape}")
        logger.debug(f"Shape Y: {np.array(Y).shape}")
        logger.debug(f"Shape Z: {np.array(Z).shape}")

        previsao = machine(X, Y, Z)

        return jsonify({"previsao": previsao})
    except Exception as e:
        logger.error(f"Erro no servidor: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


