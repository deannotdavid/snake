import sqlite3

def create_leaderboard():
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS leaderboard(name,score,mode)""")


def add_score(name: str, score: int, mode: str) -> None:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""INSERT INTO leaderboard(name, score, mode)
			VALUES(?,?)""", (name, score, mode))


def get_lowest_score() -> int:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""SELECT min(score) FROM LEADERBOARD""")
		return cur.fetchall()[0][0]


def get_leaderboard() -> list:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""SELECT * FROM leaderboard ORDER BY score DESC""")
		scores = cur.fetchall()
	return scores


def get_top(x: int) -> list:
	return get_leaderboard()[:x]


def reset_leaderboard() -> None:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""DELETE FROM LEADERBOARD""")
		print("Leaderboard reset.")