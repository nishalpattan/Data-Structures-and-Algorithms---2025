# Last updated: 8/3/2025, 9:02:21 PM
class Leaderboard:

    def __init__(self):
        self.score_board = dict()

    def addScore(self, playerId: int, score: int) -> None:
        self.score_board[playerId] = self.score_board.get(playerId, 0) + score

    def top(self, K: int) -> int:
        top_k_scores = list()
        for playerId, score in self.score_board.items():
            if len(top_k_scores) < K:
                heapq.heappush(top_k_scores, score)
            else:
                prev_score = heapq.heappop(top_k_scores)
                if score > prev_score:
                    heapq.heappush(top_k_scores, score)
                else:
                    heapq.heappush(top_k_scores, prev_score)
        return sum(top_k_scores)

    def reset(self, playerId: int) -> None:
        del self.score_board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)