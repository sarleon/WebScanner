def parse_robots_txt(content):
    location = set()
    lines = content.split('\n')
    for line in lines:
        i = line.find('/')
        if i != -1:
            loc = line[i+1:-1]
            if len(loc) > 0 :
                location.add(loc)

    return  list(location)


""" test code:::

if __name__ == '__main__':
    import requests
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 5.2) AppleWebKit/510.0 (KHTML, like Gecko) Chrome/17.0556.768 Safari/510"}
    content = requests.get("http://baidu.com/robots.txt",headers=headers).content
    print(content)
    print parse_robots_txt(content)
"""