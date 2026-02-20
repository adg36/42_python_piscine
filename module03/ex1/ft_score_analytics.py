import sys


def ft_score_analytics() -> None:
    args = sys.argv

    print(" === Player Score Analytics ===")

    if len(args) == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = []

        for score in args[1:]:
            try:
                scores.append(int(score))
            except ValueError:
                print(f"Error. The score '{score}' is not valid. "
                      "Scores must be numeric values.")
                return

        total_players = len(args) - 1
        sum_scores = sum(scores)
        avg_scores = sum_scores / total_players
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}\n"
              f"Total score: {sum_scores}\n"
              f"Average score: {avg_scores}\n"
              f"High score: {high_score}\n"
              f"Low score: {low_score}\n"
              f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
