import sqlite3

def create_leaderboard():
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""CREATE TABLE IF NOT EXISTS leaderboard(name,score)""")

def add_score(name: str=None, score: int=None, limit: int=0) -> None:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""INSERT INTO leaderboard(name, score)
			VALUES(?,?)""", (name, score))

	# reduce leaderboard length if limit is given
	while limit > 0 and len(get_leaderboard()) > limit:
		delete_lowest()

def get_lowest_score() -> int:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""SELECT min(score) FROM LEADERBOARD""")
		return cur.fetchall()[0][0]

def delete_lowest() -> None:
	minimum = get_lowest_score()
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""DELETE FROM LEADERBOARD WHERE score = ?""", (minimum,))

def get_leaderboard() -> list:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""SELECT * FROM leaderboard ORDER BY score DESC""")
		scores = cur.fetchall()
	return scores

def reset_leaderboard() -> None:
	with sqlite3.connect("leaderboard.db") as db:
		cur = db.cursor()
		cur.execute("""DELETE FROM LEADERBOARD""")
		print("Leaderboard reset.")