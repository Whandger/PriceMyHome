from flask import Flask
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

def create_app():
    print("Criando app e registrando blueprints...")

    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), '..', 'template'),
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
    )

    # Registrar blueprints, se ainda não registrados
    print(app.url_map)
    if 'page' not in app.blueprints:
        from server.routes.routes import page_bp
        app.register_blueprint(page_bp)
        print(app.url_map)

    if 'data' not in app.blueprints:
        from server.routes.get_data import get_databp
        app.register_blueprint(get_databp)
        print(app.url_map)

    return app

if __name__ == '__main__':
    app = create_app()
    # Rodar app normalmente, debug True só em desenvolvimento
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug_mode, use_reloader=False)
