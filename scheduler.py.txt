from apscheduler.schedulers.blocking import BlockingScheduler
from agent import run_agent
from db import init_db

init_db()
scheduler = BlockingScheduler()
scheduler.add_job(run_agent, "interval", hours=6)
scheduler.start()
