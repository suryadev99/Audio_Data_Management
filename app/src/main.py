from app import create_app

if __name__=="__main__":
    # Set Values
    HOST="0.0.0.0"
    PORT=5000
    # create app and run
    app = create_app()
    app.run(host=HOST, port=PORT, debug=True)