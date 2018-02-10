from config import config
def parse_robots_txt(content):
    if not content:
        return []
    location = set()
    lines = content.split('\n')
    for line in lines:
        i = line.find('/')
        if i != -1:
            loc = line[i+1:-1]
            if len(loc) > 0 :
                location.add(loc)

    return  list(location)

def filter_postfix(name):
    if name[-4:]==".php" or name[-4:]==".jsp" or name[-4:]==".asp" or name[-4:]=="aspx"  or name[-4:]=="phps" :
        return name[:name.rfind('.')]
    else:
        return name


def parse_res(location):
    lines = open(config.PROJECT_DIR + config.DIR_SEPERATOR + config.DICTIONARY_DIR + config.DIR_SEPERATOR + config.LOC_SCHEME, 'r').readlines()
    location = filter_postfix(location)
    result_lines = map(lambda x:x.replace("{{name}}",location),lines)
    return result_lines


""" test code:::

if __name__ == '__main__':
    import requests
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 5.2) AppleWebKit/510.0 (KHTML, like Gecko) Chrome/17.0556.768 Safari/510"}
    content = requests.get("http://baidu.com/robots.txt",headers=headers).content
    print(content)
    print parse_robots_txt(content)
"""
