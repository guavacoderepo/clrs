from apscheduler.schedulers.background import BackgroundScheduler
from src import mainProcess
from flask import Flask


sched = BackgroundScheduler(daemon=True)
# sched.add_job(mainProcess, 'interval', minutes=0.01)
sched.add_job(mainProcess, 'interval', minutes=720)



def create_app():
  app = Flask(__name__)

  sched.start()
  
  return app


run_app = create_app()

# if __name__ == "__main__":
#     run_app =  create_app()
#     run_app.run()

