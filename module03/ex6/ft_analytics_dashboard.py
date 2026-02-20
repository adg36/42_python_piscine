#!/usr/bin/env python3

def ft_analytics_dashboard() -> None:

    data = {
        'players': {
            'alice': {'total_score': 2300, 'achievements_count': 5},
            'bob': {'total_score': 1800, 'achievements_count': 3},
            'charlie': {'total_score': 2150, 'achievements_count': 7},
            'diana': {'total_score': 1900, 'achievements_count': 2}
        },
        'sessions': [
            {'player': 'alice', 'mode': 'north'},
            {'player': 'bob', 'mode': 'east'},
            {'player': 'charlie', 'mode': 'central'},
            {'player': 'alice', 'mode': 'north'}
        ],
        'achievements': ['first_kill', 'level_10', 'boss_slayer']
    }
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")

    high_scorers = [player for player, info in
                    data['players'].items() if info['total_score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [info['total_score'] * 2 for info in
                      data['players'].values()]
    print(f"Scores doubled: {scores_doubled}")

    active_players = list({session['player'] for session in
                           data['sessions']})
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {player: info['total_score']
                     for player, info in data['players'].items()}
    print(f"Player scores: {player_scores}")

    score_categories = {
            'high': sum(1 for info in data['players'].values()
                        if info['total_score'] > 5000),
            'medium': sum(1 for info in data['players'].values()
                          if 3000 <= info['total_score'] <= 5000),
            'low': sum(1 for info in data['players'].values()
                       if info['total_score'] < 3000)}
    print(f"Score categories: {score_categories}")

    achievement_counts = {player: info['achievements_count']
                          for player, info in data['players'].items()}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {player for player in data['players']}
    print(f"Unique players: {unique_players}")

    unique_achievements = {ach for ach in ['first_blood',
                                           'level_master', 'speed_runner']}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {session['mode'] for session in data['sessions']}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(data['players'])
    print("Total players:", total_players)

    total_unique_achievements = 8  # from your data['achievements']
    print("Total unique achievements:", total_unique_achievements)

    average_score = sum(info['total_score']
                        for info in data['players'].values()) / total_players
    print(f"Average score: {average_score:.1f}")

    top_name = ""
    top_info = None
    max_score = -1

    for player, info in data['players'].items():
        if info['total_score'] > max_score:
            max_score = info['total_score']
            top_name = player
            top_info = info
    print(f"Top performer: {top_name} ({top_info['total_score']} "
          f"points, {top_info['achievements_count']} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
