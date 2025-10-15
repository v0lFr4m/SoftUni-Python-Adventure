from collections import deque

suggested_links = deque(map(int, input().split()))  # FIFO
featured_articles = list(map(int, input().split()))  # LIFO
target = int(input())

final_feed = []

while suggested_links and featured_articles:
    suggested_links_first_el = suggested_links.popleft()
    featured_articles_last_el = featured_articles.pop()

    # if equal add zero and continue
    if suggested_links_first_el == featured_articles_last_el:
        final_feed.append(0)
        continue

    greater_value = max(suggested_links_first_el, featured_articles_last_el)
    smaller_value = min(suggested_links_first_el, featured_articles_last_el)

    # check for division by zero
    if smaller_value == 0:
        final_feed.append(0)
        continue

    remainder = greater_value % smaller_value

    if remainder == 0:
        final_feed.append(0)
        continue

    # greater is from Featured Articles (LIFO)
    if featured_articles_last_el == greater_value:
        final_feed.append(remainder)
        featured_articles.append(remainder * 2)

    # greater is from Suggested Links (FIFO)
    else:
        final_feed.append(-remainder)
        suggested_links.append(remainder * 2)

total_sum = sum(final_feed)

print(f"Final Feed: {', '.join(str(i) for i in final_feed)}")

if total_sum >= target:
    print(f"Goal achieved! Engagement Value: {total_sum}")
else:
    print(f"Goal not achieved! Short by: {target - total_sum}")
