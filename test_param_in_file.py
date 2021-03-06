import yaml
import pytest
def add_function(a,b):
 return a++b
'''@pytest.mark.parametrize("a,b,expected",
                           yaml.safe_load(open("./data.yml.py"))["datas"]
                           ,ids= yaml.safe_load(open("./data.yml.py"))["myid"])
'''
def get_datas():
    with open("./data.yml.py") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids =datas["myid"]
        return[add_datas,add_ids]

@pytest.mark.parametrize("a,b,expected",
                         get_datas()[0],
                         ids=get_datas()[1]
                         )


def test_add(a,b,expected):
 assert add_function(a,b) == expected