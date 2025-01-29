from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=['*'],
allow_methods=['*'],
allow_headers=['*'],
allow_credentials=True
	)


@app.get("/")

def def_root():
	return {
	"email": "makueireng98@gmail.com",
	"curr_datetime": datetime.now(pytz.utc).isoformat(),
	"github_link": "https://github.com/codewithaguek/stage_zero"
	}