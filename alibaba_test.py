from pylru import lrudecorator

@lrudecorator(100)
def fetchLogs(namespace=None, numberOfLines=100, offset=0, reverse=False):
    content =[]
    # with open('/Users/gilzellner/Downloads/log_example.txt') as f:
    with open('/Users/gilzellner/dev/alibaba_homework/test_data') as f:
        content = f.readlines()
    if namespace is not None:
        content = [elem for elem in content if elem.startswith(namespace)]
    if offset:
        content = content[offset:]
    if numberOfLines > 100:
        raise(Exception('Number of lines limited to 100'))
    if reverse:
        content=content[-numberOfLines:]
        return content[::-1]
    return content[:numberOfLines]

def tail(namespace=None, numberOfLines=100):
    return fetchLogs(namespace=namespace, numberOfLines=numberOfLines, reverse=True)


print fetchLogs(numberOfLines=5, offset=0, reverse=True)
# print fetchLogs(namespace='2018-08-12', numberOfLines=5, offset=0, reverse=False)


# print tail(namespace='', numberOfLines=5)

