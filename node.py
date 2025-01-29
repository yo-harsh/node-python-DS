import sys
import json

# print("yo!")

var1 = 5
var2 = 8
var3 = 'bye'

def main():
    if len(sys.argv) == 1:
        raise IndexError('Give proper argument')

    try:
        obj = CallOut(sys.argv[1], sys.argv[2], sys.argv)
        if len(sys.argv) == 3:
            response = obj.node()
            # print(response)
            return {'response': response, 'var':var1}
        else:
            # obj = CallOut(sys.argv[1], sys.argv[2], sys.argv[1:])
            response = obj.method()
            # print(response)
            return {'response': response}
    except Exception as e:
        print(e)

class CallOut():

    def __init__(self, name, place, *kwargs):
        self.name = name
        self.place = place
        self.kwargs = kwargs

    def method(self):
        # print("hello world")
        return self.kwargs

    def node(self):
        return(f'{self.name} is from {self.place}')

if __name__ == "__main__":
    res = main()
    print(json.dumps(res))

sys.stdout.flush()