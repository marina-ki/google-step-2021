import sys
import time
import copy


def read_pages(pages_file):
    pages = {}
    with open(pages_file) as f:
        for data in f.read().splitlines():
            page = data.split('\t')
            # page[0]: id, page[1]: title
            pages[int(page[0])] = page[1]
    return pages


def read_links(links_file):
    links = {}
    with open(links_file) as f:
        for data in f.read().splitlines():
            link = data.split('\t')
            # link[0]: id (from), links[1]: id (to)
            link[0], link[1] = int(link[0]), int(link[1])
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}
    return links


def find_page_id_from_word(pages, word):
    for k, v in pages.items():
        if v == word:
            return k
    print("not found in pages")
    exit(1)


def search_route(pages, links, start_word, goal_word):
    start_page_id = find_page_id_from_word(pages, start_word)
    goal_page_id = find_page_id_from_word(pages, goal_word)

    routes = [[start_page_id]]

    while True:
        new_routes = []

        for route in routes:
            last_visited_page_id = route[-1]
            if last_visited_page_id == goal_page_id:
                return route

            try:
                for next_page_id in links[last_visited_page_id]:
                    if next_page_id in route:  # page_idを既に通った場合はそのルートはNG
                        continue

                    new_route = copy.copy(route)
                    new_route.append(next_page_id)
                    new_routes.append(new_route)

            except KeyError:
                continue

            if len(new_routes) == 0:
                print("not found")
                return
        routes = copy.copy(new_routes)


def print_route(route, pages):
    words = []
    for page_id in route:
        words.append(pages[page_id])
    print(words)


def get_time(process):
    begin = time.time()
    process()
    end = time.time()
    return end - begin


def main():
    if len(sys.argv) != 3:
        print("please input pages_file and links_file")
        exit(1)

    pages_file = sys.argv[1]
    links_file = sys.argv[2]

    print("Path from:")
    start_word = input()
    print("Path to:")
    goal_word = input()

    begin = time.time()

    pages = read_pages(pages_file)
    links = read_links(links_file)

    route = search_route(pages, links, start_word, goal_word)
    print_route(route, pages)

    end = time.time()
    print("処理時間：{}".format(end - begin))


if __name__ == '__main__':
    main()
