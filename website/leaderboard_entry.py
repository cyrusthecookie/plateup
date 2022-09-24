from datetime import datetime

class LeaderboardEntry:
    def __init__(self, email, score, time_played = datetime.now()):
        self.email = email
        self.score = score
        self.time_played = time_played