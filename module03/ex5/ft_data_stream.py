#!/usr/bin/env python3


from typing import Generator
import time


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield n
        n += 1


def event_stream(events: list[dict]) -> Generator[dict, None, None]:
    for event in events:
        yield event


def ft_data_stream() -> None:
    events = [
            {'player': 'alice', 'event_type': 'kill', 'data': {'level': 5}},
            {'player': 'bob', 'event_type': 'item_found',
             'data': {'level': 12}},
            {'player': 'charlie', 'event_type': 'level_up',
             'data': {'level': 8}}]

    print("=== Game Data Stream Processor ===")
    print(f"\nProcessing {len(events)} game events...\n")

    total_events = 0
    high_level_players = 0
    treasure_events = 0
    levelled_up = 0

    start = time.perf_counter()

    stream = event_stream(events)

    for event in stream:
        total_events += 1

        if event["event_type"] == "item_found":
            treasure_events += 1
            action = "found treasure"
        elif event["event_type"] == "kill":
            action = "killed monster"
        elif event["event_type"] == "death":
            action = "died"
        elif event["event_type"] == "login":
            action = "logged in"
        elif event["event_type"] == "level_up":
            levelled_up += 1
            action = "leveled up"
        else:
            action = event["event_type"]

        if event["data"]["level"] >= 10:
            high_level_players += 1

        print(
            f"Event {total_events}: Player {event['player']}"
            f" (level {event['data']['level']}) {action}")

    end = time.perf_counter()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High Level Players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelled_up}")

    print("\nMemory usage: Constant (streaming)\n"
          f"Processing time: {end - start:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    fib_values = [str(next(fib)) for _ in range(10)]
    print("Fibonacci (first 10):", ", ".join(fib_values))

    prime_gen = primes()
    prime_values = [str(next(prime_gen)) for _ in range(5)]
    print("Primes (first 5):", ", ".join(prime_values))


if __name__ == "__main__":
    ft_data_stream()
