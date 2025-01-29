import sys
import json
import pandas as pd

var1 = 3
def main():
    if len(sys.argv) !=2:
        raise IndexError('Give proper argument:\n Length not equal to two')
    try:
        json_data = sys.argv[1]

        data = json.loads(json_data)

        df = pd.DataFrame(data)
    except Exception as e:
        print(e)
        raise ValueError('Give a proper dataframe')

    if isinstance(df, pd.DataFrame):
        return {'data_shape':df.shape, 'var': var1}
    else:
        raise ValueError('Not a dataframe')

if __name__ == "__main__":
    res = main()
    print(json.dumps(res))

sys.stdout.flush()