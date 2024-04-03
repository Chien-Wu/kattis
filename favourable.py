"https://open.kattis.com/problems/favourable"

cases = int(input(""))

def get_chapters_list():
    n = int(input(""))
    chapters = []
    for i in range(n):
        chapter = input("").split(" ")
        chapters.append(chapter)
    return chapters

def get_results_list(chapters):
    results = ["1"]
    while not all(item in ["favourably", "catastrophically"] for item in results):
        items_to_remove = []
        for result in results:
            for chapter in chapters:
                if result == chapter[0]:            
                    if chapter[1] in ["favourably", "catastrophically"]:
                        items_to_remove.append(chapter[0])
                        results.append(chapter[1])
                    else:
                        items_to_remove.append(chapter[0])
                        results.extend(chapter[1:4])
            for item in items_to_remove:
                if item in results:
                    results.remove(item)
    return results

def count_good_endings(results):
    good_endings = 0
    for result in results:
        if result == "favourably":
            good_endings += 1
    return good_endings

def main():
    for i in range(cases):
        chapters = get_chapters_list()
        results = get_results_list(chapters)
        good_endings = count_good_endings(results)
        print(good_endings)

main()
                    