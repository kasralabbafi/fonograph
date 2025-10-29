from youtube_search import YoutubeSearch


def yt_searcher(searchParam):
    searchResult = YoutubeSearch(searchParam, max_results=10).to_dict()
    finalResult = []
    for i in searchResult:
        finalResult.append({"title": i['title'], 'channel': i['channel'], 'url_suffix': i['url_suffix']})
    return finalResult


print(yt_searcher())
